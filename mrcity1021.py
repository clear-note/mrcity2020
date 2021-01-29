
import pyautogui
import time
import os
import datetime
from pygame import mixer
import keyboard
import pyperclip
import sys, fileinput
import win32gui
from PIL import ImageGrab
from PIL import Image




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

        

## 텍스트파일 필드 앞부분을 주고 '=' 뒷부둔을 리턴받음
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

        return result
    except:
        print("config load error")   


def discard(num) :
    
    
        
    
   

        mouseLoc =  pyautogui.locateOnScreen('button/scroll.png',confidence= 0.9)
        pyautogui.moveTo(mouseLoc) 

        print('start monster kill ' + str(num)   ) 
        

        # 최근 소환된 몬스터로 스크롤 
        for i in range(25) :
          pyautogui.click()

        try:

            # 삭제 num번 반복 
            for i in range(num):
                kill2 = pyautogui.locateOnScreen('button/kill.png',confidence= 0.9)
                kill2 = list(kill2) 
                kill2 = kill2[:2]
                kill2 = tuple(kill2)

                # 방출 메뉴 소환
                pyautogui.rightClick(kill2)
                pyautogui.rightClick(kill2)
                pyautogui.rightClick(kill2)
                

                # 방출 메뉴 버튼
                discard = pyautogui.locateOnScreen('button/discard.png',confidence= 0.9)
                pyautogui.click(discard)
                
                # 방출 확인
                mixButton2 = pyautogui.locateOnScreen('button/button2.png',confidence= 0.9)
                pyautogui.click(mixButton2)

                # 확인 
                time.sleep(0.1)
                enter3 = pyautogui.locateOnScreen('button/enter3.png',confidence= 0.95)
                pyautogui.click(enter3)
                pyautogui.click(enter3)
                

                time.sleep(0.3)
                
                # 한칸 스크롤
                pull = pyautogui.locateOnScreen('button/pull.png',confidence= 0.95)
                pyautogui.click(pull)

                time.sleep(0.2)


            

        except :
            print('image found faild')
            
        
  
  
        return 0



def scrollmouse(num):
    mouseLoc =  pyautogui.locateOnScreen('button/scroll.png',confidence= 0.9)
    pyautogui.moveTo(mouseLoc) 
    
    for i in range(num) :
      pyautogui.click()
    
    

def replace():

    #mouseLoc =  pyautogui.locateOnScreen('place/moveTo.png',confidence= 0.9)
    pyautogui.moveTo(1,1) 
    

## 현재 위치 파악
def nowPlace():
    myroom = pyautogui.locateOnScreen('place/myroom1.png',confidence= 0.9)
    otherroom = pyautogui.locateOnScreen('place/otherroom1.png',confidence= 0.9)
    shop= pyautogui.locateOnScreen('place/shop.png',confidence= 0.9)
    
    if myroom :
     print('now place is myroom')
     return 1

    if otherroom :
     print('now place is ohterroom')
     return 2

    if shop :
     pyautogui.click(shop)
     print('now place is shop')

     return 3

    
    return -1 
    


