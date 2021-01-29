

### 뭐부터 할까?
### 파이선 
## 마이마이 연습 
## 사쿠라모유
## 노래 찾아서 듣기
## 웹 개발 시작
## 사쿠라장 시청
## 양파가루 구입 요거톡 구입
##원순



import pyautogui
import time
import os
import datetime
from pygame import mixer
import sys, fileinput
import pyperclip

def lineChange( Replace_What , New_Value ) :

    try:
        File = r"config.txt"        
        for Line in fileinput.input(File, inplace=True):  #:- Entire Line Replace
            if Replace_What in Line:
                Line = Line.replace(Line, Replace_What + '=' + str(New_Value) + '\n')
            sys.stdout.write(Line)

        print('config file changed.')    
    except :
        print('failed to read config file')



def lineReturn(Replace_What):
            
    try:   
        f = open("config.txt", 'r')
        lines = f.readlines()
        for line in lines:
        #     item = line.split("=")
            if line.find(Replace_What) == 0:  
        #     index = item[item.index(Replace_What)+1]
                result = line.lstrip(Replace_What)
                result = result.lstrip('=')
                result = result.rstrip('\n')
                result = int(result)
        
        
        f.close()
        return result
    except:
        print("config load error")   


def moveToFriend()  : 
    try:
        config = open("Parms.txt", 'r+')
        lines = config.readlines()


        #config의 index값 읽어옴
        index1 = lineReturn("index")

        #인덱스가 다 찼을경우 종료
        if index1 == -1:
            print('mixed all the friend farms today... ')
            return -1

        if index1 >= len(lines)  :
            lineChange('index', -1 )
            print('mixed all the friend farms today... ')
            return -1
        # parm.txt에서 인덱스에 맞는 줄을 읽어서 변수에 저장
        friendClip = str(lines[index1].rstrip('\n'))

        pyperclip.copy(friendClip)
        pasteParm= pyperclip.paste()



        time.sleep(2)

        # 친구메뉴 소환
        friend1 = pyautogui.locateOnScreen('button/friend0.png',confidence= 0.94)
        pyautogui.click(friend1)

        time.sleep(0.2)

        # 2. 친구창 농장방문 클릭
        friend1 = pyautogui.locateOnScreen('button/friend1.png',confidence= 0.9)
        pyautogui.click(friend1)

        time.sleep(0.5)
        #3. 복붙
        pyautogui.keyDown('ctrl')  
        pyautogui.press('v')  
        pyautogui.keyUp('ctrl') 




        #4. 확인
        mixButton2 = pyautogui.locateOnScreen('button/button2.png',confidence= 0.9)
        pyautogui.click(mixButton2)
        pyautogui.click(mixButton2)
        time.sleep(0.2)
        mixButton2 = pyautogui.locateOnScreen('button/button2.png',confidence= 0.9)
        pyautogui.click(mixButton2)
        pyautogui.click(mixButton2)

        #성공적으로 이동시 인덱스를 변경한다

        if index1 >= len(lines):
            lineChange('index', -1 )
            print('mixed all the friend farms today.... ')
            return -1

        index1 = lineChange('index', index1 + 1 )

        print(len(lines))
    except:
        print('parm.txt error...')
    return 0
   



# 날짜가 다르면 인덱스 초기화 하는 함수
def initIndextoDate(): 
    try:

        da = "date"
        New_Value = str(time.strftime('%d', time.localtime(time.time() )) )


        i = lineReturn(da)
        today =  int(time.strftime('%d', time.localtime(time.time() ))  )

        # 날짜가 바뀌었다면 날짜와 인덱스 초기화
        if not(i == today):
            index = "index"
            
            lineChange( index , 0 )
            lineChange( da , today )

            print("init index..")


        
        return 0

    except:
        print('init error...')
        return -1
# 인덱스 순서대로 텍스트 처리 작업
# 농장 한줄에 방문 시 인덱스 추가   

def exception():
    if pyautogui.locateOnScreen('button/nope1.png',confidence= 0.97) :
        nope2 = pyautogui.locateOnScreen('button/nope2.png',confidence= 0.97)
        pyautogui.click(nope2)

    nope3= pyautogui.locateOnScreen('button/nope3.png',confidence= 0.97)
    pyautogui.click(nope3)


exception()