import tkinter as ttk
from pynput.keyboard import Key, Controller

def cancel(self):
    global counter
    print(counter)
    button_start['state'] = 'normal'
    text_status.config(text = 'Apague e Cole as novas notas. Aperte no botão Iniciar para começar.')
    raiz.after_cancel(counter)
    
def start3():
    button_start['state'] = 'disabled'
    text_status.config(text = 'Começando em 3s')
    global counter
    counter = raiz.after(1000, start2)

def start2():
    text_status.config(text = 'Começando em 2s')
    global counter
    counter = raiz.after(1000, start1)

def start1():
    text_status.config(text = 'Começando em 1s')
    global counter
    counter = raiz.after(1000, start0)

def start0():
    text_status.config(text = 'Notas sendo digitadas')
    global counter
    counter = raiz.after(1, start)

def start():
    global counter, text_notas,CheckVar1
    notas = text_notas.get('1.0','end')
    for char in notas:
        if char == '\n':
            print(CheckVar1.get())
            for j in range(CheckVar1.get()):
                
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)
        else:
            keyboard.type(char)
    text_status.config(text = 'Apague e Cole as novas notas. Aperte no botão Iniciar para começar.')
    button_start['state'] = 'normal'

keyboard = Controller()
raiz = ttk.Tk()
raiz.title("Digitar Notas")
counter =''
raiz.bind("<Escape>",cancel) 

text_esc = ttk.Label(raiz,text='Para cancelar aperte ESC')
text_esc.pack()
CheckVar1 = ttk.IntVar()
c1 = ttk.Checkbutton(raiz, text='Nota Final?',variable=CheckVar1, onvalue=5, offvalue=1)
c1.select()
c1.pack()
status ='Cole as notas e aperte no botão Iniciar'
text_status = ttk.Label(raiz,text=status)
text_status.pack()

button_start = ttk.Button(raiz,text = 'Iniciar',command= start3)
button_start.pack()

text_notas = ttk.Text(raiz)
text_notas.pack()

raiz.mainloop()
