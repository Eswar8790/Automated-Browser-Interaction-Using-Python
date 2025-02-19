import pyautogui
import time
import random
import subprocess
from itertools import permutations

def permutation_generator(val):
    return list(permutations(val[0:5]))[:34]

def close_eng(closeen):
    close_chrm=[1886,23]
    indication=[[1843,542],[863,534],[1824,31],[878,22]][::-1]
    for i in indication[0:closeen]:
        pyautogui.leftClick(i[0],i[1])
        time.sleep(2)
        pyautogui.leftClick(close_chrm[0],close_chrm[1])
        time.sleep(2)

def searches_perform(perm_word):
    search_bar=[[447,76],[1324,78],[1311,588],[394,587]]
    for i in perm_word:
        for j in search_bar[0:4]:
            pyautogui.leftClick(random.randint(j[0],j[0]+150),random.randint(j[1],j[1]+10))
            pyautogui.write("".join(i))
            pyautogui.press('enter')
            time.sleep(random.randint(1,2))
            
def arrange():
    arrange_lst=[[1206,182],[510,751],[1392,786]]
    pyautogui.hotkey("win","left")
    time.sleep(2)
    pyautogui.leftClick(50,500)
    time.sleep(2)
    pyautogui.moveTo(872,18)
    time.sleep(2)
    pyautogui.leftClick(888,270)
    time.sleep(2)
    for i in arrange_lst:
        pyautogui.leftClick(i)
        time.sleep(1)


user_lst = ["Profile 2", "Profile", "Profile 5", "Profile 11", "Default", "Profile 4", "Profile 10", "Profile 12","Profile 8","Profile 6","Profile 3","Profile 7","Profile 14"]

def search_engine(users):
    i=0
    eng=r'"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --profile-directory="'
    while i <12:
        time.sleep(2)
        for j in users[i:i+4]:
            subprocess.Popen(eng + j+ r'" ')
            time.sleep(2)
        
        arrange()
        searches_perform(permutation_generator("nagbh"))
        time.sleep(2)
   
        close_eng(4)
        i+=4

        
search_engine(user_lst)