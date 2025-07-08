import torch
from torchvision import transforms
from PIL import Image
from datasets import CustomImageDataset
from utils import show_images, show_single_augmentation, show_multiple_augmentations
from extra_augs import (AddGaussianNoise, RandomErasingCustom, CutOut, 
                       Solarize, Posterize, AutoContrast, ElasticTransform)
import random
from Task2 import RandomBlur, RandomBrightness, RandomContrast
from typing import Dict, Any, List

# Загрузка датасета без аугментаций
root = 'C:/Users/lego/practice/data/train'
dataset = CustomImageDataset(root, transform=None, target_size=(224, 224))

original_img, label = dataset[2]


class AugmentationPipeline:
    """Пайплайн для применения последовательности аугментаций."""
    def __init__(self):
        self.augmentations = {}

    def add_augmentation(self, name: str, aug: Any) -> None:
        #добавляет аугментацию в пайплайн
        self.augmentations[name] = aug
    
    def remove_augmentation(self, name: str) -> None:
        #удаляет аугментацию из пайплайна
        self.augmentations.pop(name, None)
    
    def apply(self, image) -> torch.Tensor:
        """Применяет все аугментации к изображению последовательно"""
        transform = transforms.ToTensor()
        tensor_image = transform(image)
        result = tensor_image.clone()
        for aug in self.augmentations.values():
            result = aug(result)
            show_single_augmentation(image, result, title="Аугментация")
        return result
    
    def get_augmentations(self) -> Dict[str, Any]:
        """Возвращает словарь аугментаций конфигурации"""
        return self.augmentations.copy()

    @staticmethod
    def light_config() -> 'AugmentationPipeline':
        """Легкие аугментации (минимальные изменения)."""
        pipeline = AugmentationPipeline()
        pipeline.add_augmentation('random_brightness', RandomBrightness((0.1, 1.1)))
        pipeline.add_augmentation('random_contrast', RandomContrast((0.1, 1.05)))
        return pipeline
    
    @staticmethod
    def medium_config() -> 'AugmentationPipeline':
        """Умеренные аугментации (заметные но реалистичные изменения)."""
        pipeline = AugmentationPipeline()
        pipeline.add_augmentation('brightness', RandomBrightness((0.8, 1.2)))
        pipeline.add_augmentation('contrast', RandomContrast((0.9, 1.1)))
        pipeline.add_augmentation('blur', RandomBlur((1, 3)))
        return pipeline
    
    @staticmethod
    def heavy_config() -> 'AugmentationPipeline':
        """Сильные аугментации (сильные изменения)."""
        pipeline = AugmentationPipeline()
        pipeline.add_augmentation('brightness', RandomBrightness((0.5, 10.5)))
        pipeline.add_augmentation('contrast', RandomContrast((0.7, 10.3)))
        pipeline.add_augmentation('blur', RandomBlur((3, 10)))
        pipeline.add_augmentation('solarize', Solarize(threshold=192))
        return pipeline
    
pipeline = AugmentationPipeline
#pipeline_light = pipeline.light_config()
#pipeline_medium = pipeline.medium_config()
pipeline_heavy = pipeline.heavy_config()
pipeline_heavy.apply(original_img)
