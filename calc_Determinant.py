from tkinter import *
import tkinter.messagebox



def determ():
    input_prompt = Tk(className=" Calc Derivate")
    input_prompt.geometry("300x100+600+250")

    mess = Label(input_prompt, text="Cate randuri/coloane are determinantul? \n{2 - 5}")
    qu = Entry(input_prompt, width=28, borderwidth=4, justify="center")
    nothing = Label(input_prompt, text="          ")

    nothing.grid(row=0, column=0)
    qu.grid(row=2, column=2)
    qu.insert(0, '2')
    mess.grid(row=0, column=2)

    def calc_make_try():
        try:
            nr = int(qu.get())
        except:
            return tkinter.messagebox.showerror(title="Error", message="Număr invalid!!!")
        if int(nr)>=2 and int(nr)<=5:
            input_prompt.destroy()
            if nr==2:
                return nr_2()
            elif nr==3:
                return nr_3()
            elif nr==4:
                return nr_4()
            else:
                return nr_5()
        else:
            return tkinter.messagebox.showerror(title="Error", message="Număr invalid!!!")
    finish = Button(input_prompt, text="Continue", activebackground="grey", width=25, command=calc_make_try)
    finish.grid(row=3, column=2)

    input_prompt.mainloop()



def nr_2():
    root = Tk(className=' Calculator Determinanti')
    root.geometry("350x165+600+250")

    a11 = Entry(root, width=3, borderwidth=2,font="Times 16", justify="center")
    a12 = Entry(root, width=3, borderwidth=2,font="Times 16", justify="center")
    a21 = Entry(root, width=3, borderwidth=2,font="Times 16", justify="center")
    a22 = Entry(root, width=3, borderwidth=2,font="Times 16", justify="center")



    a11.grid(row=0, column=0, ipady=10, ipadx=15)
    a12.grid(row=0, column=1, ipady=10, ipadx=15)
    a21.grid(row=1, column=0, ipady=10, ipadx=15)
    a22.grid(row=1, column=1, ipady=10, ipadx=15)


    def back():
        root.destroy()
        determ()
    def nr_2_calc():
        try:
            a_11 = float(a11.get())
            a_12 = float(a12.get())
            a_21 = float(a21.get())
            a_22 = float(a22.get())
        except:
            m11 = a11.get().replace(',','.')
            m12 = a12.get().replace(',', '.')
            m21 = a21.get().replace(',', '.')
            m22 = a22.get().replace(',', '.')
            a_11 = float(m11)
            a_12 = float(m12)
            a_21 = float(m21)
            a_22 = float(m22)

        final_num = a_11*a_22-a_12*a_21
        final_rezult = Label(root, text="Rezultatul:", font="Helvetica 20")
        final_rezult_num = Label(root, text=str(final_num), font="Helvetica 25")
        final_rezult.grid(row=0,column=3,columnspan=2)
        final_rezult_num.grid(row=1, column=3, columnspan=2, rowspan=2)
    fin = Button(root, text="Calculeaza", command=nr_2_calc, activebackground="grey")
    back = Button(root, text="Back", command=back)
    back.grid(row=3, column=3, ipady=20, ipadx=88, columnspan=2)
    fin.grid(row=3,column=0, ipady=20, ipadx=34, columnspan=2)
    root.mainloop()

