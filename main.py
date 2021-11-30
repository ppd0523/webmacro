# -*- coding: utf-8 -*-

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
is_running = False


def open_browser(_btn):
    def task():
        global driver
        try:
            windows = driver.window_handles
            if windows:
                return
        except AttributeError as e:
            if driver:
                return
        except WebDriverException as e:
            pass

        opt = webdriver.ChromeOptions()
        files = glob.glob('./extensions/*')
        [opt.add_extension(file) for file in files if file.endswith('.crx')]

        driver = webdriver.Chrome(service=service, options=opt)
        driver.get(url=init_url)

    threading.Thread(target=task).start()


def on_start():
    global driver
    log.info('click start')


def on_stop():
    global driver
    log.info('click stop')


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


def ctrl_event(event):
    if not (12 == event.state and event.keysym == 'c'):
        return "break"


if __name__ == "__main__":
    # General Color
    BEIGE_COLOR = '#FEF8E7'
    BOLD_BEIGE_COLOR = '#ECE6CC'

    # Root
    root = tk.Tk()
    root.configure(bg='#fef8e7')
    root.title("Web Controller")
    root.geometry("320x240+100+100")
    root.resizable(True, True)

    # Top panel
    panel_top = tk.PanedWindow(root, bg=BEIGE_COLOR)
    panel_top.place(relx=0.5, y=30, anchor=tk.N)

    # Button
    btn_opt = {
        'relief': 'groove',
        'width': 8,
        'height': 3,
        'bg': BEIGE_COLOR,
        'activebackground': BOLD_BEIGE_COLOR,
        'font': 25,
    }

    open_btn = tk.Button(panel_top, text='OPEN', **btn_opt)
    open_btn.config(command=partial(open_browser, open_btn))
    start_btn = tk.Button(panel_top, text='START', command=on_start, **btn_opt)
    stop_btn = tk.Button(panel_top, text='STOP', command=on_stop, **btn_opt)

    panel_top.add(open_btn, padx=5)
    panel_top.add(start_btn, padx=5)
    panel_top.add(stop_btn, padx=5)
    # open_btn.pack(side=tk.LEFT, padx=(5, 20))
    # start_btn.pack(side=tk.LEFT, padx=5)
    # stop_btn.pack(side=tk.LEFT, padx=5)

    # panel_bottom = tk.PanedWindow(root, bg=BEIGE_COLOR)
    # panel_bottom.pack(side='top', pady=20, fill='both', padx=20, expand=True)
    #
    # text_area = tk.Text(panel_bottom)
    #
    # text_area.insert(tk.END, 'hello world')
    # text_area.bind("<Key>", lambda e: ctrl_event(e))
    # panel_bottom.add(text_area)

    root.protocol("WM_DELETE_WINDOW", partial(on_destroy, root))
    root.mainloop()