import tkinter as tk
from tkinter import messagebox
from io import StringIO
import sys

# Sample log analysis code and visualizations
# ... (paste the log analysis code snippets here) ...

def top_hits_per_hour():
    # Sample: Display a message box with top 10 hits per hour
    messagebox.showinfo("Top Hits Per Hour", "This is a sample message box for top hits per hour.")

def http_codes_count():
    # Sample: Display a message box with HTTP codes count
    messagebox.showinfo("HTTP Codes Count", "This is a sample message box for HTTP codes count.")

# Function to redirect sys.stdout to a variable
def redirect_stdout():
    sys.stdout = StringIO()

# Function to restore sys.stdout
def restore_stdout():
    sys.stdout = sys.__stdout__

# Create the tkinter window
root = tk.Tk()
root.title("Log Analysis GUI")
root.configure(bg='blue')  # Set the window background color to blue

# Create buttons to trigger log analysis tasks with custom styling
btn_top_hits = tk.Button(root, text="Top Hits Per Hour", command=top_hits_per_hour, bg='green', fg='white', padx=20, pady=10, font=('Arial', 14))
btn_top_hits.pack(pady=10)

btn_http_codes = tk.Button(root, text="HTTP Codes Count", command=http_codes_count, bg='orange', fg='white', padx=20, pady=10, font=('Arial', 14))
btn_http_codes.pack(pady=10)

# Button to redirect sys.stdout
btn_redirect_stdout = tk.Button(root, text="Redirect stdout", command=redirect_stdout, bg='purple', fg='white', padx=20, pady=10, font=('Arial', 14))
btn_redirect_stdout.pack(pady=10)

# Button to restore sys.stdout
btn_restore_stdout = tk.Button(root, text="Restore stdout", command=restore_stdout, bg='red', fg='white', padx=20, pady=10, font=('Arial', 14))
btn_restore_stdout.pack(pady=10)

# Run the tkinter main loop
root.mainloop()
