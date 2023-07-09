import pyautogui
import time
import tkinter as tk
import tkinter.messagebox as tkMessageBox

def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def send_messages():
    msg = message_input.get()
    n = count_input.get()
    
    if not is_int(n):
        tkMessageBox.showerror("Input Error", "Please enter an integer number of times to send.")
        return
    
    n = int(n)

    countdown = tk.Toplevel(root)
    countdown_label = tk.Label(countdown, text="", font=("Arial", 14))
    countdown_label.pack(padx=10, pady=10)

    for i in reversed(range(1, 8)):
        countdown_label.config(text=f"Starting in {i} seconds...")
        time.sleep(1)

    for i in range(n):
        pyautogui.write(msg + '\n')

    status_label.config(text=f"{n} messages sent successfully!")
    countdown.destroy()

def clear_all():
    message_input.delete(0, 'end')
    count_input.delete(0, 'end')
    status_label.config(text="")

root = tk.Tk()
root.title("S3THR0's ChatNuke")
root.geometry("400x300")
root.configure(bg="#2C2F33")

message_label = tk.Label(root, text="Enter the message:", font=("Arial", 12), fg="#FFFFFF", bg="#2C2F33")
message_label.pack(pady=10)

message_input = tk.Entry(root, font=("Arial", 12), bg="#FFFFFF")
message_input.pack()

count_label = tk.Label(root, text="Enter the number of times to send:", font=("Arial", 12), fg="#FFFFFF", bg="#2C2F33")
count_label.pack(pady=10)

count_input = tk.Entry(root, font=("Arial", 12), bg="#FFFFFF")
count_input.pack()

send_button = tk.Button(root, text="Send Messages", font=("Arial", 12), bg="#7289DA", fg="#FFFFFF", command=send_messages)
send_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear All", font=("Arial", 12), bg="#7289DA", fg="#FFFFFF", command=clear_all)
clear_button.pack(pady=10)

status_label = tk.Label(root, text="", font=("Arial", 14), fg="#FFFFFF", bg="#2C2F33")
status_label.pack()

created_by_label = tk.Label(root, text="Created by S3THR0", font=("Arial", 10), fg="#FFFFFF", bg="#2C2F33")
created_by_label.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
