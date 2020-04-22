from tkinter import *
import tkinter.messagebox
from tkinter import Entry
from typing import List
import base64
import os

icon = """
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
"""
icondata= base64.b64decode(icon)
tempFile= "icon.ico"
iconfile= open(tempFile,"wb")
## Extract the icon
iconfile.write(icondata)
iconfile.close()

def determ():
    input_prompt = Tk(className=" Calc Derivate")
    input_prompt.geometry("325x120+600+250")
    input_prompt.iconbitmap(tempFile)


    mess = Label(input_prompt, text="Cate randuri/coloane are determinantul? \n{2 - 5}")
    qu = Entry(input_prompt, width=28, borderwidth=4, justify="center")
    nothing = Label(input_prompt, text="          ")

    nothing.grid(row=0, column=0)
    qu.grid(row=2, column=2)
    qu.insert(0, '2')
    mess.grid(row=0, column=2)

    def on_closing():
        os.remove(tempFile)
        input_prompt.destroy()

    def calc_make_try():
        try:
            nr = int(qu.get())
            check = int(var.get())
        except:
            return tkinter.messagebox.showerror(title="Error", message="Număr invalid!!!")
        if 2 <= int(nr) <= 5:
            input_prompt.destroy()
            DETERM(check, nr).nr_x()
        else:
            return tkinter.messagebox.showerror(title="Error", message="Număr invalid!!!")

    continu = Button(input_prompt, text="Continue", activebackground="grey", width=25, command=calc_make_try)
    var = IntVar()
    cramer = Checkbutton(input_prompt, text="Bifează pentru sisteme de ecuații (Cramer)", variable=var)
    continu.grid(row=3, column=2)
    cramer.grid(row=4, column=2, columnspan=2)

    input_prompt.protocol("WM_DELETE_WINDOW", on_closing)
    input_prompt.mainloop()


class DETERM:

    def __init__(self, check, nr):
        self.check = check
        self.nr = nr

    def nr_x(self):

