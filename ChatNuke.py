import pyautogui
import time
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def send_messages():
    messages = [message_entries[i].get() for i in range(5) if message_entries[i].get()]

    if not messages:
        show_error("Input Error", "Please enter at least one message.")
        return

    n = count_input.get()
    delay_value = delay_input.get()

    if not is_int(n):
        show_error("Input Error", "Please enter an integer number of times to send.")
        return

    if not is_float(delay_value):
        show_error("Input Error", "Please enter a valid delay (in seconds).")
        return

    n = int(n)
    delay_value = float(delay_value)

    countdown = tk.Toplevel(root)
    countdown.title("Countdown")
    countdown.geometry("250x100")  # Adjusted size
    countdown.resizable(False, False)  # Disabled resizing
    countdown.configure(bg="#2C2F33")

    countdown_label = tk.Label(countdown, text="", font=("Arial", 14), fg="#FFFFFF", bg="#2C2F33")
    countdown_label.pack(padx=10, pady=10)

    for i in reversed(range(1, 8)):
        countdown_label.config(text=f"Starting in {i} seconds...")
        time.sleep(1)

    for _ in range(n):
        for message in messages:
            pyautogui.write(message + '\n')
            time.sleep(delay_value)  # Introduce the delay between messages

    status_label.config(text="Messages sent successfully!")
    countdown.destroy()

def show_error(title, message):
    tk.messagebox.showerror(title, message)

def clear_all():
    for entry in message_entries:
        entry.delete(0, 'end')

    count_input.delete(0, 'end')
    delay_input.delete(0, 'end')
    status_label.config(text="")

def set_background(event=None):
    # Specify the image file name and path
    wallpaper_filename = "woodland.jpg"
    wallpaper_path = os.path.join(script_directory, "img", wallpaper_filename)

    # Load the woodland.jpg image
    image = Image.open(wallpaper_path)

    # Get the window size
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    # Resize the image to fit the window without antialiasing
    resized_image = image.resize((window_width, window_height))

    # Convert the resized image to PhotoImage
    photo = ImageTk.PhotoImage(resized_image)

    # Set the background image
    background_label.configure(image=photo)
    background_label.image = photo

root = tk.Tk()
root.title("S3THR0's ChatNuke")
root.geometry("700x500")  # Adjusted size
root.minsize(400, 350)  # Minimum size when minimized

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Specify the image file name and path
wallpaper_filename = "woodland.jpg"
wallpaper_path = os.path.join(script_directory, "img", wallpaper_filename)

# Load the initial background image
initial_background = Image.open(wallpaper_path)
initial_photo = ImageTk.PhotoImage(initial_background)

background_label = tk.Label(root, image=initial_photo)
background_label.place(relwidth=1, relheight=1)

style = ttk.Style()
style.configure("TButton", padding=5, relief="flat", foreground="#000000")  # Black text color

# Red color for "Send Messages" button
style.map("Red.TButton", background=[('active', '#AA0000'), ('!disabled', '#FF0000')])
send_button = ttk.Button(root, text="Send Messages", style="Red.TButton", command=send_messages)
send_button.pack(pady=10)

# Green color for "Clear All" button
style.map("Green.TButton", background=[('active', '#008000'), ('!disabled', '#00FF00')])
clear_button = ttk.Button(root, text="Clear All", style="Green.TButton", command=clear_all)
clear_button.pack(pady=10)

message_label = tk.Label(root, text="Enter up to 5 messages:", font=("Arial", 12), fg="#FFFFFF", bg="#394240")
message_label.pack(pady=10)

message_entries = []
for i in range(5):
    entry = tk.Entry(root, font=("Arial", 12), bg="#FFFFFF")
    entry.pack(pady=5)
    message_entries.append(entry)

count_label = tk.Label(root, text="Enter the number of times to send:", font=("Arial", 12), fg="#FFFFFF", bg="#394240")
count_label.pack(pady=10)

count_input = tk.Entry(root, font=("Arial", 12), bg="#FFFFFF")
count_input.pack()

delay_label = tk.Label(root, text="Enter the delay between messages (seconds):", font=("Arial", 12), fg="#FFFFFF", bg="#394240")
delay_label.pack(pady=10)

delay_input = tk.Entry(root, font=("Arial", 12), bg="#FFFFFF")
delay_input.pack()

send_button.pack(pady=10)

clear_button.pack(pady=10)

status_label = tk.Label(root, text="", font=("Arial", 14), fg="#FFFFFF", bg="#394240")
status_label.pack()

created_by_label = tk.Label(root, text="Created by S3THR0", font=("Arial", 10), fg="#FFFFFF", bg="#394240")
created_by_label.pack(side=tk.BOTTOM, pady=10)

set_background()  # Call this function to set the background image initially

# Bind the function to the window resize event
root.bind("<Configure>", set_background)

root.mainloop()
