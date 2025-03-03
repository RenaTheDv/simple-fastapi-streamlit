import logging
import random
from contextlib import asynccontextmanager

import PIL
import numpy as np 
import torch
import uvicorn
from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from utils.models_func import (
    class_id_to_label, class_id_to_label_text,
    load_distilbert, load_roberta,
    first_image_model, second_image_model, 
    transform_image
)


logger = logging.getLogger('uvicorn.info')


# определение класса ответа для классификации изображения
class ImageResponse(BaseModel):
    class_name: str
    class_index: int 

# определение класса запроса для классификации текста
class TextInput(BaseModel):
    text: str 

# определение класса ответа для классификации текста
class TextResponse(BaseModel):
    label: str
    prob: float 


# глобальные переменные для моделей
resnet = None
mobilenet = None
distilbert = None
roberta = None
dis_token = None
rob_token = None

# контекстный менеджер для инициализации и заверщения работы FastAPI приложения
# загружает модели машинного обучения при запуске и удаляет их после завершения
@asynccontextmanager
async def lifespan(app: FastAPI):
    global resnet
    global mobilenet
    global distilbert
    global roberta
    global dis_token
    global rob_token

    resnet = first_image_model()
    logger.info('First image model loaded')
    mobilenet = second_image_model()
    logger.info('Second image model loaded')
    distilbert, dis_token = load_distilbert()
    logger.info('Distilbert model + tokenizer loaded')
    roberta, rob_token = load_roberta()
    logger.info('Roberta model + tokenizer loaded')

    yield

    del first_img_model, second_img_model, distilbert, dis_token, roberta, rob_token

app = FastAPI(lifespan=lifespan)

# возвращаем приветственное сообщение
@app.get('/')
def return_info():
    return 'Welcome on simple FastAPI test by RenaTheDv!'

# первый эндпоинт для классификации изображения
@app.post('/clf_image_resnet34')
def classify_image_resnet(file: UploadFile):
    # открываем изображение
    image = PIL.Image.open(file.file)
    # предобработка изображения + логирование
    adapted_image = transform_image(image)
    logging.info(f'{adapted_image.shape} - transform image')
    # предсказание класса изображения
    with torch.inference_mode():
        pred_index = resnet(adapted_image).numpy().argmax()
    # преобразуем индекс в класс
    imagenet_class = class_id_to_label(pred_index)
    # формируем отчет
    response = ImageResponse(
        class_name=imagenet_class,
        class_index=pred_index
    )
    return response

# второй эндпоинт для классификации изображения
@app.post('/clf_image_mobilenet')
def classify_image_mobilenet(file: UploadFile):
    # делаем те же действия, что и ранее
    image = PIL.Image.open(file.file)
    adapted_image = transform_image(image)
    logging.info(f'{adapted_image.shape} - transform image')
    with torch.inference_mode():
        pred_index = mobilenet(adapted_image).numpy().argmax()
    imagenet_class = class_id_to_label(pred_index)
    response = ImageResponse(
        class_name=imagenet_class,
        class_index=pred_index
    )
    return response

# третий эндпоинт - для классификации текста
@app.post('/clf_text_distilbert')
def classify_text_distilber(data: TextInput):
    # токенизируем входной текст (включаем обрезку текста + заполнение до максимума + максимальную длину)
    inputs = dis_token(data.text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    # начинаем предсказывать
    with torch.no_grad():
        outputs = distilbert(**inputs)
        logits = outputs.logits
        pred_index = torch.argmax(logits, dim=1).item()
        prob = torch.softmax(logits, dim=1)[0, pred_index].item()
    # преобразуем индекс в класс
    text_class = class_id_to_label_text(pred_index)
    # формируем отчет
    response = TextResponse(
        label=text_class,
        prob=prob
    )
    return response

# четвертый эндпоинт - для классификации текста через другую модель
@app.post('/clf_text_roberta')
def classify_text_roberts(data: TextInput):
    # делаем такие же действия, что и выше
    inputs = rob_token(data.text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = roberta(**inputs)
        logits = outputs.logits
        pred_index = torch.argmax(logits, dim=1).item()
        prob = torch.softmax(logits, dim=1)[0, pred_index].item()
    text_class = class_id_to_label_text(pred_index)
    response = TextResponse(
        label=text_class,
        prob=prob
    )
    return response

# запуск
if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)