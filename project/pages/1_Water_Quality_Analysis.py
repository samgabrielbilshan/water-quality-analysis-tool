import streamlit as st
import pandas as pd
import json

st.set_page_config(layout="wide")


with open("translations.json", "r", encoding="utf-8") as f:
    translations = json.load(f)

lang = st.sidebar.selectbox("Language", options=["en", "ta"], format_func=lambda x: {"ta": "தமிழ்", "en": "English"}[x])
t = translations[lang]

st.title(t["title"])
st.write(t["description"])

STANDARDS = {
    'pH': (6.5, 8.5),
    'Turbidity (NTU)': (0, 5),
    'TDS (mg/L)': (0, 500),
    'DO (mg/L)': (5, 50),
    'Ammonia (mg/L)': (0, 0.5),
    'Hardness (mg/L)': (0, 200),
    'Nitrate (mg/L)': (0, 45),
    'Chloride (mg/L)': (0, 250),
}

def validate_input(param, value):
    min_val, max_val = STANDARDS[param]
    if param == "DO (mg/L)":
        return value >= min_val
    return min_val <= value <= max_val

with st.form("water_quality_form"):
    st.header(t["basic_header"])
    ph = st.slider("pH (6.5 – 8.5)", 0.0, 14.0, 7.0)
    turbidity = st.number_input(f"{t['turbidity']} (NTU, ≤ 5)", min_value=0.0)
    tds = st.number_input(f"{t['tds']} (mg/L, ≤ 500)", min_value=0.0)
    ammonia = st.number_input("Ammonia (mg/L, ≤ 0.5)", min_value=0.0)
    nitrate = st.number_input("Nitrate (mg/L, ≤ 45)", min_value=0.0)

    st.header(t["advanced_header"])
    do = st.number_input("Dissolved Oxygen (mg/L, ≥ 5)", min_value=0.0)
    hardness = st.number_input("Hardness (mg/L, ≤ 200)", min_value=0.0)
    chloride = st.number_input("Chloride (mg/L, ≤ 250)", min_value=0.0)

    submitted = st.form_submit_button(t["submit_button"])

if submitted:
    results = {
        'pH': ph,
        'Turbidity (NTU)': turbidity,
        'TDS (mg/L)': tds,
        'DO (mg/L)': do,
        'Ammonia (mg/L)': ammonia,
        'Hardness (mg/L)': hardness,
        'Nitrate (mg/L)': nitrate,
        'Chloride (mg/L)': chloride,
    }
    violations = []
    for param, value in results.items():
        if value != 0 and not validate_input(param, value):
            violations.append(param)
    basic_safe = all(validate_input(param, results[param]) for param in ['pH', 'Turbidity (NTU)', 'TDS (mg/L)', 'Ammonia (mg/L)', 'Nitrate (mg/L)'])

    st.subheader(t["result_header"])
    if basic_safe and len(violations) == 0:
        st.success(t["potable"])
    else:
        st.error(t["not_potable"])
        st.write(t["violations_header"])
        for param in violations:
            val = results[param]
            min_val, max_val = STANDARDS[param]
            limit_str = f"{min_val} – {max_val}" if param != "DO (mg/L)" else f"≥ {min_val}"
            st.markdown(f"- **{param}**: {val} ({t['limit']}: {limit_str})")
        st.info(t["tip"])

    missing_values = [param for param, value in results.items() if value == 0]

    if basic_safe and missing_values:
        st.error(f"""✅ {t["basic_meets_standards"]}  
                    ⚠️ {t["missing_params_warning"]}  
                    👉 {", ".join(missing_values)}""")
        
    # Count tested parameters (value != 0)
    tested_params = [param for param, value in results.items() if value != 0]
    valid_params = [param for param in tested_params if validate_input(param, results[param])]
    confidence_percent = round((len(valid_params) / len(tested_params)) * 100) if tested_params else 0

    st.info(f"🔎 **{t['confidence_level']}**: {confidence_percent}% ({len(tested_params)} {t['tested_parameters']})")

    if confidence_percent >= 90:
        st.success(t["high_confidence"])
    elif confidence_percent >= 60:
        st.warning(t["moderate_confidence"])
    else:
        st.error(t["low_confidence"])


        

    st.subheader(t["summary_header"])
    df = pd.DataFrame({
        t["parameter"]: list(results.keys()),
        t["value"]: list(results.values()),
        t["range"]: [
            f"{v[0]} – {v[1]}" if k != "DO (mg/L)" else f"≥ {v[0]}"
            for k, v in STANDARDS.items()
        ],
        t["status"]: [
            t["not_entered"] if v == 0 else (t["ok"] if validate_input(k, v) else t["unsafe"])
            for k, v in results.items()
        ]
    })
    
    st.table(df)
    csv = '\ufeff' + df.to_csv(index=False)
    csv = csv.encode('utf-8')

    st.download_button(t["download_csv"], data=csv, file_name="water_quality_report.csv", mime="text/csv")
