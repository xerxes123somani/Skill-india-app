from kivymd.uix.screen import MDScreen
from kivymd.uix.list import TwoLineListItem
import firebase_connect
class Jobpost(MDScreen):
    def onstart(self):
        
        job_list=firebase_connect.get_job_post_list()
        for job in job_list.each():
            print("key:",job.key())
            print("val:",job.val())
        for job in job_list.each():
            self.ids.Job_post_list.add_widget(TwoLineListItem(text=job.key(),secondary_text=job.val()))

