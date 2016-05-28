import time
import webbrowser

""" my version
count = 0
while(count < 3):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=ylXKpn9cgsM")
    count = count + 1"""

#Udacity version

print ("This program started on "+time.ctime())
total_breaks = 3
break_count = 0
while(break_count < total_breaks):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=ylXKpn9cgsM")
    break_count = break_count + 1

#can add a time statement with time.ctime() = current time
#can use CTRL+C in shell window to stop execution of module during (or close IDLE)
#time.sleep takes seconds so to make two hours could just work it out in the function
#e.g. time.sleep(2*60*60)
