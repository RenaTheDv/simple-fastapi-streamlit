import torch
import torchvision.models as models
from transformers import AutoModelForSequenceClassification, AutoTokenizer

resnet34 = models.resnet34(pretrained=True)
mobilenet_v2 = models.mobilenet_v2(pretrained=True)

torch.save(resnet34.state_dict(), 'resnet34_weights.pth')
torch.save(mobilenet_v2.state_dict(), 'mobilenet_v2_weights.pth')

models_to_download = {
    'distilbert': 'distilbert-base-uncased-finetuned-sst-2-english',
    'xlm_roberta': 'xlm-roberta-base'
}

for model_name, model_path in models_to_download.items():
    print(f"Загружаю модель: {model_name}")

    # загружаем модель с указанием num_labels
    model = AutoModelForSequenceClassification.from_pretrained(model_path, num_labels=2, force_download=True)
    tokenizer = AutoTokenizer.from_pretrained(model_path, force_download=True)

    # сохраняем
    model.save_pretrained(f'{model_name}_weights')
    tokenizer.save_pretrained(f'{model_name}_tokenizer')

    print(f"✅ Модель {model_name} загружена и сохранена")