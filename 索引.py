import streamlit as st
from streamlit_ace import st_ace

PAGE_LINK = "https://teddyhuang-00.github.io/posts/2023/01/streamlit-tutorial-preface"

st.set_page_config(
    "Streamlit 教程",
    "📚",
    layout="wide",
    menu_items={
        "Get help": PAGE_LINK + "#comment",
        "Report a bug": PAGE_LINK + "#comment",
        "About": "教程正文见" + PAGE_LINK,
    },
)

st.title("Streamlit 教程")

"⬅️点击左侧选择章节开始阅读"

THEMES = [
    "ambiance",
    "chaos",
    "chrome",
    "clouds",
    "clouds_midnight",
    "cobalt",
    "crimson_editor",
    "dawn",
    "dracula",
    "dreamweaver",
    "eclipse",
    "github",
    "gob",
    "gruvbox",
    "idle_fingers",
    "iplastic",
    "katzenmilch",
    "kr_theme",
    "kuroir",
    "merbivore",
    "merbivore_soft",
    "mono_industrial",
    "monokai",
    "nord_dark",
    "pastel_on_dark",
    "solarized_dark",
    "solarized_light",
    "sqlserver",
    "terminal",
    "textmate",
    "tomorrow",
    "tomorrow_night",
    "tomorrow_night_blue",
    "tomorrow_night_bright",
    "tomorrow_night_eighties",
    "twilight",
    "vibrant_ink",
    "xcode",
]

KEYBINDINGS = ["emacs", "sublime", "vim", "vscode"]

if "code" not in st.session_state:
    st.session_state[
        "code"
    ] = """import pandas as pd

st.header("Streamlit 游乐场🎠")
st.write("你可以在网页里看到实时运行的结果！")
table_data = {"A": [1, 2], "B": [3, 4]}
st.write(pd.DataFrame(data=table_data))
"""

st.sidebar.subheader("编辑器设置")
st.sidebar.radio("布局方式", ["垂直分屏", "水平分屏"], index=0, key="layout", horizontal=True)
st.sidebar.select_slider(
    "分屏比例",
    range(11),
    5,
    format_func=lambda x: f"{x+1}:{11-x}",
    key="split",
    disabled=st.session_state["layout"] == "垂直分屏",
)
if st.session_state["layout"] == "垂直分屏":
    editor = st.container()
    output = st.container()
else:
    editor, output = st.columns(
        [st.session_state["split"] + 1, 11 - st.session_state["split"]]
    )

with editor:
    "⬇️这里可以编辑代码"
    "按 Ctrl/Cmd+回车 或右下角按钮来应用变更，除 `streamlit` 外还支持 `numpy`、`pandas`、`matplotlib`、`seaborn`、`plotly` 等库"
    st.session_state["code"] = st_ace(
        value=st.session_state["code"],
        language="python",
        placeholder="st.header('Hello world!')",
        theme=st.sidebar.selectbox("主题", options=THEMES, index=22) or "monokai",
        keybinding=st.sidebar.selectbox("按键绑定", options=KEYBINDINGS, index=3)
        or "vscode",
        font_size=st.sidebar.slider("字号大小", 5, 24, 14),
        tab_size=st.sidebar.slider("制表符大小", 1, 8, 4),
        wrap=st.sidebar.checkbox("软换行", value=False),
        show_gutter=True,
        show_print_margin=True,
        auto_update=False,
        readonly=False,
        key="editor",
    )

with output:
    "⬇️这里显示输出结果"
    exec(st.session_state["code"])
