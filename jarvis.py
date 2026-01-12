
import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import wikipedia
import pywhatkit as wk
import pyautogui as ag
import time
import psutil
import sys
import operator
import requests
import screen_brightness_control as sbc

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def open_whatsapp():
    ag.press('win')
    time.sleep(3)
    ag.typewrite('whatsapp',0.1)
    time.sleep(3)
    ag.press('enter')
    time.sleep(5)

def open_camera():
    ag.press('win')
    time.sleep(3)
    ag.typewrite('camera',0.1)
    time.sleep(3)
    ag.press('enter')
    time.sleep(5)

def increase_brightness(num):
    current_brightness = sbc.get_brightness()[0]  # Extract the first brightness value
    if current_brightness < 100:
        new_brightness = min(100, current_brightness + num)
        sbc.set_brightness(new_brightness)
        engine.say(f"Brightness increased to {new_brightness}%")
        engine.runAndWait()    

def decrease_brightness(num):
    current_brightness = sbc.get_brightness()[0]  # Extract the first brightness value
    if current_brightness > 0:
        new_brightness = max(0, current_brightness - num)
        sbc.set_brightness(new_brightness)
        engine.say(f"Brightness decreased to {new_brightness}%")
        engine.runAndWait()

def send_whatsapp_message(name,message):
    ag.moveTo(140,120) 
    ag.leftClick()
    ag.typewrite(name,0.1)
    ag.moveTo(207,185)
    ag.leftClick()
    time.sleep(2)
    ag.moveTo(632,825)
    ag.typewrite(message,0.1)
    ag.press('enter')

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
         speak("Good Evening!")

    speak("What can I do for you sir ?")

def open_notepad():
    speak("Opening Notepad...")
    ag.press('win')
    time.sleep(1)
    ag.typewrite('notepad')
    time.sleep(1)
    ag.press('enter')
    time.sleep(2)

def type_message(message):
    speak("Typing message...")
    ag.typewrite(message,interval=0.01)
    ag.press('enter')

def open_spotify():
    ag.press('win')
    time.sleep(3)
    ag.typewrite('spotify')
    time.sleep(3)
    ag.press('enter')
    time.sleep(5)

def play_music(music):
    ag.moveTo(1534,24)
    ag.leftClick()
    time.sleep(1)
    ag.moveTo(425,41)
    ag.leftClick()
    ag.typewrite(music,0.1)
    ag.press('enter')
    time.sleep(3)
    ag.moveTo(543, 449)  
    ag.leftClick()


def monitor_system():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
    print(f"Disk Usage: {disk_usage}%")
    speak(f"CPU Usage: {cpu_usage}%")
    speak(f"Memory Usage: {memory_usage}%")
    speak(f"Disk Usage: {disk_usage}%")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...") 
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source,phrase_time_limit=3)

    try:
      print("Recognizing...")
      query = r.recognize_google(audio, language='en-in ') # for more advancing start working on multiple languages
      print(f"User said: {query}\n")       

    except Exception as e :
        print("Say that again please...")    
        return "None"
    return query

def save_file():
                ag.hotkey('ctrl','shift','s')
                time.sleep(3)
                ag.moveTo(287,413)
                time.sleep(2)
                speak("what would you like to name it")
                name = takeCommand().lower()
                ag.typewrite(name,0.1)
                ag.press('enter')
                time.sleep(1)


def take_screenshot():
    speak("What would you like to name the screenshot?")
    name = takeCommand().lower()    
    
    screenshot_directory = r"D:\C PROGRAMING\jarvis\Screenshots"  
    if not os.path.exists(screenshot_directory):
        os.makedirs(screenshot_directory)  
     
    screenshot_path = os.path.join(screenshot_directory, f"{name}.png")
    speak("please open the slide you want to take screenshot of")
    time.sleep(3)
    speak("Taking screenshot...")
    screenshot = ag.screenshot()
    
    screenshot.save(screenshot_path)
    print(f"Screenshot saved as {name}.png in {screenshot_directory}")
    speak("screenshot captured")

