
import threading
import time


exitflag = False
globallightstate = False

globallightlock = threading.RLock()

event = threading.Event()


class LightHandler(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        global globallightstate

        self.id = id
        self.lastlightstate = globallightstate

    def run(self):
        global globallightstate, exitflag, globallightlock, event

        while not exitflag:
            if event.wait(0.01):
                print("event received")
                if globallightstate != self.lastlightstate:
                    print("Switching lighstate from ",
                          self.lastlightstate, " to ", globallightstate)
                    self.lastlightstate = globallightstate
                event.clear()
            # else:
            #     print("Event timeout")


class LightControler():
    __instance = None
    @staticmethod 
    def get_instance():
        if LightControler.__instance == None:
            LightControler()
        return LightControler.__instance

    def __init__(self):
        if LightControler.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            LightControler.__instance = self
            self.lighthandler = LightHandler(1)

    def start(self):
        self.lighthandler.start()

    def stop(self):
        global exitflag
        exitflag = True
        self.lighthandler.join()

    def setLightState(self, newlightstate):
        global globallightlock, globallightstate, event

        globallightstate = newlightstate
        event.set()

    def getLightState(self):
        global globallightstate
        return globallightstate
