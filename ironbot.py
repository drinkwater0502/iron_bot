# oddloop comments:
# original source code from https://github.com/matiasperz/lol-auto-accept

# program so far only accepts queue and exits once inside champ select
# need to add lines that will find and lock in a champion
# as well as starting a new lobby once the game ends
# i added some comments in main if you want to see whats going on here

import pyautogui
from python_imagesearch.imagesearch import imagesearch_loop, imagesearch
import time

pyautogui.FAILSAFE = False
TIMELAPSE = 1

acceptButtonImg = './sample.png'
acceptedButtonImg = './sample-accepted.png'
championSelectionImg_flash = './flash-icon.png'
championSelectionImg_emote = './emote-icon.png'
playButtonImg = './play-button.png'
dravenImg = './draven.png'
lockinImg = './LockInButton.png'
dravenlockedinImg = './dravenlockedin.png'
banImg = './ban.png'
chooseImg = './choose.png'


def LockInDraven():
    while True:
        pos = imagesearch(dravenImg, 0.8)
        if not pos[0] == -1:
            pyautogui.click(pos[0], pos[1])
            break
        time.sleep(TIMELAPSE)
    pos = imagesearch(lockinImg, 0.8)
    pyautogui.click(pos[0], pos[1])

def checkGameAvailableLoop():
    while True:
        pos = imagesearch(acceptButtonImg, 0.8)
        if not pos[0] == -1:
            pyautogui.click(pos[0], pos[1])
            print("Game accepted!")
            break
        
        time.sleep(TIMELAPSE)
    

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



def main():
    run = True

    while run is True:
        checkGameAvailableLoop()                                # continually checks for queue pop image, loop breaks once found
        time.sleep(TIMELAPSE)                                   # time.sleep makes the program wait before continuing each iteration of a loop, timelapse is set to 1 so it will wait 1 second 

        while True:                                             # this loop runs after queue pop is found and accept is clicked on
            cancelled = checkGameCancelled()                    # this one is kinda gay, this is the thing i made trent cancel queue for, it just checks that you're back in lobby screen after someone declined
            if cancelled is True:
                print("Some retard declined")
                break                                           # loop breaks and goes back to outer loop to check for queue pop again
            
            csResult = checkChampionSelection()
            if csResult is True:
                print("In Champ Select")
                while True:
                    if YourTurnToPick() is True:
                        print("Your turn to pick")
                        LockInDraven()
                        print("Draven found and locked in")
                        run = False
                        break
                    time.sleep(TIMELAPSE)
                break
        time.sleep(TIMELAPSE)
        

if __name__ == '__main__':
    print("Running...")
    main()