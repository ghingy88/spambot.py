import pyautogui, time
#may need to pip install pyautogui or it wont work

def spamMsg():
    time.sleep(0.75)
    f = open("word.txt", 'r')
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")


#start the bot by inputting "x"
startBot = input("press 'x' to start bot\n>")
if startBot == "x":
    while True:
        spamMsg()

#end by closing bot