#-----------------------------------------------------------------------------------------------------------------------
        if self.check ==1:

            win = Tk(className=' Calculator Determinanti')
            win.geometry("+600+250")
            win.iconbitmap(tempFile)


            names = []
            names2 = []

            for i in range(0, self.nr):
                names.append([])
                for j in range(0, self.nr):
                    names[i].append(Entry(win, width=3, borderwidth=2, font="Times 16", justify="center"))
                    names[i][j].grid(row=i, column=j, ipady=10, ipadx=15)

            for l in range(self.nr):
                Label(win, text="   =   ", font="Helvetica 17").grid(row=l, column=self.nr)
                nms = Entry(win, width=3, borderwidth=2, font="Times 16", justify="center")
                names2.append(nms)
                nms.grid(row=l, column=self.nr+1, ipady=10, ipadx=15)

            def back():
                win.destroy()
                determ()

            def on_closing():
                os.remove(tempFile)
                win.destroy()

            def calc_c():
                if self.nr == 2:

                    a1 = float(names[0][0].get().replace(',', '.'))
                    a2 = float(names[0][1].get().replace(',', '.'))
                    a3 = float(names[1][0].get().replace(',', '.'))
                    a4 = float(names[1][1].get().replace(',', '.'))
                    b1 = float(names2[0].get().replace(',', '.'))
                    b2 = float(names2[1].get().replace(',', '.'))


                    final_rez_1, final_rez_2 = DETERM.calc_nr_2_c(self, a1, a2, a3, a4, b1, b2)

                    final_rezult = Label(win, text="Rezultatul:", font="Helvetica 20")
                    final_rezult_num_1 = Label(win, text="x1 = " + str(final_rez_1), font="Helvetica 25")
                    final_rezult_num_2 = Label(win, text="x2 = " + str(final_rez_2), font="Helvetica 25")
                    final_rezult.grid(row=0, column=self.nr+2)
                    final_rezult_num_1.grid(row=1, column=self.nr+2)
                    final_rezult_num_2.grid(row=3, column=self.nr+2)
                elif self.nr ==3:
                    a1 = float(names[0][0].get().replace(',', '.'))
                    a2 = float(names[0][1].get().replace(',', '.'))
                    a3 = float(names[0][2].get().replace(',', '.'))
                    a4 = float(names[1][0].get().replace(',', '.'))
                    a5 = float(names[1][1].get().replace(',', '.'))
                    a6 = float(names[1][2].get().replace(',', '.'))
                    a7 = float(names[2][0].get().replace(',', '.'))
                    a8 = float(names[2][1].get().replace(',', '.'))
                    a9 = float(names[2][2].get().replace(',', '.'))
                    b1 = float(names2[0].get().replace(',', '.'))
                    b2 = float(names2[1].get().replace(',', '.'))
                    b3 = float(names2[2].get().replace(',', '.'))

                    final_rez_1, final_rez_2, final_rez_3 = DETERM.calc_nr_3_c(self, a1, a2, a3, a4, a5, a6, a7, a8, a9, b1, b2, b3)

                    final_rezult = Label(win, text="Rezultatul:", font="Helvetica 20")
                    final_rezult_num_1 = Label(win, text="x1 =" + str(final_rez_1), font="Helvetica 25")
                    final_rezult_num_2 = Label(win, text="x2 =" + str(final_rez_2), font="Helvetica 25")
                    final_rezult_num_3 = Label(win, text="x3 =" + str(final_rez_3), font="Helvetica 25")
                    final_rezult.grid(row=0, column=self.nr+2)
                    final_rezult_num_1.grid(row=1, column=self.nr+2)
                    final_rezult_num_2.grid(row=2, column=self.nr+2)
                    final_rezult_num_3.grid(row=3, column=self.nr+2, rowspan=2)
                elif self.nr == 4:
                    a1 = float(names[0][0].get().replace(',', '.'))
                    a2 = float(names[0][1].get().replace(',', '.'))
                    a3 = float(names[0][2].get().replace(',', '.'))
                    a4 = float(names[0][3].get().replace(',', '.'))
                    a5 = float(names[1][0].get().replace(',', '.'))
                    a6 = float(names[1][1].get().replace(',', '.'))
                    a7 = float(names[1][2].get().replace(',', '.'))
                    a8 = float(names[1][3].get().replace(',', '.'))
                    a9 = float(names[2][0].get().replace(',', '.'))
                    a10 = float(names[2][1].get().replace(',', '.'))
                    a11 = float(names[2][2].get().replace(',', '.'))
                    a12 = float(names[2][3].get().replace(',', '.'))
                    a13 = float(names[3][0].get().replace(',', '.'))
                    a14 = float(names[3][1].get().replace(',', '.'))
                    a15 = float(names[3][2].get().replace(',', '.'))
                    a16 = float(names[3][3].get().replace(',', '.'))

                    b1 = float(names2[0].get().replace(',', '.'))
                    b2 = float(names2[1].get().replace(',', '.'))
                    b3 = float(names2[2].get().replace(',', '.'))
                    b4 = float(names2[3].get().replace(',', '.'))

                    final_rez_1, final_rez_2, final_rez_3, final_rez_4 = DETERM.calc_nr_4_c(self, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, b1, b2, b3, b4)

                    final_rezult = Label(win, text="Rezultatul:", font="Helvetica 20")
                    final_rezult_num_1 = Label(win, text="x1 =" + str(final_rez_1), font="Helvetica 25")
                    final_rezult_num_2 = Label(win, text="x2 =" + str(final_rez_2), font="Helvetica 25")
                    final_rezult_num_3 = Label(win, text="x3 =" + str(final_rez_3), font="Helvetica 25")
                    final_rezult_num_4 = Label(win, text="x4 =" + str(final_rez_4), font="Helvetica 25")
                    final_rezult.grid(row=0, column=self.nr+2)
                    final_rezult_num_1.grid(row=1, column=self.nr+2)
                    final_rezult_num_2.grid(row=2, column=self.nr+2)
                    final_rezult_num_3.grid(row=3, column=self.nr+2)
                    final_rezult_num_4.grid(row=4, column=self.nr+2, rowspan=2)
                elif self.nr == 5:
                    a1 = float(names[0][0].get().replace(',', '.'))
                    a2 = float(names[0][1].get().replace(',', '.'))
                    a3 = float(names[0][2].get().replace(',', '.'))
                    a4 = float(names[0][3].get().replace(',', '.'))
                    a5 = float(names[0][4].get().replace(',', '.'))
                    a6 = float(names[1][0].get().replace(',', '.'))
                    a7 = float(names[1][1].get().replace(',', '.'))
                    a8 = float(names[1][2].get().replace(',', '.'))
                    a9 = float(names[1][3].get().replace(',', '.'))
                    a10 = float(names[1][4].get().replace(',', '.'))
                    a11 = float(names[2][0].get().replace(',', '.'))
                    a12 = float(names[2][1].get().replace(',', '.'))
                    a13 = float(names[2][2].get().replace(',', '.'))
                    a14 = float(names[2][3].get().replace(',', '.'))
                    a15 = float(names[2][4].get().replace(',', '.'))
                    a16 = float(names[3][0].get().replace(',', '.'))
                    a17 = float(names[3][1].get().replace(',', '.'))
                    a18 = float(names[3][2].get().replace(',', '.'))
                    a19 = float(names[3][3].get().replace(',', '.'))
                    a20 = float(names[3][4].get().replace(',', '.'))
                    a21 = float(names[4][0].get().replace(',', '.'))
                    a22 = float(names[4][1].get().replace(',', '.'))
                    a23 = float(names[4][2].get().replace(',', '.'))
                    a24 = float(names[4][3].get().replace(',', '.'))
                    a25 = float(names[4][4].get().replace(',', '.'))

                    b1 = float(names2[0].get().replace(',', '.'))
                    b2 = float(names2[1].get().replace(',', '.'))
                    b3 = float(names2[2].get().replace(',', '.'))
                    b4 = float(names2[3].get().replace(',', '.'))
                    b5 = float(names2[4].get().replace(',', '.'))

                    final_rez_1, final_rez_2, final_rez_3, final_rez_4, final_rez_5 = DETERM.calc_nr_5_c(self, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11,
                                                                                                         a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22,
                                                                                                         a23, a24, a25, b1, b2, b3, b4, b5)

                    final_rezult = Label(win, text="Rezultatul:", font="Helvetica 20")
                    final_rezult_num_1 = Label(win, text="x1 =" + str(final_rez_1), font="Helvetica 25")
                    final_rezult_num_2 = Label(win, text="x2 =" + str(final_rez_2), font="Helvetica 25")
                    final_rezult_num_3 = Label(win, text="x3 =" + str(final_rez_3), font="Helvetica 25")
                    final_rezult_num_4 = Label(win, text="x4 =" + str(final_rez_4), font="Helvetica 25")
                    final_rezult_num_5 = Label(win, text="x5 =" + str(final_rez_5), font="Helvetica 25")
                    final_rezult.grid(row=0, column=self.nr+2)
                    final_rezult_num_1.grid(row=1, column=self.nr+2)
                    final_rezult_num_2.grid(row=2, column=self.nr+2)
                    final_rezult_num_3.grid(row=3, column=self.nr+2)
                    final_rezult_num_4.grid(row=4, column=self.nr+2)
                    final_rezult_num_5.grid(row=5, column=self.nr+2, rowspan=2)

            calc = Button(win, text="Calculeaza", comman=calc_c)
            back_b = Button(win, text="Back", command=back)
            spa = Label(win, text="  ")
            spa2 = Label(win, text="  ")
            spa.grid(row=self.nr, column=0, columnspan=self.nr+2)
            spa2.grid(row=self.nr+2, column=0, columnspan=self.nr + 2)
            calc.grid(row=self.nr+1, column=0, columnspan=self.nr, sticky="nesw", ipady=25)
            back_b.grid(row=self.nr+1, column=self.nr, columnspan=2, sticky="nesw", ipady=25)

            win.protocol("WM_DELETE_WINDOW", on_closing)

            win.mainloop()
