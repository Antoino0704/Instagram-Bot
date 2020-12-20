from instabot import Bot        #richiama moduli per instabot, os e tkinter
import os
import os.path
import tkinter as tk
from tkinter import *

#crea finestra principale 
window = tk.Tk()
window.geometry("1200x900")
window.title('Instagram')
window.iconbitmap('C:\\Users\\asus\\OneDrive\\Pictures\\icone_personalizzate\\instapy.ico')
window.grid_columnconfigure(0, weight=1)

bot = Bot()     


#inserisci immagine e descrizione
img = tk.StringVar()
desc = tk.StringVar()
img_label = tk.Label(window, text='inserisci nome immagine con estenzione (immaggine deve essere presente nella stessa cartella del file):', font=('', 16))
img_label.grid(row='1', column='0', stick="W")
img_entry = tk.Entry(window, textvariable=img)
img_entry.grid(row='2', column='0', pady="50")
desc_label = tk.Label(window, text='inserisci descrizione:', font=('', 16))
desc_label.grid(row='3', column='0', stick="W")
desc_entry = tk.Entry(window, textvariable=desc)
desc_entry.grid(row='4', column='0', pady="50")


#acquisire dati nome utente e password se non c'è un file chiamato dati.txt
very = os.path.exists('dati.txt')
print(very)
if (very != 1):
    us = tk.StringVar()
    passer = tk.StringVar()
    us_label = tk.Label(window, text="inserisci nome utente", font=('', 16))
    us_label.grid(row='5', column='0', pady="50", stick='W')
    us_entry = tk.Entry(window, textvariable=us)
    us_entry.grid(row='6', column='0', pady="50")
    passw_label = tk.Label(window, text='inserisci password', font=('', 16))
    passw_label.grid(row='7', column='0', pady="50", stick='W')
    passw_entry = tk.Entry(window, textvariable=passer)
    passw_entry.grid(row='8', column='0', pady="50")



#funzione per creare fil di testo e salvarci nome utente e password
def salva_dati():
            fps = open("dati.txt", "w")
            fps.write("username\n" + str(us.get()) + "\npassword\n" + str(passer.get()))
            fps.close()



def carica_foto():
    
    ver = os.path.exists("dati.txt")        #se il file dati.txt esiste
    if ver == 1:
        f = open("dati.txt", "r")       #acquisire nome utente e password dal file dati.txt
        for i in range(1, 3):
            usert = f.readline()
        f.close()
        user = usert [:-1]

        fp = open("dati.txt", "r")
        for o in range(1, 5):
            passw = fp.readline()
        fp.close()

        attesa = tk.Tk()            #intefaccia di avviso per attesa
        attesa.title('Instagram_success')
        attesa.iconbitmap('C:\\Users\\asus\\OneDrive\\Pictures\\icone_personalizzate\\instapy.ico')
        attes = tk.Label(attesa, text='FOTO CARICATA')
        attes.grid(row='0', column='0')

        #accedere al profilo e caricare la foto
        bot.login(username=user, password=passw)        
        bot.upload_photo(str(img.get()), str(desc.get()))


    else:       #se il file dati.txt non esiste
       attesa = tk.Tk()            #intefaccia di avviso per attesa
       attesa.geometry('400x400')
       attesa.title('Instagram_success')
       attesa.iconbitmap('C:\\Users\\asus\\OneDrive\\Pictures\\icone_personalizzate\\instapy.ico')
       attes = tk.Label(attesa, text='FOTO CARICATA')
       attes.pack()
       datil = tk.Label(attesa, text='ti consigliamo di salvare i dati per la prossima volta, clicca su salva dati in basso', fg='red')
       datil.pack()

       #accedere al profilo e caricare la foto
       bot.login(username=str(us.get()), password=str(passer.get()))
       bot.upload_photo(str(img.get()), str(desc.get()))

       #bottone per portare alla funzione per salvare i dati
       dati = tk.Button(text='salva dati', command=salva_dati)
       dati.grid(row='9', column='0', stick='W')
        
#bottone per portare alla funzione per caricare la foto
fun = tk.Button(text='carica', command=carica_foto, font=('', 16))
fun.grid(row='9', column='0', pady="50")


window.mainloop()
