from tkinter import * 
from tkinter import ttk
from googletrans import Translator 

root = Tk()
root.title("tradutor")
s = ttk.Style()
s.configure("prin.TFrame", borderwidth=5,relief="raised", background="black")

def traducao(*args):
    translator = Translator()
    
    if op == "en" or "pt" or "es":
        text.delete("1.0", "end")
        tr = translator.translate(textvar.get(), dest=op.get())
        text.insert("1.0", tr.text)
    else:
        text.insert("1.0", "escolha uma das opçõe de tradução: Português, Inglês, Espanhol")


tela = ttk.Frame(root, style="prin.TFrame", padding=(12, 12, 12, 12))
tela.grid(column=0, row=1, sticky=(N, W, E, S))

label1 = Label(tela, text="Traduzir", background="red")
label1.grid(column=1, row=2, sticky=(W, E))

textvar = StringVar()
text_in = Entry(tela,borderwidth=5, textvariable= textvar)
text_in.grid(column=1, row=4, sticky=(W, E))
text_in.focus()
op = StringVar()

one = ttk.Radiobutton(tela, text="Português", variable=op, value="pt")
one.grid(column=1, row=7, sticky=(W, E))

two = ttk.Radiobutton(tela, text="Inglês", variable=op, value="en")
two.grid(column=1, row=8, sticky=(W, E))

three = ttk.Radiobutton(tela, text="espanhol", variable=op, value="es")
three.grid(column=1, row=9, sticky=(W, E))


label2= Label(tela, text="Tradução:", background="green")
label2.grid(column=1, row=6, sticky=(W, E))

text= Text(tela, width=40, height=10, borderwidth=5)
text.grid(column=1, row=10)

iniciar = Button(tela, text="traduzir", command=traducao)
iniciar.grid(column=1, row=11, sticky=(W, E))

root.mainloop()
