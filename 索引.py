import streamlit as st

PAGE_LINK = "https://teddyhuang-00.github.io/posts/2023/01/streamlit-tutorial-preface"

st.set_page_config(
    "Streamlit 教程",
    "📚",
    menu_items={
        "Get help": PAGE_LINK + "#comment",
        "Report a bug": PAGE_LINK + "#comment",
        "About": "教程正文见" + PAGE_LINK,
    },
)

st.title("Streamlit 教程")

"⬅️点击左侧选择章节开始阅读"