# 조합식 1
def mix(num, mixcount):
   # 타깃 몬스터 서치 
   mix1_2 =  pyautogui.locateOnScreen('Rec' + str(num)+ '/mix2.png',confidence= 0.995)
   # 타깃 몬스터가 없으면 함수 종료
   if mix1_2 is None:
       print ('target '+ str(num) +  ' is not exist..') 
       return 0
   else:
       print ('target '+ str(num) +  ' found, start mix') 

   time.sleep(0.5)

   # 타깃 몬스터  우 클릭
   pyautogui.rightClick(mix1_2)
   pyautogui.rightClick(mix1_2)
   pyautogui.rightClick(mix1_2)
   
   if keyboard.is_pressed('q'):
        print('Quit')
        time.sleep(10000)
        return 0  
   # 메뉴 버튼 서치
   mixButton = pyautogui.locateOnScreen('button/mixButton.png',confidence= 0.9)
   pyautogui.click(mixButton)
   
   # 조합 시 등급과 레벨이
   mixButton2 = pyautogui.locateOnScreen('button/button2.png',confidence= 0.9)
   pyautogui.click(mixButton2)

   # 내 몬스터 클릭
   
   if keyboard.is_pressed('q'):
        print('Quit')
        time.sleep(10000)
        return 0  
   mix1_1 =  pyautogui.locateOnScreen('Rec' + str(num)+ '/mix1.png',confidence= 0.9)
   pyautogui.click(mix1_1)


   # 조합하기 클릭 
   mixButton3 = pyautogui.locateOnScreen('button/button3.png',confidence= 0.95)
   pyautogui.click(mixButton3)
    
   # 특별 조합식 조합을 시작합니다
   mixButton2 = pyautogui.locateOnScreen('button/button2.png',confidence= 0.9)
   pyautogui.click(mixButton2)

   # 조합에 5000 와르가 소모됩니다
   mixButton2 = pyautogui.locateOnScreen('button/button2.png',confidence= 0.9)
   pyautogui.click(mixButton2)
   

   time.sleep(1)
   if keyboard.is_pressed('q'):
        print('Quit')
        time.sleep(10000)
        return 0  
   # 여유 공간이 없을경우 집으로 직행
   if pyautogui.locateOnScreen('button/notspace.png',confidence= 0.95) and pyautogui.locateOnScreen('place/otherroom1.png',confidence= 0.95) :

     mixButton2 = pyautogui.locateOnScreen('button/button2.png',confidence= 0.9)
     pyautogui.click(mixButton2)

     gohome = pyautogui.locateOnScreen('button/gohome.png',confidence= 0.9)
     pyautogui.click(gohome)
     
     

     return 2

    
   # 조합 대기시간
   time.sleep(2.4)
   
   #조합 로그 출력
   
   print('target ' + str(num) +' mix count: ' + str(mixcount))


   # 확인
   enter = pyautogui.locateOnScreen('button/enter.png',confidence= 0.95)
   
   # 스페셜이 나왔다면 정지
   if (pyautogui.locateOnScreen('button/enter2.png',confidence= 0.95)) :

       mixer.init()
       mixer.music.load('alarm.mp3')
       mixer.music.play()
       time.sleep(50000)
       mixer.music.stop()

    
       return -1
   
   pyautogui.click(enter)
   pyautogui.click(enter)

   
   time.sleep(0.2)

   # 확인
   enter2 = pyautogui.locateOnScreen('button/enter2.png',confidence= 0.95)
   pyautogui.click(enter2)
   

   time.sleep(0.2)

   # 조합된 몬스터는 당신의 농장으로
   mixButton2 = pyautogui.locateOnScreen('button/button2.png',confidence= 0.95)
   pyautogui.click(mixButton2)
   
   if keyboard.is_pressed('q'):
        print('Quit')
        time.sleep(10000)
        return 0  
   
   #예외 창 처리
   exception()

   time.sleep(0.07)
   # 타깃 몬스터가 남아있다면?
   mix1_2 =  pyautogui.locateOnScreen('Rec' + str(num)+ '/mix2.png',confidence= 0.99)
   # 타깃 몬스터가 없으면 함수 종료
   if mix1_2 :
       print ('one more target '+ str(num) +  '  found')
       mix(num, mixcount +1 ) 
       return 0



   return 1


def visit():
   # 랜덤방문 버튼 클릭
   visit = pyautogui.locateOnScreen('button/visit.png',confidence= 0.9)
   pyautogui.click(visit)
   time.sleep(0.1)
   
   # 농장에 방문합니다
   mixButton2 = pyautogui.locateOnScreen('button/button2.png',confidence= 0.9)
   pyautogui.click(mixButton2)
   time.sleep(2)



def visitMyroomTo():
   

   # 상점에 방문합니다
   shop = pyautogui.locateOnScreen('button/shop.png',confidence= 0.9)
   pyautogui.click(shop)
   
   # 랜덤방문 버튼 클릭
   visit = pyautogui.locateOnScreen('button/door.png',confidence= 0.9)
   pyautogui.click(visit)
  
   
   # 농장에 방문합니다
   door2 = pyautogui.locateOnScreen('button/door2.png',confidence= 0.9)
   pyautogui.click(door2)
   

   #확인
   mixButton2 = pyautogui.locateOnScreen('button/button2.png',confidence= 0.9)
   pyautogui.click(mixButton2)
   
   
   
   time.sleep(2)

   # 현 위치가 아직도 샵이라면 재실행
   if nowPlace() is 3 :
       visitMyroomTo()

     

