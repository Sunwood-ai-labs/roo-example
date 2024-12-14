"""
統計データページのコンポーネントを管理するモジュール
"""
import streamlit as st
import pandas as pd
from data.cat_data import YEARLY_STATS, TREND_DATA

def show_yearly_statistics():
    """年間の猫の統計を表示する"""
    st.markdown("### 年間の猫の統計")
    df_yearly = pd.DataFrame(YEARLY_STATS)
    st.table(df_yearly)

def show_popularity_trend():
    """猫の人気度トレンドを表示する"""
    st.markdown("### 猫の人気度トレンド")
    df_trend = pd.DataFrame(TREND_DATA)
    st.line_chart(df_trend.set_index("年"))

def render_statistics_page():
    """統計データページを表示する"""
    st.subheader("猫の統計データ")
    show_yearly_statistics()
    show_popularity_trend()
