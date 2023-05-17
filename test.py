import os

 # displaying the oparating system
#os.system("winver")




# displaying message
"""from plyer import notification

notification_title = 'GREETINGS FROM JAVATPOINT!'
notification_message = 'Thank you for reading. Have a Good Day.'

notification.notify(
    title=notification_title,
    message=notification_message,
    app_icon=None,
    timeout=10,
    toast=False
)"""



filename = 'C:\Desktop\test.txt'
#os.startfile(filename)


import subprocess

#p = subprocess.Popen(["notepad.exe", 'C:\Desktop\test.txt'])



 # opening notepad with message
"""import os

file = 'test.txt'

def openFile():
    os.system("notepad.exe " + file)
openFile()"""



# getting the username
user = os.getlogin()
user_1 = os.path.expanduser('~')
print(user)


# getting current time
from datetime import datetime
time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(time)