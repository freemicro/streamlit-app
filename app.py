import streamlit as st
import torch

st.title("Streamlit + PyTorch App")

# Create a tensor
data = [1, 2, 3, 4, 5]
tensor = torch.tensor(data)

st.write("Tensor Output:")
st.write(tensor)

st.write("Tensor Shape:")
st.write(tensor.shape)