import streamlit as st 
import requests



st.title('Классификация текста')
st.write('Полное описание работы модели смотри на странице 4')

txt = st.text_input('Введите текст для классификации сюда!')
res = None

col1, col2, col3, col4, col5 = st.columns(5)
with col2:
    if st.button('Используем DistilBERT') and txt is not None:
        text = {'text': txt}
        res = requests.post('http://127.0.0.1:8000/clf_text_distilbert', json=text)

with col4:
    if st.button('Используем XLM-RoBERTa') and txt is not None:
        text = {'text': txt}
        res = requests.post('http://127.0.0.1:8000/clf_text_roberta', json=text)

if res is not None:
    prob = round(res.json()['prob'], 2) * 100
    col6, col7, col8 = st.columns(spec=[0.2, 0.6, 0.2])
    if res.json()['label'] == 'Положительный':
        with col7:
            st.image("images/good_girl.jpg", width=500)
        st.markdown(f"<h2 style='text-align: center;'>С..С..Семпаи.. Ты..Ты так добр... o(≧▽≦)o</h2>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='text-align: center;'>Я считаю тебя.. Хорошим семпаем.. И я уверена в этом.. На <b>{prob}%</b>!</h4>", unsafe_allow_html=True)
    
    if res.json()['label'] == 'Негативный':
        with col7:
            st.image("images/bad_girl.jpg", width=400)
        st.markdown(f"<h2 style='text-align: center;'>Ах ты маленький комнатный воин...Не стыдно тебе? (￢‿￢ )</h2>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='text-align: center;'>Ты у нас плохиш, да? Я уверена на <b>{prob}%</b>, что ты заслужил наказание...</h4>", unsafe_allow_html=True)