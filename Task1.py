import torch
from torchvision import transforms
from PIL import Image
from datasets import CustomImageDataset
from utils import show_images, show_single_augmentation, show_multiple_augmentations
from extra_augs import (AddGaussianNoise, RandomErasingCustom, CutOut, 
                       Solarize, Posterize, AutoContrast, ElasticTransform)

# Загрузка датасета без аугментаций
root = 'C:/Users/lego/practice/data/train'
dataset = CustomImageDataset(root, transform=None, target_size=(224, 224))

def standard_augs(original_image):
    # Демонстрация стандартных аугментаций torchvision
    print("\n=== Стандартные аугментации torchvision ===")

    standard_augs = [
        ("RandomHorizontalFlip", transforms.RandomHorizontalFlip(p=100.0)),
        ("RandomCrop", transforms.RandomCrop(200, padding=20)),
        ("ColorJitter", transforms.ColorJitter(brightness=0.5, contrast=0.5, saturation=0.5, hue=0.1)),
        ("RandomRotation", transforms.RandomRotation(degrees=30)),
        ("RandomGrayscale", transforms.RandomGrayscale(p=100.0))
    ]

    augmented_imgs = []
    titles = []

    for name, aug in standard_augs:
        aug_transform = transforms.Compose([
            aug,
            transforms.ToTensor()
        ])
        aug_img = aug_transform(original_img)
        augmented_imgs.append(aug_img)
        titles.append(name)

    show_multiple_augmentations(original_img, augmented_imgs, titles)

    # Демонстрация комбинированных аугментаций
    print("\n=== Всё вместе ===")

    combined_aug = transforms.Compose([
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomCrop(200, padding=20),
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
        transforms.RandomRotation(degrees=30),
        transforms.RandomGrayscale(p=1.0),
        transforms.ToTensor()
    ])

    combined_img = combined_aug(original_img)

    show_single_augmentation(original_img, combined_img, "Всё вместе")

idx = 0

for i in range(6):
    original_img, label = dataset[idx]
    standard_augs(original_img)
    idx += 30