from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import json
from datetime import datetime
import glob
from pathlib import Path
import random

Builder.load_file('design.kv')


class ImageButton(ButtonBehavior, Image, HoverBehavior):
    pass


class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def login(self, uname, pword):
        with open("users.json") as file:
            users1 = json.load(file)
        if uname in users1 and users1[uname]['password'] == pword:
            self.manager.current = "login_screen_success"
        else:
            self.ids.loginwrong.text = "Wrong Username or Password"


class RootWidget(ScreenManager):
    pass


users = {}


class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        users[uname] = {'username': uname, 'password': pword, 'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        with open("users.json", 'w') as file:
             json.dump(users, file)
        self.manager.current = "sign_up_screen_success"


class SignUpScreenSuccess(Screen):
    def gotologin(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"


class LoginScreenSuccess(Screen):
    def logout(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

    def getquote(self, feel):
        feel = feel.lower()
        available_feeling = glob.glob("quotes/*txt")
        available_feelings = [Path(filename).stem for filename in available_feeling]
        if feel in available_feelings:
            with open(f"quotes/{feel}.txt", encoding="utf-8") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling"


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