def nr_3():
    root = Tk(className=' Calculator Determinanti')
    root.geometry("400x215+600+250")


    a11 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a12 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a13 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a21 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a22 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a23 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a31 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a32 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a33 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")

    a11.grid(row=0, column=0, ipady=10, ipadx=15)
    a12.grid(row=0, column=1, ipady=10, ipadx=15)
    a13.grid(row=0, column=2, ipady=10, ipadx=15)
    a21.grid(row=1, column=0, ipady=10, ipadx=15)
    a22.grid(row=1, column=1, ipady=10, ipadx=15)
    a23.grid(row=1, column=2, ipady=10, ipadx=15)
    a31.grid(row=2, column=0, ipady=10, ipadx=15)
    a32.grid(row=2, column=1, ipady=10, ipadx=15)
    a33.grid(row=2, column=2, ipady=10, ipadx=15)

    def back():
        root.destroy()
        determ()
    def nr_3_calc():
        try:
            a_11 = float(a11.get())
            a_12 = float(a12.get())
            a_13 = float(a13.get())
            a_21 = float(a21.get())
            a_22 = float(a22.get())
            a_23 = float(a23.get())
            a_31 = float(a31.get())
            a_32 = float(a32.get())
            a_33 = float(a33.get())
        except:
            m11 = a11.get().replace(',', '.')
            m12 = a12.get().replace(',', '.')
            m13 = a13.get().replace(',', '.')
            m21 = a21.get().replace(',', '.')
            m22 = a22.get().replace(',', '.')
            m23 = a23.get().replace(',', '.')
            m31 = a31.get().replace(',', '.')
            m32 = a32.get().replace(',', '.')
            m33 = a33.get().replace(',', '.')
            a_11 = float(m11)
            a_12 = float(m12)
            a_13 = float(m13)
            a_21 = float(m21)
            a_22 = float(m22)
            a_23 = float(m23)
            a_31 = float(m31)
            a_32 = float(m32)
            a_33 = float(m33)

        final_num = a_11*a_22*a_33+a_12*a_23*a_31+a_13*a_21*a_32-a_13*a_22*a_31-a_11*a_23*a_32-a_12*a_21*a_33
        final_rezult = Label(root, text="Rezultatul:", font="Helvetica 20")
        final_rezult_num = Label(root, text=str(final_num), font="Helvetica 25")
        final_rezult.grid(row=0, column=3, columnspan=2)
        final_rezult_num.grid(row=1, column=4, columnspan=2, rowspan=2)

    fin = Button(root, text="Calculeaza", command=nr_3_calc, activebackground="grey")
    back = Button(root, text="Back", command=back)
    back.grid(row=3, column=4, ipady=20, ipadx=78, columnspan=3)
    fin.grid(row=3, column=0, ipady=20, ipadx=70, columnspan=3)
    root.mainloop()
def nr_4():
    root = Tk(className=' Calculator Determinanti')
    root.geometry("500x265+600+250")

    a11 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a12 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a13 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a14 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a21 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a22 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a23 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a24 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a31 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a32 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a33 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a34 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a41 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a42 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a43 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a44 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")

    a11.grid(row=0, column=0, ipady=10, ipadx=15)
    a12.grid(row=0, column=1, ipady=10, ipadx=15)
    a13.grid(row=0, column=2, ipady=10, ipadx=15)
    a14.grid(row=0, column=3, ipady=10, ipadx=15)
    a21.grid(row=1, column=0, ipady=10, ipadx=15)
    a22.grid(row=1, column=1, ipady=10, ipadx=15)
    a23.grid(row=1, column=2, ipady=10, ipadx=15)
    a24.grid(row=1, column=3, ipady=10, ipadx=15)
    a31.grid(row=2, column=0, ipady=10, ipadx=15)
    a32.grid(row=2, column=1, ipady=10, ipadx=15)
    a33.grid(row=2, column=2, ipady=10, ipadx=15)
    a34.grid(row=2, column=3, ipady=10, ipadx=15)
    a41.grid(row=3, column=0, ipady=10, ipadx=15)
    a42.grid(row=3, column=1, ipady=10, ipadx=15)
    a43.grid(row=3, column=2, ipady=10, ipadx=15)
    a44.grid(row=3, column=3, ipady=10, ipadx=15)

    def back():
        root.destroy()
        determ()
    def nr_4_calc():
        try:
            a_11 = float(a11.get())
            a_12 = float(a12.get())
            a_13 = float(a13.get())
            a_14 = float(a14.get())
            a_21 = float(a21.get())
            a_22 = float(a22.get())
            a_23 = float(a23.get())
            a_24 = float(a24.get())
            a_31 = float(a31.get())
            a_32 = float(a32.get())
            a_33 = float(a33.get())
            a_34 = float(a34.get())
            a_41 = float(a41.get())
            a_42 = float(a42.get())
            a_43 = float(a43.get())
            a_44 = float(a44.get())
        except:
            m11 = a11.get().replace(',', '.')
            m12 = a12.get().replace(',', '.')
            m13 = a13.get().replace(',', '.')
            m14 = a14.get().replace(',', '.')
            m21 = a21.get().replace(',', '.')
            m22 = a22.get().replace(',', '.')
            m23 = a23.get().replace(',', '.')
            m24 = a24.get().replace(',', '.')
            m31 = a31.get().replace(',', '.')
            m32 = a32.get().replace(',', '.')
            m33 = a33.get().replace(',', '.')
            m34 = a34.get().replace(',', '.')
            m41 = a41.get().replace(',', '.')
            m42 = a42.get().replace(',', '.')
            m43 = a43.get().replace(',', '.')
            m44 = a44.get().replace(',', '.')
            a_11 = float(m11)
            a_12 = float(m12)
            a_13 = float(m13)
            a_14 = float(m14)
            a_21 = float(m21)
            a_22 = float(m22)
            a_23 = float(m23)
            a_24 = float(m24)
            a_31 = float(m31)
            a_32 = float(m32)
            a_33 = float(m33)
            a_34 = float(m34)
            a_41 = float(m41)
            a_42 = float(m42)
            a_43 = float(m43)
            a_44 = float(m44)

        t = -1
        first = a_11*(a_22*a_33*a_44 + a_23*a_34*a_42 + a_24*a_32*a_43 - a_24*a_33*a_42 - a_23*a_32*a_44 - a_22*a_34*a_43)
        second = a_12*t*(a_21*a_33*a_44 + a_23*a_34*a_41 + a_24*a_31*a_43 - a_24*a_33*a_41 - a_23*a_31*a_44 - a_21*a_34*a_43)
        third = a_13*(a_21*a_32*a_44 + a_22*a_34*a_41 + a_24*a_31*a_42 - a_24*a_32*a_41 - a_22*a_31*a_44 - a_21*a_34*a_42)
        fourth = a_14*t*(a_21*a_32*a_43 + a_22*a_33*a_41 + a_23*a_31*a_42 - a_23*a_32*a_41 - a_22*a_31*a_43 - a_21*a_33*a_42)

        final_num = first + second + third + fourth
        final_rezult = Label(root, text="Rezultatul:", font="Helvetica 20")
        final_rezult_num = Label(root, text=str(final_num), font="Helvetica 25")
        final_rezult.grid(row=0, column=4, columnspan=3, rowspan=2)
        final_rezult_num.grid(row=2, column=5, columnspan=3, rowspan=2)

    fin = Button(root, text="Calculeaza", command=nr_4_calc, activebackground="grey")
    back = Button(root, text="Back", command=back)
    back.grid(row=4, column=6, ipady=20, ipadx=92, columnspan=3)
    fin.grid(row=4, column=0, ipady=20, ipadx=106, columnspan=4)
    root.mainloop()

