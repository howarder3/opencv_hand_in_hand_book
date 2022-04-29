# import the necessary packages
import cv2
import numpy as np

point_list = []
cropping = False

keyboard_array = [
["q","w","e","r","t","y","u","i","o","p"],
["a","s","d","f","g","h","j","k","l",";"],
["z","x","c","v","b","n","m",",",".","/"]
]



class CV_KEYBORAD:
    # 初始化鍵盤、顯示用的螢幕
    def __init__(self, keyboard_array):
        self.keyboard_array = keyboard_array
        self.keyboard_height = len(self.keyboard_array)
        self.keyboard_width = len(self.keyboard_array[0])
        self.keyboard_size = 100
        shape = (self.keyboard_height*self.keyboard_size, self.keyboard_width*self.keyboard_size, 3) # y, x, RGB
        self.clean_keyboard = np.full(shape, 255).astype(np.uint8)
        self.key_setting()

        self.word_list = ""
        shape = (100, 1000, 3) # y, x, RGB
        self.clean_screen = np.zeros(shape).astype(np.uint8)
        self.current_screen = self.clean_screen.copy()
        self.show_screen()


    # 13-4 更新畫面
    def update_screen(self):
        word = self.word_list
        word_size = 1 # 字體大小
        word_position = (50, 50) # 字體位置
        word_color = (0, 255, 255) # 字體顏色
        word_thickness = 1 # 字體粗度
        word_lineType =  cv2.LINE_AA # 字體形式
        cv2.putText(self.current_screen, word, word_position, cv2.FONT_HERSHEY_DUPLEX, word_size, word_color, word_thickness, word_lineType) # 寫字


    # 13-3-1 滑鼠控制(input)
    def get_words_from_keyboard(self, x, y):
        return self.keyboard_array[x][y]

    # 13-3-2 按鍵回饋(output)與文字儲存
    def click_and_show(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            point = (x, y)
            cv2.circle(self.keyboard_img, point, self.keyboard_size//10, (0, 0, 255), -1) # 畫圓
            self.word_list += self.get_words_from_keyboard(x=y//self.keyboard_size, y=x//self.keyboard_size) # iamge position (x,y) -> list position (y,x)
            self.update_screen()

    # 13-2 顯示畫面
    def show_screen(self):
        cv2.namedWindow("keyboard")
        cv2.namedWindow("show_screen")
        cv2.setMouseCallback("keyboard", self.click_and_show)


        while True:
            # display the image and wait for a keypress
            cv2.imshow("keyboard", self.keyboard_img)
            cv2.imshow("show_screen", self.current_screen)
            key = cv2.waitKey(1) & 0xFF
            # if the 'r' key is pressed, reset the cropping region
            if key == ord("r"): # use ord() to change "r" to ASCII
                self.keyboard_img = self.clean_keyboard.copy()
                self.word_list = ""
                self.current_screen = self.clean_screen.copy()
            # if the 'c' key is pressed, break from the loop
            elif key == ord("c"):
                break

        cv2.destroyAllWindows()

    # 13-1 設計鍵盤畫面
    def key_setting(self):
        self.keyboard_img = self.clean_keyboard.copy()
        for y_idx in range(self.keyboard_height):
            for x_idx in range(self.keyboard_width):
                color = (200, 200, 200) if (x_idx+y_idx)%2==0 else (100, 100, 100)
                self.add_key(x=x_idx*self.keyboard_size, y=y_idx*self.keyboard_size, color = color)
                self.write_word(x=x_idx*self.keyboard_size, y=y_idx*self.keyboard_size, word_color = (0, 255, 255), word=self.keyboard_array[y_idx][x_idx])

    # 13-1-3 在鍵盤上刻字!
    def write_word(self, x=0, y=0, word_color=(0, 255, 255), word=""):
        word_size = 1 # 字體大小
        word_position = (x+self.keyboard_size//2, y+self.keyboard_size//2) # 字體位置
        word_color = (0, 255, 255) # 字體顏色
        word_thickness = 1 # 字體粗度
        word_lineType =  cv2.LINE_AA # 字體形式
        cv2.putText(self.keyboard_img, word, word_position, cv2.FONT_HERSHEY_DUPLEX, word_size, word_color, word_thickness, word_lineType) # 寫字

    # 13-1-2 替每個鍵盤畫上顏色!
    def add_key(self, x=0, y=0, color=(0, 0, 0)):
        left_up = (x, y)
        right_down =  (x+self.keyboard_size, y+self.keyboard_size)
        thickness = -1
        cv2.rectangle(self.keyboard_img, left_up, right_down, color, thickness) # 畫方型




if __name__ == '__main__':
    my_keyboard = CV_KEYBORAD(keyboard_array)

