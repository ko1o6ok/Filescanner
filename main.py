from PIL import Image
import numpy as np
from tqdm import tqdm

name = input('Введите название файла:')  # Filename input
img = Image.open(name)
w, h = img.size
pixels = img.load()
p_w = int(w / 2)  # The image is cut into 4 parts
p_h = int(h / 2)
COEF = 1.45  # Shows how much average value of one pixel can exceed the mean of others


def scan(start_x, end_x, start_y, end_y):
    array = []
    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            array.append(pixels[i, j])
    m = np.mean(array)
    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            av = sum(pixels[i, j]) / 3
            pixels[i, j] = (0, 0, 0) if av < m / COEF else (255, 255, 255)


print('Пожалуйста, подождите. Изображение обрабатывается...')  # Please, wait. The image's being processed...
# scan(0, p_w, 0, p_h) 1
# scan(0, p_w, p_h,h)  2
# scan(p_w,w,0,p_h)    3
# scan(p_w, w,p_h,h)   4
for i in tqdm(range(1, 5)):
    scan(p_w * (i > 2), p_w if i < 3 else w, p_h * ((i + 1) % 2),
         p_h if (i % 2 != 0) else h)  # A weird way of making tqdm progressbar work
img.save('result.pdf')
