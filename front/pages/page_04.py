import streamlit as st 


st.title('Описание работы сервиса')
# st.markdown(f"<h2 style='text-align: center;'>Здесь можно найти основную информацию про модели и идею мини-проектика...</h2>", unsafe_allow_html=True)
st.write('Здесь можно найти основную информацию про использованные модели и идею мини-проектика...')

st.divider()

st.markdown(f"<h3 style='text-align: center;'>Какие модели используются?</h3>", unsafe_allow_html=True)

st.divider()

col1, col2, col3 = st.columns(spec=[0.6, 0.4, 0.4])
with col1:
    st.markdown(f"<h5 style='text-align: center;'>Первая модель:</h5>", unsafe_allow_html=True)

col4, col5, col6 = st.columns(spec=[0.2, 0.6, 0.3])
with col5:
    st.markdown(
        f"<h4 style='text-align: center; font-weight: bold;'>"
        f"ResNet34 - <a href='https://pytorch.org/hub/pytorch_vision_resnet/' target='_blank' style='color: #007bff; text-decoration: none; font-weight: bold;'>модель-тут</a>"
        f"</h4>",
        unsafe_allow_html=True
    )

col7, col8, col9 = st.columns(spec=[0.4, 0.4, 0.6])
with col9:
    st.markdown(f"<h5 style='text-align: center;'>Использовалась предобученная на ImageNet версия, способная классифицировать 1000 классов изображений</h5>", unsafe_allow_html=True)

st.divider()

col10, col11, col12 = st.columns(spec=[0.6, 0.4, 0.4])
with col10:
    st.markdown(f"<h5 style='text-align: center;'>Вторая модель:</h5>", unsafe_allow_html=True)

col13, col14, col15 = st.columns(spec=[0.2, 0.6, 0.3])
with col14:
    st.markdown(
        f"<h4 style='text-align: center; font-weight: bold;'>"
        f"MobileNet_v2 - <a href='https://pytorch.org/hub/pytorch_vision_mobilenet_v2/' target='_blank' style='color: #007bff; text-decoration: none; font-weight: bold;'>модель-тут</a>"
        f"</h4>",
        unsafe_allow_html=True
    )

col16, col17, col18 = st.columns(spec=[0.4, 0.4, 0.6])
with col18:
    st.markdown(f"<h5 style='text-align: center;'>Так же предобучена на ImageNet c использованием 1000 классов. Менее точна, чем ResNet в виду своей более легкой структуры</h5>", unsafe_allow_html=True)

st.divider()

col10, col11, col12 = st.columns(spec=[0.6, 0.4, 0.4])
with col10:
    st.markdown(f"<h5 style='text-align: center;'>Третья модель:</h5>", unsafe_allow_html=True)

col13, col14, col15 = st.columns(spec=[0.2, 0.6, 0.3])
with col14:
    st.markdown(
        f"<h4 style='text-align: center; font-weight: bold;'>"
        f"distilBERT - <a href='https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english' target='_blank' style='color: #007bff; text-decoration: none; font-weight: bold;'>модель-тут</a>"
        f"</h4>",
        unsafe_allow_html=True
    )

col16, col17, col18 = st.columns(spec=[0.4, 0.4, 0.6])
with col18:
    st.markdown(f"<h5 style='text-align: center;'>Специализированная версия модели для классификации текста с учетом эмоциональных окрасок. Только на английском</h5>", unsafe_allow_html=True)

st.divider()

col10, col11, col12 = st.columns(spec=[0.6, 0.4, 0.4])
with col10:
    st.markdown(f"<h5 style='text-align: center;'>Четвертая модель:</h5>", unsafe_allow_html=True)

col13, col14, col15 = st.columns(spec=[0.2, 0.6, 0.3])
with col14:
    st.markdown(
        f"<h4 style='text-align: center; font-weight: bold;'>"
        f"XLM-RoBERTa - <a href='https://huggingface.co/xlm-roberta-base' target='_blank' style='color: #007bff; text-decoration: none; font-weight: bold;'>модель-тут</a>"
        f"</h4>",
        unsafe_allow_html=True
    )

col16, col17, col18 = st.columns(spec=[0.4, 0.4, 0.6])
with col18:
    st.markdown(f"<h5 style='text-align: center;'>Мультиязыковая модель, не обученная для классификации текста - потому чаще ошибается. Зато в рекомендациях работает лучше</h5>", unsafe_allow_html=True)

st.divider()

st.header('Общие выводы')
st.markdown(
    f"<h5 style='text-align: center;'>"
    f"Основные проблемы возникли с некоторыми ошибками в написании сервера - одна пропущенная запятая забрала слишком много времени... "
    f"Работать с FastAPI - не так сложно, как может показаться. Что по моделям? В картинка лучше справляется ResNet - и это естественно, она сильнее, чем упрощенная MobileNet_v2. "
    f"По тексту - лучше справляется DistilBERT - но только английский текст. RoBERTa старается - и иногда удачно угадывает - но все же не предназначена для подобной работы."
    f"</h5>", unsafe_allow_html=True)

st.divider()

st.header('Какие улучшения можно добавить?')
st.markdown(
    f"<h5 style='text-align: center;'>"
    f"Поменять RoBERTa на более подходящую модель - или обучить ее... Добавить функционал - генерация текста, разметка классов на картинках, рекомендательная система."
    f"</h5>", unsafe_allow_html=True)
