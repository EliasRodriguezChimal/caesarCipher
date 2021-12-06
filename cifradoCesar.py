#Creado por Elias Rodriguez Chimal - 201730966
#Created by Elias Rodriguez Chimal - 201730966

from tkinter import *
from tkinter import messagebox as MessageBox

root = Tk()

#Function to encrypt the string, using the shift specified within the UI
def cifrar(cadena, shift):
    if (shift).isdigit() == True and cadena!="":
        shiftC = int(shift)
        listaCadCifrada = []

        for i in cadena:
            listaCadCifrada.append(chr(abs(((ord(i)) + shiftC%256))))

        print(listaCadCifrada)
        result = "".join(listaCadCifrada)

        resultText = Label(root, text=result)
        resultText.place(x=150, y=160)
        resultText['fg'] = 'white'
        resultText['background'] = '#0e0e0e'

        buttonDes = Button(root, text="Descifrar texto", padx = 4, pady = 4, command = lambda: descifrar(result, shift, 200))
        buttonDes.place(x=150,y=240)

    else:
        MessageBox.showwarning('Atención', 'El campo "número de corrimiento" debe ser un número y ningún campo puede estar vacío.')


#Function to decrypt the string, using the inverse process to 'encrypt' ('cifrar') function.
def descifrar(cadena, shift, yPos):
    if (shift).isdigit() == True and cadena!="":
        shiftDes = int(shift)
        listaCadDescifrada = []

        for i in cadena:
            listaCadDescifrada.append(chr(abs(((ord(i)) - shiftDes))%256))

        result = "".join(listaCadDescifrada)

        resultText = Label(root, text=result)
        resultText.place(x=150, y=yPos)
        resultText['fg'] = 'white'
        resultText['background'] = '#0e0e0e'

    else:
        MessageBox.showwarning('Atención', 'El campo "número de corrimiento" debe ser un número y ningún campo puede estar vacío.')


# All the code related with UI design

root.geometry("820x500")
root['background'] = '#0e0e0e'

title = Label(root, text="CIFRADO CESAR")
title.place(x=380, y=10)
title['fg'] = 'white'
title['background'] = '#0e0e0e'

subtitle1 = Label(root, text="Cifrado y descifrado")
subtitle1.place(x=370, y=40)
subtitle1['fg'] = 'white'
subtitle1['background'] = '#0e0e0e'

inputFieldText = Label(root, text="Ingrese la cadena a cifrar: ")
inputFieldText.place(x=10, y=80)
inputFieldText['fg'] = 'white'
inputFieldText['background'] = '#0e0e0e'

inputField = Entry(root, width=100, borderwidth=4)
inputField.place(x=175, y=80)
inputField['fg'] = 'white'
inputField['background'] = '#0e0e0e'
inputField['highlightcolor'] = 'white'
inputField['highlightthickness'] = 1
inputField['highlightbackground'] = 'green'

shiftLabel = Label(root, text="Número de corrimientos a la izquierda ")
shiftLabel.place(x=475, y=120)
shiftLabel['fg'] = 'white'
shiftLabel['background'] = '#0e0e0e'

shiftField = Entry(root, width=10, borderwidth=4)
shiftField.place(x=715, y=120)
shiftField['fg'] = 'white'
shiftField['background'] = '#0e0e0e'
shiftField['highlightcolor'] = 'white'
shiftField['highlightthickness'] = 1
shiftField['highlightbackground'] = 'green'

text = Label(root, text="La cadena resultante es: ")
text.place(x=10, y=160)
text['fg'] = 'white'
text['background'] = '#0e0e0e'

text2 = Label(root, text="La cadena descifrada es: ")
text2.place(x=10, y=200)
text2['fg'] = 'white'
text2['background'] = '#0e0e0e'

button = Button(root, text="Cifrar texto", padx = 4, pady = 4, command = lambda: cifrar(inputField.get(), shiftField.get()))
button.place(x=10,y=240)

subtitle2 = Label(root, text="Descifrado directo")
subtitle2.place(x=370, y=280)
subtitle2['fg'] = 'white'
subtitle2['background'] = '#0e0e0e'

inputFieldTextDes = Label(root, text="Ingrese la cadena a descifrar: ")
inputFieldTextDes.place(x=10, y=320)
inputFieldTextDes['fg'] = 'white'
inputFieldTextDes['background'] = '#0e0e0e'

inputFieldDes = Entry(root, width=100, borderwidth=4)
inputFieldDes.place(x=175, y=320)
inputFieldDes['fg'] = 'white'
inputFieldDes['background'] = '#0e0e0e'
inputFieldDes['highlightcolor'] = 'white'
inputFieldDes['highlightthickness'] = 1
inputFieldDes['highlightbackground'] = 'green'

shiftLabelDes = Label(root, text="Número de corrimientos a la izquierda ")
shiftLabelDes.place(x=475, y=360)
shiftLabelDes['fg'] = 'white'
shiftLabelDes['background'] = '#0e0e0e'

shiftFieldDes = Entry(root, width=10, borderwidth=4)
shiftFieldDes.place(x=715, y=360)
shiftFieldDes['fg'] = 'white'
shiftFieldDes['background'] = '#0e0e0e'
shiftFieldDes['highlightcolor'] = 'white'
shiftFieldDes['highlightthickness'] = 1
shiftFieldDes['highlightbackground'] = 'green'

text = Label(root, text="La cadena resultante es: ")
text.place(x=10, y=400)
text['fg'] = 'white'
text['background'] = '#0e0e0e'

buttonDesD = Button(root, text="Descifrar texto", padx = 4, pady = 4, command = lambda: descifrar(inputFieldDes.get(), shiftFieldDes.get(), 400))
buttonDesD.place(x=10,y=440)

creditos = Label(root, text="Creado por: Elías Rodríguez Chimal - 201730966")
creditos.place(x=550, y=440)
creditos['fg'] = 'white'
creditos['background'] = '#0e0e0e'

root.mainloop() 

