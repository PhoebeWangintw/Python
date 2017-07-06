from tkinter import *
import re

def build_dic():
    global dic_list
    d = {}
    dic_list = []
    with open("words.txt") as f:
        for line in f:
            dic_list.append(line)

def main():
    build_dic()
    window = Tk()
    window.geometry('500x250')
    window.title('Little Dictionary')
    
    global entry
    entry = Entry(window)
    entry.pack()
    entry.focus_set()

    btn = Button(window, text='Look up!')
    btn.configure(command=btn_click)
    btn.pack()

    global text
    text = Text(window, height=10, borderwidth=10, width=50, bg='lightgrey', relief='flat')
    text.pack()
    # text.configure(state="disabled")  # forbid text edition
    
    window.mainloop()

def btn_click():
    string = entry.get()
    search(string)

def search(string):
    text.config(state="normal")
    text.delete('1.0', END)  # delete all text in the text box
    r = re.compile(string + ".*", re.IGNORECASE)
    search_list = list(filter(r.match, dic_list))
    index = 1.0
    if len(search_list) < 20:
        for l in search_list:
            text.insert(index, l.lower())
            index += 1
    else:
        for l in search_list[:20]:
            text.insert(index, l.lower())
            index += 1
    text.pack()
    text.config(state="disabled")


if __name__ == '__main__':
    main()