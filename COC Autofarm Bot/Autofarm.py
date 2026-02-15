import pyautogui
import time

coclogo=pyautogui.locateOnScreen("coc.png",confidence=0.9)
pyautogui.click(coclogo)

start=time.time()
while True:
    if pyautogui.pixelMatchesColor(378,809,(221,208,180)):
        pyautogui.click(378,809)
        time.sleep(0.5)
        match=pyautogui.locateOnScreen("findamatch.png",confidence=0.9)
        pyautogui.click(match)
        time.sleep(0.5)
        attack=pyautogui.locateOnScreen("attack.png",confidence=0.9)
        pyautogui.click(attack)
    elif pyautogui.pixelMatchesColor(967,831,(66,39,10)):
            pyautogui.click(967,831)
            for i in range(0,4):
                    pyautogui.click(716,499)
            for i in range(0,4):
                    pyautogui.click(1003,347)
            for i in range(0,3):
                    pyautogui.click(1206,490)
            if pyautogui.pixelMatchesColor(632,833,(81,41,31)):
                pyautogui.click(632,833)
                pyautogui.moveTo(430,487)
                pyautogui.dragTo(872,165,2,pyautogui.easeInQuad,button='left')
                pyautogui.moveTo(1514,507)  
                pyautogui.dragTo(1188,752,2,pyautogui.easeInQuad,button='left')
                pyautogui.moveTo(430,487)         
                pyautogui.dragTo(753,767,2,pyautogui.easeInQuad,button='left')
                pyautogui.moveTo(1514,507)
                pyautogui.dragTo(1091,191,2,pyautogui.easeInQuad,button='left')
                time.sleep(2)
            pyautogui.click(709,828)
            time.sleep(0.2)
            pyautogui.click(1255,312)
            time.sleep(0.2)
            pyautogui.click(709,828)
            time.sleep(0.2)
            pyautogui.click(800,830)
            time.sleep(0.2)
            pyautogui.click(1255,312)
            time.sleep(0.2)
            pyautogui.click(800,830)
            time.sleep(0.2)
            pyautogui.click(881,819)
            time.sleep(0.2)
            pyautogui.click(1255,312)
            time.sleep(0.2)
            pyautogui.click(881,819)
    else:
        end=time.time()
        if pyautogui.pixelMatchesColor(1447,736,(173,176,171)):
                    end=pyautogui.locateOnScreen("endbattle.png",confidence=0.9)
                    pyautogui.click(end)
                    time.sleep(0.5)
                    ok=pyautogui.locateOnScreen("okay.png",confidence=0.9)
                    pyautogui.click(ok)
                    time.sleep(0.5)
                    returnh=pyautogui.locateOnScreen("returnhome.png",confidence=0.9)
                    pyautogui.click(returnh)
        elif int(time.time() - end)==50:
                end=pyautogui.locateOnScreen("endbattle.png",confidence=0.9)
                pyautogui.click(end)
                time.sleep(0.5)
                ok=pyautogui.locateOnScreen("okay.png",confidence=0.9)
                pyautogui.click(ok)
                time.sleep(0.5)
                returnh=pyautogui.locateOnScreen("returnhome.png",confidence=0.9)
                pyautogui.click(returnh)