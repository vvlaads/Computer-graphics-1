import os
from pathlib import Path

# Получаем корневую директорию проекта
PROJECT_ROOT = Path(__file__).parent.parent

# Пути к ресурсам
RESOURCES_DIR = PROJECT_ROOT / "resources"
IMAGES_DIR = RESOURCES_DIR / "images"


# Функция для получения пути к ресурсам
def get_image_path(filename):
    return str(IMAGES_DIR / filename)
