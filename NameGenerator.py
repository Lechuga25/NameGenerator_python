from tkinter import Tk, Frame, StringVar, Label, Entry, Label, Button, W
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
        self.font = ("Helvetica", 20, )
        self.bgcolor = "#1D2021"
        self.fgcolor = "#DEDBCC"

        self.root = Tk()
        self.root.configure(bg=self.bgcolor)
        self.frame = Frame(self.root)
        self.frame.configure(bg=self.bgcolor)
        self.frame.pack()

        self.res = StringVar()
        self.res.set("Result")

        self.numSyll_lbl = Label(self.frame,
            text="Number of Syllables: ",
            font=self.font,
            bg=self.bgcolor,
            fg=self.fgcolor)
        self.numSyll_lbl.grid(row=0, column=0, sticky=W)

        self.numSyll_txt = Entry(self.frame,
            bg="#2F3436",
            fg="#83A598",
            font=self.font,
            borderwidth=0,
            width=10,
            insertbackground=self.fgcolor)
        self.numSyll_txt.grid(row=0, column=1)

        self.space_lbl = Label(self.frame, bg=self.bgcolor)
        self.space_lbl.grid(row=1, column=0)

        self.result_lbl = Label(self.frame,
        textvariable=self.res,
        font=self.font,
        bg=self.bgcolor,
        fg="#8EC07C")
        self.result_lbl.grid(row=2, column=1)

    # Function call to the name generator.
    def setName(self, num):
        try:
            self.numi = int(num)
            self.res.set(self.namegen.generator(self.numi).capitalize())
            print("Generated name: ", end="")
            print(self.res.get())
        except Exception as ex:
            print(ex.__class__)
            # print(self.numSyll_txt.get())
            return

    # button instanciator
    def btn(self):
        self.gen = Button(self.frame,
        text="Generate",
        command= lambda num=self.numSyll_txt.get(): self.setName(self.numSyll_txt.get()))
        self.gen.configure(bg="#2F3436", fg="#83A598", font=self.font, borderwidth=0)
        self.gen.grid(row=2, column=0, sticky=W)    

    # loop call
    def loop(self):
        self.root.tk.call('tk', 'scaling', 2.0)
        self.root.mainloop()

    

class NameGen():
    """
    this is the name generator (WIP)
    you have to instanciate the object using a path to the file.txt
    and then call the function generator(length) where length is the number
    of times it will mix things.
    
    every object in the file.txt needs to be separated by lines.
    and you can use:
    - 0 to especificate that it should only appear at the start of the name
    - 1 to especificate that it should be at the middle of the name
    - 2 to especificate that it should be at the end of the name
    """

    def __init__(self, path):
        self.path = path
        self.lon = 0

    # store's the file syllables into a list
    def readfile(self, syllables):
        with open(self.path, "r") as self.name:
            self.rows = self.name.readlines()
            for self.row in self.rows:
                syllables.append(self.row.strip('\n'))
        return syllables

    # generates the name
    def generator(self , lon):
        self.syllables = []
        self.gen_name = ""
        self.i = 0
        self.lon = lon - 1
        self.syll = ""
        self.syllables = self.readfile(self.syllables)

        while self.i <= (self.lon):
            self.r = randint(0, self.syllables.__len__()-1)
            self.syll = self.syllables[self.r]

            if (not(self.syll.startswith("0")) and not(self.syll.startswith("1")) and not(self.syll.startswith("2"))):
                self.gen_name += self.syll
                self.i += 1
                continue

            if (not(self.syll.startswith("0")) and self.i == 0):
                continue

            if (not(self.syll.startswith("1")) and (self.i >= 1 and self.i < self.lon)):
                continue

            if (not(self.syll.startswith("2")) and self.i == self.lon):
                continue
            
            self.gen_name += self.syll[1:]
            self.i += 1
            

        return self.gen_name


if(__name__ == "__main__"):
    namegen = NameGen("./syllables.txt")
    graphics = Graphics(namegen)
    graphics.btn()
    graphics.loop()