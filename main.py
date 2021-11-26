import tkinter as tk, sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


URL = 'https://www.google.co.kr'

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
# driver.get(url=URL)

import functools
def print_func(text):
    f = functools.partial(print, text)
    return f

root = tk.Tk()
root.title("Web Macro")
root.geometry("480x320+100+100")
root.resizable(True, True)

button1 = tk.Button(root, text='sample', width=15, height=15, command=print_func('hello'))
button2 = tk.Button(root, text='sample', width=15, height=15, command=print_func('world'))
button1.pack()
button2.pack()

root.mainloop()

# try:
#     element = WebDriverWait(driver, timeout=5, poll_frequency=1).until(
#         ec.presence_of_element_located((By.XPATH, 'hello')),
#         'try...'
#     )
# except Exception as e:
#     print('Error: ', e, file=sys.stderr)
