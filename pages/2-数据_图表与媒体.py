import numpy as np
import pandas as pd
import streamlit as st

PAGE_LINK = (
    "https://teddyhuang-00.github.io/posts/2023/01/streamlit-tutorial-data-chart-media"
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
    # dataframe 数据框
    st.dataframe(
        # 数据框对象
        {"a": [1, 2], "b": [3, 4]},
        # 可以指定显示宽高（默认根据适应内容大小）
        width=200,
        height=100,
    )
    st.dataframe(
        # 数据框可以是 pandas.DataFrame, pandas.Styler,
        # pyarrow.Table, numpy.ndarray, pyspark.sql.DataFrame,
        # snowflake.snowpark.dataframe.DataFrame,
        # snowflake.snowpark.table.Table, Iterable, dict 或者 None
        pd.DataFrame({"a": [1, 2], "b": [3, 4]}),
        # 可以指定使用父容器宽度（优先级高于指定宽度）
        use_container_width=True,
    )

    # table 表格
    st.table(
        # 接受的数据框对象与 dataframe 一致
        {"a": [1, 2], "b": [3, 4]},
    )

    # metric 度量
    st.metric(
        # 标签文本语法同 markdown
        "这是度量的标签",
        # 值（大字部分）
        value=100,
        # 增量（小字部分）
        delta=2,
        # 增量颜色（normal 为正常「增绿减红」，inverse 为相反，off 为灰色）
        delta_color="normal",
        # 说明文本仅支持普通 str
        help="这是度量的说明",
        # 标签可见性（visible 为显示，hidden 为隐藏）
        label_visibility="visible",
    )
    st.metric(
        "delta 的颜色会根据是否为负号开头为来决定，如为 None 则显示为灰色",
        # value 支持 str, int, float, None
        value="100",
        # delta 支持 str, int, float, None
        delta="-2",
        help="更改 delta_color 为 inverse 则颜色相反，为 off 则一律为灰色",
    )

    # json
    st.json(
        # 接受可以被序列化为 JSON 的对象
        # 或者一个 JSON 序列化后的 str
        [1, 2, {"key": "value"}],
        # 展开状态（默认为 True 全部展开）
        expanded=True,
    )

    # line_chart 折线图
    st.line_chart(
        # 数据框，支持对象类型同 dataframe
        pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"]),
        # x 轴数据，None 则使用索引，否则应为数据框中的列名
        x=None,
        # y 轴数据，None 则使用所有列，否则应为数据框中的列名
        y=["a", "b", "c"],
        # 指定宽度（0 则自动选择）
        width=0,
        # 指定高度（0 则自动选择）
        height=0,
        # 使用父容器宽度（优先级高于指定宽度）
        use_container_width=True,
    )

    # area_chart 区域图
    st.area_chart(
        # 参数说明同 line_chart
        pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"]),
    )

    # bar_chart 柱状图
    st.bar_chart(
        # 参数说明同 line_chart
        pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"]),
    )

    # 以下均为显示第三方库图表的方法，不作详细介绍
    # st.pyplot
    # st.altair_chart
    # st.vega_lite_chart
    # st.plotly_chart
    # st.bokeh_chart
    # st.pydeck_chart
    # st.graphviz_chart

    # map 地图
    st.map(
        # 数据框必须包含经纬度
        pd.DataFrame(
            np.random.randn(100, 2) / [150, 150] + [39.990, 116.305],
            columns=[
                # 纬度列名：lat, latitude, LAT, LATITUDE 之一
                "lat",
                # 经度列名：lon, longitude, LON, LONGITUDE 之一
                "lon",
            ],
        ),
        # 初始缩放倍数，详见 https://wiki.openstreetmap.org/wiki/Zoom_levels
        zoom=13,
    )

    # image 图像
    st.image(
        # 可以直接传入图像路径或 URL，支持列表传入多个图像链接
        "https://streamlit.io/images/brand/streamlit-mark-color.svg",
        # 图片说明
        caption="这是 Streamlit 的 logo",
        # 使用父容器宽度（优先级高于指定宽度）
        use_column_width=True,
    )
    st.image(
        # 也可以传入图像数据，比如 numpy.ndarray, [numpy.ndarray] 或 BytesIO
        np.random.randint(0, 256, (100, 100, 3)),
        # 指定宽度
        width=200,
        # 设置截断，为 True 时传入 0-255 范围外的值会被截断，否则报错
        clamp=True,
        # 通道顺序，RGB 或 BGR
        channels="RGB",
        # 图片显示格式，可选 JPEG, PNG 或 auto，auto 时根据图像数据自动选择
        output_format="auto",
    )

    # audio 音频
    st.audio(
        # 与 image 类似可以直接传入音频路径或 URL，支持列表传入多个
        # 这里演示传入音频数据，生成两秒 440Hz 的正弦波，采样率为 44.1kHZ
        np.sin(440 * np.linspace(0, 2, 2 * 44100, False) * 2 * np.pi),
        # 采样率，仅当传入 numpy.ndarray 时需要
        sample_rate=44100,
        # 音频开始播放时间，单位秒
        start_time=0,
        # 格式需要与文件或数据匹配，详见 https://tools.ietf.org/html/rfc4281
        format="audio/wav",
    )

    # video 视频
    st.video(
        # 与 image 类似可以直接传入视频路径或 URL，支持列表传入多个
        # 也可以是 BytesIO, Bytes 或 numpy.ndarray
        "./assets/Streamlit-hello.webm",
        # 视频开始播放时间，单位秒
        start_time=0,
        # 格式需要与文件或数据匹配，详见 https://tools.ietf.org/html/rfc4281
        format="video/webm",
    )
