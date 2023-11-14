import os
from tkinter import *

search_history = []
window = Tk()

user_search = Entry(window)
user_search.place(x=80, y=20)
v0 = IntVar()
v0.set(1)
r1 = Radiobutton(window, text="Chrome", variable=v0, value=1)
r2 = Radiobutton(window, text="Edge", variable=v0, value=2)
r1.place(x=0, y=50)
r2.place(x=200, y=50)


def initalize():
    read_history()
    print('Welcome back your history is currently: ')
    print(search_history)


def get_wiki_search():
    url_lookup = user_search.get()
    clean_url = '_'.join(url_lookup.split())
    user_search.delete(0, END)

    return clean_url


def read_history():
    try:
        with open('history.text') as read_output:
            search_history = read_output.readlines()
    except FileNotFoundError:
        print('No "history.text" exist in directory: Creating new File...')


def save_history(search_item):
    search_history.append(search_item)
    try:
        with open('history.text', 'w') as saved_output:
            saved_output.writelines(search_history)
    except FileNotFoundError:
        print('No "history.text" exist in directory: Creating new File...')


def search_function(event):
    url = get_wiki_search()
    browser = v0.get()
    save_history(url)
    chrome_url = "start chrome https://en.wikipedia.org/wiki/" + url
    edge_url = "start msedge https://en.wikipedia.org/wiki/" + url

    if browser == 1:
        os.system('cmd /c ' + chrome_url)

    elif browser == 2:
        os.system('cmd /c' + edge_url)

    read_history()


initalize()

window.geometry("300x200+10+10")
window.title('Wiki Quick Search')
window.bind('<Return>', search_function)
window.mainloop()
