import streamlit as st
import numpy as np
import joblib
import pandas as pd


feature_names = [
    'Curricular_units_2nd_sem_grade', 'Application_mode', 'Curricular_units_2nd_sem_approved', 'Course',
    'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade', 'Mothers_occupation', 'Fathers_occupation',
    'Age_at_enrollment', 'Curricular_units_2nd_sem_evaluations', 'Previous_qualification', 'Mothers_qualification',
    'Scholarship_holder', 'Debtor', 'Curricular_units_1st_sem_evaluations', 'Curricular_units_2nd_sem_without_evaluations',
    'Gender', 'Curricular_units_2nd_sem_credited', 'Curricular_units_1st_sem_credited', 'Admission_grade',
    'Curricular_units_1st_sem_enrolled', 'Curricular_units_2nd_sem_enrolled', 'Tuition_fees_up_to_date',
    'Fathers_qualification', 'Curricular_units_1st_sem_without_evaluations', 'Previous_qualification_grade',
    'Nacionality', 'Application_order', 'Displaced', 'Marital_status', 'Unemployment_rate'
]

# Load model dan scaler
model = joblib.load('model/random_forest.pkl')
scaler = joblib.load('model/scaler.pkl')

# Judul aplikasi
st.title("Aplikasi Prediksi Status Mahasiswa")

# Input dari pengguna
application_mode_options = {
    1: "1st phase - general contingent",
    2: "Ordinance No. 612/93",
    5: "1st phase - special contingent (Azores Island)",
    7: "Holders of other higher courses",
    10: "Ordinance No. 854-B/99",
    15: "International student (bachelor)",
    16: "1st phase - special contingent (Madeira Island)",
    17: "2nd phase - general contingent",
    18: "3rd phase - general contingent",
    26: "Ordinance No. 533-A/99, item b2) (Different Plan)",
    27: "Ordinance No. 533-A/99, item b3 (Other Institution)",
    39: "Over 23 years old",
    42: "Transfer",
    43: "Change of course",
    44: "Technological specialization diploma holders",
    51: "Change of institution/course",
    53: "Short cycle diploma holders",
    57: "Change of institution/course (International)"
}
previous_qualification_options = {
    1: "Secondary education",
    2: "Higher education - bachelor's degree",
    3: "Higher education - degree",
    4: "Higher education - master's",
    5: "Higher education - doctorate",
    6: "Frequency of higher education",
    9: "12th year of schooling - not completed",
    10: "11th year of schooling - not completed",
    12: "Other - 11th year of schooling",
    14: "10th year of schooling",
    15: "10th year of schooling - not completed",
    19: "Basic education 3rd cycle (9th/10th/11th year) or equivalent",
    38: "Basic education 2nd cycle (6th/7th/8th year) or equivalent",
    39: "Technological specialization course",
    40: "Higher education - degree (1st cycle)",
    42: "Professional higher technical course",
    43: "Higher education - master (2nd cycle)"
}

nationality_options = {
    1: "Portuguese",
    2: "German",
    6: "Spanish",
    11: "Italian",
    13: "Dutch",
    14: "English",
    17: "Lithuanian",
    21: "Angolan",
    22: "Cape Verdean",
    24: "Guinean",
    25: "Mozambican",
    26: "Santomean",
    32: "Turkish",
    41: "Brazilian",
    62: "Romanian",
    100: "Moldova (Republic of)",
    101: "Mexican",
    103: "Ukrainian",
    105: "Russian",
    108: "Cuban",
    109: "Colombian"
}

