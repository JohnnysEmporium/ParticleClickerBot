# https://particle-clicker.web.cern.ch/particle-clicker/

import pyautogui
import time
import threading

class center():
    
    def data(self):
        self.scsh = pyautogui.screenshot(region = (550, 240, 1050, 700))
        self.target = pyautogui.locateOnScreen('particle.png')
        self.target = pyautogui.center(self.target)

    def clck(self):
        self.data()
        try:
            while True:
                pyautogui.click(self.target)
        except KeyboardInterrupt:
            pass
    
# ZJEBANE KLIKA ZABLOKOWANE PRZYCISKI, WYMYSLIC COS INNEGO OD LOCATEONSCREEN, 424 W AUTOMATE (albo locate all on screen, puscisc klikanie z listy od tylu(lepsze upgrady))

class upgrades():
    
    def data(self):
        self.targets = []
        self.target = pyautogui.locateAllOnScreen('data.png')
        for i in self.target:
            self.targets.append(i)
        self.targets.reverse()
        print(self.targets)
        
            
        
    def clck(self):
        while True:
            try:
                self.data()
                for i in range(len(self.targets)):
                    if pyautogui.pixelMatchesColor(int(self.targets[i][0]) + 10, int(self.targets[i][1]) + 10, (51, 122, 183), tolerance = 40):
                        pyautogui.click(self.targets[i][0] + 10, self.targets[i][1] + 10)
                        print('upgrade click')
            except KeyboardInterrupt:
                break
            finally:
                time.sleep(.01)


if __name__ == "__main__":
    threadCenter = threading.Thread(target = center().clck)
    threadUpgrades = threading.Thread(target = upgrades().clck)
    
    threadCenter.start()
    threadUpgrades.start()