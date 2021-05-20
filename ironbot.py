# oddloop comments:
# queue accept portion source code from https://github.com/matiasperz/lol-auto-accept

import pyautogui
from python_imagesearch.imagesearch import imagesearch
import time
import pydirectinput
import random

pyautogui.FAILSAFE = False
TIMELAPSE = 1

acceptButtonImg = './sample.png'
acceptedButtonImg = './sample-accepted.png'
championSelectionImg_flash = './flash-icon.png'
championSelectionImg_emote = './emote-icon.png'
playButtonImg = './play-button.png'
dravenImg = './draven.png'
amumuImg = './amumu.png'
eveImg = './eve.png'
lockinImg = './LockInButton.png'
dravenlockedinImg = './dravenlockedin.png'
banImg = './ban1.png'
banbtnImg = './banbtn.png'
chooseImg = './choose.png'
baseImg = './base.png'
critlolImg = './critlol.png'
loadingscreenImg = './loadingscreen1.png'
honorImg = './honor.png'
lobbyImg = './lobby.png'
findmatchImg = './findmatch.png'
lobbyqueueImg = './lobbyqueue.png'
yuumilockedinImg = './yuumilockedin.png'
barrelImg = './barrel.png'
boatImg = './boat.png'
levelupImg = './levelup.png'
ffImg = './ff.png'
afkImg = './afk.png'
qreadyImg = './qready.png'
ereadyImg = './eready.png'
xgoodImg = './xgood.png'
xbadImg = './x.png'

def randomsmallnum():
    smallnum = random.uniform(1.0, 1.9)
    return smallnum

def randomsmolnum():
    smolnum = random.uniform(3.0, 5.9)
    return smolnum

def randommediumnum():
    mediumnum = random.uniform(12, 25)
    return mediumnum

def randombignum():
    bignum = random.uniform(45, 60)
    return bignum

def randomqcoordinates():
    xcoordinates = random.randint(900, 1300)
    ycoordinates = random.randint(300, 500)
    return xcoordinates, ycoordinates

def LockedIn():
    pos = imagesearch(yuumilockedinImg, 0.8)
    if not pos[0] == -1:
        return True
    else:
        return False


def LockInYuumi():
    pyautogui.click(1131, 262)
    pyautogui.write("yuumi")
    time.sleep(randomsmallnum())
    pyautogui.click(699, 324)
    time.sleep(randomsmallnum())
    pyautogui.click(951, 764)

def checkGameAvailableLoop():
    while True:
        pos = imagesearch(acceptButtonImg, 0.8)
        if not pos[0] == -1:
            pyautogui.click(pos[0], pos[1])
            print("Game accepted!")
            break
        
        time.sleep(randomsmallnum())
    

def checkChampionSelection():
    flash = imagesearch(championSelectionImg_flash)
    emote = imagesearch(championSelectionImg_emote)

    if not emote[0] == -1 or not flash[0] == -1:
        return True
    else:
        return False

def checkGameCancelled():
    accepted = imagesearch(acceptedButtonImg)
    play = imagesearch(playButtonImg)

    if accepted[0] == -1 and not play[0] == -1:
        return True
    else:
        return False

def YourTurnToPick():
    choose = imagesearch(chooseImg, 0.8)
    if not choose[0] == -1:
        return True
    else:
        return False

def YourTurnToBan():
    ban = imagesearch(banImg, 0.8)
    if not ban[0] == -1:
        return True

def BanEve():
    eve = imagesearch(eveImg, 0.8)
    if not eve[0] == -1:
        pyautogui.click(eve[0], eve[1])
        banbtn = imagesearch(banbtnImg, 0.8)
        if not banbtn[0] == -1:
            pyautogui.click(banbtn[0], banbtn[1])
            print("Banned Eve")
    else:
        print("Could not find Eve")


def inlobby():
    pos = imagesearch(findmatchImg, 0.8)
    if not pos[0] == -1:
        return True 

def inlobbyqueue():
    pos = imagesearch(lobbyqueueImg, 0.8)
    if not pos[0] == -1:
        return True 

def matchfound():
    pos = imagesearch(acceptButtonImg, 0.8)
    if not pos[0] == -1:
        return True 

def ingame():
    pos = imagesearch(critlolImg)
    if not pos[0] == -1:
        return True

def loadscreen():
    pos = imagesearch(loadingscreenImg)
    if not pos[0] == -1:
        return True

def inbase():
    pos = imagesearch(barrelImg)
    if not pos[0] == -1:
        return True

def inbase1():
    pos = imagesearch(boatImg)
    if not pos[0] == -1:
        return True

