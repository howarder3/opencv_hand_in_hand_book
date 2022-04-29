import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob

class opencv_tools(object):
    # 封裝 1-1-2 將圖片用 matplotlib的方式顯示
    @staticmethod
    def show_img_by_matplotlib(img):
        image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.imshow(image_rgb)
        plt.show()
        
    # 封裝 1-4 將圖片用OpenCV的方式顯示
    @staticmethod
    def show_img_by_opencv(img):
        cv2.imshow('Image window', img) # 顯示圖片，第一個參數表示視窗名稱，第二個參數就是你的圖片
        cv2.waitKey(0) # 暫停等待按鍵，使 cv2.imshow 能顯示出畫面
        cv2.destroyAllWindows() # 配合上一行，按下任意鍵則關閉所有視窗)
