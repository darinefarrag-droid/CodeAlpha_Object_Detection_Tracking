import tkinter as tk
from tkinter import filedialog
from tracking import run_tracking


def open_video():

    file_path = filedialog.askopenfilename(
        title="Select Video",
        filetypes=[("Video Files", "*.mp4 *.avi *.mov")]
    )

    if file_path:
        run_tracking(file_path)


def open_camera():

    run_tracking(0)


root = tk.Tk()

root.title("Object Detection & Tracking System")
root.geometry("500x250")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="Object Detection & Tracking System",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=20)

video_button = tk.Button(
    root,
    text="Open Video",
    font=("Arial", 12),
    width=20,
    command=open_video
)
video_button.pack(pady=10)

camera_button = tk.Button(
    root,
    text="Open Camera",
    font=("Arial", 12),
    width=20,
    command=open_camera
)
camera_button.pack(pady=10)

exit_button = tk.Button(
    root,
    text="Exit",
    font=("Arial", 12),
    width=20,
    command=root.destroy
)
exit_button.pack(pady=10)

root.mainloop()