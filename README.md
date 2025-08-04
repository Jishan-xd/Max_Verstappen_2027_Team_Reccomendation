# 🏎️ Max Verstappen 2027 Team Recommendation Dashboard

This project predicts the **best team and teammate combination** for **Max Verstappen** in the 2027 F1 season using **data-driven analysis** and **interactive dashboards**.

It features **two dashboards**:
- **Streamlit App** (Python-based)
- **Power BI Dashboard**
- **Perform EDA tp predict and clean data**

---

## 📘 Overview

- Analyzes F1 data (2019–2024)
- Calculates:
  - 🏎️ Team Score
  - 🧑‍🤝‍🧑 Teammate Score
  - 🎯 Combo Score
- Suggests ideal team + teammate for Max Verstappen

---

## 🚀 Streamlit Dashboard

The **Streamlit app** lets you:

- Select team & teammate
- See Max Fit Gauge Score
- View team/teammate images
- Analyze top 5 combos
- Visualize funnel chart for top 3 fits

### 🔻 Screenshot:

<img width="1920" height="1080" alt="Screenshot (84)" src="https://github.com/user-attachments/assets/d9f63751-b7be-4121-826a-b5b53f19a85c" />

---

## 📊 Power BI Dashboard

Includes:

- Donut chart for top 3 combos
- Bar chart for top 5 combos
- Line graph showing all combination scores
- Image previews
- Interactive slicers for team & teammate

### 🔻 Screenshot:

<img width="1276" height="796" alt="Screenshot (83)" src="https://github.com/user-attachments/assets/c773b5a6-e685-46c4-a904-31ccf1922bb1" />

---

## 🧠 Score Calculation

- **Team Score**: Based on constructor’s points, wins, and DNFs  
- **Teammate Score**: Based on podiums, fastest laps, and consistency  
- **Combo Score**: Average of team + teammate score (scaled 0–1)

---

## 🛠️ Tech Stack

- Python (Pandas, Plotly, Streamlit)
- Power BI
- Google Sheets (for hosting images)
- Git & GitHub

---

## 📂 Data Source

- Historical F1 data (Kaggle + Ergast API)
- Manually added team and driver images

---

--Made by Jishan Ansari--
