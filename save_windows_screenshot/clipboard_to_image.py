#!/usr/bin/env python3
from PIL import ImageGrab
from PIL import Image
import os
from win32com.shell import shell # pywin32
import sys
import traceback
from pyautogui import hotkey # pyautogui
import time
import win32gui # pywin32
from win32com.client import Dispatch # pywin32

startingPath = r"D:\Images"

def launch_file_explorer(path, files):
    '''Given an absolute base path and names of its children (no path), open
up one File Explorer window with all the child files selected'''
    folder_pidl = shell.SHILCreateFromPath(path,0)[0]
    desktop = shell.SHGetDesktopFolder()
    shell_folder = desktop.BindToObject(folder_pidl, None, shell.IID_IShellFolder)
    name_to_item_mapping = dict([(desktop.GetDisplayNameOf(item, 0), item) for item in shell_folder])
    to_show = []
    for file in files:
        if not file in name_to_item_mapping:
            raise Exception('File: "%s" not found in "%s"' % (file, path))
        to_show.append(name_to_item_mapping[file])
    shell.SHOpenFolderAndSelectItems(folder_pidl, to_show, 1)

im = ImageGrab.grabclipboard()

def main():
    if Image.isImageType(im):
        filename = 'tempfile.jpg'
        try:
            fullPath = os.path.join(startingPath,filename)
            im.save(fullPath,'JPEG', subsampling=0, quality=95)
            launch_file_explorer(os.path.dirname(fullPath),[os.path.basename(fullPath)])
        except Exception as ex:
            ex_type, ex_value, ex_traceback = sys.exc_info() # get current system exception
            trace_back = traceback.extract_tb(ex_traceback) # extract unformatter stack traces as tuples
            stack_trace = list() # format stacktrace

            for trace in trace_back:
                stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))

            print("Exception type : %s " % ex_type.__name__)
            print("Exception message : %s" %ex_value)
            print("Stack trace : %s" %stack_trace)
            input("Press enter to exit...")

def get_we(shell,handle):
    for win in shell.Windows():
        if win.hwnd == handle: return win
    return None
            
if __name__ == "__main__":
    hotkey('alt','tab')
    time.sleep(0.05)
    w = win32gui
    
    SHELL = Dispatch("Shell.Application")
    we = get_we(SHELL,w.GetForegroundWindow())
    if we:
        startingPath = we.LocationURL.replace("file:///","").replace("/","\").replace("%20"," ")
    main()
