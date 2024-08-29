from pandas import read_csv
import cv2
import numpy as np



filename="data/labels.csv"
labelsNames=["id","breed"]
labels=read_csv(filename,names=labelsNames)
print(labels.shape)


label_list=labels["breed"].tolist()
label_list=label_list[1:]


def extractFeaturesFromImage(image_file):
        img = cv2.imread(image_file)#读取图片
        print(img.shape)
        img = cv2.resize(img, (400,400), interpolation=cv2.INTER_CUBIC)
        #对图片进行resize操作统一大小
        img = img.flatten()#对图像进行降维操作，方便算法计算
        img = img / np.mean(img)#归一化，突出特征
        return img


imagesIds = labels["id"].tolist()
imagesIds = imagesIds[1:]
feature_list = list()
for imageId in imagesIds:
    print("data/train/" + imageId + ".jpg")
    feature_list.append(extractFeaturesFromImage("data/train/" + imageId + ".jpg"))


print(len(feature_list))