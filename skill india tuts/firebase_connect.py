import pyrebase
config = {
  "apiKey": "AIzaSyB40vHxHZKgDUYvMN7dw7zlrYrTtKIuGKU",
  "authDomain": "skill-india-5d549.firebaseapp.com",
  "databaseURL": "https://skill-india-5d549.firebaseio.com",
  "storageBucket": "gs://skill-india-5d549.appspot.com",
  #"serviceAccount": "/storage/emulated/0/Download/skill-india-5d549-2222225dd2b7.json"
}
firebase = pyrebase.initialize_app(config)
auth=firebase.auth()
db=firebase.database()
def create_user(email,password):
	signup=auth.create_user_with_email_and_password(email,password)
	return signup
	
def signin_user(email,password):
	login=auth.sign_in_with_email_and_password(email,password)
	return login
def reset_password(email):
	auth.send_password_reset_email(email)
	
def get_job_post_list():
    all_jobs_list=db.child("job post").get()
    return all_jobs_list
    
