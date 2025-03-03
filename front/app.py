import streamlit as st 


page01 = st.Page('pages/page_01.py', title='1. Оглавление ->')
page02 = st.Page('pages/page_02.py', title='2. Классификация изображения')
page03 = st.Page('pages/page_03.py', title='3. Классификация текста')
page04 = st.Page('pages/page_04.py', title='4. Описание проекта')

pg = st.navigation(
    [
        page01,
        page02,
        page03,
        page04
        ], expanded=True)
    
pg.run()

st.sidebar.title('Кто сие создатель?')
st.sidebar.markdown('<a href="https://github.com/RenaTheDv" target="_blank">Зарницына Алина/RenaTheDv</a>', unsafe_allow_html=True)