def chrome_automation():
    os.startfile('C:\\Program Files\\Google\\Chrome\\Application')
    time.sleep(1)
    ag.moveTo(259,312)
    ag.doubleClick()
    time.sleep(1)
    ag.moveTo(1043, 375)
    time.sleep(1)
    ag.leftClick()
    time.sleep(1)

    while True:
        time.sleep(3)
        query = takeCommand().lower()

        if 'maximize this window' in query:
            ag.hotkey('alt', 'space')
            time.sleep(1)
            ag.press('x')
        elif 'google search' in query:
            query = query.replace('google search', '')
            ag.hotkey('alt', 'd')
            ag.write(f"{query}", 0.1)
            ag.press('enter')
        elif 'youtube search' in query:
            query = query.replace('youtube search', '')
            ag.hotkey('alt', 'd')
            time.sleep(1)
            ag.press('tab')
            ag.press('tab')
            ag.press('tab')
            ag.press('tab')
            time.sleep(1)
            ag.write(f"{query}", 0.1)
            ag.press('enter')
        elif 'open new window' in query:
            ag.hotkey('ctrl', 'n')
        elif "open incognito window" in query:
            ag.hotkey('ctrl', 'shift', 'n')
        elif "minimize this window" in query:
            ag.hotkey('alt', 'space')
            time.sleep(1)
            ag.press('n')
        elif "open history" in query:
            ag.hotkey('ctrl', 'h')
        elif "open downloads" in query:
            ag.hotkey('ctrl', 'j')
        elif "previous tab" in query:
            ag.hotkey('ctrl', 'shift', 'tab')
        elif "next tab" in query:
            ag.hotkey('ctrl', 'tab')
        elif "close tab" in query:
            ag.hotkey('ctrl', 'w')
        elif "close window" in query:
            ag.hotkey('ctrl', 'shift', 'w')
        elif "clear browsing history" in query:
            ag.hotkey('ctrl', 'shift', 'delete')
        elif "close chrome" in query:
            os.system("taskkill /f /im chrome.exe")
            break
        else :
            continue

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'jarvis' in query:
           print("yes sir")
           speak("yes sir")

        elif ( "who are you") in query:
            print("my name  is jarvis")
            speak("my name is jarvis")
            print("I can do everything that sir created me to do")
            speak("I can do everything that sir created me to do")

        elif "who created you" in query:
            print("i dont know there name but a group of 3 created me.")
            speak("i dont know there name but a group of 3 created me.")

        elif "what is" in query:
            try :
             speak("Searching Wikipedia...")   
             query = query.replace("what is","")
             results = wikipedia.summary(query,sentences=3)
             speak("According to Wikipedia")
             print(results)
             speak(results)

            except Exception as e :
                print("please tell the complete sentence") 
                speak("you have not told me what to search")

        elif 'who is' in query:
            try:
             speak("Searching Wikipedia...")   
             query = query.replace("who is","")
             results = wikipedia.summary(query,sentences=3)
             speak("According to Wikipedia")
             print(results)
             speak(results)

            except Exception as e :
                print("please tell the complete sentence") 
                speak("you have not told me what to search") 
          
        elif "just open google" in query:
            webbrowser.open('google.com') 

        elif "open google" in query:
            speak("what should i search")
            qry = takeCommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=3)
            speak(results)
        
        elif 'just open youtube' in query:
            webbrowser.open('youtube.com')

        elif "open youtube" in query:
            speak("what would like to watch")
            qrry = takeCommand().lower()
            wk.playonyt(f"{qrry}")

        elif "search on youtube" in query:
            query=query.replace("search on youtube","")    
            webbrowser.open(f"www.youtube.com/results?search_query={query}")
        
        elif "close browser" in query:
            os.system("taskkill /f /im msedge.exe")   
       
        elif "close google" in query:
            os.system("taskkill /f /im chrome.exe")   
       
        elif ('End' or "end" ) in query:
            speak("Goodbye sir!")
            exit()
      
        elif 'kill yourself'  in query:
            speak("Goodbye sir!")
            exit()
       
        elif 'type' in query:
            query = query.replace("type","")
            ag.typewrite(f"{query}",3.0)   

        elif 'Thank you'   in query:
            speak("you're welcome !")         
        
        elif 'open notepad' in query:
              open_notepad()
              speak("What should i type sir")
              message = takeCommand()
              type_message(message)
              time.sleep(1)
              speak("Do you want to save the file?")
              attempts = 0
              while attempts < 3:
               res = takeCommand()
               if res in ['no', 'nope']:
                speak("File not saved.")
                break
               elif res in ['ha','ho','yes','yes yes','yup']:
                save_file()
                break
               else:
                 speak("Say that again, please.")
                 attempts += 1
                
        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")   

        elif "play music"  in query:
            speak("opening spotify") 
            open_spotify()
            speak("What music would you like to play")
            music = takeCommand().lower()
            play_music(music)

        elif "pause music" in query:
            open_spotify()
            ag.moveTo(794,776)  
            ag.leftClick()  

        elif "close spotify" in query:
            os.system("taskkill /f /im spotify.exe")   

        elif "open whatsapp" in query:
            open_whatsapp()

        elif "send message on whatsapp" in query:
            open_whatsapp()
            speak("what is the contact name")
            name = takeCommand().lower()
            speak("what message would you like to send")
            message = takeCommand().lower()
            send_whatsapp_message(name,message)  
            speak("message sended") 

        elif "close whatsapp" in query:
            os.system("taskkill /f /im whatsapp.exe")   

        elif "tell me the time" in query:           
          strTime = datetime.datetime.now().strftime("%I:%M:%p")
          speak(f"Sir, the time is {strTime}")
          
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "Lock the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "Hibernate the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "go to sleep" in query:
            speak("enabling sleep mode")
            sys.exit()

        elif "take screenshot" in query:
            take_screenshot()

        elif "calculate" in query:
            try :
             r = sr.Recognizer()
             with sr.Microphone() as source:
                speak("ready")
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return{
                        '+':operator.add,
                        '-':operator.sub,
                        'x':operator.mul,
                        '/':operator.__truediv__,
                    }[op]
                def eval_binary_exp(op1,oper,op2)  :
                    op1,op2 = int(op1), int (op2) 
                    return get_operator_fn(oper)(op1,op2)
                speak("your result is:")
                speak(eval_binary_exp(*(my_string.split())))   
            except Exception as e :
                speak("Some error has occured")

        elif "what's my ip address" in query:
            speak("checking")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                speak("your ip address is")
                speak(ipAdd)
            except Exception as e:
                speak("please try again later")              

        elif "volume up" in query: 
          speak("One volume up causes it to add by 2.")
          speak("How many times do you want to raise your volume?")
          while True:
           try:
            command = takeCommand()
            if command is None or command == "":
                speak("Sorry, I didn't hear that. Please try again.")
                continue
            x = int(command)
            if x <= 0:
                speak("Please enter a positive number.")
                continue
            break
           except ValueError:
            speak("That's not a valid number. Please try again.")

          for _ in range(x):
           ag.press('volumeup')
          speak(f"Volume raised by {x * 2} units.")


        elif "volume down" in query:  
          speak("One volume down causes it to deduce by 2.")
          speak("How many times do you want to deduce your volume?")
          while True:
           try:
            command = takeCommand()
            if command is None or command == "":
                speak("Sorry, I didn't hear that. Please try again.")
                continue
            x = int(command)
            if x <= 0:
                speak("Please enter a positive number.")
                continue
            break
           except ValueError:
            speak("That's not a valid number. Please try again.")

          for _ in range(x):
           ag.press('volumedown')
          speak(f"Volume downed by {x * 2} units.")

        elif "mute"  in query:
            ag.press("volumemute")

        elif "unmute"  in query:
            ag.press("volumemute")
 
        elif "refresh the system" in query:
            ag.moveTo(1479,15)
            ag.leftClick()
            time.sleep(3)
            ag.moveTo(812,271)
            ag.rightClick()
            ag.moveTo(869,352)
            time.sleep(3)
            ag.leftClick()
            speak("system refreshed")
            ag.moveTo(1131,878)
            ag.leftClick()

        elif "open chrome" in query:    
            #chrome automation
            #not working properly
            chrome_automation()

        elif "open camera" in query:
                open_camera()

        elif "take a photo"in query:
                open_camera()
                ag.moveTo(1547,439)
                speak("Say cheeseeee")
                time.sleep(3)
                ag.leftClick()
                speak("photo captured")

        elif "close camera" in query:
            
                os.system("taskkill /f /im WindowsCamera.exe")    

        elif "open cmd" in query:
           speak("opening cmd")
           os.system('start cmd') 

        elif "close cmd" in query:
            os.system('taskkill /f /im cmd.exe')       

        elif "what's my pc status" in query:
            monitor_system()
       
        elif "increase brightness" in query:
            speak("By what number do you want to increase brightness")
            num = int(takeCommand())
            increase_brightness(num)

        elif "decrease brightness" in query:
            speak("By what number do you want to decrease brightness")
            num = int(takeCommand())
            decrease_brightness(num)

            
