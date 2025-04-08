import streamlit as st
from openai import OpenAI

# Tạo client mới với API key
client = OpenAI(api_key="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")  # ← Thay bằng API Key thật của cô

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
                {"role": "system", "content": "Bạn là trợ lý dạy Python cho học sinh THPT. Trả lời ngắn gọn, dễ hiểu, ví dụ minh hoạ rõ ràng."},
                {"role": "user", "content": question}
            ]
        )
        # Hiển thị kết quả trả lời
        answer = response.choices[0].message.content
        st.write("Chatbot trả lời:")
        st.success(answer)

    except Exception as e:
        st.error(f"Đã xảy ra lỗi: {e}")
