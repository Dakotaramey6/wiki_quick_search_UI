import os
from tkinter import *
from turtle import title

window = Tk()

user_search = Entry(window)
user_search.place(x=80, y=20)
v0 = IntVar()
v0.set(1)
r1 = Radiobutton(window, text="Chrome", variable=v0, value=1)
r2 = Radiobutton(window, text="Edge", variable=v0, value=2)
r1.place(x=0, y=50)
r2.place(x=200, y=50)
show_history_btn = Button(text='Show History', background='LightBlue')
show_history_btn.place(x=80, y=140, width=120)
clear_history_btn = Button(text='Clear History', background='Red')
clear_history_btn.place(x=80, y=170, width=120)


def check_history(event):
    history_window = Tk()
    history_window.title('Search History')
    history = Label(history_window, text=read_history())
    history.pack()
    history.bind('<button-1>', get_wiki_search())
    history_window.mainloop()


def get_wiki_search():
    url_lookup = user_search.get()
    clean_url = '_'.join(url_lookup.split())
    user_search.delete(0, END)

    return clean_url


def read_history():
    try:
        with open('history.text') as read_output:
            file_read_res = read_output.read()
    except FileNotFoundError:
        print('No "history.text" exist in directory: Creating new File...')
    return file_read_res


def save_history(search_item):
    search_item += ' \n'
    try:
        with open('history.text', 'a') as saved_output:
            saved_output.writelines(search_item)

    except FileNotFoundError:
        print('No "history.text" exist in directory: Creating new File...')


def clear_history(event):
    try:
        with open('history.text', 'w') as saved_output:
            saved_output.writelines('')

    except FileNotFoundError:
        print('No "history.text" exist in directory: Creating new File...')
    clear_history_window = Tk()
    clear_history_window.title('History Deleted')
    history = Label(clear_history_window, text='History Cleared...')
    history.pack()
    clear_history_window.mainloop()


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


window.geometry("300x200+10+10")
window.title('Wiki Quick Search')
window.bind('<Return>', search_function)
show_history_btn.bind('<Button-1>', check_history)
clear_history_btn.bind('<Button-1>', clear_history)
window.mainloop()