def nr_5():
    root = Tk(className=' Calculator Determinanti')
    root.geometry("700x312+600+250")

    a11 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a12 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a13 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a14 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a15 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a21 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a22 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a23 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a24 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a25 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a31 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a32 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a33 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a34 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a35 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a41 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a42 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a43 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a44 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a45 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a51 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a52 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a53 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a54 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")
    a55 = Entry(root, width=3, borderwidth=2, font="Times 16", justify="center")

    a11.grid(row=0, column=0, ipady=10, ipadx=15)
    a12.grid(row=0, column=1, ipady=10, ipadx=15)
    a13.grid(row=0, column=2, ipady=10, ipadx=15)
    a14.grid(row=0, column=3, ipady=10, ipadx=15)
    a15.grid(row=0, column=4, ipady=10, ipadx=15)
    a21.grid(row=1, column=0, ipady=10, ipadx=15)
    a22.grid(row=1, column=1, ipady=10, ipadx=15)
    a23.grid(row=1, column=2, ipady=10, ipadx=15)
    a24.grid(row=1, column=3, ipady=10, ipadx=15)
    a25.grid(row=1, column=4, ipady=10, ipadx=15)
    a31.grid(row=2, column=0, ipady=10, ipadx=15)
    a32.grid(row=2, column=1, ipady=10, ipadx=15)
    a33.grid(row=2, column=2, ipady=10, ipadx=15)
    a34.grid(row=2, column=3, ipady=10, ipadx=15)
    a35.grid(row=2, column=4, ipady=10, ipadx=15)
    a41.grid(row=3, column=0, ipady=10, ipadx=15)
    a42.grid(row=3, column=1, ipady=10, ipadx=15)
    a43.grid(row=3, column=2, ipady=10, ipadx=15)
    a44.grid(row=3, column=3, ipady=10, ipadx=15)
    a45.grid(row=3, column=4, ipady=10, ipadx=15)
    a51.grid(row=4, column=0, ipady=10, ipadx=15)
    a52.grid(row=4, column=1, ipady=10, ipadx=15)
    a53.grid(row=4, column=2, ipady=10, ipadx=15)
    a54.grid(row=4, column=3, ipady=10, ipadx=15)
    a55.grid(row=4, column=4, ipady=10, ipadx=15)


    def back():
        root.destroy()
        determ()

    def nr_4_calc():
        a_11 = float(a11.get().replace(',', '.'))
        a_12 = float(a12.get().replace(',', '.'))
        a_13 = float(a13.get().replace(',', '.'))
        a_14 = float(a14.get().replace(',', '.'))
        a_15 = float(a15.get().replace(',', '.'))
        a_21 = float(a21.get().replace(',', '.'))
        a_22 = float(a22.get().replace(',', '.'))
        a_23 = float(a23.get().replace(',', '.'))
        a_24 = float(a24.get().replace(',', '.'))
        a_25 = float(a25.get().replace(',', '.'))
        a_31 = float(a31.get().replace(',', '.'))
        a_32 = float(a32.get().replace(',', '.'))
        a_33 = float(a33.get().replace(',', '.'))
        a_34 = float(a34.get().replace(',', '.'))
        a_35 = float(a35.get().replace(',', '.'))
        a_41 = float(a41.get().replace(',', '.'))
        a_42 = float(a42.get().replace(',', '.'))
        a_43 = float(a43.get().replace(',', '.'))
        a_44 = float(a44.get().replace(',', '.'))
        a_45 = float(a45.get().replace(',', '.'))
        a_51 = float(a51.get().replace(',', '.'))
        a_52 = float(a52.get().replace(',', '.'))
        a_53 = float(a53.get().replace(',', '.'))
        a_54 = float(a54.get().replace(',', '.'))
        a_55 = float(a55.get().replace(',', '.'))


        t = -1
        first = a_11 * nr_5_formula(a_22, a_23, a_24, a_25, a_32, a_33, a_34, a_35, a_42, a_43, a_44, a_45, a_52, a_53, a_54, a_55)
        second = a_12 * t * nr_5_formula(a_21, a_23, a_24, a_25, a_31, a_33, a_34, a_35, a_41, a_43, a_44, a_45, a_51, a_53, a_54, a_55)
        third = a_13 * nr_5_formula(a_21, a_22, a_24, a_25, a_31, a_32, a_34, a_35, a_41, a_42, a_44, a_45, a_51, a_52, a_54, a_55)
        fourth = a_14 * t * nr_5_formula(a_21, a_22, a_23, a_25, a_31, a_32, a_33, a_35, a_41, a_42, a_43, a_45, a_51, a_52, a_53, a_55)
        fith = a_15* nr_5_formula(a_21, a_22, a_23, a_24, a_31, a_32, a_33, a_34, a_41, a_42, a_43, a_44, a_51, a_52, a_53, a_54)

        final_num = first + second + third + fourth + fith
        final_rezult = Label(root, text="Rezultatul:", font="Helvetica 20")
        final_rezult_num = Label(root, text=str(final_num), font="Helvetica 25")
        final_rezult.grid(row=0, column=5, columnspan=3, rowspan=2)
        final_rezult_num.grid(row=3, column=6, columnspan=3, rowspan=2)

    fin = Button(root, text="Calculeaza", command=nr_4_calc, activebackground="grey")
    back = Button(root, text="Back", command=back)
    back.grid(row=5, column=6, ipady=20, ipadx=159, columnspan=3)
    fin.grid(row=5, column=0, ipady=20, ipadx=138, columnspan=5)
    root.mainloop()

def nr_5_formula(a_11, a_12, a_13, a_14, a_21, a_22, a_23, a_24, a_31, a_32, a_33, a_34, a_41, a_42, a_43, a_44):
    t=-1
    first = a_11 * (a_22 * a_33 * a_44 + a_23 * a_34 * a_42 + a_24 * a_32 * a_43 - a_24 * a_33 * a_42 - a_23 * a_32 * a_44 - a_22 * a_34 * a_43)
    second = a_12 * t * (a_21 * a_33 * a_44 + a_23 * a_34 * a_41 + a_24 * a_31 * a_43 - a_24 * a_33 * a_41 - a_23 * a_31 * a_44 - a_21 * a_34 * a_43)
    third = a_13 * (a_21 * a_32 * a_44 + a_22 * a_34 * a_41 + a_24 * a_31 * a_42 - a_24 * a_32 * a_41 - a_22 * a_31 * a_44 - a_21 * a_34 * a_42)
    fourth = a_14 * t * (a_21 * a_32 * a_43 + a_22 * a_33 * a_41 + a_23 * a_31 * a_42 - a_23 * a_32 * a_41 - a_22 * a_31 * a_43 - a_21 * a_33 * a_42)
    return first + second + third + fourth

determ()