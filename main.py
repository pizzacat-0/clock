import time
import os
os.chdir("c:/progetti/clock/")

def loadarray():

    file = open("numbers.txt", "r")
    file_Array = file.read().split("|\n")
    file_Arrayfinal = []

    for i in file_Array:
        i = i.split("\n")
        file_Arrayfinal.append(i)

    file.close()

    return file_Arrayfinal


def numdisplay(Time,nums_array,settings):    
    for i in range(settings["Enters"]):
        print("\n")
    head = ""
    for i in range(settings["Spaces"]):
        head = head + " "
    for i in range(8):  #print cycle
        time.sleep(0.1)
        print(head + nums_array[12][i]+nums_array[Time[0]][i]+nums_array[Time[1]][i]+nums_array[10][i]+nums_array[Time[2]][i]+nums_array[Time[3]][i]+nums_array[11][i])


def get_time():
    t = time.localtime()
    hours = int(time.strftime("%H", t))
    minutes = int(time.strftime("%M", t))
    h1 = hours // 10
    h2 = hours % 10
    m1 = minutes // 10
    m2 = minutes % 10
    return (h1,h2,m1,m2)


def get_secs():
    t = time.localtime()
    return int(time.strftime("%S", t))


def get_settings():
    f = open("settings.txt", "r")
    dictsettings = {}
    check = False

    while check == False:
        line = f.readline().strip("\n").split(": ")
        if line[0] == "":
            break
        dictsettings[line[0]] = int(line[1])
    f.close()

    return dictsettings


def time_loop():
    arr = loadarray()
    while True:
        times = get_time()
        numdisplay(times,arr,get_settings())
        time.sleep(60-get_secs())
        os.system('cls')


time_loop()


