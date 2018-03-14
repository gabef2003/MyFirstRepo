import webbrowser
import pyautogui as pg

videos = ["https://www.youtube.com/watch?v=c3WtpRyQE8E","https://www.youtube.com/watch?v=-RYkapHBVs8"]
music = ["https://www.youtube.com/watch?v=XUqRem0W8L8&list=PLFgquLnL59amBBTCULGWSotJu2CkioYkj"]

answer = pg.prompt (
"""
What would you like to do?
a) Watch Videos
b) listen to music 
"""
) 

    
if answer == "a":
    for i in videos:
        webbrowser.open(i)

elif answer == "b":
    for i in music:
         webbrowser.open(i)
