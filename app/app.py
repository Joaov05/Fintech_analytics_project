import streamlit as st
import pandas as pd

from data_loader import load_data
from metrics import get_funnel_data, calculate_kpis, activation_trend
from charts import funnel_chart, user_growth_chart, activation_chart

# Config
st.set_page_config(layout="wide")

users, events, transactions, accounts = load_data()

# =========================
# KPIs
# =========================
kpis = calculate_kpis(users, events, transactions)

st.title("📊 Fintech Analytics Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Users", kpis["total_users"])
col2.metric("Signup Completed", kpis["signup_completed"])
col3.metric("Activated Users", kpis["activated_users"])
col4.metric("Activation Rate", f"{kpis['activation_rate']:.2%}")

# =========================
# FUNNEL
# =========================
funnel_dict = get_funnel_data(events, transactions)

funnel_df = pd.DataFrame({
    "stage": list(funnel_dict.keys()),
    "users": list(funnel_dict.values())
})

activation_df = activation_trend(events, transactions, accounts)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Conversion Funnel")
    st.plotly_chart(funnel_chart(funnel_df), width="stretch")

with col2:
    st.subheader("User Growth per Month")
    st.plotly_chart(user_growth_chart(users), width="stretch")

st.subheader("Activation Trend per Month")
st.plotly_chart(activation_chart(activation_df), width="stretch")