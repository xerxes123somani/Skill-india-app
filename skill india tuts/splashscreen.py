from kivy.app import App
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.clock import Clock

class SplashScreen(App):
    def on_start(self):
        wing=Image(source="/home/xerxes/Pictures/Skill_India.png",pos=(800,800))
        animation = Animation(x=0, y=0, d=2, t='out_bounce')
        animation.start(wing)
        return wing
    
SplashScreen().run()