def OtherToHome():
     if pyautogui.locateOnScreen('button/fulled.png',confidence= 0.98) and   pyautogui.locateOnScreen('place/otherroom1.png',confidence= 0.95)   :
        gohome = pyautogui.locateOnScreen('button/gohome.png',confidence= 0.9)
        
        pyautogui.click(gohome)


        time.sleep(4)
        
        return 1

     else :
        return 0  



#남의 농장 방문
def friendVisit()  : 
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
            config.close()
            return -1

        index1 = lineChange('index', index1 + 1 )
        config.close()
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



def exception():
    if pyautogui.locateOnScreen('button/nope1.png',confidence= 0.97) :
        nope2 = pyautogui.locateOnScreen('button/nope2.png',confidence= 0.97)
        pyautogui.click(nope2)

    nope3= pyautogui.locateOnScreen('button/nope3.png',confidence= 0.97)
    pyautogui.click(nope3)


def screenshots(screenshots):
      
    if int(screenshots) == 1:
      #if lineReturn("index") == -1 :   # 농장돌이가 종료되었을때만 스샷
        try:
            
            print("target parm cature..")
            hwnd = win32gui.FindWindow(None, r'MapleStory')
            win32gui.SetForegroundWindow(hwnd)
            dimensions = win32gui.GetWindowRect(hwnd)
            
            area =  (5,30 , 119 , 224)

            image = ImageGrab.grab(dimensions)
            image = image.crop(area)
            nowDate = datetime.datetime.now()

            image.save('screenshots/parm' + nowDate.strftime("%Y-%m-%d %M-%S") + '.png'    )
        except:
            print("capture error...")        
  
## 메인 프로그램 


da = "date"
New_Value = str(time.strftime('%d', time.localtime(time.time() )) )


i = lineReturn(da)
today =  int(time.strftime('%d', time.localtime(time.time() ))  )

print(today)

# 날짜가 바뀌었다면 날짜와 인덱스 초기화





# 프로그램 속도
speed = 1
time.sleep(2)

try:
    config = open("config.txt", 'r+')
    lines = config.readlines()
    config.close()


    rec1 = str(lines[1].rstrip('\n'))
    rec2 = str(lines[5].rstrip('\n'))
    rec3 = str(lines[9].rstrip('\n'))
    rec4 = str(lines[13].rstrip('\n'))
    rec5 = str(lines[17].rstrip('\n'))
    rec6 = str(lines[21].rstrip('\n'))
    rec7 = str(lines[25].rstrip('\n'))
    


    mixcount1 = 0
    mixcount2 = 0
    mixcount3 = 0
    mixcount4 = 0
    mixcount5 = 0
    mixcount6 = 0
    mixcount7 = 0
    
    screenshots1 = int(lineReturn("screenshots1"))
    screenshots2 = int(lineReturn("screenshots2"))
    screenshots3 = int(lineReturn("screenshots3"))
    screenshots4 = int(lineReturn("screenshots4"))
    screenshots5 = int(lineReturn("screenshots5"))
    screenshots6 = int(lineReturn("screenshots6"))
    screenshots7 = int(lineReturn("screenshots7"))
    
    #버릴 몬스터 수
    dis = int(lineReturn("discard"))
    
    # 농장 인덱싱을 위해 텍스트파일에서 인덱스 필드를 소환
    #index1 = lineReturn("index")
    index1 = -1

    # Parms = open("Parms.txt", 'r+')
    # initIndextoDate()
    # linesParm = Parms.readlines()
    # Parms.close()
    
   



except :
    print('config file error')
    time.sleep(40000)






