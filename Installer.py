# Peeper Installer


import PySimpleGUI as sg
import os
import sys
from distutils.dir_util import copy_tree

def work_site():                #cause script to execute in directory containing script
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))  #move to dir that holds this script and ADB (need to change for exe)
    global working_dir
    working_dir = os.path.dirname(os.path.abspath(__file__))
work_site()

folder_of_stuff = os.path.join(working_dir + "/Installation_Files/")

user_path = os.path.expanduser("~")

open = sg.PopupOKCancel("Peeper Installation - An image processing and review tool. \n\nThis will install Peeper and associated files and programs.\nInstallation includes:\n\n\t-Tesseract (OCR Engine)\n\n\t-Nudenet (Nudity Detection Engine)\n\nTo proceed press 'OK'. To exit hit 'Cancel'\n\n")
if open == 'Cancel':
    sys.exit()
if open == 'OK':
    pass
# os.startfile(os.path.join(folder_of_stuff + "tesseract-ocr-w64-setup-v4.1.0.20190314.exe"))

tes_to_path = sg.PopupOK("REQUIRED - Add Tesseract to Path\n\n1. Click on the Windows Start Button and search for 'Environment Variables'.\n\n2. Select 'Edit the system environment variables'.\n\n3. In the new 'System Properties' window, select 'Environment Variables'.\n\n4. In the new window edit the user or system variable to add Tesseract to Path by double clicking 'Path'.\n\n5.Browse to the Tesseract installation directory (the path is likely C:\\Program Files\\Tesseract-OCR if you used default installation settings) and select the directory to be added to Path.")



# copy subdirectory example
nudenet_dir = folder_of_stuff + '.Nudenet/'
peepr_dir = folder_of_stuff + "Peeper/"
usr_dir = user_path
program_dir = usr_dir + "/Program Files/"


copy_tree(peepr_dir, program_dir)
copy_tree(nudenet_dir, usr_dir)
