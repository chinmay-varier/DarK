import os
from tkinter import *
import tkinter
from buttons import (cpuButton, powerSavingForUsb,
    Guide, disableDiagnosticServices,
    disableBluetooth, disableMaps,
    msiModeUtility, disableXbox,
    nvidiaPI, restart
)

"""Code By Chinmay Varier"""

ROOT = Tk()
ROOT.geometry("1600x900")
ROOT.iconbitmap(os.path.dirname(__file__) + r"\icons\icon.ico")
ROOT.title("DarK")
ROOT.wm_title("DarK")
ROOT.resizable(width=False, height=False)

img = PhotoImage(file=os.path.dirname(__file__) + r"\icons\bg.png")
Fh = 800/2
Sh = 3*(800/2)

MC = Canvas(ROOT, width=1000, height=700)
MC.pack(fill="both", expand=True)
MC.create_image(0,0,image=img, anchor="nw")

cpuOptimization = Label(ROOT, text="Apply CPU Optimizations", bg="#cba4ff")
cpuOptimization.config(font=("Times", 20, "italic"))
cpuOptimization_canvas = MC.create_window(Fh-95, 10, anchor='nw', window=cpuOptimization)
cpuButton = Button(ROOT, text="Confirm", command=cpuButton, bg="#00FFFF", width=20)
cpuButton_canvas = MC.create_window(Fh-20, 50, anchor='nw', window=cpuButton)

PowerSaving = Label(ROOT, text="Apply USB Optimizations", bg="#cba4ff", font=("Times", 20, "italic"))
PowerSaving_canvas = MC.create_window(Fh-95, 120, anchor='nw', window=PowerSaving)
PowerSavingButton = Button(ROOT, text="Confirm", command=powerSavingForUsb, bg="#00FFFF", width=20)
PowerSavingButton_canvas = MC.create_window(Fh-20, 160, anchor='nw', window=PowerSavingButton)

DisableDiagnosticServices = Label(ROOT, text="Disable Diagnostics and Telemetry Services", font=("Times", 20, "italic"), bg="#cba4ff")
DisableDiagnosticServices_canvas = MC.create_window(Fh-190, 230, anchor='nw', window=DisableDiagnosticServices)
DisableDiagnosticServicesButton = Button(ROOT, text="Cofirm", bg="#00FFFF", width=20, command=disableDiagnosticServices)
DisableDiagnosticServicesButton_canvas = MC.create_window(Fh-20, 270, anchor='nw', window=DisableDiagnosticServicesButton)

DisableBlueTooth = Label(ROOT, text="Disable BlueTooth Services", font=("Times", 20, "italic"), bg="#cba4ff")
DisableBlueTooth_canvas = MC.create_window(Fh-105, 340, anchor='nw', window=DisableBlueTooth)
DisableBlueToothBtn = Button(ROOT, text="Confirm", bg="#00FFFF", width=20, command=disableBluetooth)
DisableBlueToothbtn_canvas = MC.create_window(Fh-20, 380, anchor="nw", window=DisableBlueToothBtn)

DisableMaps = Label(ROOT, text="Disable MS Maps", font=("Times", 20, "italic"), bg="#cba4ff")
DisableMaps_canvas = MC.create_window(Sh-50  ,10, anchor='nw', window=DisableMaps)
DisableMapsBtn = Button(ROOT, text="Confirm", bg="#00FFFF", width=20, command=disableMaps)
DisableMapsBtn_canvas = MC.create_window(Sh-20,50, anchor='nw', window=DisableMapsBtn)

xbox = Label(ROOT, text="Disable Xbox Services", font=("Times", 20, 'italic'), bg="#cba4ff")
xbox_canvas = MC.create_window(Sh-75, 120, anchor='nw', window=xbox)
xboxBtn = Button(ROOT, text="Confirm", bg="#00FFFF", width=20, command=disableXbox)
xboxbtn_canvas = MC.create_window(Sh-20, 160, anchor='nw', window=xboxBtn)

MsiMode = Label(ROOT, text="Open Msi Mode Utility", font=("Times", 20, 'italic'), bg="#cba4ff")
MsiMode_canvas = MC.create_window(Sh-80, 230, anchor='nw', window=MsiMode)
MsiModebtn = Button(ROOT, text="Confrim", bg="#00FFFF", width=20, command=msiModeUtility)
MsiModebtn_canvas = MC.create_window(Sh-20, 270, anchor='nw', window=MsiModebtn)

nvPI = Label(ROOT, text="Open Nvidia Profile Inspector", font=("Times", 20, 'italic'), bg="#cba4ff")
nvPI_canvas = MC.create_window(Sh-117, 340, anchor='nw', window=nvPI)
nvPIBtn = Button(ROOT, text="Confirm", bg="#00FFFF", width=20, command=nvidiaPI)
nvPIBtn_canvas = MC.create_window(Sh-20, 380, anchor='nw', window=nvPIBtn)

restart = Button(ROOT,text="Restart Computer", bg="#b187f4", command=restart, width=80, height=1,font=("Times", 20, 'italic'))
restart_canvas = MC.create_window(0+200, 765, anchor='nw', window=restart)
guideButton = Button(ROOT, text="Guide", bg="#ffa781", command=lambda: Guide(ROOT), width=80, height=1, font=("Times", 20, "italic"))
guideButton_canvas = MC.create_window(0+200, 830, anchor='nw', window=guideButton)


ROOT.mainloop()