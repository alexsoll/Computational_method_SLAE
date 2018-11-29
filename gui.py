from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from math import floor
import SLAE

class slae_gui:
    def __init__(self, master):
        self.buttonOK = Button(master, text = "Ok", command= lambda: self.set_size_of_matrix(master))
        self.ent = Entry(master)
        self.readFile = Button(master, text = "Read Matrix", command = lambda: self.ReadMatrix(master))
        self.readFile.place(x = 200, y = 15)
        self.sizeMatrix = Label(master, text = "Enter the size of matrix")
        self.buttonOK.place(x = 130, y = 15)
        self.ent.grid(row = 1, column = 0)
        self.sizeMatrix.grid(row = 0, column = 0)
        self.matrix = []
        self.b = []
    def set_size_of_matrix(self, master, s = None):
        self.l = []
        self.vecB = []
        if s == None:
            self.size = int(self.ent.get())
        else:
            self.size = s
        for i in range(self.size):
            self.tmp = []
            for j in range(self.size):
                e = Entry(master, width = 5)
                e.grid(row = i + 3, column = j + 2)
                #print(e.winfo_width())
                self.tmp.append(e)
            self.l.append(self.tmp)
        for i in range(self.size):
            e = Entry(master, width = 5)
            e.grid(row = i + 3, column = 6 + self.size)
            self.vecB.append(e)
        self.labelb = Label(master, text = "b = ")
        #self.labelb.place(x = 130 + self.size * 30 ,y = (self.size  + 3)/2 * int(self.ent.winfo_height()))
        self.labelb.grid(row = floor(self.size / 2) + 3,column =  self.size + 4)
        self.labelMatrix = Label(master, text = "Matrix = ")
        self.labelMatrix.place(x = 70 ,y = (self.size  + 3)/2 * int(self.ent.winfo_height()))
        self.matrixOK = Button(master, text = "Run methods", command = lambda: self.Run(master))
        #print(self.ent.winfo_width())
        self.matrixOK.place(x = 125 ,y = (self.size  + 2)* int(self.ent.winfo_height()) + 3)

    def Run(self,master):
        if len(self.matrix) == 0:
            b = []
            for i, line in enumerate(self.l):
                s = []
                b.append(self.vecB[i].get())
                for j, val in enumerate(line):
                    s.append(val.get())
                matrix.append(s)
            SLAE.main(matrix, b)
        else:
            SLAE.main(self.matrix, self.b)

    def ReadMatrix(self,master):
        filename = askopenfilename()
        file = open(filename, "r")
        lines = file.read().splitlines()
        for line in lines:
            line = line.split(" ")
            tmp = line[-1]
            tmp = tmp.split('\t')
            line[-1] = tmp[0]
            self.b.append(tmp[1])
            self.matrix.append(line)
        N = len(self.matrix)
        self.set_size_of_matrix(master,N)
        for i, line in enumerate(self.matrix):
            self.vecB[i].insert(0, self.b[i])
            for j, val in enumerate(line):
                self.l[i][j].insert(0,val)

    

root = Tk()
fb = slae_gui(root)
root.title("Сomputational_method_SLAE")
root.geometry("500x500")
root.mainloop()