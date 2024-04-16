
import numpy as np
import cv2
import tkinter as tk
from PIL import ImageTk, Image
import os
import tensorflow as tf
from operator import itemgetter
loaded_model = tf.keras.models.load_model('NeuralNet30_5_0.99.h5')

def get_nombers (fld, img_name):  # Функция
    imgOriginal = cv2.imread(fld+img_name)  #загрузка изображения в переменную imgOriginal
    img = np.array(imgOriginal[:, :, 0])  #делаем срез массива до нужного размера
    N = 0
    xy_nadpis = []  #создаем массив координат
    img2 = np.zeros(img.shape, dtype=np.uint8)  #создаем массив нулей
    img2[img > 1.25*np.mean(img)] = 255  #максимальное значение массива = 255
    contours, hierarchy = cv2.findContours(img2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Находим контуры на изображение

    AreaTreshMin, AreaTreshMax = 300, 2000  #минимальная и максимальная площадь контура

    mas1 = []
    for contour in contours:
        mas1.append(AreaTreshMax > cv2.contourArea(contour) > AreaTreshMin)
        # добавляем в массив контуры подходящие по размеру

    np_contours = np.array(contours)  #добавляем в массив все контуры которые нашли на картинке
    our_contours = np_contours[mas1]
    # добавляем в отдельный массив нужные контуры с цифрами(мусор на изображение подходящие по размеру тоже)

    images = []
    for contour in our_contours:
        massiv_x = []
        massiv_y = []
        for point in contour:
            x = point[0][0]
            y = point[0][1]
            massiv_x.append(x)
            massiv_y.append(y)

        images.append(img2[np.min(massiv_y)-N:np.max(massiv_y)+N, np.min(massiv_x)-N:np.max(massiv_x)+N])
        xy_nadpis.append((np.min(massiv_x), np.min(massiv_y)))
        imgOriginal = cv2.rectangle(imgOriginal, (np.min(massiv_x),np.min(massiv_y)),(np.max(massiv_x),np.max(massiv_y)), (255,0,0), 2)
        # отрисовываем контуры нужных элементов подходящих по размеру на изображение
    return images, xy_nadpis, imgOriginal


fld = 'right/'  #Путь к папке с изображениями номеров
imglist = os.listdir(fld)  #imglist - хранит в себе список, содержащий все изображения вагонов
img_array, xy_nadpis, imgOriginal = get_nombers(fld, imglist[1300])
# обращаемся к функции, где fld(путь к папке) и imglist(список изображений, с указаным номером изображения) - аргументы
print('Распознанный номер вагона: ')

numbers = []  # список для хранения распознанных номеров

for i, img in enumerate(img_array):
    img2 = np.zeros([1, 60, 30, 1])
    img2[0, 0:np.min([img.shape[0], 60]), 0:np.min([img.shape[1], 30]), 0] = img[
                                                                              0:np.min([img.shape[0], 60]),
                                                                              0:np.min([img.shape[1], 30])]
    img2 = img2 / 255

    number = np.argmax(loaded_model.predict(img2))
    numbers.append((number, xy_nadpis[i]))

    if number < 10:
        txt = str(number)
    else:
        txt = ''
    cv2.putText(imgOriginal, txt,
                xy_nadpis[i], cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                color=(0, 0, 0), thickness=2)
    print('Распознанное число:', number, '  Процент распознания:', np.max(loaded_model.predict(img2)))

# Сортировка списка номеров
sorted_numbers = sorted(numbers, key=itemgetter(1))

for number in sorted_numbers:
    print(number, end=" ")

# cv2.imshow('1', cv2.imread(fld + imglist[1300]))
# cv2.waitKey()
# cv2.imshow('2', imgOriginal)
# cv2.waitKey()
# cv2.destroyAllWindows()

