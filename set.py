import inquirer
import os
os.chdir("c:/progetti/clock/")
def ask_setting():


    questions = [
    inquirer.List('setting',
                    message="choose a setting$>",
                    choices=['Enters', 'Spaces',"exit"],
                ),
    ]

    return inquirer.prompt(questions)["setting"]


def set_new_value(setting):
    print(f"you choose {setting}\n\n what will the new value be?")
    new_value = input("$>")    #TODO make this part check values

    file = open("settings.txt", "r")

    text = file.read().split("\n")
    file.close()
    text_array = []
    for i in text:
        try:

            i = i.split(": ")
            i[1]
            text_array.append(i)
        except:

            continue

    for i in range(len(text_array)):

        if text_array[i][0] == setting:
            text_array[i][1] = new_value

    file = open("settings.txt", "w")

    for i in text_array:
        file.write(i[0]+": "+i[1]+"\n")


def main():
    print("Welcome to Yet-another-clock settings editor!\n\n")

    while True:
        os.system('cls')
        setting = ask_setting()
        os.system('cls')

        if setting == "exit":
            break

        set_new_value(setting)




main()

