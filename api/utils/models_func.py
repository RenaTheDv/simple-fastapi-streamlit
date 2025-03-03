import torch
import torchvision.models as models
import torchvision.transforms as T 
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, DistilBertConfig
from transformers import XLMRobertaTokenizer, XLMRobertaForSequenceClassification, XLMRobertaConfig
import json
import os


# для динамической загрузки путей с весами (и токенизаторами) моделей
def get_model_path(filename):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'weights', filename)

# настройка для ImageNet
mean = (0.485, 0.456, 0.406)
std = (0.229, 0.224, 0.225)

# загружаем классы ImageNet
def load_classes():
    with open('utils/imagenet-simple-labels.json') as f:
        labels = json.load(f)
    return labels

# предсказываем класс картинки
def class_id_to_label(i):
    labels = load_classes()
    return labels[i]

# загружаем первую модель для классифицирования картинок
def first_image_model():
    model = models.resnet34(pretrained=False)
    model_path = get_model_path('resnet34_weights.pth')
    model.load_state_dict(torch.load(model_path, map_location='cpu'))
    model.eval()
    return model

# вторая модель для классифицирования картинок
def second_image_model():
    model = models.mobilenet_v2(pretrained=False)
    model_path = get_model_path('mobilenet_v2_weights.pth')
    model.load_state_dict(torch.load(model_path, map_location='cpu'))
    model.eval()
    return model

#предобработка картинки
def transform_image(img):
    trnsfm = T.Compose(
        [
            T.Resize((224, 224)),
            T.ToTensor(),
            T.Normalize(mean, std)
        ]
    )
    print(trnsfm(img).shape)
    return trnsfm(img).unsqueeze(0)

# ===============================================================================

# загружаем классы для классификации текста
def load_text_classes():
    return {
        0:'Негативный',
        1:'Положительный'
    }

# получаем класс текста
def class_id_to_label_text(i):
    labels = load_text_classes()
    return labels.get(i, 'Неизвестный класс')

# первая модель (DistilBERT)
def load_distilbert():
    model_name = 'distilbert-base-uncased-finetuned-sst-2-english'
    tokenizer_name = 'distilbert-base-uncased'

    model = DistilBertForSequenceClassification.from_pretrained(model_name, num_labels=2)
    tokenizer = DistilBertTokenizer.from_pretrained(tokenizer_name)

    model.eval()
    return model, tokenizer


# вторая модель (XLM-RoBERTa)
def load_roberta():
    model_name = 'xlm-roberta-base'
    tokenizer_name = 'xlm-roberta-base'
    
    model = XLMRobertaForSequenceClassification.from_pretrained(model_name, num_labels=2)
    tokenizer = XLMRobertaTokenizer.from_pretrained(tokenizer_name)
    
    model.eval()
    return model, tokenizer

