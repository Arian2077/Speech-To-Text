# you have to install speech_recognition,pyaudio and pyttsx3
import speech_recognition as spr
# import platform
# to get user OS ('Linux', 'Darwin', 'Java', 'Windows'):
# MY_OS = platform.system()

# with using lock , Im going to force user to select a file
lock = False
r = spr.Recognizer()
my_language = "fa-IR"

'''
in this section , We send our user to recording part then 
we are going to save our text in the txt file that the user can choose and in the
end the program show us the result
'''


def speech_To_Text():
    global lock
    if lock == True:
        while True:
            text = record_text()
            if text == "پایان" or text == "stop":
                break
            else:
                output_text(text)
                print(text)
    else:
        print("please load your txt file\n")


'''
in this function we are giving the voice , recognize the language and
then turn it to string
'''


def record_text():
    global my_language
    while True:
        try:

            with spr.Microphone() as source:

                r.adjust_for_ambient_noise(source, duration=0.2)

                audio2 = r.listen(source)

                Mytext = r.recognize_google(audio2, language=my_language)

                return Mytext

        except spr.RequestError as e:
            print("Could not request the results;{0}".format(e))

        except spr.UnknownValueError:
            print("you have to talk!!!")
    return


'''
we are going to save our string in a txt file, Im using (utf-8) encoding because
the recognizer had some problems with persian language

'''


def output_text(text):
    global file_name, drive

    # (value_when_true) if (condition) else (value_when_false)
    path = ("" if drive == "" else drive + ":/") + file_name + ".txt"

    f = open(path, "a", encoding="utf-8")
    f.write(text)
    f.write("\n")
    f.close()
    return


########################### loading or making new txt file ####################

def loading_file():
    global file_name, drive, lock
    try:
        file_name = input("Enter your file name: ")
        drive = input("Enter the drive that you saved your file in: ")
        
        file_name = "new file" if file_name == "" else file_name

        path = ("" if drive == "" else drive + ":/") + file_name + ".txt"
        
        with open(path, "r")as f:
            f.read()
            print("file found succsesfully\n")
            f.close()
            lock = True
    except:
        pass
        return


def making_file():
    global lock
    while True:
        file = input("What do you want to name your file? ")
        drive = input("Which drive you want to save your file? ")

        file = "new file" if file == "" else file

        path = ("" if drive == "" else drive + ":/") + file + ".txt"
        
        with open(path, "w")as f:
            f.write("")
            print("making file went succesfully\n")
            f.close()
            lock = False
            return
            
########################### Language Selection ####################


def language():
    global my_language
    print("1.Persian\n"+"2.English")
    choice = input("Select you're language(use numbers): ")
    
    match choice:
        case "1":
            my_language = "fa-IR"
            print("Now you can record your voice using Persian language\n")
            return
        case "2":
            my_language = "en-US"
            print("Now you can record your voice using English language\n")
            return
        case _:
            print("returning to menu...\n")

########################### Menu #########################


print("___\___\___\___\______Speech To Text______/___/___/___/_____")

while True:
    #  ( \r ) makes the cursor jump to the first column(begin of the line)
    myMenu = """
        \r1.start
        \r2.Enter new file
        \r3.making new file
        \r4.Language
        \r5.exit
        \r"""

    plan = input(myMenu+"what is your plan(use numbers)? ")

    match plan:
        case "1":
            speech_To_Text()
        case "2":
            loading_file()
        case "3":
            making_file()
        case "4":
            language()
        case "5":
            print("goodbye")
            break
        case _:
            # action-default
            print("Please enter one of the numbers on the menu!!!!")
