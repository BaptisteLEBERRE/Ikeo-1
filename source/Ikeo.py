import mysql.connector
import tkinter as tk


mydb = mysql.connector.connect(
  host = "localhost",
    user = "root",
    passwd = "root",
    database = "ikeo"
)

mycursor = mydb.cursor()

def factory_list():
    mycursor.execute("""SELECT produits.nom_produit, usines.nom_usine FROM produits 
    JOIN usine_produit ON produits.id_produit = usine_produit.id_produit
    JOIN usines ON usine_produit.id_usine = usines.id_usine""")
    s = mycursor.fetchall()
    d = {}
    n = 1
    for i in s:
        d[i[0]] = i[1]
        entry = tk.Entry(fenetre, width="100")
        entry.insert(0, f"{d[i]} : {d[i[0]]}")
        entry.grid(row=n, column=0)
        n += 1

fenetre = tk.Tk()

fenetre.title("Ikeo")
fenetre.geometry("400x400")

bouton_usines = tk.Button(fenetre, text='Afficher Usines', command=factory_list)
bouton_usines.grid(row=0, column=0)

fenetre.mainloop()
