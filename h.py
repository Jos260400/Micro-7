from tkinter import*
import random
import time

class Pelota:
    def _init_(self,canvas,color):
        self.canvas = canvas
        self.id=canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        
    def dibujar(self):
        pass
    
tk = Tk()
tk.title("Juego")
tk.resizable(0,0)
tk.wm_attributes("Top",1)
canvas = Canvas(tk, width=500, height=400, bd=0, highligh=0)
canvas.pack()
tk.update()

pelota = Pelota(canvas, 'red')

while 1:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    