mothers_qualification_options = {
    1:  "Secondary Education - 12th Year of Schooling or Eq.",
    2:  "Higher Education - Bachelor's Degree",
    3:  "Higher Education - Degree",
    4:  "Higher Education - Master's",
    5:  "Higher Education - Doctorate",
    6:  "Frequency of Higher Education",
    9:  "12th Year of Schooling - Not Completed",
    10: "11th Year of Schooling - Not Completed",
    11: "7th Year (Old)",
    12: "Other - 11th Year of Schooling",
    14: "10th Year of Schooling",
    18: "General commerce course",
    19: "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.",
    22: "Technical-professional course",
    26: "7th year of schooling",
    27: "2nd cycle of the general high school course",
    29: "9th Year of Schooling - Not Completed",
    30: "8th year of schooling",
    34: "Unknown",
    35: "Can't read or write",
    36: "Can read without having a 4th year of schooling",
    37: "Basic education 1st cycle (4th/5th year) or equiv.",
    38: "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",
    39: "Technological specialization course",
    40: "Higher education - degree (1st cycle)",
    41: "Specialized higher studies course",
    42: "Professional higher technical course",
    43: "Higher Education - Master (2nd cycle)",
    44: "Higher Education - Doctorate (3rd cycle)"
}

fathers_qualification_options = {
    1:  "Secondary Education - 12th Year of Schooling or Eq.",
    2:  "Higher Education - Bachelor's Degree",
    3:  "Higher Education - Degree",
    4:  "Higher Education - Master's",
    5:  "Higher Education - Doctorate",
    6:  "Frequency of Higher Education",
    9:  "12th Year of Schooling - Not Completed",
    10: "11th Year of Schooling - Not Completed",
    11: "7th Year (Old)",
    12: "Other - 11th Year of Schooling",
    13: "2nd year complementary high school course",
    14: "10th Year of Schooling",
    18: "General commerce course",
    19: "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.",
    20: "Complementary High School Course",
    22: "Technical-professional course",
    25: "Complementary High School Course - not concluded",
    26: "7th year of schooling",
    27: "2nd cycle of the general high school course",
    29: "9th Year of Schooling - Not Completed",
    30: "8th year of schooling",
    31: "General Course of Administration and Commerce",
    33: "Supplementary Accounting and Administration",
    34: "Unknown",
    35: "Can't read or write",
    36: "Can read without having a 4th year of schooling",
    37: "Basic education 1st cycle (4th/5th year) or equiv.",
    38: "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",
    39: "Technological specialization course",
    40: "Higher education - degree (1st cycle)",
    41: "Specialized higher studies course",
    42: "Professional higher technical course",
    43: "Higher Education - Master (2nd cycle)",
    44: "Higher Education - Doctorate (3rd cycle)"
}

mothers_occupation_options = {
    0: "Student",
    1: "Legislative/Executive Power Representatives, Directors and Managers",
    2: "Specialists in Intellectual and Scientific Activities",
    3: "Intermediate Level Technicians and Professions",
    4: "Administrative Staff",
    5: "Personal Services, Security, Safety Workers and Sellers",
    6: "Farmers & Skilled Workers in Agriculture/Fisheries/Forestry",
    7: "Skilled Workers in Industry/Construction/Craftsmen",
    8: "Machine Operators and Assembly Workers",
    9: "Unskilled Workers",
    10: "Armed Forces Professions",
    90: "Other Situation",
    99: "(Blank)",
    122: "Health Professionals",
    123: "Teachers",
    125: "ICT Specialists",
    131: "Intermediate Science/Engineering Technicians",
    132: "Intermediate Health Technicians and Professionals",
    134: "Intermediate Technicians - Legal/Social/Sports/Culture etc.",
    141: "Office Workers, Secretaries, Data Processing Operators",
    143: "Accounting/Statistical/Financial/Registry Operators",
    144: "Other Administrative Support Staff",
    151: "Personal Service Workers",
    152: "Sellers",
    153: "Personal Care Workers and Similar",
    171: "Skilled Construction Workers (excl. electricians)",
    173: "Skilled Workers - Printing, Instruments, Jewelers, Artisans",
    175: "Food Processing, Woodworking, Clothing, Other Crafts",
    191: "Cleaning Workers",
    192: "Unskilled Workers in Agriculture/Fisheries/Forestry",
    193: "Unskilled Workers in Industry/Construction/Transport",
    194: "Meal Preparation Assistants"
}


