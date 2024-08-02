import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import shutil
import os

def start_nginx():
    try:
        subprocess.Popen(['start', 'nginx.exe'], shell=True)
        messagebox.showinfo("Success", "NGINX started successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start NGINX!\n{str(e)}")

def run_nginx_command(command):
    try:
        result = subprocess.run(['nginx', '-s', command], capture_output=True, text=True, check=True)
        messagebox.showinfo("Success", f"Command '{command}' executed successfully!\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Command '{command}' failed!\n{e.stderr}")

def import_conf_file():
    conf_file_path = filedialog.askopenfilename(title="Select NGINX Config File", filetypes=[("Conf Files", "*.conf")])
    if conf_file_path:
        try:
            shutil.copy(conf_file_path, "./conf/nginx.conf")
            messagebox.showinfo("Success", "Configuration file imported successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to import configuration file!\n{e}")

def create_ui():
    root = tk.Tk()
    root.title("NGINX Controller")

    # Set the dimensions of the window
    window_width = 500
    window_height = 350
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    frame = tk.Frame(root)
    frame.pack(pady=20, padx=20)

    tk.Button(frame, text="Start NGINX", command=start_nginx, width=30).grid(row=0, column=0, pady=5)
    tk.Button(frame, text="Fast Shutdown", command=lambda: run_nginx_command("stop"), width=30).grid(row=1, column=0, pady=5)
    tk.Button(frame, text="Graceful Shutdown", command=lambda: run_nginx_command("quit"), width=30).grid(row=2, column=0, pady=5)
    tk.Button(frame, text="Reload Configuration", command=lambda: run_nginx_command("reload"), width=30).grid(row=3, column=0, pady=5)
    tk.Button(frame, text="Reopen Log Files", command=lambda: run_nginx_command("reopen"), width=30).grid(row=4, column=0, pady=5)
    tk.Button(frame, text="Import Config File", command=import_conf_file, width=30).grid(row=5, column=0, pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_ui()

