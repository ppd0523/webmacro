import os, sys
if getattr(sys, 'frozen', False):
    _path = sys.executable
else:
    _path = __file__

os.chdir(os.path.dirname(os.path.abspath(_path)))

import tkinter as tk
import threading
import glob
from sslog.logger import SimpleLogger
from functools import partial
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchWindowException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

log = SimpleLogger()
service = Service(ChromeDriverManager().install())
driver = None
init_url = 'https://www.google.co.kr'

def open_browser():
    def task():
        global driver
        try:
            windows = driver.window_handles
            if windows:
                return
        except AttributeError as e:
            if driver:
                return

        opt = webdriver.ChromeOptions()
        files = glob.glob('./extensions/*')
        [opt.add_extension(file) for file in files if file.endswith('.crx')]

        driver = webdriver.Chrome(service=service, options=opt)
        driver.get(url=init_url)

    threading.Thread(target=task).start()


def on_text():
    global driver
    log.info(driver.title)


def on_destroy(_root):
    global driver
    if driver:
        try:
            driver.quit()
        except NoSuchWindowException:
            pass
        except WebDriverException:
            pass
    _root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Web Controller")
    root.geometry("480x320+100+100")
    root.resizable(True, True)

    frame = tk.Frame(root, relief="solid")
    frame.pack(side="left", fill="both", expand=True)

    button1 = tk.Button(frame, text='Open\nChrome', width=5, height=5, command=open_browser)
    button1.pack(side='left')

    button2 = tk.Button(frame, text='btn', width=5, height=5, command=on_text)
    button2.pack(side='left')

    root.protocol("WM_DELETE_WINDOW", partial(on_destroy, root))
    root.mainloop()