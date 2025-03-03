import streamlit as st


st.title('Оглавление')

st.write('-------------------------------------------------------------------------------------')

col1, col2 = st.columns(spec=[0.3, 0.7])
with col1:
    st.image('images/page01.png', width=100)
with col2:
    st.write('Страница 1')
    st.page_link('pages/page_01.py', label='Оглавление')

st.write('-------------------------------------------------------------------------------------')

col3, col4 = st.columns(spec=[0.3, 0.7])
with col3:
    st.image('images/page02.png', width=100)
with col4:
    st.write('Страница 2')
    st.page_link('pages/page_02.py', label='Классификация изображения')

st.write('-------------------------------------------------------------------------------------')

col5, col6 = st.columns(spec=[0.3, 0.7])
with col5:
    st.image('images/page03.png', width=100)
with col6:
    st.write('Страница 3')
    st.page_link('pages/page_03.py', label='Классификация текста')

st.write('-------------------------------------------------------------------------------------')

col7, col8 = st.columns(spec=[0.3, 0.7])
with col7:
    st.image('images/page04.png', width=100)
with col8:
    st.write('Страница 4')
    st.page_link('pages/page_04.py', label='Описание проекта')

st.write('-------------------------------------------------------------------------------------')