def skillupavailable():
    pos = imagesearch(levelupImg)
    if not pos[0] == -1:
        return True

def iloveff():
    pos = imagesearch(ffImg)
    if not pos[0] == -1:
        return True

def honorscreen():
    pos = imagesearch(honorImg)
    if not pos[0] == -1:
        return True

def afk():
    pos = imagesearch(afkImg)
    if not pos[0] == -1:
        return True

def clickok():
    pos = imagesearch(afkImg)
    pyautogui.moveTo(pos[0], pos[1], randomsmallnum(), pyautogui.easeInQuad)
    pydirectinput.mouseDown(); pydirectinput.mouseUp()

def qready():
    pos = imagesearch(qreadyImg)
    if not pos[0] == -1:
        return True

def eready():
    pos = imagesearch(ereadyImg)
    if not pos[0] == -1:
        return True

def postgame():
    pos = imagesearch(xgoodImg)
    if not pos[0] == -1:
        return True

def postgameafk():
    pos = imagesearch(xbadImg)
    if not pos[0] == -1:
        return True

def choosepositions():
    print('choosing positions')
    pyautogui.click(800, 632)
    time.sleep(randomsmallnum())
    pyautogui.click(903, 637)
    time.sleep(randomsmallnum())
    pyautogui.click(903, 637)
    time.sleep(randomsmallnum())
    pyautogui.click(897, 536)
    time.sleep(randomsmallnum())
    pyautogui.click(853, 841)

def restartlobby():
    if postgame() is True:
        pyautogui.click(853, 841)
    if postgameafk() is True:
        pyautogui.click(765, 840)
        time.sleep(randomsmallnum())
        pyautogui.click(436, 200)
        time.sleep(randomsmallnum())
        pyautogui.click(547, 730)
        time.sleep(randomsmallnum())
        pyautogui.click(853, 841)
        time.sleep(randomsmallnum())
    choosepositions()


def yuumibot():
    if loadscreen() is True:
        print("waking up, we're in loading screen")
        while True:
            pos = imagesearch(loadingscreenImg)
            if pos[0] == -1:
                break
            time.sleep(5)
    
    # initial instructions for start of game
    pydirectinput.write('y')                                    # lock screen xD
    time.sleep(randomsmallnum())

    print('buying support item')
    pydirectinput.write('p')                                     # buy support item
    pyautogui.moveTo(606, 261, randomsmallnum(), pyautogui.easeInQuad)
    pydirectinput.mouseDown(); pydirectinput.mouseUp()
    pyautogui.moveTo(692, 477, randomsmallnum(), pyautogui.easeInQuad)
    pydirectinput.click(692, 477, button='right')
    pydirectinput.write('p')

    print('attaching to host')
    pyautogui.moveTo(1571, 690, randomsmallnum(), pyautogui.easeInQuad)           # attaching to host
    pydirectinput.write('w')
    time.sleep(randommediumnum())

    print('leveling up e')
    pydirectinput.keyDown('ctrl')                                   # leveling up heal
    pydirectinput.press('e')
    pydirectinput.keyUp('ctrl')
    time.sleep(randomsmallnum())

    print('chatting with humans')
    pydirectinput.press('enter')
    pydirectinput.write('sry went to grab food')                    # pretend im human
    pydirectinput.press('enter')

    print('yuumi bot is tired again ;_; resting for 2 min')
    time.sleep(120)                                                 # wait 2 min since nothing will happen in game (jungle leash maybe, minion spawn)

    # yuumi should now be attached to someone, loop should run until game ends
    while True:
        w = 'inside'
        if inbase() is True or inbase1() is True:                 # 
            print('opening shop')
            pydirectinput.write('p')

            print('moving to all items')
            pyautogui.moveTo(750, 250, randomsmallnum(), pyautogui.easeInQuad)
            time.sleep(randomsmallnum())
            
            print('clicking on all items')
            pydirectinput.mouseDown(); pydirectinput.mouseUp()
            time.sleep(randomsmallnum())

            print('moving to star')
            pyautogui.moveTo(586, 335, randomsmallnum(), pyautogui.easeInQuad)
            time.sleep(randomsmallnum())

            print('clicking star')
            pydirectinput.mouseDown(); pydirectinput.mouseUp()
            time.sleep(randomsmallnum())

            print('moving to tear')
            pyautogui.moveTo(636, 402, randomsmallnum(), pyautogui.easeInQuad)
            time.sleep(randomsmallnum())

            print('buying tear')
            pydirectinput.click(636, 402, button='right')
            time.sleep(randomsmallnum())
            
            print('moving to support section')
            pyautogui.moveTo(796, 350, randomsmallnum(), pyautogui.easeInQuad)
            time.sleep(randomsmallnum())
            
            print('clicking support section')
            pydirectinput.mouseDown(); pydirectinput.mouseUp()
            time.sleep(randomsmallnum())
            
            print('moving to moonstone')
            pyautogui.moveTo(717, 748, randomsmallnum(), pyautogui.easeInQuad)
            time.sleep(randomsmallnum())
            
            print('buying moonstone')
            pydirectinput.click(717, 748, button='right')
            time.sleep(randomsmallnum())

            print('closing shop')
            pydirectinput.write('p')
            time.sleep(randomsmallnum())

            pyautogui.moveTo(1571, 690, randomsmallnum(), pyautogui.easeInQuad)
            pydirectinput.write('w')
            w = 'waiting'

        
        if skillupavailable() is True:
            pydirectinput.keyDown('ctrl')
            pydirectinput.press('r')
            pydirectinput.keyUp('ctrl')
            time.sleep(randomsmallnum())
            
            pydirectinput.keyDown('ctrl')
            pydirectinput.press('e')
            pydirectinput.keyUp('ctrl')
            time.sleep(randomsmallnum())

            pydirectinput.keyDown('ctrl')
            pydirectinput.press('q')
            pydirectinput.keyUp('ctrl')
            time.sleep(randomsmallnum())

            pydirectinput.keyDown('ctrl')
            pydirectinput.press('w')
            pydirectinput.keyUp('ctrl')
            time.sleep(randomsmallnum())
        
        if iloveff() is True:
            print('yuumi loves ff meowie <3')
            pyautogui.moveTo(1471, 594, randomsmallnum(), pyautogui.easeInQuad)
            time.sleep(randomsmallnum())

            pydirectinput.mouseDown(); pydirectinput.mouseUp()
            time.sleep(randomsmallnum())
        
        if afk() is True:
            clickok()

        if qready() is True:
            xco, yco = randomqcoordinates()
            pyautogui.moveTo(xco, yco, randomsmallnum(), pyautogui.easeInQuad)
            pydirectinput.write('q')
            time.sleep(randomsmallnum())

        if eready() is True:
            pydirectinput.write('e')
            time.sleep(randomsmolnum())

        if postgame() is True:
            break

        if postgameafk() is True:
            break

        if w == 'waiting':
            time.sleep(randombignum())
        
        if w == 'inside':
            time.sleep(randomsmolnum())