fathers_occupation_options = {
    0: "Student",
    1: "Legislative/Executive Representatives, Directors & Managers",
    2: "Specialists in Intellectual and Scientific Activities",
    3: "Intermediate Level Technicians and Professions",
    4: "Administrative Staff",
    5: "Personal Services, Security, Safety Workers and Sellers",
    6: "Farmers and Skilled Workers in Agriculture/Fisheries/Forestry",
    7: "Skilled Workers in Industry, Construction and Craftsmen",
    8: "Machine Operators and Assembly Workers",
    9: "Unskilled Workers",
    10: "Armed Forces Professions",
    90: "Other Situation",
    99: "(Blank)",
    101: "Armed Forces Officers",
    102: "Armed Forces Sergeants",
    103: "Other Armed Forces Personnel",
    112: "Directors of Administrative and Commercial Services",
    114: "Hotel, Catering, Trade and Other Services Directors",
    121: "Specialists in Physical Sciences, Math, Engineering, etc.",
    122: "Health Professionals",
    123: "Teachers",
    124: "Finance/Accounting/Admin/Public & Commercial Relations Specialists",
    131: "Intermediate Science/Engineering Technicians",
    132: "Intermediate Health Technicians",
    134: "Legal/Social/Sports/Culture Technicians (Intermediate)",
    135: "ICT Technicians",
    141: "Office Workers, Secretaries, Data Processing Operators",
    143: "Accounting/Statistical/Financial/Registry Operators",
    144: "Other Administrative Support Staff",
    151: "Personal Service Workers",
    152: "Sellers",
    153: "Personal Care Workers and Similar",
    154: "Protection and Security Services Personnel",
    161: "Market-Oriented Farmers & Skilled Agricultural Workers",
    163: "Subsistence Farmers, Fishermen, Hunters and Gatherers",
    171: "Skilled Construction Workers (excl. electricians)",
    172: "Skilled Workers in Metallurgy/Metalworking",
    174: "Skilled Workers in Electricity and Electronics",
    175: "Food Processing, Woodworking, Clothing, Other Crafts",
    181: "Fixed Plant and Machine Operators",
    182: "Assembly Workers",
    183: "Vehicle Drivers and Mobile Equipment Operators",
    192: "Unskilled Workers in Agriculture/Fisheries/Forestry",
    193: "Unskilled Workers in Industry/Construction/Transport",
    194: "Meal Preparation Assistants",
    195: "Street Vendors (Except Food) and Street Service Providers"
}

course_options = {
    33: "Biofuel Production Technologies",
    171: "Animation and Multimedia Design",
    8014: "Social Service (Evening Attendance)",
    9003: "Agronomy",
    9070: "Communication Design",
    9085: "Veterinary Nursing",
    9119: "Informatics Engineering",
    9130: "Equinculture",
    9147: "Management",
    9238: "Social Service",
    9254: "Tourism",
    9500: "Nursing",
    9556: "Oral Hygiene",
    9670: "Advertising and Marketing Management",
    9773: "Journalism and Communication",
    9853: "Basic Education",
    9991: "Management (Evening Attendance)"
}

marital_status_options = {
    1: "Single",
    2: "Married",
    3: "Widower",
    4: "Divorced",
    5: "Facto Union",
    6: "Legally Separated"
}



# Input pengguna (disesuaikan dengan urutan fitur yang digunakan model)
age = st.number_input("Umur saat masuk (Age_at_enrollment)", min_value=15, max_value=60)
admission_grade = st.number_input("Admission Grade", min_value=0.0, max_value=200.0)

application_mode = st.selectbox("Application Mode", list(application_mode_options.values()))
application_order = st.slider("Application Order", 0, 9)

previous_qualification = st.selectbox("Previous Qualification", list(previous_qualification_options.values()))
previous_qualification_grade = st.number_input("Previous Qualification Grade", 0.0, 200.0)

mothers_qualification = st.selectbox("Mother's Qualification", list(mothers_qualification_options.values()))
fathers_qualification = st.selectbox("Father's Qualification", list(fathers_qualification_options.values()))

