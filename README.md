# 🏎️ Max Verstappen 2027 Team Recommendation Dashboard

This project aims to recommend the **best possible F1 team + teammate combination** for **Max Verstappen** in the 2027 Formula 1 season using data analysis and visualization.

It features **two interactive dashboards** — one built with **Streamlit** (Python) and another in **Power BI** — to explore and visualize combo scores based on historical F1 performance metrics.


## 📌 Project Overview

- 🔍 Analyzes team and driver data from 2019–2024
- 📊 Calculates scores for team, teammate, and overall combination
- 🧠 Recommends top teams and drivers Max Verstappen could pair with
- 🎯 Visual insights through gauges, bar charts, funnel views, and more

---

## 🚀 Streamlit Dashboard (Python)

The **Streamlit app** allows you to interactively select a team and teammate and instantly see:

- Combo Fit Gauge Score
- Team and Teammate Score Metrics
- Top 5 Combination Bar Chart
- Visual Preview (Team + Teammate Images)
- Funnel of Top 3 Combos


<img width="1920" height="1080" alt="Screenshot (82)" src="https://github.com/user-attachments/assets/21072352-f990-4b8e-836d-22e66384c08b" />

📸 Power BI Dashboard Preview


<img width="1920" height="1080" alt="Screenshot (82)" src="https://github.com/user-attachments/assets/30306371-7f73-4fee-bbd2-b1db8dd0b21b" />

📈 Score Calculation
Team Score: Based on constructor’s points, wins, DNFs

Teammate Score: Based on podiums, fastest laps, consistency

Combo Score: Average of Team Score & Teammate Score (0 to 1 scale)

🛠️ Tools & Technologies
Python, Pandas, Matplotlib, Plotly

Streamlit (for web app)

Power BI (for BI dashboard)

Google Sheets (image hosting)

Git & GitHub (version control)

📂 Data Source
Processed F1 dataset (from Ergast API/Kaggle F1 archives)

Manually curated teammate and team images
