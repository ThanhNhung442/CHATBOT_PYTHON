import streamlit as st
import openai

# Cô nhập API key tại đây
openai.api_key = "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"

# Tiêu đề giao diện
st.title("Chatbot Python - Trợ lý học Python cho học sinh THPT (GPT-4o)")

# Hướng dẫn sử dụng
st.write("Chào mừng bạn đến với Chatbot hỗ trợ học Python!")
st.write("Hãy nhập câu hỏi của bạn về lập trình Python và nhận câu trả lời ngay nhé.")

# Ô nhập câu hỏi của học sinh
question = st.text_input("Nhập câu hỏi của bạn:")

# Xử lý khi có câu hỏi
if question:
    try:
        # Gọi API ChatGPT-4o
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": question}]
        )
        # Hiển thị câu trả lời
        answer = response['choices'][0]['message']['content']
        st.write("Chatbot trả lời:", answer)

    except Exception as e:
        st.error(f"Đã xảy ra lỗi: {e}")
        st.info("Vui lòng kiểm tra lại API Key hoặc kết nối mạng.")

# Lưu ý cho học sinh
st.markdown("---")
st.write("📌 Lưu ý: Chatbot hỗ trợ các câu hỏi về Python cơ bản như: khai báo biến, kiểu dữ liệu, vòng lặp, hàm, xử lý lỗi,...")