mothers_occupation = st.selectbox("Mother's Occupation", list(mothers_occupation_options.values()))
fathers_occupation = st.selectbox("Father's Occupation", list(fathers_occupation_options.values()))

course = st.selectbox("Course", list(course_options.values()))
nacionality = st.selectbox("Nationality", list(nationality_options.values()))
marital_status = st.selectbox("Marital Status", list(marital_status_options.values()))
gender = st.selectbox("Gender (1 = Male, 0 = Female)", [0, 1])
displaced = st.selectbox("Displaced (0 = Tidak, 1 = Ya)", [0, 1])
debtor = st.selectbox("Debtor (0 = Tidak, 1 = Ya)", [0, 1])
scholarship_holder = st.selectbox("Scholarship Holder (0 = Tidak, 1 = Ya)", [0, 1])
tuition_fees_up_to_date = st.selectbox("Tuition Fees Up To Date (0 = Tidak, 1 = Ya)", [0, 1])
unemployment_rate = st.number_input("Unemployment Rate", 0.0, 100.0)

# Curricular Units - Semester 1
cu1_enrolled = st.number_input("CU 1st Sem Enrolled", 0)
cu1_approved = st.number_input("CU 1st Sem Approved", 0)
cu1_grade = st.number_input("CU 1st Sem Grade", 0.0)
cu1_evaluations = st.number_input("CU 1st Sem Evaluations", 0)
cu1_credited = st.number_input("CU 1st Sem Credited", 0)
cu1_without_eval = st.number_input("CU 1st Sem Without Evaluations", 0)

# Curricular Units - Semester 2
cu2_enrolled = st.number_input("CU 2nd Sem Enrolled", 0)
cu2_approved = st.number_input("CU 2nd Sem Approved", 0)
cu2_grade = st.number_input("CU 2nd Sem Grade", 0.0)
cu2_evaluations = st.number_input("CU 2nd Sem Evaluations", 0)
cu2_credited = st.number_input("CU 2nd Sem Credited", 0)
cu2_without_eval = st.number_input("CU 2nd Sem Without Evaluations", 0)

# Tombol prediksi
if st.button("🔍 Prediksi Status"):
    application_mode_code = [k for k, v in application_mode_options.items() if v == application_mode][0]
    previous_qualification_code = [k for k, v in previous_qualification_options.items() if v == previous_qualification][0]
    mothers_qualification_code = [k for k, v in mothers_qualification_options.items() if v == mothers_qualification][0]
    fathers_qualification_code = [k for k, v in fathers_qualification_options.items() if v == fathers_qualification][0]
    mothers_occupation_code = [k for k, v in mothers_occupation_options.items() if v == mothers_occupation][0]
    fathers_occupation_code = [k for k, v in fathers_occupation_options.items() if v == fathers_occupation][0]
    course_code = [k for k, v in course_options.items() if v == course][0]
    nationality_code = [k for k, v in nationality_options.items() if v == nacionality][0]
    marital_status_code = [k for k, v in marital_status_options.items() if v == marital_status][0]

    user_input = pd.DataFrame([[
    cu2_grade, application_mode_code, cu2_approved, course_code, cu1_approved,
    cu1_grade, mothers_occupation_code, fathers_occupation_code, age, cu2_evaluations,
    previous_qualification_code, mothers_qualification_code, scholarship_holder, debtor,
    cu1_evaluations, cu2_without_eval, gender, cu2_credited, cu1_credited,
    admission_grade, cu1_enrolled, cu2_enrolled, tuition_fees_up_to_date,
    fathers_qualification_code, cu1_without_eval, previous_qualification_grade,
    nationality_code, application_order, displaced, marital_status_code, unemployment_rate
]], columns=feature_names)

    input_scaled = scaler.transform(user_input)
    prediction = model.predict(input_scaled)
    label_dict = {0: "Dropout", 1: "Enrolled", 2: "Graduate"}
    st.success(f"📊 Prediksi Status Mahasiswa: **{label_dict[prediction[0]]}**")
