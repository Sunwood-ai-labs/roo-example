"""
基本情報ページのコンポーネントを管理するモジュール
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from data.cat_data import CAT_FEATURES, BREED_DATA, ACTIVITY_DATA

def show_cat_features():
    """猫の特徴を表示する"""
    st.subheader("猫の特徴")
    st.markdown("\n".join([f"- {feature}" for feature in CAT_FEATURES]))

def show_breed_chart():
    """猫の品種チャートを表示する"""
    st.subheader("主な品種")
    df_breeds = pd.DataFrame(BREED_DATA)
    st.bar_chart(df_breeds.set_index("品種名"))

def show_activity_chart():
    """猫の行動パターンチャートを表示する"""
    st.subheader("猫の行動パターン")
    df_activities = pd.DataFrame(ACTIVITY_DATA)
    fig = px.pie(df_activities, values="時間割合", names="活動", title="1日の活動割合")
    st.plotly_chart(fig)

def render_basic_info_page():
    """基本情報ページを表示する"""
    col1, col2 = st.columns(2)
    
    with col1:
        show_cat_features()
        show_breed_chart()
    
    with col2:
        show_activity_chart()
