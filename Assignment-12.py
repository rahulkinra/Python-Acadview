#Q.1- Print the current day using Datetime module.
import datetime as dt
x = dt.date.today()
print(x.strftime("%A"))

#Q.2- Open your browser and play a video using webbrowser module in python.
import webbrowser
search = "Eminem – Kamikaze"
webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % search)

#Q.3- Write a program to rename all the files in a directory and convert them into .jpg file format.
import os
path = r'''C:/Users/hp/Desktop/Python-Acadview/Acadview-Python/NewDir'''
files = os.listdir(path)
i = 1
for f in files:
    os.rename(os.path.join(path, f), os.path.join(path, str(i)+'.jpg'))
    i += 1
