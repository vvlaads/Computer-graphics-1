import tkinter as tk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from config import get_image_path

# Глобальные переменные для хранения данных гистограммы
red_count = 0
green_count = 0
blue_count = 0


def show_image(r, name):
    global red_count, green_count, blue_count

    # Создаем canvas для изображения
    canvas = tk.Canvas(r, height=200, width=300, name="image_canvas")
    image = Image.open(name)
    image = image.resize((300, 200))  # Масштабируем изображение
    photo = ImageTk.PhotoImage(image)
    canvas.image = photo
    canvas.create_image(0, 0, anchor='nw', image=photo)
    canvas.grid(row=1, column=3, rowspan=6, padx=20, pady=10)

    # Считаем пиксели и обновляем данные
    red_count, green_count, blue_count = count_pixels(name)

    # Обновляем метки с количеством пикселей
    update_pixel_labels(r)


def count_pixels(name):
    image = Image.open(name).resize((300, 200)).convert("RGB")
    red = 0
    green = 0
    blue = 0

    for i in range(0, image.width):
        for j in range(0, image.height):
            pixel = image.getpixel((i, j))
            max_value = max(pixel)
            if pixel[0] == max_value and pixel[0] > 0:
                red += 1
            if pixel[1] == max_value and pixel[1] > 0:
                green += 1
            if pixel[2] == max_value and pixel[2] > 0:
                blue += 1

    return red, green, blue


def update_pixel_labels(r):
    # Обновляем метки с количеством пикселей
    for widget in r.grid_slaves():
        if widget.grid_info()["row"] in [4, 5, 6] and widget.grid_info()["column"] == 2:
            widget.destroy()

    tk.Label(r, text=f"{red_count}").grid(row=4, column=2)
    tk.Label(r, text=f"{green_count}").grid(row=5, column=2)
    tk.Label(r, text=f"{blue_count}").grid(row=6, column=2)


def show_hist():
    # Используем глобальные переменные с данными
    global red_count, green_count, blue_count

    names = ["Red", "Green", "Blue"]
    values = [red_count, green_count, blue_count]
    colors = ["red", "green", "blue"]

    plt.figure(figsize=(8, 6))
    plt.bar(names, values, color=colors)

    # Добавляем значения на столбцы
    bars = plt.bar(names, values, color=colors)
    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02,
                 str(value), ha='center', va='bottom', fontweight='bold')

    plt.title("Гистограмма цветов")
    plt.ylabel("Количество пикселей")
    plt.xlabel("Цвета")
    plt.show()


# Создаем основное окно
root = tk.Tk()
root.title("Lab1")
root.geometry("800x600")

student = tk.Label(root, text="Силинцев Владислав P3314")
student.grid(row=0, column=0, columnspan=3, pady=10)

# Кнопки для изображений
button1 = tk.Button(root, text="Изображение 1", command=lambda: show_image(root, get_image_path("img_1.png")))
button1.grid(row=1, column=0, padx=10, pady=5)

button2 = tk.Button(root, text="Изображение 2", command=lambda: show_image(root, get_image_path("img_2.png")))
button2.grid(row=2, column=0, padx=10, pady=5)

# Кнопка для гистограммы
button3 = tk.Button(root, text="Гистограмма", command=show_hist)
button3.grid(row=3, column=0, padx=10, pady=5)

# Метки для цветов
label_r = tk.Label(root, text="R:")
label_g = tk.Label(root, text="G:")
label_b = tk.Label(root, text="B:")

label_r.grid(row=4, column=0, sticky="e", padx=10, pady=2)
label_g.grid(row=5, column=0, sticky="e", padx=10, pady=2)
label_b.grid(row=6, column=0, sticky="e", padx=10, pady=2)

# Изображение по умолчанию
show_image(root, get_image_path("img_1.png"))

root.mainloop()
