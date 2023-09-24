from tkinter import messagebox
import os
import sys
import webbrowser
import threading
import customtkinter
import time
import keyboard
import pyautogui

root = customtkinter.CTk()
root.title("")
Macro1Bind1 = "f4"
Macro1Bind2 = "f3"
Macro2Bind1 = "f2"
Macro2Bind2 = "f1"


def start_macro1():
    global running_macro1 
    running_macro1 = True
    threading.Thread(target=macro1).start()

def stop_macro1():
    global running_macro1
    running_macro1 = False
    print("Macro One Ended")


def macro1():
    print("Macro One Started")
    while running_macro1:
        pyautogui.keyDown('S')
        time.sleep(0.5)
        pyautogui.keyUp('S')
        pyautogui.keyDown('Q')
        pyautogui.keyUp('Q')
        time.sleep(2.2)

def start_macro2():
    global running_macro2 
    running_macro2 = True
    threading.Thread(target=macro2).start()

def stop_macro2():
    global running_macro2
    running_macro2 = False
    print("Macro Two Ended")

def macro2():
    while running_macro2:
        pyautogui.keyDown('s')
        time.sleep(0.2)
        pyautogui.keyUp('s')
        pyautogui.move(0, 100)
        pyautogui.mouseDown(button='left')
        time.sleep(3.5)
        pyautogui.mouseUp(button='left')

def reload_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def join_server():
    webbrowser.open("https://discord.gg/Rk9BsjRe7Q")

def macro1_bind1(self):
    self.configure(text="Press a key to bind...")
    print("Worked")

    def bind_key():

        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            global Macro1Bind1
            keyboard.remove_hotkey(Macro1Bind1)  # Remove old hotkey binding
            print(event.name)
            Macro1Bind1 = event.name
            self.configure(text="Start Macro Key : " + Macro1Bind1)
            keyboard.add_hotkey(Macro1Bind1, start_macro1)

    # Create a new thread to bind the key without freezing the GUI
    threading.Thread(target=bind_key).start()

def macro1_bind2(self):
    self.configure(text="Press a key to bind...")
    print("Worked")

    def bind_key():
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            global Macro1Bind2
            keyboard.remove_hotkey(Macro1Bind2)  # Remove old hotkey binding
            print(event.name)
            Macro1Bind2 = event.name
            self.configure(text="End Macro Key : " + Macro1Bind2)
            keyboard.add_hotkey(Macro1Bind2, stop_macro1)

    # Create a new thread to bind the key without freezing the GUI
    threading.Thread(target=bind_key).start()

def macro2_bind1(self):
    self.configure(text="Press a key to bind...")
    print("Worked")

    def bind_key():
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            global Macro2Bind1
            keyboard.remove_hotkey(Macro2Bind1)  # Remove old hotkey binding
            print(event.name)
            Macro2Bind1 = event.name
            self.configure(text="Start Macro Key : " + Macro2Bind1)
            keyboard.add_hotkey(Macro2Bind1, start_macro2)

    # Create a new thread to bind the key without freezing the GUI
    threading.Thread(target=bind_key).start()

def macro2_bind2(self):
    self.configure(text="Press a key to bind...")
    print("Worked")

    def bind_key():
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            global Macro2Bind2
            keyboard.remove_hotkey(Macro2Bind2)  # Remove old hotkey binding
            print(event.name)
            Macro2Bind2 = event.name
            self.configure(text="End Macro Key : " + Macro2Bind2)
            keyboard.add_hotkey(Macro2Bind2, stop_macro2)


    threading.Thread(target=bind_key).start()

def quit2():
    quit()


