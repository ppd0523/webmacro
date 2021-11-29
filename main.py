import tkinter as tk
import threading
from functools import partial
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchWindowException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


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

        driver = webdriver.Chrome(service=service)
        init_url = 'https://www.google.co.kr'
        driver.get(url=init_url)

    threading.Thread(target=task).start()


def on_destroy(_root):
    global driver
    if driver:
        try:
            driver.close()
        except NoSuchWindowException:
            pass
    _root.destroy()


root = tk.Tk()
root.title("Web Controller")
root.geometry("480x320+100+100")
root.resizable(True, True)

frame = tk.Frame(root, relief="solid", bd=1)
frame.pack(side="left", fill="both", expand=False)

button1 = tk.Button(frame, text='Open\nChrome', width=5, height=5, command=open_browser)
button1.pack()

on_destroy = partial(on_destroy, root)
root.protocol("WM_DELETE_WINDOW", on_destroy)
root.mainloop()

# try:
#     element = WebDriverWait(driver, timeout=5, poll_frequency=1).until(
#         ec.presence_of_element_located((By.XPATH, 'hello')),
#         'try...'
#     )
# except Exception as e:
#     print('Error: ', e, file=sys.stderr)
