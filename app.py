import streamlit as st

st.title("我的學習名片")
st.write("歡迎來到我的個人學習空間！")

st.subheader("基本資料")
name = st.text_input("請輸入姓名")
interest = st.text_input("請輸入感興趣的資訊主題")

if st.button("建立我的學習名片"):
    if name.strip() == "" or interest.strip() == "":
        st.warning("請完整輸入姓名與興趣主題！")
    else:
        st.success("資料已成功送出！")
        st.write("### 我的學習名片")
        st.write("姓名：", name)
        st.write("興趣主題：", interest)
        st.write("我的學習目標：熟悉 Python 程式設計")
        st.write("我正在學習 Python，")
        st.write("希望透過程式解決生活中的問題。")
