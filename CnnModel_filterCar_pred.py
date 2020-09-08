# --coding:utf-8--
import os
import shutil
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.models import load_model
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

train_dir = r'E:\car_pic\training_in_out'
# validation_dir = r'E:\car_pic\validation_in_out'
# test_dir = r'E:\car_pic\test_in_out'

train_datagen =  ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(train_dir)

print('='*30)
print('訓練的分類：',train_generator.class_indices)
print('='*30)
#
labels = train_generator.class_indices

#將分類做成字典方便查詢
labels = dict((v,k) for k,v in labels.items())
print(labels)

# 載入模型
model = load_model('cnn_filterCar')

# 將圖片轉為待測數據
def read_image(img_path):
    try:
        img = image.load_img(img_path, target_size=(150, 150))
    except Exception as e:
        print(img_path,e)

    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    return img

Path = r"E:\car_pic\hot_all"
Path_2 = r"E:\car_pic\hot_outside"
Path_3 = r"E:\car_pic\hot_inside"
allList = os.walk(Path)
# 列出所有子目錄與子目錄底下所有的檔案
for root, dirs, files in allList:

    for i in files:
        try:
            # 辨識圖片
            filename = Path +"\\" + i
            # plt.figure()
            im = Image.open(filename)
            im_list = np.asarray(im)
            # plt.title("predict")
            # plt.axis("off")
            # plt.imshow(im_list)
            # plt.show()
            img = read_image(filename)
            pred = model.predict(img)[0]
            output = labels[pred[0]]
            print('辨識結果:',output)
            if output == "outside":
                # 將辨識為車的圖片移動到新路徑Path_2
                dst = shutil.move(filename, Path_2)
            elif output == "inside":
                dst = shutil.move(filename, Path_3)
        except Exception as e:
            print(e)



