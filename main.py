import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import shutil
import os

nginx_process = None

def start_nginx(show_message=True):
    global nginx_process
    try:
        nginx_process = subprocess.Popen(['nginx.exe'], shell=True)
        if show_message:
            messagebox.showinfo("Success", "NGINX started successfully!")
    except Exception as e:
        if show_message:
            messagebox.showerror("Error", f"Failed to start NGINX!\n{str(e)}")

def stop_nginx(show_message=True):
    global nginx_process
    try:
        if nginx_process:
            nginx_process.terminate()
            nginx_process = None
        subprocess.run(['TASKKILL', '/F', '/IM', 'nginx.exe'], capture_output=True, text=True, check=True)
        if show_message:
            messagebox.showinfo("Success", "NGINX stopped successfully!")
    except subprocess.CalledProcessError as e:
        if show_message:
            messagebox.showerror("Error", f"Failed to stop NGINX!\n{e.stderr}")

def reload_nginx():
    stop_nginx(show_message=False)  # Do not show message box when stopping
    start_nginx(show_message=False)  # Do not show message box when starting

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
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    frame = tk.Frame(root)
    frame.pack(pady=20, padx=20)

    tk.Button(frame, text="Start NGINX", command=lambda: start_nginx(show_message=True), width=30).grid(row=0, column=0, pady=5)
    tk.Button(frame, text="Stop NGINX", command=lambda: stop_nginx(show_message=True), width=30).grid(row=1, column=0, pady=5)
    tk.Button(frame, text="Reload Configuration", command=reload_nginx, width=30).grid(row=2, column=0, pady=5)
    tk.Button(frame, text="Reopen Log Files", command=lambda: messagebox.showinfo("Info", "Reopen Log Files command placeholder"), width=30).grid(row=3, column=0, pady=5)
    tk.Button(frame, text="Import Config File", command=import_conf_file, width=30).grid(row=4, column=0, pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_ui()
