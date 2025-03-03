import requests
import streamlit as st 
from googletrans import Translator
from PIL import Image
from io import BytesIO


# функция для перевода названия классов
def translate_class_name(english_class:str) -> str:
    translator = Translator()
    translated = translator.translate(english_class, src='en', dest='ru')
    return translated.text

# функция загрузки картинки с интернета
def load_image_from_net(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img


st.title('Классификация изображения')
st.write('Полное описание работы модели смотри на странице 4')

uploaded_files = st.file_uploader("Загрузите изображения", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
image_urls = image_urls = st.text_area("Введите ссылки на изображения (работает, если нет загруженных файлов)")
res = None

if uploaded_files:
    img = Image.open(uploaded_files[0])
elif image_urls:
    urls = image_urls.splitlines()
    img = load_image_from_net(urls[0])

col1, col2, col3, col4, col5 = st.columns(5)
with col2:
    if st.button('Используем Resnet34') and img is not None:
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        files = {'file': buffered.getvalue()}
        res = requests.post('http://127.0.0.1:8000/clf_image_resnet34', files=files).json()

with col4:
    if st.button('Используем MobileNet_v2') and img is not None:
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        files = {'file': buffered.getvalue()}
        res = requests.post('http://127.0.0.1:8000/clf_image_mobilenet', files=files).json()

if res is not None:
    col6, col7, col8 = st.columns(spec=[0.2, 0.6, 0.2])
    with col7:
        st.image(img, width=400)

    imagenet_class = res['class_name']
    translated_class_name = translate_class_name(imagenet_class)
    st.write(f'Предсказанный класс: ')
    st.markdown(f"<h1 style='text-align: center;'>{translated_class_name}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align: center;'>{res['class_index']} индекс в ImageNet-Simple-Labels</h4>", unsafe_allow_html=True)
