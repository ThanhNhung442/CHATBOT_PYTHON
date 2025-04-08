import streamlit as st
import os
from openai import OpenAI

# Tạo client mới với API key từ biến môi trường
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Giao diện Streamlit
st.title("Chatbot Python - Trợ lý học Python cho học sinh THPT Sông Công")
st.write("Chào mừng bạn đến với Chatbot hỗ trợ học Python!")
st.write("Hãy nhập câu hỏi của bạn về lập trình Python và nhận câu trả lời ngay nhé.")

# Nhập câu hỏi từ học sinh
question = st.text_input("Nhập câu hỏi của bạn:")

# Xử lý câu hỏi
if question:
    try:
        # Gửi câu hỏi tới ChatGPT
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Bạn là trợ lý dạy Python cho học sinh THPT. Trả lời ngắn gọn, dễ hiểu, ví dụ minh họa rõ ràng."},
                {"role": "user", "content": question}
            ]
        )
        # Hiển thị câu trả lời
        answer = response.choices[0].message.content
        st.write("Chatbot trả lời:")
        st.success(answer)

    except Exception as e:
        st.error(f"Đã xảy ra lỗi: {e}")
