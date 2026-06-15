# 📊 Placement Insights Dashboard

Placement Insights Dashboard is an interactive data analytics application designed to help placement coordinators, institutions, and students analyze recruitment distributions. Built using Streamlit and Plotly, the dashboard allows users to upload raw placement CSV records and instantly extract actionable metrics, data visualizations, and top-tier salary breakdowns like a professional data analyst.

---

## 🚀 Key Features

- **📂 Dynamic CSV Ingestion:** Drag-and-drop file uploader that parses student placement files on the fly.
- **📌 Automated Live Metrics:** Displays real-time calculations for Total Records processed, Average Package (Salary), and Highest Package offering.
- **🔍 Multi-Select Sidebar Filters:** Instantly filters the global dataframe configuration dynamically based on selectable enterprise/company values.
- **💰 Rich Data Visualizations:** - **Salary Distribution:** An interactive Plotly histogram tracking package density curves.
  - **Company Hiring Velocity:** A vertical categorical bar chart displaying overall student hire volumes per organization.
- **🏆 Leaderboard Generation:** Extracts and isolates a dedicated preview sheet focusing exclusively on the Top 10 highest-paid individuals.

---

## 🛠️ Tech Stack & Requirements

The operational landscape runs completely on an agile, data-focused Python configuration:
- **Framework UI:** `streamlit` (App state architecture & dashboard widgets)
- **Data Wrangling:** `pandas` (Matrix filtering, sorting, aggregation logic)
- **Charting Engine:** `plotly` (Responsive, hoverable vector charts)

---

## 📂 Repository Layout

```text
├── app.js               # Main layout coordinator (if extended to frontend web viewports)
├── app.py               # Streamlit application containing metrics, dashboard filters, and charts
└── requirements.txt     # Python dependency installation ledger
