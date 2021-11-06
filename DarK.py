import os
from tkinter import *
import tkinter
from buttons import (cpuButton, powerSavingForUsb,
    Guide, disableDiagnosticServices,
    disableBluetooth, disableMaps,
    msiModeUtility, disableXbox,
    nvidiaPI, restart,
    disableWinDef, Enable
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
MC.create_window(Fh-95, 10, anchor='nw', window=cpuOptimization)
cpuButton = Button(ROOT, text="Confirm", command=cpuButton, bg="#00FFFF", width=20)
MC.create_window(Fh-20, 50, anchor='nw', window=cpuButton)

PowerSaving = Label(ROOT, text="Apply USB Optimizations", bg="#cba4ff", font=("Times", 20, "italic"))
MC.create_window(Fh-95, 120, anchor='nw', window=PowerSaving)
PowerSavingButton = Button(ROOT, text="Confirm", command=powerSavingForUsb, bg="#00FFFF", width=20)
MC.create_window(Fh-20, 160, anchor='nw', window=PowerSavingButton)

DisableDiagnosticServices = Label(ROOT, text="Disable Diagnostics and Telemetry Services", font=("Times", 20, "italic"), bg="#cba4ff")
MC.create_window(Fh-190, 230, anchor='nw', window=DisableDiagnosticServices)
DisableDiagnosticServicesButton = Button(ROOT, text="Cofirm", bg="#00FFFF", width=10, command=disableDiagnosticServices)
revertDg = Button(ROOT, text="Revert", bg="#FF0000", width=10, command=lambda: Enable("Diagnostics Telemtry Services"))
MC.create_window(Fh+50, 270, anchor='nw', window=revertDg)
MC.create_window(Fh-50, 270, anchor='nw', window=DisableDiagnosticServicesButton)

DisableBlueTooth = Label(ROOT, text="Disable BlueTooth Services", font=("Times", 20, "italic"), bg="#cba4ff")
MC.create_window(Fh-115, 340, anchor='nw', window=DisableBlueTooth)
DisableBlueToothBtn = Button(ROOT, text="Confirm", bg="#00FFFF", width=10, command=disableBluetooth)
enableBt = Button(ROOT, text="Revert", bg="#FF0000", width=10, command=lambda: Enable("Bluetooth Services"))
MC.create_window(Fh+50, 380, anchor='nw', window=enableBt)
MC.create_window(Fh-50, 380, anchor="nw", window=DisableBlueToothBtn)

DisableMaps = Label(ROOT, text="Disable MS Maps", font=("Times", 20, "italic"), bg="#cba4ff")
MC.create_window(Sh-63  ,10, anchor='nw', window=DisableMaps)
DisableMapsBtn = Button(ROOT, text="Confirm", bg="#00FFFF", width=10, command=disableMaps)
enableMaps = Button(ROOT, text="Revert", bg="#FF0000", width=10, command=lambda: Enable("Download Maps Manager"))
MC.create_window(Sh+50,50,anchor='nw', window=enableMaps)
MC.create_window(Sh-50,50, anchor='nw', window=DisableMapsBtn)

xbox = Label(ROOT, text="Disable Xbox Services", font=("Times", 20, 'italic'), bg="#cba4ff")
MC.create_window(Sh-90, 120, anchor='nw', window=xbox)
xboxBtn = Button(ROOT, text="Confirm", bg="#00FFFF", width=10, command=disableXbox)
revertXbox = Button(ROOT, text="Revert", bg="#FF0000", width=10, command=lambda: Enable("Xbox Services"))
MC.create_window(Sh+50, 160, anchor='nw', window=revertXbox)
MC.create_window(Sh-50, 160, anchor='nw', window=xboxBtn)

MsiMode = Label(ROOT, text="Open Msi Mode Utility", font=("Times", 20, 'italic'), bg="#cba4ff")
MC.create_window(Sh-80, 230, anchor='nw', window=MsiMode)
MsiModebtn = Button(ROOT, text="Confrim", bg="#00FFFF", width=20, command=msiModeUtility)
MC.create_window(Sh-20, 270, anchor='nw', window=MsiModebtn)

nvPI = Label(ROOT, text="Open Nvidia Profile Inspector", font=("Times", 20, 'italic'), bg="#cba4ff")
MC.create_window(Sh-117, 340, anchor='nw', window=nvPI)
nvPIBtn = Button(ROOT, text="Confirm", bg="#00FFFF", width=20, command=nvidiaPI)
MC.create_window(Sh-20, 380, anchor='nw', window=nvPIBtn)

DisableWinDef = Label(ROOT, text="Disable Windows Defender", font=("Times", 20, 'italic'), bg="#cba4ff")
MC.create_window(800-113, 440, anchor='nw', window=DisableWinDef)
DisableWinDefbtn = Button(ROOT, text="Confirm", bg="#00FFFF", width=10, command=disableWinDef)
enableWinDef = Button(ROOT, text="Revert", bg="#FF0000", width=10, command=lambda: Enable("Windows Defender"))
MC.create_window(800+50, 480, anchor='nw', window=enableWinDef)
MC.create_window(800-50, 480, anchor='nw', window=DisableWinDefbtn)

restart = Button(ROOT,text="Restart Computer", bg="#b187f4", command=restart, width=80, height=1,font=("Times", 20, 'italic'))
restart_canvas = MC.create_window(0+200, 765, anchor='nw', window=restart)
guideButton = Button(ROOT, text="Guide", bg="#ffa781", command=lambda: Guide(ROOT), width=80, height=1,font=("Times", 20, 'italic'))
guideButton_canvas = MC.create_window(0+200, 830, anchor='nw', window=guideButton)

ROOT.mainloop()