## ---------------------------------------------------------------------------------------------------------------------
        else:

            win = Tk(className=' Calculator Determinanti')
            win.geometry("+600+250")
            win.iconbitmap(tempFile)

            names = []

            for i in range(0, self.nr):
                names.append([])
                for j in range(0, self.nr):
                    names[i].append(Entry(win, width=3, borderwidth=2, font="Times 16", justify="center"))
                    names[i][j].grid(row=i, column=j, ipady=10, ipadx=15)

            def back():
                win.destroy()
                determ()

            def on_closing():
                os.remove(tempFile)
                win.destroy()

            def calc_():
                if self.nr == 2:
                    a1 = float(names[0][0].get().replace(',', '.'))
                    a2 = float(names[0][1].get().replace(',', '.'))
                    a3 = float(names[1][0].get().replace(',', '.'))
                    a4 = float(names[1][1].get().replace(',', '.'))

                    final_rez = DETERM.calc_nr_2(self, a1, a2, a3, a4)

                    final_rezult = Label(win, text="Rezultatul:", font="Helvetica 20")
                    final_rezult_num = Label(win, text=str(final_rez), font="Helvetica 25")
                    final_rezult.grid(row=0, column=self.nr)
                    final_rezult_num.grid(row=1, column=self.nr, columnspan=self.nr-1)
                if self.nr == 3:
                    a1 = float(names[0][0].get().replace(',', '.'))
                    a2 = float(names[0][1].get().replace(',', '.'))
                    a3 = float(names[0][2].get().replace(',', '.'))
                    a4 = float(names[1][0].get().replace(',', '.'))
                    a5 = float(names[1][1].get().replace(',', '.'))
                    a6 = float(names[1][2].get().replace(',', '.'))
                    a7 = float(names[2][0].get().replace(',', '.'))
                    a8 = float(names[2][1].get().replace(',', '.'))
                    a9 = float(names[2][2].get().replace(',', '.'))

                    final_rez = DETERM.calc_nr_3(self, a1, a2, a3, a4, a5, a6, a7, a8, a9)

                    final_rezult = Label(win, text="Rezultatul:", font="Helvetica 20")
                    final_rezult_num = Label(win, text=str(final_rez), font="Helvetica 25")
                    final_rezult.grid(row=0, column=self.nr)
                    final_rezult_num.grid(row=1, column=self.nr, columnspan=self.nr-1)
                if self.nr == 4:
                    a1 = float(names[0][0].get().replace(',', '.'))
                    a2 = float(names[0][1].get().replace(',', '.'))
                    a3 = float(names[0][2].get().replace(',', '.'))
                    a4 = float(names[0][3].get().replace(',', '.'))
                    a5 = float(names[1][0].get().replace(',', '.'))
                    a6 = float(names[1][1].get().replace(',', '.'))
                    a7 = float(names[1][2].get().replace(',', '.'))
                    a8 = float(names[1][3].get().replace(',', '.'))
                    a9 = float(names[2][0].get().replace(',', '.'))
                    a10 = float(names[2][1].get().replace(',', '.'))
                    a11 = float(names[2][2].get().replace(',', '.'))
                    a12 = float(names[2][3].get().replace(',', '.'))
                    a13 = float(names[3][0].get().replace(',', '.'))
                    a14 = float(names[3][1].get().replace(',', '.'))
                    a15 = float(names[3][2].get().replace(',', '.'))
                    a16 = float(names[3][3].get().replace(',', '.'))

                    final_rez = DETERM.calc_nr_4(self, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16)

                    final_rezult = Label(win, text="Rezultatul:", font="Helvetica 20")
                    final_rezult_num = Label(win, text=str(final_rez), font="Helvetica 25")
                    final_rezult.grid(row=0, column=self.nr)
                    final_rezult_num.grid(row=1, column=self.nr, columnspan=self.nr-1)
                if self.nr == 5:
                    a1 = float(names[0][0].get().replace(',', '.'))
                    a2 = float(names[0][1].get().replace(',', '.'))
                    a3 = float(names[0][2].get().replace(',', '.'))
                    a4 = float(names[0][3].get().replace(',', '.'))
                    a5 = float(names[0][4].get().replace(',', '.'))
                    a6 = float(names[1][0].get().replace(',', '.'))
                    a7 = float(names[1][1].get().replace(',', '.'))
                    a8 = float(names[1][2].get().replace(',', '.'))
                    a9 = float(names[1][3].get().replace(',', '.'))
                    a10 = float(names[1][4].get().replace(',', '.'))
                    a11 = float(names[2][0].get().replace(',', '.'))
                    a12 = float(names[2][1].get().replace(',', '.'))
                    a13 = float(names[2][2].get().replace(',', '.'))
                    a14 = float(names[2][3].get().replace(',', '.'))
                    a15 = float(names[2][4].get().replace(',', '.'))
                    a16 = float(names[3][0].get().replace(',', '.'))
                    a17 = float(names[3][1].get().replace(',', '.'))
                    a18 = float(names[3][2].get().replace(',', '.'))
                    a19 = float(names[3][3].get().replace(',', '.'))
                    a20 = float(names[3][4].get().replace(',', '.'))
                    a21 = float(names[4][0].get().replace(',', '.'))
                    a22 = float(names[4][1].get().replace(',', '.'))
                    a23 = float(names[4][2].get().replace(',', '.'))
                    a24 = float(names[4][3].get().replace(',', '.'))
                    a25 = float(names[4][4].get().replace(',', '.'))

                    final_rez = DETERM.calc_nr_5(self, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25)

                    final_rezult = Label(win, text="Rezultatul:", font="Helvetica 20")
                    final_rezult_num = Label(win, text=str(final_rez), font="Helvetica 25")
                    final_rezult.grid(row=0, column=self.nr)
                    final_rezult_num.grid(row=1, column=self.nr, columnspan=self.nr-1)

            calc = Button(win, text="Calculeaza", comman=calc_)
            back_b = Button(win, text="Back", command=back)
            calc.grid(row=self.nr, column=0, columnspan=self.nr-1, sticky="nesw", ipady=10)
            back_b.grid(row=self.nr, column=self.nr-1, sticky="nesw", ipady=10)

            win.protocol("WM_DELETE_WINDOW", on_closing)

            win.mainloop()


    def calc_nr_2_c(self, a1, a2, a3, a4, b1, b2):

        main = a1 * a4 - a2 * a3
        first = b1 * a4 - a2 * b2
        second = a1 * b2 - b1 * a3
        final_rez_1 = first / main
        final_rez_2 = second / main
        return final_rez_1, final_rez_2

    def calc_nr_3_c(self, a1, a2, a3, a4, a5, a6, a7, a8, a9, b1, b2, b3):
        main = DETERM.calc_nr_3(self, a1, a2, a3, a4, a5, a6, a7, a8, a9)
        first = DETERM.calc_nr_3(self, b1, a2, a3, b2, a5, a6, b3, a8, a9)
        second = DETERM.calc_nr_3(self, a1, b1, a3, a4, b2, a6, a7, b3, a9)
        third = DETERM.calc_nr_3(self, a1, a2, b1, a4, a5, b2, a7, a8, b3)
        final_rez_1 = first / main
        final_rez_2 = second / main
        final_rez_3 = third / main
        return final_rez_1, final_rez_2, final_rez_3

    def calc_nr_4_c(self, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, b1, b2, b3, b4):
        main = DETERM.calc_nr_4(self, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16)
        first = DETERM.calc_nr_4(self, b1, a2, a3, a4, b2, a6, a7, a8, b3, a10, a11, a12, b4, a14, a15, a16)
        second = DETERM.calc_nr_4(self, a1, b1, a3, a4, a5, b2, a7, a8, a9, b3, a11, a12, a13, b4, a15, a16)
        third = DETERM.calc_nr_4(self, a1, a2, b1, a4, a5, a6, b2, a8, a9, a10, b3, a12, a13, a14, b4, a16)
        fourth = DETERM.calc_nr_4(self, a1, a2, a3, b1, a5, a6, a7, b2, a9, a10, a11, b3, a13, a14, a15, b4)
        final_rez_1 = first / main
        final_rez_2 = second / main
        final_rez_3 = third / main
        final_rez_4 = fourth / main
        return final_rez_1, final_rez_2, final_rez_3, final_rez_4

    def calc_nr_5_c(self, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, b1, b2, b3, b4, b5):
        main = DETERM.calc_nr_5(self, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25)
        first = DETERM.calc_nr_5(self, b1, a2, a3, a4, a5, b2, a7, a8, a9, a10, b3, a12, a13, a14, a15, b4, a17, a18, a19, a20, b5, a22, a23, a24, a25)
        second = DETERM.calc_nr_5(self, a1, b1, a3, a4, a5, a6, b2, a8, a9, a10, a11, b3, a13, a14, a15, a16, b4, a18, a19, a20, a21, b5, a23, a24, a25)
        third = DETERM.calc_nr_5(self, a1, a2, b1, a4, a5, a6, a7, b2, a9, a10, a11, a12, b3, a14, a15, a16, a17, b4, a19, a20, a21, a22, b5, a24, a25)
        fourth = DETERM.calc_nr_5(self, a1, a2, a3, b1, a5, a6, a7, a8, b2, a10, a11, a12, a13, b3, a15, a16, a17, a18, b4, a20, a21, a22, a23, b5, a25)
        fith = DETERM.calc_nr_5(self, a1, a2, a3, a4, b1, a6, a7, a8, a9, b2, a11, a12, a13, a14, b3, a16, a17, a18, a19, b4, a21, a22, a23, a24, b5)
        final_rez_1 = first / main
        final_rez_2 = second / main
        final_rez_3 = third / main
        final_rez_4 = fourth / main
        final_rez_5 = fith / main
        return final_rez_1, final_rez_2, final_rez_3, final_rez_4, final_rez_5

    def calc_nr_2(self, a1, a2, a3, a4):
        final = a1 * a4 - a2 * a3
        return final

    def calc_nr_3(self, a1, a2, a3, a4, a5, a6, a7, a8, a9):
        t = -1
        first = a1 * DETERM.calc_nr_2(self, a5, a6, a8, a9)
        second = a2 * t * DETERM.calc_nr_2(self, a4, a6, a7, a9)
        third = a3 * DETERM.calc_nr_2(self, a4, a5, a7, a8)
        return first + second + third

    def calc_nr_4(self, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16):
        t = -1
        first = a1 * DETERM.calc_nr_3(self, a6, a7, a8, a10, a11, a12, a14, a15, a16)
        second = a2 * t * DETERM.calc_nr_3(self, a5, a7, a8, a9, a11, a12, a13, a15, a16)
        third = a3 * DETERM.calc_nr_3(self, a5, a6, a8, a9, a10, a12, a13, a14, a16)
        fourth = a4 * t * DETERM.calc_nr_3(self, a5, a6, a7, a9, a10, a11, a13, a14, a15)
        return  first + second + third + fourth

    def calc_nr_5(self, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25):
        t = -1
        first = a1 * DETERM.calc_nr_4(self, a7, a8, a9, a10, a12, a13, a14, a15, a17, a18, a19, a20, a22, a23, a24, a25)
        second = a2 * t * DETERM.calc_nr_4(self, a6, a8, a9, a10, a11, a13, a14, a15, a16, a18, a19, a20, a21, a23, a24, a25)
        third = a3 * DETERM.calc_nr_4(self, a6, a7, a9, a10, a11, a12, a14, a15, a16, a17, a19, a20, a21, a22, a24, a25)
        fourth = a4 * t * DETERM.calc_nr_4(self, a6, a7, a8, a10, a11, a12, a13, a15, a16, a17, a18, a20, a21, a22, a23, a25)
        fith = a5 * DETERM.calc_nr_4(self, a6, a7, a8, a9, a11, a12, a13, a14, a16, a17, a18, a19, a21, a22, a23, a24)
        return first + second + third + fourth + fith

determ()