import streamlit as st
import pandas as pd

def main():
    st.title("GDB9 CSV Viewer")
    
    uploaded_file = st.file_uploader("Upload gdb9.sdf.csv", type=["csv"])
    if uploaded_file is not None:
        # 1) Load into a Pandas DataFrame
        df = pd.read_csv(uploaded_file)
        
        # 2) Display the first few rows
        st.write("Preview of the dataset:")
        st.dataframe(df.head(20))
        
if __name__ == "__main__":
    main()

