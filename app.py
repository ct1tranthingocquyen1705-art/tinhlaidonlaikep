import streamlit as st

st.title("Tính tiền gửi tiết kiệm")

# Nhập dữ liệu
C = st.number_input("Nhập số tiền gửi (triệu đồng):", min_value=0.0, format="%.2f")
i = st.number_input("Nhập lãi suất tiết kiệm theo năm (ví dụ 0.06 cho 6%):", min_value=0.0, format="%.4f")
n = st.number_input("Nhập số tháng gửi:", min_value=1, step=1)

# Nút tính toán
if st.button("Tính"):
    # Lãi đơn
    A = C * (1 + i * n / 12)

    # Lãi kép
    B = C * (1 + i / 12) ** n

    st.subheader("Kết quả")
    st.write(f"**Tổng số tiền nhận được theo lãi đơn:** {A:,.4f} triệu đồng")
    st.write(f"**Tổng số tiền nhận được theo lãi kép:** {B:,.4f} triệu đồng")
