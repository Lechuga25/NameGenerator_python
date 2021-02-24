from tkinter import *
from random import randint 

res = "Result"

root = Tk()
frame = Frame(root)
frame.pack()

res = StringVar()

numSyll_lbl = Label(frame, text="Number of Syllables", font=(30))
numSyll_lbl.grid(row=0, column=0)

numSyll_txt = Entry(frame)
numSyll_txt.grid(row=0, column=1)


def generator():
    lon = int(numSyll_txt.get())
    syllables = []

    with open("./names.txt", "r") as name:
        rows = name.readlines()
        for row in rows:
            syllables.append(row.strip('\n'))

    gen_name = ""
    i = 0

    while i <= (lon - 1):
        r = randint(0, syllables.__len__()-1)
        if (syllables[r].startswith("0") and i == 0):
            gen_name += syllables[r].lstrip('0')
            i += 1
        elif (syllables[r].startswith("1") and i == lon):
            gen_name += syllables[r].lstrip('1')
            i += 1
        elif (not(syllables[r].startswith("0")) and not(syllables[r].startswith("1"))):
            gen_name += syllables[r]
            i += 1

    res.set(gen_name)
    result_lbl = Label(frame, textvariable=res, font=40)
    result_lbl.grid(row=2, column=1)   


gen = Button(frame, text = "Generate", command = generator)
gen.grid(row=2, column=0)



root.mainloop()


