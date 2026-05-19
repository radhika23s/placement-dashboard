import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Placement Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- TITLE ----------------
st.title("📊 Placement Insights Dashboard")
st.markdown("Upload your dataset and explore insights like a data analyst 😎")

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    # ---------------- SIDEBAR FILTERS ----------------
    st.sidebar.header("Filters")

    if "Company" in df.columns:
        selected_company = st.sidebar.multiselect(
            "Select Company",
            df["Company"].dropna().unique(),
            default=df["Company"].dropna().unique()
        )
        df = df[df["Company"].isin(selected_company)]

    # ---------------- METRICS ----------------
    st.subheader("📌 Key Metrics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Records", len(df))

    with col2:
        if "Salary" in df.columns:
            st.metric("Average Salary", f"₹ {int(df['Salary'].mean())}")

    with col3:
        if "Salary" in df.columns:
            st.metric("Highest Salary", f"₹ {df['Salary'].max()}")

    # ---------------- DATA PREVIEW ----------------
    st.subheader("📄 Dataset Preview")
    st.dataframe(df, use_container_width=True)

    # ---------------- SALARY DISTRIBUTION ----------------
    if "Salary" in df.columns:
        st.subheader("💰 Salary Distribution")

        fig1 = px.histogram(
            df,
            x="Salary",
            nbins=20,
            title="Salary Distribution"
        )
        st.plotly_chart(fig1, use_container_width=True)

    # ---------------- COMPANY ANALYSIS ----------------
    if "Company" in df.columns:
        st.subheader("🏢 Company-wise Hiring")

        company_counts = df["Company"].value_counts().reset_index()
        company_counts.columns = ["Company", "Count"]

        fig2 = px.bar(
            company_counts,
            x="Company",
            y="Count",
            title="Students Placed per Company"
        )

        st.plotly_chart(fig2, use_container_width=True)

    # ---------------- TOP STUDENTS ----------------
    if "Salary" in df.columns:
        st.subheader("🏆 Top 10 Highest Paid")

        top_df = df.sort_values(by="Salary", ascending=False).head(10)
        st.dataframe(top_df, use_container_width=True)

else:
    st.info("Upload a CSV file to start analyzing placement data 🚀")