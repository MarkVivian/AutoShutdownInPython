import datetime
import os
# this will allow us to know the platform we are running in.
import platform
import time
# pyttsx3 package is better since it works offline.
# in ubuntu, we have to install another package called libspeak1 using sudo apt-get install
# it is needed to run the pyttsx3 in ubuntu.
import pyttsx3
'''
there is an error downloading this file.
# win10toast package will allow us to produce a pop-up.
from win10toast import ToastNotifier
'''
# this will initiate the pyttsx3 module
engine = pyttsx3.init()


class Shutdown:
    def __init__(self):
        # this will call the function when we call the class.
        self.auto_shutdown()

        # this code will produce a prompt which will inform us that the script is running.

    @staticmethod
    def shutdown():

        # this will check the os being used.
        if platform.system() == "Linux":
            # this will Shut down the pc
            os.system("shutdown -t 3600")
        else:
            # this will Shut down the pc
            os.system("shutdown /s /t 1")

        # this will make sure greeting is concurrent with the time.
        if datetime.datetime.now().hour < 12:
            # this is what the engine will say.
            engine.say("Good Morning Sir")
        else:
            engine.say("good evening Sir")

        engine.say("the pc is shutting down")
        # this will run the engine and play the sound
        engine.runAndWait()

    def auto_shutdown(self):
        while True:
            # gets the current time and date
            current = datetime.datetime.now()

            # filters the current to only the hour.
            hour = current.hour

            print(f"{current.time()}")
            if hour == 22:
                # calls the Shutdown function
                engine.say("the pc will Shutdown in an hour")
                engine.say("please finish up")
                # this will run the engine and play the sound
                engine.runAndWait()

                # this will make the code wait for an hour
                time.sleep(3600)
                self.shutdown()

                # the return will stop the code
                return False

            # it will sleep for one second
            time.sleep(1)


if __name__ == '__main__':
    if platform.system() != "Linux":
        '''
        toast = ToastNotifier()
        # give it the title, message and the duration
        toast.show_toast("Auto Shutdown", "the Shutdown script is running", duration=30)
        '''
    shutdown = Shutdown()
