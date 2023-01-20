import streamlit as st

PAGE_LINK = (
    "https://teddyhuang-00.github.io/posts/2023/01/streamlit-tutorial-basic-output"
)

st.set_page_config(
    "Streamlit 教程",
    "📚",
    menu_items={
        "Get help": PAGE_LINK + "#comment",
        "Report a bug": PAGE_LINK + "#comment",
        "About": "教程正文见" + PAGE_LINK,
    },
)

with st.echo("below"):
    # Title 一级标题
    st.title(
        # 所有标题类函数支持的文本语法与 markdown 一致
        # 详见下文 markdown 处介绍
        "一级标题",
        # 所有标题类函数都可以添加额外的 anchor 参数来指定锚链接
        # 即 <URL>#<anchor> 的形式，默认使用标题名字作为锚名称，下同
        anchor="默认使用标题名",
    )

    # Header 二级标题
    st.header("二级标题")

    # Subheader 三级标题
    st.subheader("三级标题")

    # Text 纯文本
    st.text("纯文本")

    # Code 代码
    st.code(
        "print('Hello, world!') # 展示代码，使用 language 指定语言",
        # 默认显示语言为 Python，支持高亮的语言见
        # https://github.com/react-syntax-highlighter/react-syntax-highlighter/blob/master/AVAILABLE_LANGUAGES_PRISM.MD
        language="python",
    )

    # Markdown
    st.markdown(
        # 基础 Markdown 语法见 https://github.github.com/gfm
        # emoji 简码参考 https://share.streamlit.io/streamlit/emoji-shortcodes
        # 支持的 LaTeX 表达式见 https://katex.org/docs/supported.html
        "*GitHub*风格的**Markdown**:sunglasses:，"
        # 可添加的颜色仅有 blue, green, orange, red, violet
        + "可以给:blue[任意部分]添加:red[颜色]，"
        # 可以通过指定 unsafe_allow_html 参数来开启 HTML 渲染
        # 由于可能执行不安全的代码，因此默认情况下被关闭
        + "以及可选的 <b style='opacity: .5;'>HTML</b> 支持",
        unsafe_allow_html=True,
    )

    # Caption 说明文字
    st.caption(
        # 说明文字支持的文本语法与 markdown 一致
        # 并且同样支持 HTML 渲染
        "小号显示的说明文字"
    )

    # Latex
    st.latex(
        # LaTeX 表达式的支持同 markdown 中 LaTeX 部分
        # 也可以为 sympy 的表达式，会自动转换为 LaTeX
        r"""\LaTeX"""
    )

    # Write 万能输出
    st.write("write 不仅支持字符串，还可以是几乎任意对象类型，不限个数：", [], {}, ())

    # Magic 魔法方法
    """
    魔法方法指可以直接在 Python 代码中写下要输出的内容，类似于你在 notebook 中做的那样，
    同样会进行输出，效果同使用 st.write
    """

    # Echo 源代码
    with st.echo("above"):
        # 通过 st.echo 可以将源代码输出到页面中
        # 该函数接受一个参数，用于指定输出的位置，可选值有 "above" 和 "below"
        # 默认为 "below"
        st.write("只有在 st.echo 环境内的代码才会被输出")

    # Help 打印函数文档
    """你可以使用 st.help 来打印函数文档"""
    st.help(st.help)
