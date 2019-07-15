import tkinter as tk
 
def showxy(event):
    xm, ym = event.x, event.y
    str1 = "mouse at x=%d  y=%d" % (xm, ym + 30)
    # show cordinates in title
    root.title(str1)
 
root = tk.Tk()
frame = tk.Frame(root, bg= 'yellow', width=1366, height=768)
frame.bind("<Motion>", showxy)
frame.pack()
root.attributes('-alpha', 0.7)
root.mainloop()
