# st.set_page_config

## 是什么？

1. st.set_page_config 就是用来设置 Streamlit 页面外观的，比如标题、图标、布局、侧边栏和菜单。
2. st.set_page_config 只负责页面外观（标题、图标、布局、菜单），它本身不会渲染任何内容。

---

## 我的尝试1

```
import streamlit as st
import pandas as pd

页面配置

st.set_page_config(
    page_title="我的第一个 MVP",
    page_icon="🚀",
    layout="wide",  # 改成 "centered" 看区别
    initial_sidebar_state="expanded",  # 改成 "collapsed" 看区别
    menu_items={
        'Get Help': 'https://www.streamlit.io/help',
        'Report a bug': "https://www.streamlit.io/bug",
        'About': "# 这是一个示例页面，用来演示 st.set_page_config 的效果。",
    }
)

页面内容

st.write("👋 欢迎来到我的第一个 MVP 页面！")

加一个宽表格，方便观察布局变化

df = pd.DataFrame({"数字": range(100)})
st.dataframe(df)

侧边栏内容

st.sidebar.write("这里是侧边栏内容")
```

---

## 我的尝试2

```
import streamlit as st
import pandas as pd

页面配置

st.set_page_config(
    page_title="我的第一个 MVP",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.streamlit.io/help',
        'Report a bug': "https://www.streamlit.io/bug",
        'About': "# 这是一个示例页面，用来演示 st.set_page_config 的效果。",

}

)

主页面内容

st.write("👋 欢迎来到我的第一个 MVP 页面！")

df = pd.DataFrame({"数字": range(100)})
st.dataframe(df)

侧边栏功能

st.sidebar.header("侧边栏功能区")

输入框

name = st.sidebar.text_input("请输入你的名字")

下拉选择

option = st.sidebar.selectbox(
    "选择一个功能",
    ["显示欢迎语", "显示表格", "显示数字平方"]
)

按钮

if st.sidebar.button("运行功能"):
    if option == "显示欢迎语":
        st.write(f"你好，{name if name else '访客'}！欢迎使用 MVP 页面 🚀")
    elif option == "显示表格":
        st.write("这是一个示例表格：")
        st.dataframe(df)
    elif option == "显示数字平方":
        st.write("数字平方：")
        st.write([x**2 for x in range(10)])
```