while 1 :
     
    # 현재 위치 파악
    np = nowPlace()

    ## 현재 위치가 남의 농장일 경우
    if np is 2 :
        
        for i in range(4):


            GoHome = OtherToHome()                  
            if GoHome == 1 :
                    break
            

            # 키보드 이벤트 캐치    
            if keyboard.is_pressed('q'):
                print('Quit')
                time.sleep(10000)
                break


            if rec1 == "run" :         
                mix1 =  mix(1, mixcount1)

                
                # 로그 출력기능
                if mix1 is 1:
                  screenshots(screenshots1)
                  GoHome = OtherToHome()  
                  mixcount1 = mixcount1 + 1

                  if GoHome == 1 :
                   break
           
            #키보드 이벤트 캐치
            if keyboard.is_pressed('q'):
                print('Quit')
                time.sleep(10000)
                break

            if rec2 == "run" :         
                mix2 =  mix(2, mixcount2)

                # 로그 출력기능
                if mix2 is 1:
                  screenshots(screenshots2)
                  GoHome = OtherToHome()  
                  mixcount2 = mixcount2 + 1
                  
                  if GoHome == 1 :
                   break

            # 키보드 이벤트 캐치    
            if keyboard.is_pressed('q'):
                print('Quit')
                time.sleep(10000)
                break


            if rec3 == "run" :         
                mix3 =  mix(3, mixcount3)
                # 로그 출력기능
                if mix3 is 1:
                  screenshots(screenshots3)  
                  GoHome = OtherToHome()  
                  mixcount3 = mixcount3 + 1
                  
                  if GoHome == 1 :
                   break

            # 키보드 이벤트 캐치    
            if keyboard.is_pressed('q'):
                print('Quit')
                time.sleep(10000)
                break


            if rec4 == "run" :         
                mix4 =  mix(4, mixcount4)
                # 로그 출력기능
                if mix4 is 1:
                  screenshots(screenshots4)  
                  GoHome = OtherToHome()  
                  mixcount4 = mixcount4 + 1
                  
                  if GoHome == 1 :
                   break
           
            # 키보드 이벤트 캐치    
            if keyboard.is_pressed('q'):
                print('Quit')
                time.sleep(10000)
                break


            if rec5 == "run" :         
                mix5 =  mix(5, mixcount5)
                # 로그 출력기능
                if mix5 is 1:
                  screenshots(screenshots5)  
                  GoHome = OtherToHome()  
                  mixcount5 = mixcount5 + 1
                  
                  if GoHome == 1 :
                   break 

            # 키보드 이벤트 캐치    
            if keyboard.is_pressed('q'):
                print('Quit')
                time.sleep(10000)
                break

            if rec6 == "run" :         
                mix6 =  mix(6, mixcount6)
                # 로그 출력기능
                if mix6 is 1:
                  screenshots(screenshots6)  
                  GoHome = OtherToHome()  
                  mixcount6 = mixcount6 + 1
                  
                  if GoHome == 1 :
                   break
            
            if rec7 == "run" :         
                mix7 =  mix(7, mixcount7)
                # 로그 출력기능
                if mix7 is 1:
                  screenshots(screenshots7)  
                  GoHome = OtherToHome()  
                  mixcount7 = mixcount7 + 1
                  
                  if GoHome == 1 :
                   break
            


            if i < 4:
             scrollmouse(7)
            

       
        #농장 꽉 차있다면 중단하고 내 농장 직행
                           
        # 그렇지 않다면 랜덤방문 시전
        
        else: 
            exception()       
            
          #인덱스가 남아있다면 프렌드 방문            
              #
           ## 인덱스가 다 찼다면 랜덤방문 
            if index1 == -1:             
                 visit()      
            
            # 농장 목록을 다 순회하였으면 랜덤 방문
            else: 
                visit()


    ## 현재 위치가 내 농장일 경우
    if np is 1 :
          
          exception()

          
           # 키보드 이벤트 캐치 
          if keyboard.is_pressed('q'):
                print('Quit')
                time.sleep(10000)
                break
          
          discard(dis)
      
          time.sleep(2)
            

        ## 랜덤방문 이용
          if keyboard.is_pressed('q'):
                print('Quit')
                time.sleep(10000)
                break
          
          
          #인덱스가 남아있다면 프렌드 방문

          initIndextoDate()
          
          ## 인덱스가 다 찼다면 랜덤방문 
          if index1 == -1:          
            visitMyroomTo()
          else:
              visit()