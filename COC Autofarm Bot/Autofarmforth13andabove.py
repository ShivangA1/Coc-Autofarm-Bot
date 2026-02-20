import pyautogui
import time

coclogo = pyautogui.locateOnScreen("coc.png", confidence=0.9)
pyautogui.click(coclogo)
battle_start = None

while True:
    if pyautogui.pixelMatchesColor(350, 779, (239, 173, 66), tolerance=10):
        pyautogui.click(350, 779)
        time.sleep(0.7)
        match = pyautogui.locateOnScreen("findamatch.png", confidence=0.9)
        pyautogui.click(match)
        time.sleep(0.7)
        attack = pyautogui.locateOnScreen("attack.png", confidence=0.9)
        pyautogui.click(attack)
        time.sleep(2)
        battle_start = time.time()

    elif pyautogui.pixelMatchesColor(1129, 834, (147, 110, 77), tolerance=10):
        pyautogui.click(1129, 834)
        for i in range(0, 4):
            pyautogui.click(716, 499)
        for i in range(0, 4):
            pyautogui.click(1003, 347)
        for i in range(0, 3):
            pyautogui.click(1206, 490)
        pos = pyautogui.locateOnScreen("valkyrie.png", confidence=0.9)
        pyautogui.click(pos)
        pyautogui.moveTo(430, 487)
        pyautogui.dragTo(872, 165, 2, pyautogui.easeInQuad, button="left")
        pyautogui.moveTo(1514, 507)
        pyautogui.dragTo(1188, 752, 2, pyautogui.easeInQuad, button="left")
        pyautogui.moveTo(430, 487)
        pyautogui.dragTo(753, 767, 2, pyautogui.easeInQuad, button="left")
        pyautogui.moveTo(1514, 507)
        pyautogui.dragTo(1091, 191, 2, pyautogui.easeInQuad, button="left")
        time.sleep(0.2)
        pyautogui.click(709, 828)
        time.sleep(0.2)
        pyautogui.click(1255, 312)
        time.sleep(0.2)
        pyautogui.click(799, 832)
        time.sleep(0.2)
        pyautogui.click(1255, 312)
        time.sleep(0.2)
        pyautogui.click(799, 832)
        time.sleep(0.2)
        pyautogui.click(889, 831)
        time.sleep(0.2)
        pyautogui.click(1255, 312)
        time.sleep(0.2)
        pyautogui.click(889, 831)
        time.sleep(0.2)
        pyautogui.click(966, 824)
        time.sleep(0.2)
        pyautogui.click(1255, 312)
        time.sleep(0.2)
        pyautogui.click(966, 824)
        time.sleep(0.2)
        pyautogui.click(1038, 833)
        time.sleep(0.2)
        pyautogui.click(1255, 312)
        time.sleep(0.2)
        pyautogui.click(1038, 833)
        time.sleep(0.2)

    else:
        time.sleep(2)
        if pyautogui.pixelMatchesColor(1447, 736, (197, 201, 195), tolerance=10):
            end = pyautogui.locateOnScreen("endbattle.png", confidence=0.9)
            pyautogui.click(end)
            time.sleep(0.5)
            pyautogui.click(1060,613)
            time.sleep(0.5)
            pyautogui.click(958,786)
        elif battle_start is not None:
            if time.time() - battle_start >= 40:
                pyautogui.click(389,732)
                time.sleep(0.5)
                pyautogui.click(1060,613)
                time.sleep(0.5)
                pyautogui.click(958,786)
                battle_start = None
