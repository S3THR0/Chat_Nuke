import pyautogui
import time
import tkinter as tk

def send_messages():
    # Get the message and number of times to send from the GUI inputs
    msg = message_input.get()
    n = int(count_input.get())

    # Hide the GUI window to begin the countdown
    root.withdraw()

    # Countdown before sending messages
    for i in reversed(range(1, 8)):
        status_label.config(text=f"Starting in {i} seconds...")
        time.sleep(1)

    # Send the messages
    for i in range(n):
        pyautogui.write(msg + '\n')
    
    # Display message sent status
    status_label.config(text=f"{n} messages sent successfully!")

# Create the GUI window
root = tk.Tk()
root.title("S3THR0's ChatNuke")
root.geometry("400x300")
root.configure(bg="#2C2F33")

# Create the message input widget
message_input = tk.Entry(root, font=("Arial", 12), bg="#FFFFFF")
message_input.pack(pady=10)
message_label = tk.Label(root, text="Enter the message:", font=("Arial", 12), fg="#FFFFFF", bg="#2C2F33")
message_label.pack()

# Create the message count input widget
count_input = tk.Entry(root, font=("Arial", 12), bg="#FFFFFF")
count_input.pack(pady=10)
count_label = tk.Label(root, text="Enter the number of times to send:", font=("Arial", 12), fg="#FFFFFF", bg="#2C2F33")
count_label.pack()

# Create the send button
send_button = tk.Button(root, text="Send Messages", font=("Arial", 12), bg="#7289DA", fg="#FFFFFF", command=send_messages)
send_button.pack(pady=10)

# Create the status label
status_label = tk.Label(root, text="", font=("Arial", 14), fg="#FFFFFF", bg="#2C2F33")
status_label.pack()

# Create the created by label
created_by_label = tk.Label(root, text="Created by S3THR0", font=("Arial", 10), fg="#FFFFFF", bg="#2C2F33")
created_by_label.pack(side=tk.BOTTOM, pady=10)

# Start the GUI event loop
root.mainloop()
