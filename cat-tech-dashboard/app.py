"""
猫猫テクノロジー ダッシュボードのメインアプリケーション
"""
import streamlit as st
from config import APP_CONFIG, PAGES, SIDEBAR_CONFIG
from pages.basic_info import render_basic_info_page
from pages.statistics import render_statistics_page

def setup_page():
    """ページの基本設定を行う"""
    st.set_page_config(
        page_title=APP_CONFIG["title"],
        page_icon=APP_CONFIG["icon"],
        layout=APP_CONFIG["layout"]
    )

def setup_header():
    """ヘッダーを設定する"""
    st.title(f"{APP_CONFIG['icon']} {APP_CONFIG['title']}")
    st.markdown("### 猫の技術革新をリードする")

def setup_sidebar():
    """サイドバーを設定する"""
    st.sidebar.header(SIDEBAR_CONFIG["title"])
    return st.sidebar.radio(
        SIDEBAR_CONFIG["page_selector_label"],
        PAGES
    )

def main():
    """メインアプリケーションの実行"""
    setup_page()
    setup_header()
    
    # ページ選択
    selected_page = setup_sidebar()
    
    # 選択されたページの表示
    if selected_page == "基本情報":
        render_basic_info_page()
    else:
        render_statistics_page()

if __name__ == "__main__":
    main()
