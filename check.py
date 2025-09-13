from  data_manager import DataManager
import os



dm=DataManager()    
data  =  dm.get_customer_emails()
print(data)