def main():
    run = True

    while run is True:
        print("currently looking for queue pop or loading screen")
        checkGameAvailableLoop()                                # continually checks for queue pop image, loop breaks once found
        time.sleep(TIMELAPSE)                                   # time.sleep makes the program wait before continuing each iteration of a loop, timelapse is set to 1 so it will wait 1 second 
        
        # only continues when queue pops and accept is clicked
        
        while True:                                             # break out of this loop if someone decline/dodge 
            cancelled = checkGameCancelled()                    # this one is kinda gay, this is the thing i made trent cancel queue for, it just checks that you're back in lobby screen after someone declined
            if cancelled is True:
                print("Some retard declined")
                break                                           # loop breaks and goes back to outer loop to check for queue pop again
            
            csResult = checkChampionSelection()
            if csResult is True:
                print("In Champ Select")
                while True:                                     # once in champ select, will constantly check for either: 1. dodge 2. your turn to pick 3. waiting to pick
                    if checkGameCancelled() is True:
                        print("Some retard dodged")
                        break

                    if YourTurnToBan() is True:
                        BanEve()

                    if YourTurnToPick() is True and LockedIn() is False:
                        print("Your turn to pick")
                        LockInYuumi()
                        print("Yuumi found and locked in :3")
                        break
                    time.sleep(TIMELAPSE)
                break
            time.sleep(TIMELAPSE)                               # remove if it causes problems
        print("yuumi bot is tired (>.<) going to rest for 3 minutes")           # self explanatory.
        time.sleep(180)
        if inlobbyqueue() is True or matchfound() is True:         # if game got cancelled, continue queue pop search loop
            print('guess someone dodged while i slept :(')
            pyautogui.click(853, 841)
            continue
        if inlobby() is True:
            pyautogui.click(859, 844)
        if ingame() is True or loadscreen() is True or inbase() is True or inbase1() is True:
            yuumibot()
            restartlobby()
        time.sleep(TIMELAPSE)
        

if __name__ == '__main__':
    print("welcome to yuumi bot :3")
    main()