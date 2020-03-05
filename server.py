import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import messaging

cred = credentials.Certificate("serviceAccountKey.json")
default_app = firebase_admin.initialize_app(cred)

from pyfcm import FCMNotification
 

def send(st):
	push_service = FCMNotification(api_key="AAAAn80dI2s:APA91bE6thcPcV-8SkaN1uuWTfVGt4pc2emAQC0SWebOi5yzYalLTXQFxTEryzr9R71JK5V_hBSwRDZIbeM7Mi7SId5ts7H6NSKE11Y47lGc05fwkzCHjO4VJ2OTe1Q0UTINiH0NFG3R")
	 
	proxy_dict = {
	          "http"  : "http://127.0.0.1",
	          "https" : "http://127.0.0.1",
	        }
	push_service = FCMNotification(api_key="AAAAn80dI2s:APA91bE6thcPcV-8SkaN1uuWTfVGt4pc2emAQC0SWebOi5yzYalLTXQFxTEryzr9R71JK5V_hBSwRDZIbeM7Mi7SId5ts7H6NSKE11Y47lGc05fwkzCHjO4VJ2OTe1Q0UTINiH0NFG3R")
	 
	registration_id = "dhPRzoPG9YE:APA91bF_N3pMPYwAcY-W4geyO-3RyPAsHed9swEkiR1WZ6UCTYh4vs7vzVAk_vjy6fS32fNZ8THkPJF5VVopOD_Ot-CcxNRbyLCrK83Klq3iCWH1rGt-7iF_1Y47e5oZtzgbP53FnqJk"
	message_title = "Sample Alert"
	message_body = "You recevied a complaint about " + st + " at Bowenpally Main Road"
	result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
	print(result)
	return True