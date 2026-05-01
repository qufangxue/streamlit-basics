import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="st.write() MVP",
    page_icon="🍒",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.streamlit.io/help',
        'Report a bug': "https://www.streamlit.io/bug",
        'About': "# 这是一个示例页面，用来演示 st.write 的效果。",
    }
)

st.title("st.write() MVP 🍒")

name = st.text_input("请输入你的名字")

try:
    age = st.number_input("请输入你的年龄", min_value=0, max_value=100, value=20)
except:
    st.write("请输入有效的年龄")
    age = 0

gender = st.selectbox("请选择你的性别", ["男", "女"])
city = st.text_input("请输入你的城市")

if name:
    st.write(f"你好，{name}！欢迎使用 st.write() MVP 🍒")

    df = pd.DataFrame({
        "名字": [name],
        "年龄": [age],
        "性别": [gender],
        "城市": [city]
    })

    st.write("你的数据表：", df)
