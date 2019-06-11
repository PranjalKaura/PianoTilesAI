    
import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from mss import mss 

# cords_x = [472, 628, 777, 902]
cords_x = [60,180 ,327 , 442]
start_x = 410
last_time = time.time()
def Print_MousePos():
    print("pos", pyautogui.position()) 
    time.sleep(1)



def Mouse_clicks(gray): # gray[y][x]
    for cords in cords_x:
        if gray[577-78, cords - 410] < 30:
            pyautogui.click(cords, 740)
            break
    # cv2.imshow('Mask', gray)
   

def FirstCLick():
        original_image =  np.array(ImageGrab.grab(bbox=(410,78,987,798)))
        #GreyScaling
        gray = cv2.cvtColor(original_image,  cv2.COLOR_BGR2GRAY)
        #FirstCLick
        for cords in cords_x:
            if gray[667-78, cords - 410] > 140 and gray[667-78, cords - 410] < 168 :
                pyautogui.click(cords, 667)
                break
        screen_record()
        
def SpeedCheck():
    # last_time = time.time() 
    # for i in range(1,100):
    #     original_image =  np.array(ImageGrab.grab(bbox=(410,78,987,798)))

    # print("Seconds: ", time.time() - last_time)
    bbox = (440, 577, 920, 577 + 1) 
    last_time = time.time() 
    with mss() as sct:
        for i in range(1,2):
            original_image = sct.grab(bbox)
            print(original_image)

    print("Seconds: ", time.time() - last_time) 


def Faster_Algo_FirstCLick():
    click = 0
    buf = 15
    bbox = (440, 577, 920, 577 + 1) 
    with mss() as sct:
        while(True):
            original_image = sct.grab(bbox)
            for cords in cords_x:
                if original_image.pixel(cords, 0)[0] < 100:
                    pyautogui.click(cords + start_x + buf, 597)
                    click+=1
                    if click>=1000:
                    	buf = 70
                    break


def screen_record(): 
    # 
    while(True):
        original_image =  np.array(ImageGrab.grab(bbox=(410,78,987,798)))
        #GreyScaling
        gray = cv2.cvtColor(original_image,  cv2.COLOR_BGR2GRAY)
        #Game
        for cords in cords_x:
            if gray[577-78, cords - 410] < 168:
                pyautogui.click(cords, 577)
                break

        # Print_MousePos()
        # if cv2.waitKey(25) & 0xFF == ord('q'):
        #     cv2.destroyAllWindows()
        #     break
        

time.sleep(4)
Faster_Algo_FirstCLick()
# SpeedCheck()