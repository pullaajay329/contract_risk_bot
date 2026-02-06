import streamlit as st
import tempfile

from main import run_pipeline

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Contract Risk Assessment Bot",
    layout="wide"
)

st.title("📄 Contract Analysis & Risk Assessment Bot")
st.caption("AI-powered assistant for small & medium businesses")

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙️ Settings")
language = st.sidebar.selectbox(
    "Contract Language",
    ["English", "Hindi"]
)

uploaded_file = st.sidebar.file_uploader(
    "Upload Contract (PDF or TXT)",
    type=["pdf", "txt"]
)

analyze_btn = st.sidebar.button("🔍 Analyze Contract")

# ---------------- MAIN LOGIC ----------------
if analyze_btn and uploaded_file is not None:

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        file_path = tmp.name

    with st.spinner("Analyzing contract..."):
        results = run_pipeline(file_path)

    # ---------------- SUMMARY DASHBOARD ----------------
    st.subheader("📊 Contract Risk Summary")

    risk_counts = {"High": 0, "Medium": 0, "Low": 0}
    for r in results:
        risk_counts[r["risk"]] += 1

    col1, col2, col3 = st.columns(3)
    col1.metric("🔴 High Risk Clauses", risk_counts["High"])
    col2.metric("🟡 Medium Risk Clauses", risk_counts["Medium"])
    col3.metric("🟢 Low Risk Clauses", risk_counts["Low"])

    # Overall Risk
    if risk_counts["High"] > 0:
        overall_risk = "🔴 HIGH"
    elif risk_counts["Medium"] > 0:
        overall_risk = "🟡 MEDIUM"
    else:
        overall_risk = "🟢 LOW"

    st.markdown(f"### **Overall Contract Risk: {overall_risk}**")

    st.divider()

    # ---------------- CLAUSE ANALYSIS ----------------
    st.subheader("🧾 Clause-by-Clause Analysis")

    for idx, item in enumerate(results, start=1):
        with st.expander(f"Clause {idx} | Risk: {item['risk']}"):
            st.markdown("**📄 Clause Text:**")
            st.write(item["clause"])

            st.markdown("**🧠 Explanation:**")
            st.info(item["explanation"])

            st.markdown("**⚠️ Risk Reason:**")
            st.warning(item["reason"])

            st.markdown("**✅ Suggested Alternative:**")
            st.success(item["suggestion"])

else:
    st.info("⬅️ Upload a contract and click **Analyze Contract** to begin.")