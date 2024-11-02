import time
from plyer import notification

if __name__=="__main__":
        while True:  
            notification.notify(
                  
            title="**Please Drink Water!! ", # notification title
            message="The U.S. National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women.", # write whatever message u want to display in notification
            app_icon=r"C:\Users\MAYANK\Desktop\coding\python projects\drink water\drink.ico", # add the path of ur icon(.ico) file here 
            timeout=10 # set this in seconds of how long u want ur notification to display
            )
            time.sleep(60*60) # set timer in seconds . it will run the program after the seconds u hv given in input in brackets.