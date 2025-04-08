import streamlit as st
import openai

# Cấu hình API key
openai.api_key = "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"

# Tiêu đề giao diện
st.title("Chatbot Python - Trợ lý học Python cho học sinh THPT Sông Công")

# Hướng dẫn sử dụng
st.write("Chào mừng bạn đến với Chatbot hỗ trợ học Python!")
st.write("Hãy nhập câu hỏi của bạn về lập trình Python và nhận câu trả lời ngay nhé.")

# Nhập câu hỏi
question = st.text_input("Nhập câu hỏi của bạn:")

# Xử lý khi có câu hỏi
if question:
    try:
        # Gọi API ChatGPT-4o
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Bạn là trợ lý dạy Python dành cho học sinh THPT, hãy trả lời ngắn gọn và dễ hiểu."},
                {"role": "user", "content": question}
            ]
        )
        # Hiển thị câu trả lời
        answer = response.choices[0].message.content
        st.write("Chatbot trả lời:", answer)

    except Exception as e:
        st.error(f"Đã xảy ra lỗi: {e}")
