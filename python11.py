import tkinter as tk
import webbrowser as wb

root = tk.Tk()
def display_udemy():
    user_enq = enq.get()
    print(user_enq)
    if user_enq: 
        l2.config(text="Where did you hear about us?")
        wb.open("https://www.youtube.com/results?q")
    else:
        l2.config(text="Please enter required information")


def display_ig():
        user_enq = enq.get()
        print(user_enq)
        if user_enq: 
            l2.config(text="Where did you hear about us?")
            wb.open("https://instagram.com/only.python?q")
        else:
            l2.config(text="Please enter required information")

def display_yt():
    user_enq = enq.get()
    print(user_enq)
    if user_enq:
        l2.config(text="Where did you hear about us?")
        wb.open("https://www.youtube.com/results?search_query")
    else:
        l2.config(text="Please enter required information")



enq = tk.Entry(root, 
               font=("Times New Roman", 20),
               width=30)
enq.grid(row=0,column=1)

l1 = tk.Label(root, 
              text="Enter enquiry:", 
              font=("Times New Roman", 25))
l1.grid(row=0,column=0)

l2 = tk.Label(root, 
              font=("Times New Roman", 25))
l2.grid()

yt = tk.Button(root, 
               text="YouTube", 
               font=("Times New Roman", 20),
               width=10,
               bg="red", 
               activebackground="green", 
               command=display_yt)
yt.grid()

ig = tk.Button(root, 
               text="Instagram", 
               font=("Times New Roman", 20),
               width=10,
               bg="red", 
               activebackground="green", 
               command=display_ig)
ig.grid()

udemy = tk.Button(root, 
               text="udemy", 
               font=("Times New Roman", 20),
               width=10,
               bg="red", 
               activebackground="green", 
               command=display_udemy)
udemy.grid()


root.mainloop()
import tkinter as tk
import webbrowser as wb

root = tk.Tk()
def display_udemy():
    user_enq = enq.get()
    print(user_enq)
    if user_enq: 
        l2.config(text="Where did you hear about us?")
        wb.open("https://www.youtube.com/results?q")
    else:
        l2.config(text="Please enter required information")


def display_ig():
        user_enq = enq.get()
        print(user_enq)
        if user_enq: 
            l2.config(text="Where did you hear about us?")
            wb.open("https://instagram.com/only.python?q")
        else:
            l2.config(text="Please enter required information")

def display_yt():
    user_enq = enq.get()
    print(user_enq)
    if user_enq:
        l2.config(text="Where did you hear about us?")
        wb.open("https://www.youtube.com/results?search_query")
    else:
        l2.config(text="Please enter required information")



enq = tk.Entry(root, 
               font=("Times New Roman", 20),
               width=30)
enq.grid(row=0,column=1)

l1 = tk.Label(root, 
              text="Enter enquiry:", 
              font=("Times New Roman", 25))
l1.grid(row=0,column=0)

l2 = tk.Label(root, 
              font=("Times New Roman", 25))
l2.grid()

yt = tk.Button(root, 
               text="YouTube", 
               font=("Times New Roman", 20),
               width=10,
               bg="red", 
               activebackground="green", 
               command=display_yt)
yt.grid()

ig = tk.Button(root, 
               text="Instagram", 
               font=("Times New Roman", 20),
               width=10,
               bg="red", 
               activebackground="green", 
               command=display_ig)
ig.grid()

udemy = tk.Button(root, 
               text="udemy", 
               font=("Times New Roman", 20),
               width=10,
               bg="red", 
               activebackground="green", 
               command=display_udemy)
udemy.grid()


root.mainloop()
