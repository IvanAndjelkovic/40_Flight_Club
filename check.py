from  data_manager import DataManager
from notification_manager import NotificationManager
import os



# dm=DataManager()    
# data  =  dm.get_customer_emails()
# print(type(data))
# print(data)
# for line in data:
#     print(line["whatIsYourEmail?"])

nm = NotificationManager()
nm.send_email("ivan.andelkovic707@gmail.com","mile voli disko")

