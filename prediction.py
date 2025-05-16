import streamlit as st
import pickle
import numpy as np
import xgboost

# Load model
try:
    with open("model_xgb.pkl", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("❌ File model_xgb.pkl tidak ditemukan. Pastikan file berada di folder yang sama dengan app.py.")
    st.stop()
except Exception as e:
    st.error(f"❌ Gagal memuat model: {e}")
    st.stop()

st.title("Prediksi Karyawan Mengundurkan Diri (Attrition)")
st.markdown("### Silakan isi informasi karyawan di bawah:")

# Input form dengan urutan pilihan sesuai mapping encode_input
business_travel = st.selectbox("Business Travel", ["Non-Travel", "Travel_Rarely", "Travel_Frequently"])

department = st.selectbox("Department", ["Human Resources", "Research & Development", "Sales"])

education_field = st.selectbox("Education Field", ["Life Sciences", "Medical", "Marketing", "Technical Degree", "Other"])

gender = st.selectbox("Gender", ["Male", "Female"])

job_role = st.selectbox("Job Role", [
    "Healthcare Representative", "Human Resources", "Laboratory Technician", "Manager",
    "Manufacturing Director", "Research Director", "Research Scientist", "Sales Executive", "Sales Representative"
])

age = st.slider("Umur", 18, 60, 30)
distance = st.slider("Jarak Rumah ke Kantor (km)", 1, 30, 10)
income = st.slider("Penghasilan Bulanan", 1000, 20000, 5000)

education = st.selectbox("Tingkat Pendidikan", [
    "Below College",  # 1
    "College",        # 2
    "Bachelor",       # 3
    "Master",         # 4
    "Doctor"          # 5
])
education_map = {
    "Below College": 1,
    "College": 2,
    "Bachelor": 3,
    "Master": 4,
    "Doctor": 5
}

marital_status = st.selectbox("Status Pernikahan", ["Single", "Married", "Divorced"])

def encode_input():
    input_dict = {
        "BusinessTravel": {"Non-Travel": 0, "Travel_Rarely": 1, "Travel_Frequently": 2},
        "Department": {"Human Resources": 0, "Research & Development": 1, "Sales": 2},
        "EducationField": {"Life Sciences": 0, "Medical": 1, "Marketing": 2, "Technical Degree": 3, "Other": 4},
        "Gender": {"Male": 0, "Female": 1},
        "JobRole": {
            "Healthcare Representative": 0, "Human Resources": 1, "Laboratory Technician": 2,
            "Manager": 3, "Manufacturing Director": 4, "Research Director": 5,
            "Research Scientist": 6, "Sales Executive": 7, "Sales Representative": 8
        },
        "MaritalStatus": {"Single": 0, "Married": 1, "Divorced": 2}
    }

    return np.array([[  
        input_dict["BusinessTravel"][business_travel],
        input_dict["Department"][department],
        input_dict["EducationField"][education_field],
        input_dict["Gender"][gender],
        input_dict["JobRole"][job_role],
        age,
        distance,
        income,
        education_map[education],
        input_dict["MaritalStatus"][marital_status]
    ]])

def faktor_positif_negatif(data):
    positif = []
    negatif = []

    # indeks sesuai urutan fitur di encode_input
    # idx 6 = distance, idx 7 = income, idx 5 = age
    if data[6] <= 10:
        positif.append("jarak rumah relatif dekat")
    else:
        negatif.append("jarak rumah jauh")

    if data[7] >= 8000:
        positif.append("penghasilan bulanan memadai")
    else:
        negatif.append("penghasilan bulanan mungkin terlalu rendah")

    if data[5] >= 25:
        negatif.append("umur lebih dari 25 tahun")
    else:
        positif.append("umur masih muda")

    return positif, negatif

if st.button("Prediksi Attrition"):
    encoded_input = encode_input()
    proba = model.predict_proba(encoded_input)[0][1]
    threshold = 0.3
    pred = 1 if proba >= threshold else 0

    positif, negatif = faktor_positif_negatif(encoded_input[0])

    st.markdown(f"**Probabilitas Attrition: {proba:.2f}**")

    if pred == 0:
        st.success("✅ Karyawan diprediksi **tidak mengundurkan diri** (No Attrition)")
    else:
        st.error("❌ Karyawan diprediksi **akan mengundurkan diri** (Attrition)")

    with st.expander("🔍 Analisis Faktor"):
        if positif:
            st.markdown("**Faktor Positif (menurunkan risiko attrition):**")
            for p in positif:
                st.markdown(f"- ✅ {p}")
        if negatif:
            st.markdown("**Faktor Negatif (meningkatkan risiko attrition):**")
            for n in negatif:
                st.markdown(f"- ❌ {n}")
