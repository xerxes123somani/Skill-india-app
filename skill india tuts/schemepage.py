from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
class SchemePage(MDApp):
    def build(self):
        icon_list=["/home/xerxes/Pictures/Skill_India.png","language-python"]
        for image in icon_list:
            pos=.5
            self.root.ids.SchemeList.add_widget(MDIconButton(icon=image,pos_hint={'x':pos,'y':pos}))
            pos+=.2
    
SchemePage().run()