import png
from tkinter import *
import webbrowser
import pyqrcode


#génération de l'écran principal
test = Tk()
test.geometry("480x720")
test.title("Générateur de Qr code")

#premier label (texte simple)
L1 = Label(text="Générateur de Qr Code créé par Thibakar#7368!", font='arial')
L1.pack()

#def
def open_git():
    webbrowser.open_new("https://github.com/thibakarr")

def open_rick_roll():
    webbrowser.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

def doc_tkinter():
    webbrowser.open_new("https://docs.python.org/fr/3/library/tk.html")

def generate():
    url = saisie.get()
    print(url)
    s = str(url)
    qrcode = pyqrcode.create(s)
    qrcode.png('testduqrcode.png', scale=6)
    win = Toplevel(test)
    photo = PhotoImage(file='testduqrcode.png')
    label = Label(win, image=photo)
    label.pack()
    win.mainloop()


# création bouton générate
BGEN = Button(text="Générer", command=(generate))
BGEN.pack()

#boutton 
B1= Button(text="My Github", command=(open_git))
B1.pack(side=BOTTOM)


B3 = Button(text='My YtChannel', command=(open_rick_roll))
B3.place(x=118,y=694)

B4 = Button(text='Tkinter Doc', command=(doc_tkinter))
B4.place(x=275,y=694)
#def de l'url qu'on veut transformer en qrcode

saisie = Entry(test)
saisie.pack()

#loop de l'écran
test.mainloop()