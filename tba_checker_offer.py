# this does things
import pyautogui

# relevant images
baseStr = "images\\"
folder = baseStr + "folder_icon.png"
sign1 = baseStr + "sign.png"
sign2 = baseStr + "Sign2.png"
suspenses = baseStr + "suspenses.png"
waiting = baseStr + "waiting.png"


def locateAndClick(clickable):
    pyautogui.click(pyautogui.locateOnScreen(clickable, 0.9))


if __name__ == "__main__":
    while True:
        locateAndClick(folder)  # click twice to select virtual machine first
        locateAndClick(folder)
        locateAndClick(sign1)
        locateAndClick(sign2)
        locateAndClick(suspenses)
