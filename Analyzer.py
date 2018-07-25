import  hashlib
import tkinter as tk
from tkinter import messagebox

from tkinter import filedialog

# Loading database to a dictionary for virus checking
with open('data.txt', 'r') as known:

    virus = {}

    for line in known:
        temp = line.rstrip('\n').split(':')
        virus[temp[0]] = temp[1]

while(True):
    root = tk.Tk()
    root.withdraw()

    # Save file path from dialog box to variable
    file_path = filedialog.askopenfilename()


    # Method for md5 genarate
    def md5(fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()


    # Main code
    if file_path == '':
        break
    elif (md5(file_path) in virus):
        messagebox.showinfo("Infected", virus[md5(file_path)])
    else:
        messagebox.showinfo("Not Infected", "Not Virus\nThis is new line\nTesst")