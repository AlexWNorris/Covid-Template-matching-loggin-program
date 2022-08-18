import cv2
import numpy as np
from matplotlib import pyplot as plt
import pyautogui
import time
import webbrowser

sites=["https://ellesmereowa.com/owa/auth/logon.aspx?replaceCurrent=1&url=https%3a%2f%2fellesmereowa.com%2fowa%2f"]
targets_raw=[[r"python\chunky bois\loginboxIdentification\sorces\U1.PNG",r"python\chunky bois\loginboxIdentification\sorces\P1.PNG",r"python\chunky bois\loginboxIdentification\sorces\S1.PNG"]]
targets=[]

for List in targets_raw:
    temp=[]
    for path in List:
        temp.append(cv2.imread(path))
    targets.append(temp)


def start():
    for site in sites:
        webbrowser.open(site)
        time.sleep(5)
        boxIdent()

def boxIdent():
    for List in targets:
        count=0
        for image in List:
            #screenshot screen
            conceptImage=pyautogui.screenshot()
            conceptImage=cv2.cvtColor(np.array(conceptImage),cv2.COLOR_RGB2BGR)


            # hard coded site image
            ###conceptImage=cv2.imread(r"loginboxIdentification\sorces\outlook.PNG")


            #locate the images
            dimensions=image.shape[::]
            h = dimensions[0]
            w = dimensions[1]
            method = eval('cv2.TM_SQDIFF')
            res = cv2.matchTemplate(image,conceptImage,method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            top_left = min_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            pass    
            centre = [(top_left[0] + top_left[0] + w)/2,(top_left[1] + top_left[1] + h)/2]

            #dynamic 
            emulateUser(centre,count)
            
            
            count+=1
            time.sleep(1)


def enterCode(x):
    with open('python\chunky bois\loginboxIdentification\codes') as fl:
        fl_con=fl.readlines()
    pyautogui.typewrite(fl_con[x][0:len(fl_con[x])-1])

def emulateUser(point,x):
    pyautogui.moveTo(point[0],point[1])
    pyautogui.click()
    if (x%(3*x-1))!=2:
        pyautogui.keyDown("ctrl")
        pyautogui.press("a")
        pyautogui.keyUp("ctrl")
        pyautogui.press("backspace")
        enterCode(x)

    

start()
while True:
    time.sleep(10)