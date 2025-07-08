import torch
from torchvision import transforms
from PIL import Image
from datasets import CustomImageDataset
from utils import show_images, show_single_augmentation, show_multiple_augmentations
from extra_augs import (AddGaussianNoise, RandomErasingCustom, CutOut, 
                       Solarize, Posterize, AutoContrast, ElasticTransform)
import random
import cv2

# Загрузка датасета без аугментаций
root = 'C:/Users/lego/practice/data/train'
dataset = CustomImageDataset(root, transform=None, target_size=(224, 224))

original_img, label = dataset[1]
#вставил сюда себе для примера реализации от которого отталкиваться
'''class Solarize:
    """Инвертирует пиксели выше порога."""
    def __init__(self, threshold=128):
        self.threshold = threshold
    def __call__(self, img):
        img_np = img.numpy()
        mask = img_np > self.threshold / 255.0
        img_np[mask] = 1.0 - img_np[mask]
        return torch.from_numpy(img_np)'''

class RandomBrightness:
    """Регулирует яркость изображения случайным образом."""
    def __init__(self, brightness_range=(0.5, 1.5)):
        self.brightness_range = brightness_range
    def __call__(self, img):
        brightness_factor = random.uniform(*self.brightness_range)
        img_np = img.numpy()
        img_np = img_np * brightness_factor
        img_np = torch.from_numpy(img_np.clip(0.0, 1.0))  # Ограничиваем значения в диапазоне [0, 1]
        return img_np
    
class RandomBlur:
    """Применяет размытие Гаусса со случайным ядром."""
    def __init__(self, kernel_range=(1, 5)):
        self.kernel_range = kernel_range
    
    def __call__(self, img):
        img_np = img.numpy().transpose(1, 2, 0)  # меняем порядок осей на HWC для OpenCV
        # Выбираем случайный нечетный размер ядра
        kernel_size = random.choice(range(self.kernel_range[0], self.kernel_range[1] + 1, 2))
        # Применяем размытие Гаусса через метод cv2
        blurred_img = cv2.GaussianBlur(img_np, (kernel_size, kernel_size), 0)
        # Возвращаем тензор с исходным порядком осей
        blurred_img = blurred_img.transpose(2, 0, 1)  # меняем обратно на CHW
        return torch.from_numpy(blurred_img)
    
class RandomContrast:
    """Применяет случайное изменение контрастности изображения."""
    def __init__(self, contrast_range=(0.5, 10.5)):
        self.contrast_range = contrast_range
    
    def __call__(self, img):
        # Генерируем случайный коэффициент контрастности
        contrast_factor = random.uniform(*self.contrast_range)
        # Конвертируем тензор в numpy array
        img_np = img.numpy()
        # Вычисляем среднее значение яркости по всем каналам
        mean_value = img_np.mean()
        # Применяем формулу изменения контрастности: (img - mean) * contrast + mean
        img_np = (img_np - mean_value) * contrast_factor + mean_value
        # Обрезаем значения в диапазон [0, 1] и возвращаем тензор
        return torch.from_numpy(img_np.clip(0.0, 1.0))
    
brightness_aug = transforms.Compose([
    transforms.ToTensor(),
    RandomBrightness(brightness_range=(0.5, 1.5))
])
brightness_img = brightness_aug(original_img)
show_single_augmentation(original_img, brightness_img, "Brightness")

blur_aug = transforms.Compose([
    transforms.ToTensor(),
    RandomBlur(kernel_range=(1, 5))
])
blurred_img = blur_aug(original_img)
show_single_augmentation(original_img, blurred_img, "Blur")

contrast_aug = transforms.Compose([
    transforms.ToTensor(),
    RandomContrast(contrast_range=(0.5, 10.5))
])
contrast_img = contrast_aug(original_img)
show_single_augmentation(original_img, contrast_img, "Contrast")
