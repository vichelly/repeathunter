from tkinter import *
from tkinter import scrolledtext

janela = Tk()
janela.title('Filtro de palavras')
janela.geometry('700x500')

txt = scrolledtext.ScrolledText(janela, width=80, height=22 )
txt.place(relx=0.04, rely=0.18 )

txt1=Label(janela, text='Palavra suspeita: ' )
txt2=Label(janela, text='Frequência: ' )
txt3=Label(janela, text='Ocorrências: ' )
txt1.place(relx=0.02 , rely=0.0 )
txt2.place(relx=0.02 , rely=0.05 )
txt3.place(relx=0.02 , rely=0.13 )  

entrada1 = Entry(janela, width=15)
entrada2 = Label(janela, width=15)
entrada1.place(relx=0.16, rely=0.01 )
entrada2.place(relx=0.13, rely=0.05 )

def check():
    i = 0
    palavra = entrada1.get()
    texto = txt.get(1.0,END)
    palavra = palavra.lower()
    texto = texto.lower()
    texto = texto.replace('.','')
    texto = texto.replace(',','')
    texto = texto.replace('!','')
    texto = texto.replace('?','')
    texto = texto.replace(':','')
    texto = str(texto).split()
    for a in texto:
        if a == palavra:
            i=i+1
    entrada2['text'] = i
    print(i)

btn = Button(janela, text='Pesquisar', command=check )
btn.place(relx=0.3 , rely=0.008 )

janela.mainloop()