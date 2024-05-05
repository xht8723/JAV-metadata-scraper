from tkinter import *
from ttkbootstrap.constants import *
from tkinter import filedialog
import ttkbootstrap as tb
import json

def updateGauge(meter, step):
    now = int(-(-(meter.amountusedvar.get() + step)//1))
    meter.configure(amountused = now)
    return

def setGauge(meter, value):
    meter.configure(amountused = value)
    return

def display(widget, text):
    widget.configure(state='normal')
    widget.insert(tb.INSERT, text+'\n')
    widget.configure(state='disabled')
    return

def dirDialog(dir = '', widget = ''):
    dir = filedialog.askdirectory(mustexist=True)
    if widget != '':
        widget.config(text=dir)
    return dir

def updateDone(widget):
    widget.pack(pady=10)
    return

def readJson(key):
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        return data[key], data
    except FileNotFoundError:
        return '', None
    except KeyError:
        return '', data

def saveJson(key, toSave):
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        newData = {
            key:toSave
        }
        with open("data.json", "w") as file:
            json.dump(newData, file, indent=4)
        return
    
    data[key] = toSave
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
    return