from tkinter import *
from random import randint 

class Graphics():
    """
    Graphics, first, it needs a generator,
    then you should call the btn() function
    and finally the loop
    graphics.btn()
    graphics.loop()
    """
    gen_name = ""
    def __init__(self, namegen):
        self.namegen = namegen

        self.root = Tk()
        self.frame = Frame(self.root)
        self.frame.pack()

        self.res = StringVar()
        self.res.set("Result")

        self.numSyll_lbl = Label(self.frame, text="Number of Syllables", font=(30))
        self.numSyll_lbl.grid(row=0, column=0)

        self.numSyll_txt = Entry(self.frame)
        self.numSyll_txt.grid(row=0, column=1)

        self.result_lbl = Label(self.frame, textvariable=self.res, font=40)
        self.result_lbl.grid(row=2, column=1)

    def setName(self, num):
        try:
            self.numi = int(num)
            self.res.set(self.namegen.generator(self.numi)) 
        except Exception as ex:
            print(ex.__class__)
            print(self.numSyll_txt.get())
            return

    def btn(self):
        self.gen = Button(self.frame, text="Generate", command= lambda num=self.numSyll_txt.get(): self.setName(self.numSyll_txt.get()))
        self.gen.grid(row=2, column=0)

        
    def loop(self):
        self.root.mainloop()

    

class NameGen():
    """
    this is the name generator (WIP)
    you have to instanciate the object using a path to the file.txt
    and then call the function generator(length) where length is the number
    of times it will mix things.
    
    every object in the file.txt needs to be separated by lines.
    """
    lon = 0
    def __init__(self, path):
        self.path = path


    def generator(self , lon):
        self.syllables = []
        self.gen_name = ""
        self.i = 0
        self.lon = lon

        with open(self.path, "r") as self.name:
            self.rows = self.name.readlines()
            for self.row in self.rows:
                self.syllables.append(self.row.strip('\n'))

        while self.i <= (self.lon - 1):
            self.r = randint(0, self.syllables.__len__()-1)
            if (self.syllables[self.r].startswith("0") and self.i == 0):
                self.gen_name += self.syllables[self.r].lstrip('0')
                self.i += 1
            elif (self.syllables[self.r].startswith("1") and self.i == self.lon):
                self.gen_name += self.syllables[self.r].lstrip('1')
                self.i += 1
            elif (not(self.syllables[self.r].startswith("0")) and not(self.syllables[self.r].startswith("1"))):
                self.gen_name += self.syllables[self.r]
                self.i += 1

        print("name generate:", end="")
        print(self.gen_name)
        return self.gen_name


if(__name__ == "__main__"):
    namegen = NameGen("./syllables.txt")
    graphics = Graphics(namegen)
    graphics.btn()
    graphics.loop()

