import os
import tkinter as tk
from tkinter import *
import ctypes, sys

drc = os.getcwd() + "\Reg"

def cpuButton():
    directory = drc + "\CPU Optimizations.reg"
    os.system('"' + directory + '"')

def powerSavingForUsb():
    directory = drc + "\Disable Power Saving Features For USB and System.reg"
    print('"' + directory + '"')
    os.system('"' + directory + '"')

def disableDiagnosticServices():
    dirc = drc + "\Disable Diagnostics and Telemetry Services.reg"
    os.system('"' + dirc+ '"')

def disableBluetooth():
    dirc = drc + "\OPTIONAL Disable Bluetooth Services.reg"
    os.system('"' + dirc + '"')

def disableMaps():
    dirc = drc + "\OPTIONAL Disable Download Maps Manager.reg"
    os.system('"' + dirc + '"')

def disableXbox():
    dirc = drc + "\OPTIONAL Disable Xbox Services.reg"
    os.system('"' + dirc + '"')

def msiModeUtility():
    dirc = drc + "\MSI Mode Utility V2.exe"
    os.system('"' + dirc + '"')

def nvidiaPI():
    dirc = drc + r"\nvidiaProfileInspector.exe"
    os.system('"' + dirc + '"')

def restart():
    os.system("shutdown /r")

def Guide(master):
    guideWin = Toplevel(master)
    guideWin.geometry("1300x600")

    heading1 = Label(guideWin, text="For Optimizations 1-6: ")
    heading1.pack()

