from kivy.app import App
from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
from kivymd.uix.button import MDTextButton
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
import firebase_connect as fcnnct

class LoginScreen(MDScreen):
	def login(self):
		return 'mainn'
	def check(self):
		username=self.username.text
		password = self.password.text
		cnfrm_pass=self.cnfrm_pass.text
		email=self.email.text
		name=self.accnt_name.text
		if len(username)<5:
			self.username.helper_text='username at least length of 5'
			return 'login'
			
		elif len(password) <6:
			self.password.helper_text="password length at least 6"
			return 'login'
			
		elif password!=cnfrm_pass:
			self.cnfrm_pass.helper_text="password does not matched"
			return 'login'
			
		elif self.validate(email) and len(password)>6:
			fcnnct.create_user(email,password)
			print('user connected')
			return 'mainn'
			
	def validate(self,email):
		if '@' and '.' in email:
			return True
		else:
			return False
class MainScreen(MDScreen):
	list_of_screen=['mainn']
	
	def nsdc(self):
		self.list_of_screen.append('nsdc')
		return 'nsdc'
		
	
class Nsdc(MDScreen):
	def go(self):
		return 'nsdctrain'
		
class NsdcTrain(MDScreen):
	lenth=.1
	def searche(self) :
		search=self.ids.searchfield.text
		center={'cor':[str(i) for i in range(0,50)]}
		if search in center:
			disp_center=center[search]
			
		
		for i in range(len(disp_center)):
			button=[i for i in disp_center]
			
			self.ids.mm.add_widget(OneLineListItem(id=button[i],text=button[i],size_hint=(.8,.1)))	

class ScrManager(ScreenManager):
	pass
	
class SkillIndia(MDApp):
	def build(self):
		return ScrManager()

SkillIndia().run()