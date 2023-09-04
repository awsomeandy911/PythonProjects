import tkinter as ui
import time
# Window variable to call tkinter module
window = ui.Tk()

# Updates clock to current time
def updateClock():
    weekDay = time.strftime("%A")
    month = time.strftime("%B")
    day = time.strftime("%d")
    year = time.strftime("%Y")
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    AM_PM = time.strftime("%p")
    clockText = weekDay + ", " + month + " " + day + ", " + year + " " + hour + ":" + minute + ":" + second + " " + AM_PM
    digitalclockLabel.config(text = clockText)
    # after label allows to keep updating clock by the second (1000 milisecond)
    digitalclockLabel.after(1000, updateClock)

# Label to hold the current time for clock
digitalclockLabel = ui.Label(window, text = "00:00:00", font = "Helvetica 60 bold")
digitalclockLabel.pack()

# use updateClock function
updateClock()

# Use main loop function on window for module to show
window.mainloop()