root.sidebar_frame = customtkinter.CTkFrame(root, width=140, corner_radius=0)
root.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
root.sidebar_frame.grid_rowconfigure(4, weight=1)
root.logo_label = customtkinter.CTkLabel(root.sidebar_frame, text="Leopold's Macro Hub", font=customtkinter.CTkFont(size=20, weight="bold"))
root.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
root.sidebar_button_1 = customtkinter.CTkButton(root.sidebar_frame, text="Join Support Server", command=join_server)
root.sidebar_button_1.grid(row=1, column=0, padx=20, pady=20)
root.sidebar_button_2 = customtkinter.CTkButton(root.sidebar_frame, text="Reload Hub", command=reload_program)
root.sidebar_button_2.grid(row=2, column=0, padx=20, pady=20)
root.sidebar_button_3 = customtkinter.CTkButton(root.sidebar_frame, text="Close Hub", command=quit2)
root.sidebar_button_3.grid(row=3, column=0, padx=20, pady=20)

tab = customtkinter.CTkTabview(root)

tab.grid(row=0, column=1, padx=20, pady=20)
tab.add(name="Home Page")
tab.add(name="AFK Seasonal XP Farm")
tab.add(name="AFK Weapon XP Farm")

tab.macro1_label = customtkinter.CTkLabel(master=tab.tab("AFK Seasonal XP Farm"), font=customtkinter.CTkFont(weight="bold"), text="Start Macro Key : " + Macro1Bind1)
tab.macro1_label.grid(row=0, column=1, padx=20, pady=20)
    
tab.macro1_button = customtkinter.CTkButton(master=tab.tab("AFK Seasonal XP Farm"), text="Bind Start Key", command=lambda: macro1_bind1(tab.macro1_label))
tab.macro1_button.grid(row=0, column=0, padx=20, pady=20)

tab.macro1_label2 = customtkinter.CTkLabel(master=tab.tab("AFK Seasonal XP Farm"), font=customtkinter.CTkFont(weight="bold"), text="End Macro Key : " + Macro1Bind2)
tab.macro1_label2.grid(row=1, column=1, padx=20, pady=20)

tab.macro1_button2 = customtkinter.CTkButton(master=tab.tab("AFK Seasonal XP Farm"), text="Bind End Key", command=lambda: macro1_bind2(tab.macro1_label2))
tab.macro1_button2.grid(row=1, column=0, padx=20, pady=20)

tab.macro2_label = customtkinter.CTkLabel(master=tab.tab("AFK Weapon XP Farm"), font=customtkinter.CTkFont(weight="bold"), text="Start Macro Key : " + Macro2Bind1)
tab.macro2_label.grid(row=0, column=1, padx=20, pady=20)

tab.macro2_button = customtkinter.CTkButton(master=tab.tab("AFK Weapon XP Farm"), text="Bind Start Key", command=lambda: macro2_bind1(tab.macro2_label))
tab.macro2_button.grid(row=0, column=0, padx=20, pady=20)

tab.macro2_label2 = customtkinter.CTkLabel(master=tab.tab("AFK Weapon XP Farm"), font=customtkinter.CTkFont(weight="bold"), text="End Macro Key : " + Macro2Bind2 )
tab.macro2_label2.grid(row=1, column=1, padx=20, pady=20)

tab.macro2_button2 = customtkinter.CTkButton(master=tab.tab("AFK Weapon XP Farm"), text="Bind End Key", command=lambda: macro2_bind2(tab.macro2_label2))
tab.macro2_button2.grid(row=1, column=0, padx=20, pady=20)

tab.home_page_label = customtkinter.CTkLabel(master=tab.tab("Home Page"), font=customtkinter.CTkFont(weight="bold"), text="Welcome to Leopold's Macro Hub\n\n Everything here is a recreation of Antra's Macros\n You can find his macros in the support server\n You can join the support server using the button in the sidebar\n If you need help or want to suggest something\n Join the support server and ping Leopold\n He will respond when he can")
tab.home_page_label.grid(row=0, column=0, padx=80, pady=20)

running_macro1 = False
running_macro2 = False

keyboard.add_hotkey(Macro1Bind1, start_macro1)
keyboard.add_hotkey(Macro1Bind2, stop_macro1)
keyboard.add_hotkey(Macro2Bind1, start_macro2)
keyboard.add_hotkey(Macro2Bind2, stop_macro2)

root.mainloop()