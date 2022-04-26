from app.excel_generator import *
import streamlit as st

header = st.container()
body = st.container()
emp = st.container()
sale = st.container()
down = st.container()

with header:
    st.title("The Excel Generator")
    st.markdown("#### generate an imaginary company database example \n #### to train your skills in sql , excel , tablau and others ")


with body:
    num_of_employees =  st.slider("chose the number of employees in your company"
              , min_value = 1)
    number_of_sales =  st.slider("chose how many sales which your employees acheived")

with emp:
    employees_table = st.button("click here to see your employees table")
    if employees_table:
        st.write(employees(num_of_employees))



with sale:
    sales_table = st.button("click here to see your sales table")
    if sales_table:
        st.write(sales(number_of_sales))
with down :
    down_button = st.button("Download your company database"  )
    if down_button :

        st.download_button("Employee Table", data=empp, file_name="generated_employments_table1.csv")
        st.download_button("Sales Table", data=sal, file_name="generated_employments_table2.csv")

