import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
# читать изображение с помощью OpenCV
image = cv2.imread("kfkff.png")
# или вы можете использовать подушку
# image = Image.open("test.png")
# получаем строку
string = pytesseract.image_to_string(image)
# печатаем
print(string)
# чтобы нарисовать сделаем копию изображения
image_copy = image.copy()
# слово для поиска
target_word = "dog"
# получить все данные из изображения
data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
# получить все вхождения нужного слова
word_occurences = [ i for i, word in enumerate(data["text"]) if word.lower() == target_word ]
for occ in word_occurences:
    # извлекаем ширину, высоту, верхнюю и левую позицию для обнаруженного слова
    w = data["width"][occ]
    h = data["height"][occ]
    l = data["left"][occ]
    t = data["top"][occ]
    # определяем все точки окружающей рамки
    p1 = (l, t)
    p2 = (l + w, t)
    p3 = (l + w, t + h)
    p4 = (l, t + h)
    # рисуем 4 линии (прямоугольник)
    image_copy = cv2.line(image_copy, p1, p2, color=(255, 0, 0), thickness=2)
    image_copy = cv2.line(image_copy, p2, p3, color=(255, 0, 0), thickness=2)
    image_copy = cv2.line(image_copy, p3, p4, color=(255, 0, 0), thickness=2)
    image_copy = cv2.line(image_copy, p4, p1, color=(255, 0, 0), thickness=2)
plt.imsave("all_dog_words.png", image_copy)
plt.imshow(image_copy)
plt.show()