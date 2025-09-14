from  data_manager import DataManager
import os



dm=DataManager()    
data  =  dm.get_customer_emails()
print(type(data))
print(data)
# for line in data:
#     print(line["whatIsYourEmail?"])



