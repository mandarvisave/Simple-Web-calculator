import streamlit as st
import requests

BACKEND_URL = 'http://127.0.0.1:5000'

st.title('Web Calculator App')

num1 = st.number_input('Enter first number', value=0.0, format='%f')
num2 = st.number_input('Enter second number', value=0.0, format='%f')
operation = st.selectbox('Select operation', ['Add', 'Subtract', 'Multiply', 'Divide'])

if st.button('Calculate'):
    endpoint_map = {
        'Add': 'add',
        'Subtract': 'subtract',
        'Multiply': 'multiply',
        'Divide': 'divide',
    }
    endpoint = endpoint_map[operation]
    try:
        response = requests.post(f'{BACKEND_URL}/{endpoint}', json={'a': num1, 'b': num2})
        data = response.json()
        if 'result' in data:
            st.success(f'Result: {data["result"]}')
        else:
            st.error(f'Error: {data.get("error", "Unknown error")}')
    except Exception as e:
        st.error(f'Error: {e}')
