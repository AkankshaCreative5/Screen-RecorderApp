from tkinter import *
import pyscreenrec

root = Tk()
root.geometry("600x800")
root.title("Screen Recorder")
root.config(bg="blue")
root.resizable(False, False)

def start_rec():
    file = Filename.get()
    rec.start_recording(str(file + ".mp4"), 5)
    start_frame.config(bg="red")
    start.config(bg="red")
    
def pause_rec():
    rec.pause_recording()
    
def resume_rec():
    rec.resume_recording()
    
def stop():
    rec.stop_recording()    
    start_frame.config(bg="white")
    start.config(bg="white")

rec = pyscreenrec.ScreenRecorder()

# Icon
image_logo = PhotoImage(file="logo.png")
root.iconphoto(False, image_logo)

# Background images
image1 = PhotoImage(file="bg.png")
Label(root, image=image1, bg="white").place(x=-2, y=3)

# Canvas
cv = Canvas(root)
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(0, 0, image=image1, anchor='nw')

# Heading+-
lbl = Label(root, text="Screen Recorder", bg="black", font="arial 15 bold")
lbl.pack(pady=30)

# Image
# image2 = PhotoImage(file="screen.png")
# Label(root, image=image2, bd=0).pack(pady=50) 
image2 = PhotoImage(file="screen.png")

label = Label(root, image=image2, bd=0)
label.place(x=180, y=100)

text = "Screen Recorder"
cv.create_text(320, 50, text=text, font="Arial 16", fill="black")

# Entry
Filename = StringVar()
entry = Entry(root, textvariable=Filename, width=18, font="arial 15",justify="center")
entry.place(x=180, y=400)
Filename.set("recording 1")

# Buttons
# start = Button(root, text="Start", font="arial 22", bd=0, command=start_rec)
# start.place(x=240, y=500,ipadx = 10)
start_frame = Frame(root)
start_frame.place(x=150, y=550)

start = Button(start_frame, text="Start", font="arial 22", bd=0, command=start_rec)
start.pack(padx=100)

# image3 = PhotoImage(file="Pause-Button-Png.jpg")
pause_frame = Frame(root)

pause_frame.place(x=270, y=480)
pause_frame.config(bg="#2EfBf7")
pause = Button(pause_frame,text="Pause", bd=0, bg="#2EfBf7", command=pause_rec)
pause.pack(pady=4,padx=20)
# pause.pack()

# image4 = PhotoImage(file="pausen.png")
resume_frame = Frame(root)

resume_frame.place(x=150, y=480)
resume_frame.config(bg="#2EfBf7")
resume = Button(resume_frame,text="Resume", bd=0, bg="#2EfBf7", command=resume_rec)
resume.pack(pady=4,padx=20)

# stop
stop_frame = Frame(root)

stop_frame.place(x=378, y=480)
stop_frame.config(bg="#2EfBf7")
stop = Button(stop_frame, text="Stop", bd=0, bg="#2EfBf7", command=stop)
stop.pack(pady=4,padx=20)


root.mainloop()
