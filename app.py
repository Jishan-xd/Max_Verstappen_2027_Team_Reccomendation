import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Max 2027 Team Predictor", layout="wide", initial_sidebar_state="expanded")

# ---------- INIT SESSION STATE ----------
if 'page' not in st.session_state:
    st.session_state.page = "dashboard"

# ---------- LOAD DATA ----------
df = pd.read_csv("max_verstappen_2027_team_prediction.csv")

# ---------- SIDEBAR ----------
st.sidebar.title("🏎️ F1 2027 - Max Verstappen Predictor")

# About Section
st.sidebar.subheader(" About This Dashboard")
st.sidebar.markdown("""
This dashboard helps predict the **best possible F1 team and teammate** for **Max Verstappen** in the 2027 season.

Select Team and Teammate to check the score.
""")

# Dropdowns (just below about)
team = st.sidebar.selectbox("Select Team", df['team_name'].unique())
filtered_df = df[df['team_name'] == team]
teammate = st.sidebar.selectbox("Select Teammate", filtered_df['teammate'].unique())
selected_row = filtered_df[filtered_df['teammate'] == teammate].iloc[0]

#  Navigation buttons
st.sidebar.markdown("---")
if st.sidebar.button(" Dashboard"):
    st.session_state.page = "dashboard"
if st.sidebar.button("Details"):
    st.session_state.page = "about"

# ---------- ABOUT PAGE ----------
if st.session_state.page == "about":
    st.title("About This Project")
    st.markdown("""
    Project Overview  
    This dashboard predicts the **best team and teammate** for **Max Verstappen** in the 2027 F1 season  
    using historical F1 data (2019–2024).

    Problem Statement  
    With uncertainty about Max's future in F1, this tool finds the best **constructor + teammate** combo.

    Graphs Explained  
    - **Gauge**: Strength of team-teammate fit.  
    - **Bar Charts**: Score breakdown and Top 5 combinations.  
    - **Funnel**: Top 3 combos visually.  
    - **Images**: Shows actual team and driver images.

    Scoring Logic  
    - **Team Score**: Based on average points, wins, and DNFs.  
    - **Teammate Score**: Based on podiums, fastest laps, consistency.  
    - **Combo Score**: Average of Team & Teammate score (0-1 scale).

    Tools Used  
    Python, Pandas, Matplotlib, Plotly, Streamlit

    Data Source  
    Processed F1 dataset from [Ergast API / Kaggle].

    ---
    _Made by Jishan Ansari
    """)

# ---------- DASHBOARD ----------
elif st.session_state.page == "dashboard":
    # --- Top Header with Max Image and Title ---
    col_img, col_title = st.columns([1, 5])
    with col_img:
        st.image(
            "https://cdn-2.motorsport.com/images/mgl/6D1XbeV0/s800/max-verstappen-red-bull-racing.jpg",
            width=200
        )
    with col_title:
        st.title(" Max Verstappen - 2027 Team Fit Prediction")
        st.markdown("Use data from recent seasons to identify the **most compatible team & teammate** for Max Verstappen.")
        st.markdown("---")

    # --- Visual Preview: Team Image + Gauge + Teammate Image ---
    st.subheader("Visual Preview + Fit Score")
    col_img1, col_gauge, col_img2 = st.columns([1, 2, 1])

    with col_img1:
        st.image(selected_row['team_image_url'], width=200)
        st.caption(f"🏎️ Team: {selected_row['team_name'].title()}")

    with col_gauge:
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=selected_row['combo_score'],
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Combo Fit Score", 'font': {'size': 18}},
            delta={'reference': 0.75, 'increasing': {'color': "green"}},
            gauge={
                'axis': {'range': [0, 1], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': "royalblue"},
                'steps': [
                    {'range': [0, 0.6], 'color': 'lightcoral'},
                    {'range': [0.6, 0.8], 'color': 'gold'},
                    {'range': [0.8, 1], 'color': 'lightgreen'}
                ],
                'threshold': {
                    'line': {'color': "black", 'width': 4},
                    'thickness': 0.75,
                    'value': selected_row['combo_score']
                }
            }
        ))
        fig_gauge.update_layout(height=300)
        st.plotly_chart(fig_gauge, use_container_width=True)

    with col_img2:
        st.image(selected_row['driver_image_url'], width=200)
        st.caption(f" Teammate: {selected_row['teammate'].title()}")

    st.markdown("---")

    # --- Metric Summary ---
    st.subheader("Combo Score Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Team Score", f"{selected_row['team_score']:.3f}")
    col2.metric("Teammate Score", f"{selected_row['driver_score']:.3f}")
    col3.metric("Combo Score", f"{selected_row['combo_score']:.3f}")

    st.markdown("---")

    # --- Score Breakdown Bar Chart ---
    st.subheader("Score Breakdown")
    labels = ['Team Score', 'Teammate Score', 'Combo Score']
    values = [
        selected_row['team_score'],
        selected_row['driver_score'],
        selected_row['combo_score']
    ]
    fig2, ax2 = plt.subplots(figsize=(7, 3))
    ax2.barh(labels, values, color=['#FF595E', '#1982C4', '#6A4C93'])
    ax2.set_xlim(0, 1)
    ax2.set_xlabel("Score")
    ax2.set_title("Performance Comparison")
    st.pyplot(fig2)

    st.markdown("---")

    # --- Top 5 Combos Chart ---
    st.subheader("Top 5 Combos Overall")
    top5 = df.sort_values(by='combo_score', ascending=False).head(5)
    top5_labels = top5['team_name'] + " + " + top5["teammate"]
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.barh(top5_labels, top5['combo_score'], color='skyblue')
    ax.invert_yaxis()
    ax.set_xlabel("Combo Score")
    ax.set_title("Top 5 Team + Teammate Combinations")
    st.pyplot(fig)

    st.markdown("---")

    # --- Funnel Chart ---
    st.subheader("Top 3 Combos (Funnel View)")
    top3 = df.sort_values(by='combo_score', ascending=False).head(3)
    fig_funnel = go.Figure(go.Funnel(
        y=[f"{r['team_name'].title()} + {r['teammate'].title()}" for _, r in top3.iterrows()],
        x=top3['combo_score'],
        textinfo="value+percent previous",
        marker={'color': ['#FF595E', '#1982C4', '#6A4C93']}
    ))
    fig_funnel.update_layout(height=400, margin=dict(l=50, r=50, t=40, b=40))
    st.plotly_chart(fig_funnel, use_container_width=True)
