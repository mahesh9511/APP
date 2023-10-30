from tkinter import *

main_window = Tk()
main_window.geometry('1920x1080')

#backimagespip
b = PhotoImage(file="ff5.png")
b_b = Label(main_window, image=b)
b_b.place(x=0.5,y=0.5)

#Frame in Main_window
def login_new():

    #Creating Frame
    f1=Frame(bg="black")
    f1.place(relx=0.352, rely=0.215, width=520, height=500)

    #Lable
    user = Label(f1, text="User ID:", font=('Comic Sans MS', 16),bg="black",fg="white")
    pwd = Label(f1, text="Password:", font=('Comic Sans MS', 16),bg="black",fg="white")
    sen1 = Label(f1, text="Login Information", font=('Merlin', 20), bg='black', fg='white')

    user.place(relx=0.145, rely=0.3, anchor=CENTER)
    pwd.place(relx=0.145, rely=0.4, anchor=CENTER)
    sen1.place(relx=0.52, rely=0.1, anchor=CENTER)


    # Entry
    user_entry = Entry(f1, width=20, font=('Merlin', 16))
    pwd_entry = Entry(f1, width=20, show='*', font=('Merlin', 16))

    user_entry.place(relx=0.6, rely=0.3, anchor=CENTER)
    pwd_entry.place(relx=0.6, rely=0.4, anchor=CENTER)

    #Function for destroying Frame
    def clear_frame():
        f1.destroy()

    def farmer_entry():
        user_inp = user_entry.get()
        pwd_inp = pwd_entry.get()

        if user_inp != '' and pwd_inp != '':
            print(user_inp, pwd_inp)
            farmerh2()
        else:
            invalid = Label(f1, text="Enter valid input", font=('Merlin', 20), bg='black', fg='red')
            invalid.place(relx=0.5, rely=0.7, anchor=CENTER)

    def consumer_entry():
        user_inp = user_entry.get()
        pwd_inp = pwd_entry.get()

        if user_inp != '' and pwd_inp != '':
            print(user_inp, pwd_inp)
            consumerh()
        else:
            invalid = Label(f1, text="Enter valid input", font=('Merlin', 20), bg='black', fg='red')
            invalid.place(relx=0.5, rely=0.7, anchor=CENTER)


    #Button
    cus = Button(f1, text="Farmer Login", font=('Merlin', 16), bg='red',command=farmer_entry)
    cus.place(relx=0.8, rely=0.55, anchor=CENTER)
    don = Button(f1, text="Customer Login", font=('Merlin', 16), bg='red', command=consumer_entry)
    don.place(relx=0.2, rely=0.55, anchor=CENTER)
    out1 = Button(f1, text="Home", font=('Merlin', 16), bg='red', command=clear_frame)
    out1.place(relx=0.09, rely=0.05, anchor=CENTER)





def sign_up():

    f2=Frame(bg="black")
    f2.place(relx=0.352,rely=0.215,width=520,height=500)




    #lable
    ee = Label(f2, text="Customer and Farmer Sign Up", font=('Merlin', 20), bg='black', fg='white')
    ee.place(relx=0.54, rely=0.05, anchor=CENTER)


    qq = Label(f2, text="User ID:", font=('Merlin', 16), bg='black',fg='white')
    pwd = Label(f2, text="Password:", font=('Merlin', 16), bg='black',fg='white')
    ww = Label(f2, text="Phone No:", font=('Merlin', 16), bg='black',fg='white')
    tt = Label(f2, text="Address:", font=('Merlin', 16), bg='black',fg='white')
    yy = Label(f2, text="Mail ID:", font=('Merlin', 16), bg='black',fg='white')
    mm = Label(f2, text="Pin code:", font=('Merlin', 16), bg='black',fg='white')



    qq.place(relx=0.28, rely=0.2, anchor=CENTER)
    ww.place(relx=0.28, rely=0.4, anchor=CENTER)
    tt.place(relx=0.28, rely=0.5, anchor=CENTER)
    yy.place(relx=0.28, rely=0.7, anchor=CENTER)
    pwd.place(relx=0.28, rely=0.3, anchor=CENTER)
    mm.place(relx=0.28, rely=0.6, anchor=CENTER)


    #customer entry
    qq_entry = Entry(f2, width=15, font=('Merlin', 16))
    ww_entry = Entry(f2, width=15, font=('Merlin', 16))
    rr_entry = Entry(f2, width=15, font=('Merlin', 16))
    tt_entry = Entry(f2, width=15, font=('Merlin', 16))
    yy_entry = Entry(f2, width=15, font=('Merlin', 16))
    pwd_entry = Entry(f2, width=15, font=('Merlin', 16))



    qq_entry.place(relx=0.65, rely=0.3, anchor=CENTER)
    ww_entry.place(relx=0.65, rely=0.4, anchor=CENTER)
    tt_entry.place(relx=0.65, rely=0.5, anchor=CENTER)
    rr_entry.place(relx=0.65, rely=0.6, anchor=CENTER)
    yy_entry.place(relx=0.65, rely=0.7, anchor=CENTER)
    pwd_entry.place(relx=0.65, rely=0.2, anchor=CENTER)

    def haii1():
        f2.destroy()


    def clear_frame():
        f2.destroy()


    def check1():
        qq_inp = qq_entry.get()
        ww_inp = ww_entry.get()
        tt_inp = tt_entry.get()
        rr_inp = rr_entry.get()
        yy_inp = yy_entry.get()
        pwd_inp = pwd_entry.get()

        if qq_inp != '' and ww_inp != '' and tt_inp != '' and rr_inp != '' and yy_inp != ''  and pwd_inp != '':
            verify_phone()
            verify_mail()

        else:
            invalid = Label(f2, text="Enter valid input", font=('Merlin', 15), bg='black', fg='red')
            invalid.place(relx=0.5, rely=0.96, anchor=CENTER)


    def verify_phone():
        ww_inp = ww_entry.get()
        if ww_inp.isdigit() and len(ww_inp) == 10:
            haii1()
        else:
            invalid2 = Label(f2, text="Enter valid mobile number", font=('Merlin', 15), bg='black', fg='red')
            invalid2.place(relx=0.25, rely=0.9, anchor=CENTER)

    def verify_mail():
        yy_inp = yy_entry.get()
        if '@' and '.' in yy_inp:
            haii1()
        else:
            invalid2 = Label(f2, text="Enter valid mail", font=('Merlin', 15), bg='black', fg='red')
            invalid2.place(relx=0.8, rely=0.9, anchor=CENTER)


    def check2():
        qq_inp = qq_entry.get()
        ww_inp = ww_entry.get()
        tt_inp = tt_entry.get()
        rr_inp = rr_entry.get()
        yy_inp = yy_entry.get()
        pwd_inp = pwd_entry.get()

        if qq_inp != '' and ww_inp != '' and tt_inp != '' and rr_inp != '' and yy_inp != '' and pwd_inp != '':

            verify_phone()
            verify_mail()
        else:
            invalid = Label(f2, text="Enter valid input", font=('Merlin', 15), bg='black', fg='red')
            invalid.place(relx=0.5, rely=0.96, anchor=CENTER)



    #Button
    out1 = Button(f2, text="Home", font=('Merlin', 16), bg='red', command=clear_frame)
    out1.place(relx=0.07, rely=0.05, anchor=CENTER)

    sid_s = Button(f2, text="Customer Sign Up", font=('Merlin', 16), bg="red",command=check1)
    sid_s.place(relx=0.75, rely=0.83, anchor=CENTER)

    sid_ss = Button(f2, text="Farmer Sign Up", font=('Merlin', 16), bg="red",command=check2)
    sid_ss.place(relx=0.25, rely=0.83, anchor=CENTER)





def consumerh():
    main_window.destroy()

    main_window2 = Tk()

    main_window2.geometry('1920x1080')

    # Packages
    bk = PhotoImage(file="consumerh1.png")
    bk_b = Label(main_window2, image=bk)
    bk_b.place(x=0.5, y=0.5)


    def clear_window1():
        main_window2.destroy()
        consumerh1()

    def clear_window2():
        main_window2.destroy()
        consumerh6()


    # Buttons
    cus = Button(main_window2, text="Proceed", font=('Merlin', 16), bg='green',command=clear_window1)
    cus.place(relx=0.7, rely=0.54, anchor=CENTER)

    cus = Button(main_window2, text="More", font=('Merlin', 16), bg='green',command=conmorh)
    cus.place(relx=0.63, rely=0.44, anchor=CENTER)

    cus = Button(main_window2, text="Buy", font=('Merlin', 16), bg='green',command=clear_window2)
    cus.place(relx=0.7, rely=0.44, anchor=CENTER)

    main_window2.mainloop()

def conmorh():

    f2=Frame(bg="sky blue")
    f2.place(relx=0.3,rely=0.215,width=500,height=500)

    #lable
    qq = Label(f2, text="Vegetable's Included", font=('Comic Sans MS', 20), bg='Red')
    pwd = Label(f2, text="Tomato - 1kg", font=('Comic Sans MS', 16), bg='sky blue')
    ww = Label(f2, text="Potato - 2kg", font=('Comic Sans MS', 16), bg='sky blue')
    tt = Label(f2, text="onion - 3kg", font=('Comic Sans MS', 16), bg='sky blue')
    yy = Label(f2, text="Carrot - 0.5kg", font=('Comic Sans MS', 16), bg='sky blue')
    mm = Label(f2, text="Brinjal - 1kg", font=('Comic Sans MS', 16), bg='sky blue')
    nn = Label(f2, text="Beans - 1kg", font=('Comic Sans MS', 16), bg='sky blue')
    lla = Label(f2, text="Total Price - 150", font=('Comic Sans MS', 16), bg='red')

    qq.place(relx=0.5, rely=0.2, anchor=CENTER)
    ww.place(relx=0.5, rely=0.4, anchor=CENTER)
    tt.place(relx=0.5, rely=0.5, anchor=CENTER)
    yy.place(relx=0.5, rely=0.7, anchor=CENTER)
    pwd.place(relx=0.5, rely=0.3, anchor=CENTER)
    mm.place(relx=0.5, rely=0.6, anchor=CENTER)
    nn.place(relx=0.5, rely=0.8, anchor=CENTER)
    lla.place(relx=0.2, rely=0.9, anchor=CENTER)
    def clear_frame():
        f2.destroy()

    #Button
    out1 = Button(f2, text="Home", font=('Merlin', 16), bg='red', command=clear_frame)
    out1.place(relx=0.09, rely=0.05, anchor=CENTER)


def consumerh6():
    main_window8 = Tk()

    main_window8.geometry('1920x1080')

    # Packages
    bk = PhotoImage(file="consumerh4.png")
    bk_b = Label(main_window8, image=bk)
    bk_b.place(x=0.5, y=0.5)


    def clear_window():
        main_window8.destroy()

    # Buttons
    cus = Button(main_window8, text="Close", font=('Merlin', 16), bg='green', command=clear_window)
    cus.place(relx=0.7, rely=0.7, anchor=CENTER)

    main_window8.mainloop()




def consumerh3():
    main_window7 = Tk()

    main_window7.geometry('1920x1080')

    # Packages
    bk = PhotoImage(file="consumerh4.png")
    bk_b = Label(main_window7, image=bk)
    bk_b.place(x=0.5, y=0.5)

    def clear_window():
        main_window7.destroy()


    # Buttons
    cus = Button(main_window7, text="Close", font=('Merlin', 16), bg='green', command=clear_window)
    cus.place(relx=0.7, rely=0.7, anchor=CENTER)



    main_window7.mainloop()

def consumerhh():

    main_window2 = Tk()

    main_window2.geometry('1920x1080')

    # Packages
    bk = PhotoImage(file="consumerh1.png")
    bk_b = Label(main_window2, image=bk)
    bk_b.place(x=0.5, y=0.5)


    def clear_window1():
        main_window2.destroy()
        consumerh1()

    def clear_window12():
        main_window2.destroy()
        consumerh3()

    # Buttons
    cus = Button(main_window2, text="Proceed", font=('Merlin', 16), bg='green',command=clear_window1)
    cus.place(relx=0.7, rely=0.54, anchor=CENTER)

    cus = Button(main_window2, text="More", font=('Merlin', 16), bg='green',command=conmorh)
    cus.place(relx=0.63, rely=0.44, anchor=CENTER)

    cus = Button(main_window2, text="Buy", font=('Merlin', 16), bg='green',command=clear_window12)
    cus.place(relx=0.7, rely=0.44, anchor=CENTER)

    main_window2.mainloop()


def consumerh1():

    main_window3 = Tk()

    main_window3.geometry('1920x1080')

    # Packages
    bk = PhotoImage(file="consumerh2.png")
    bk_b = Label(main_window3, image=bk)
    bk_b.place(x=0.5, y=0.5)

    def frame1():
        f1 = Frame(bg="Black")
        f1.place(relx=0.320, rely=0.055, width=740, height=900)

        gg = Label(f1, text="Tomato", bg="black", fg="white", font=('Merlin', 16))
        gg.place(relx=0.43, rely=0.175)

        cc = Label(f1, text="Scientific name :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.3)

        cc = Label(f1, text="Solanum lycopersicum", bg="black", fg="white", font=('Merlin', 10))
        cc.place(relx=0.3, rely=0.3)

        cc = Label(f1, text="Calories(in 100g) :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.4)

        cc = Label(f1, text="18 calories", bg="black", fg="white", font=('Merlin', 10))
        cc.place(relx=0.3, rely=0.4)

        cc = Label(f1, text="Recepies :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.7)

        cc = Label(f1, text="Tomato chutney ,Tomato soup ,Tomato rice ,Tomato sauce ", bg="black", fg="white",
                   font=('Merlin', 10))
        cc.place(relx=0.3, rely=0.7)

        cc = Label(f1, text="Cost(for 1 kilogram) :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.8)

        cc = Label(f1, text="Rs.20", bg="black", fg="white", font=('Merlin', 10))
        cc.place(relx=0.3, rely=0.8)

        cc = Label(f1, text="Health benefits :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.52)

        hh = Label(f1,
                   text="The fiber, potassium, vitamin C, and choline content in tomatoes all support heart health.\n An increase in potassium intake, along with a decrease in sodium intake, is the most important\ndietary change the average person can make to reduce their risk of cardiovascular disease.",
                   bg="black", fg="white", font=('Merlin', 10))
        hh.place(relx=0.15, rely=0.57)

        def close():
            f1.destroy()

        close = Button(f1, text="close", command=close)
        close.place(relx=0.1, rely=0.085, anchor=CENTER)

    def frame2():
        f2 = Frame(bg="Black")
        f2.place(relx=0.320, rely=0.055, width=740, height=900)

        gg = Label(f2, text="Potato", bg="black", fg="white", font=('Merlin', 16))
        gg.place(relx=0.43, rely=0.175)

        cc = Label(f2, text="Scientific name :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.3)

        cc = Label(f2, text="Solanum tuberosum", bg="black", fg="white", font=('Merlin', 10))
        cc.place(relx=0.3, rely=0.3)

        cc = Label(f2, text="Calories(in 100g) :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.4)

        cc = Label(f2, text="77 calories", bg="black", fg="white", font=('Merlin', 10))
        cc.place(relx=0.3, rely=0.4)

        cc = Label(f2, text="Health benefits :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.5)

        hh = Label(f2,
                   text="Potatoes are a good source of fiber, which can help you lose weight by keeping you full longer.\nFiber can help prevent heart disease by keeping cholesterol and blood sugar levels in check.\nPotatoes are also full of antioxidants that work to prevent diseases\nand vitamins that help your body function properly.",
                   bg="black", fg="white", font=('Merlin', 10))
        hh.place(relx=0.15, rely=0.540)

        cc = Label(f2, text="Recepies :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.66)

        cc = Label(f2,
                   text="Air Fryer Crispy Potatoes,Loaded Slow-Cooker Potatoes,Fried Mashed Potato Balls,\nOven-Fried Pickle Potato Chips",
                   bg="black", fg="white", font=('Merlin', 10))
        cc.place(relx=0.15, rely=0.7)

        cc = Label(f2, text="Cost(for 1 kilograms) :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.8)

        cc = Label(f2, text="Rs.20", bg="black", fg="white", font=('Merlin', 10))
        cc.place(relx=0.3, rely=0.8)

        def close():
            f2.destroy()

        close = Button(f2, text="close", command=close)
        close.place(relx=0.1, rely=0.085, anchor=CENTER)

    def frame3():
        f3 = Frame(bg="Black")
        f3.place(relx=0.320, rely=0.055, width=740, height=900)

        gg = Label(f3, text="Onion", bg="black", fg="white", font=('Merlin', 16))
        gg.place(relx=0.43, rely=0.175)

        cc = Label(f3, text="Scientific name :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.3)

        cc = Label(f3, text="Allium cepa", bg="black", fg="white", font=('Merlin', 10))
        cc.place(relx=0.3, rely=0.3)

        cc = Label(f3, text="Calories(in 100g) :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.4)

        cc = Label(f3, text="40 calories", bg="black", fg="white", font=('Merlin', 10))
        cc.place(relx=0.3, rely=0.4)

        cc = Label(f3, text="Health benefits :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.5)

        hh = Label(f3,
                   text="Onions contain antioxidants and compounds that fight inflammation, decrease triglycerides and\nreduce cholesterol levels — all of which may lower heart disease risk. Their potent\nanti-inflammatory properties may also help reduce high blood pressure and protect against blood clots",
                   bg="black", fg="white", font=('Merlin', 10))
        hh.place(relx=0.15, rely=0.540)

        cc = Label(f3, text="Recepies :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.72)

        cc = Label(f3, text="Cheese Onion Omelette,French Onion Soup,Onion Marmalade,Onion Rings", bg="black",
                   fg="white", font=('Merlin', 10))
        cc.place(relx=0.3, rely=0.72)

        cc = Label(f3, text="Cost(for 1 kilograms) :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.8)

        cc = Label(f3, text="Rs.30", bg="black", fg="white", font=('Merlin', 10))
        cc.place(relx=0.3, rely=0.8)

        def close():
            f3.destroy()

        close = Button(f3, text="close", command=close)
        close.place(relx=0.1, rely=0.085, anchor=CENTER)

    def frame4():
        f4 = Frame(bg="Black")
        f4.place(relx=0.320, rely=0.055, width=740, height=900)

        gg = Label(f4, text="Carrot", bg="black", fg="white", font=('Merlin', 16))
        gg.place(relx=0.43, rely=0.175)

        cc = Label(f4, text="Scientific name :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.3)

        cc = Label(f4, text="Daucus carota subsp. sativus", bg="black", fg="white", font=('Merlin', 10))
        cc.place(relx=0.3, rely=0.3)

        cc = Label(f4, text="Calories(in 100g) :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.4)

        cc = Label(f4, text="41 calories", bg="black", fg="white", font=('Merlin', 10))
        cc.place(relx=0.3, rely=0.4)

        cc = Label(f4, text="Health benefits :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.5)

        hh = Label(f4,
                   text="The fiber in carrots can help keep blood sugar levels under control.\nAnd they're loaded with vitamin A and beta-carotene, which there's evidence to suggest can lower your\ndiabetes risk. They can strengthen your bones.\nCarrots have calcium and vitamin K, both of which are important for bone health",
                   bg="black", fg="white", font=('Merlin', 10))
        hh.place(relx=0.15, rely=0.540)

        cc = Label(f4, text="Recepies :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.72)

        cc = Label(f4, text="carrot fries,carrot salad,carrot smoothie,pickled carrots", bg="black", fg="white",
                   font=('Merlin', 10))
        cc.place(relx=0.3, rely=0.720)

        cc = Label(f4, text="Cost(for 1 kilograms) :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.8)

        cc = Label(f4, text="Rs.40", bg="black", fg="white", font=('Merlin', 10))
        cc.place(relx=0.3, rely=0.8)

        def close():
            f4.destroy()

        close = Button(f4, text="close", command=close)
        close.place(relx=0.1, rely=0.085, anchor=CENTER)

    def frame5():
        f5 = Frame(bg="Black")
        f5.place(relx=0.320, rely=0.055, width=740, height=900)

        gg = Label(f5, text="Brinjal", bg="black", fg="white", font=('Merlin', 16))
        gg.place(relx=0.43, rely=0.175)

        cc = Label(f5, text="Scientific name :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.3)

        cc = Label(f5, text="Solanum melongena", bg="black", fg="white", font=('Merlin', 10))
        cc.place(relx=0.3, rely=0.3)

        cc = Label(f5, text="Calories(in 100g) :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.4)

        cc = Label(f5, text="25 calories", bg="black", fg="white", font=('Merlin', 10))
        cc.place(relx=0.3, rely=0.4)

        cc = Label(f5, text="Health benefits :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.5)

        hh = Label(f5,text="Eggplant is a high-fiber, low-calorie food that is rich in nutrients and comes with\nmany potential health benefits.From reducing the risk of heart disease to helping with blood\nsugar control and weight loss,eggplants are a simple and delicious addition to any healthy diet.",bg="black", fg="white", font=('Merlin', 10))
        hh.place(relx=0.15, rely=0.540)

        cc = Label(f5, text="Recepies :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.69)

        cc = Label(f5, text="Brinjal Sambhar,Eggplant Salad Dip ,Roasted Eggplant Soup,Andhra Brinjal Curry",
                   bg="black", fg="white", font=('Merlin', 10))
        cc.place(relx=0.3, rely=0.69)

        cc = Label(f5, text="Cost(for 1 kilograms) :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.8)

        cc = Label(f5, text="Rs.20", bg="black", fg="white", font=('Merlin', 10))
        cc.place(relx=0.3, rely=0.8)

        def close():
            f5.destroy()

        close = Button(f5, text="close", command=close)
        close.place(relx=0.1, rely=0.085, anchor=CENTER)

    def frame6():
        f6 = Frame(bg="Black")
        f6.place(relx=0.320, rely=0.055, width=740, height=900)

        gg = Label(f6, text="Beans", bg="black", fg="white", font=('Merlin', 16))
        gg.place(relx=0.43, rely=0.175)

        cc = Label(f6, text="Scientific name :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.3)

        cc = Label(f6, text="Phaseolus vulgaris", bg="black", fg="white", font=('Merlin', 10))
        cc.place(relx=0.3, rely=0.3)

        cc = Label(f6, text="Calories(in 100g) :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.4)

        cc = Label(f6, text="347 calories", bg="black", fg="white", font=('Merlin', 10))
        cc.place(relx=0.3, rely=0.4)

        cc = Label(f6, text="Health benefits :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.5)

        hh = Label(f6,
                   text="Beans are a great source of fiber. That's important because most Americans don't\nget the recommended 25 to 38 grams each day.Fiber helps keep you regular and seems to protect\nagainst heart disease, high cholesterol,high blood pressure, and digestive illness.",
                   bg="black", fg="white", font=('Merlin', 10))
        hh.place(relx=0.15, rely=0.540)

        cc = Label(f6, text="Recepies :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.69)

        cc = Label(f6, text="Sauteed Green Beans ,Green Bean Salad ,Beans Aloo ,Beans Thoran", bg="black", fg="white",
                   font=('Merlin', 10))
        cc.place(relx=0.3, rely=0.69)

        cc = Label(f6, text="Cost(for 1 kilograms) :", bg="black", fg="white", font=('Merlin', 12))
        cc.place(relx=0.1, rely=0.8)

        cc = Label(f6, text="Rs.30", bg="black", fg="white", font=('Merlin', 10))
        cc.place(relx=0.3, rely=0.8)

        def close():
            f6.destroy()

        close = Button(f6, text="close", command=close)
        close.place(relx=0.1, rely=0.085, anchor=CENTER)

    # customer entry
    qq_entry = Entry(main_window3, width=10, font=('Merlin', 16))
    ww_entry = Entry(main_window3, width=10, font=('Merlin', 16))
    rr_entry = Entry(main_window3, width=10, font=('Merlin', 16))
    tt_entry = Entry(main_window3, width=10, font=('Merlin', 16))
    yy_entry = Entry(main_window3, width=10, font=('Merlin', 16))
    pwd_entry = Entry(main_window3, width=10, font=('Merlin', 16))



    qq_entry.place(relx=0.6, rely=0.38, anchor=CENTER)
    ww_entry.place(relx=0.6, rely=0.46, anchor=CENTER)
    tt_entry.place(relx=0.6, rely=0.54, anchor=CENTER)
    rr_entry.place(relx=0.6, rely=0.62, anchor=CENTER)
    yy_entry.place(relx=0.6, rely=0.70, anchor=CENTER)
    pwd_entry.place(relx=0.6, rely=0.78, anchor=CENTER)

    q2_entry = Button(main_window3,text="more", font=('Merlin', 16),command=frame3)
    w2_entry = Button(main_window3,text="more", font=('Merlin', 16),command=frame1)
    r2_entry = Button(main_window3, text="more",font=('Merlin', 16),command=frame4)
    t2_entry = Button(main_window3,text="more", font=('Merlin', 16),command=frame2)
    y2_entry = Button(main_window3,text="more", font=('Merlin', 16),command=frame5)
    p2_entry = Button(main_window3, text="more",font=('Merlin', 16),command=frame6)

    q2_entry.place(relx=0.48, rely=0.38, anchor=CENTER)
    w2_entry.place(relx=0.48, rely=0.46, anchor=CENTER)
    t2_entry.place(relx=0.48, rely=0.54, anchor=CENTER)
    r2_entry.place(relx=0.48, rely=0.62, anchor=CENTER)
    y2_entry.place(relx=0.48, rely=0.70, anchor=CENTER)
    p2_entry.place(relx=0.48, rely=0.78, anchor=CENTER)



    def check_val(a):
        if a.isdigit():
            return int(a)

        elif '.' in a:
            l = a.split('.')[0]
            r = a.split('.')[1]

            if l.isdigit() and r.isdigit():
                ans = int(l) + (int(r) / (10 ** len(r)))
                return ans

        return 0


    def clear_window1():
        qq_val = 30 * check_val(qq_entry.get())
        ww_val = 20 * check_val(ww_entry.get())
        tt_val = 20 * check_val(tt_entry.get())
        rr_val = 40 * check_val(rr_entry.get())
        yy_val = 20 * check_val(yy_entry.get())
        pwd_val = 30 * check_val(pwd_entry.get())
        total = qq_val + ww_val + tt_val + rr_val + yy_val + pwd_val
        main_window3.destroy()
        consumerh2(total)

    # Buttons
    cus = Button(main_window3, text="Proceed", font=('Merlin', 16), bg='green',command=clear_window1)
    cus.place(relx=0.78, rely=0.5, anchor=CENTER)




    main_window3.mainloop()





def consumerh2(tot):

    main_window4 = Tk()

    main_window4.geometry('1920x1080')

    # Packages
    bk = PhotoImage(file="consumerh3.png")
    bk_b = Label(main_window4, image=bk)
    bk_b.place(x=0.5, y=0.5)

    def clear_window():
        main_window4.destroy()



    # Buttons
    cus = Button(main_window4, text="Close", font=('Merlin', 16), bg='green',command=clear_window)
    cus.place(relx=0.7, rely=0.7, anchor=CENTER)

    total_label = Label(main_window4, text=tot, font=('Anton', 20),bg='light pink')
    total_label.place(relx=0.45, rely=0.83, anchor=CENTER)


    main_window4.mainloop()



def farmerh2():
    main_window.destroy()
    main_window9 = Tk()

    main_window9.geometry('1920x1080')

    bk = PhotoImage(file="fin1.png")
    bk_b = Label(main_window9, image=bk)
    bk_b.place(x=0.5, y=0.5)

    #Text
    img1 = Label(main_window9,text = "Click the Image to know more about it",font=('Merlin',16))
    img1.place(relx=0.5,rely=0.85,anchor=CENTER)


    # customer entry
    qq_entry = Entry(main_window9, width=10, font=('Merlin', 16))
    ww_entry = Entry(main_window9, width=10, font=('Merlin', 16))
    rr_entry = Entry(main_window9, width=10, font=('Merlin', 16))
    tt_entry = Entry(main_window9, width=10, font=('Merlin', 16))
    yy_entry = Entry(main_window9, width=10, font=('Merlin', 16))
    pwd_entry = Entry(main_window9, width=10, font=('Merlin', 16))

    qq_entry.place(relx=0.33, rely=0.42, anchor=CENTER)
    ww_entry.place(relx=0.53, rely=0.42, anchor=CENTER)
    tt_entry.place(relx=0.73, rely=0.42, anchor=CENTER)
    rr_entry.place(relx=0.33, rely=0.72, anchor=CENTER)
    yy_entry.place(relx=0.53, rely=0.72, anchor=CENTER)
    pwd_entry.place(relx=0.73, rely=0.72, anchor=CENTER)

    def check_val(a):
        if a.isdigit():
            return int(a)

        elif '.' in a:
            l = a.split('.')[0]
            r = a.split('.')[1]

            if l.isdigit() and r.isdigit():
                ans = int(l) + (int(r) / (10 ** len(r)))
                return ans

        return 0

    def summary1(total):
        f2 = Frame()
        f2.place(relx=0.7,rely=0.5, width=400, height=100)

        total_label = Label(f2, text=total, font=('Anton', 20), bg="light pink")
        total_label.place(relx=0.6, rely=0.6, anchor=CENTER)

        aa = Label(f2,text="Total amount:  ", font=('Anton', 20), bg="light pink")
        aa.place(relx=0.3,rely=0.6,anchor=CENTER)


        def clear():
            f2.destroy()
            main_window9.destroy()
            farmerh3()

        zz=Button(f2,text="confirm",font=('Anton', 12), bg="red",command=clear)
        zz.place(relx=0.8,rely=0.5)

    def sum_window():
        qq_val = 30 * check_val(qq_entry.get())
        ww_val = 20 * check_val(ww_entry.get())
        tt_val = 20 * check_val(tt_entry.get())
        rr_val = 40 * check_val(rr_entry.get())
        yy_val = 20 * check_val(yy_entry.get())
        pwd_val = 30 * check_val(pwd_entry.get())
        total = qq_val + ww_val + tt_val + rr_val + yy_val + pwd_val
        summary1(total)



    def poabt():
        f2 = Frame(bg="Black")
        f2.place(relx=0.3, rely=0.215, width=500, height=500)

        gg = Label(f2, text="Potato", bg="Black", fg="white", font=('Anton', 24))
        gg.place(relx=0.42, rely=0.05)

        jj = Label(f2, text="Scientific name:- Solanum tuberosum", bg="Black", fg="white", font=('Anton', 16))
        jj.place(relx=0.1, rely=0.2)

        hh = Label(f2, text="How to cultivate this crop:- ", bg="Black", fg="white", font=('Anton', 16))
        hh.place(relx=0.1, rely=0.3)

        ee = Label(f2, text="Time duration:- 75-120 days ", bg="Black", fg="white", font=('Anton', 16))
        ee.place(relx=0.14, rely=0.4)

        ff = Label(f2, text="Seasons for cultivation:- rabi seasons  ", bg="Black", fg="white", font=('Anton', 16))
        ff.place(relx=0.14, rely=0.5)

        hh = Label(f2, text="cost for 1 kg:- ", bg="Black", fg="white", font=('Anton', 16))
        hh.place(relx=0.1, rely=0.7)

        mm = Label(f2, text="RS.20  ", bg="Black", fg="white", font=('Anton', 16))
        mm.place(relx=0.5, rely=0.7)

        def close():
            f2.destroy()

        close = Button(f2, text="close", command=close)
        close.place(relx=0.05, rely=0.05, anchor=CENTER)





    # onion
    def oniabt():
        f3 = Frame(bg="Black")
        f3.place(relx=0.3, rely=0.215, width=500, height=500)

        gg = Label(f3, text="Onion", bg="Black", fg="white", font=('Anton', 24))
        gg.place(relx=0.42, rely=0.05)

        jj = Label(f3, text="Scientific name:- Allium cepa", bg="Black", fg="white", font=('Anton', 16))
        jj.place(relx=0.1, rely=0.2)

        hh = Label(f3, text="How to cultivate this crop:- ", bg="Black", fg="white", font=('Anton', 16))
        hh.place(relx=0.1, rely=0.3)

        ee = Label(f3, text="Time duration:- 80-150 days ", bg="Black", fg="white", font=('Anton', 16))
        ee.place(relx=0.14, rely=0.4)

        ff = Label(f3,
                text="Seasons for cultivation:- rabi season crop\n but also cultivated in kharif and \nlate-kharif seasons ",
                bg="Black", fg="white", font=('Anton', 16))
        ff.place(relx=0.14, rely=0.5)

        hh = Label(f3, text="cost for 1 kg:-   ", bg="Black", fg="white", font=('Anton', 16))
        hh.place(relx=0.1, rely=0.7)

        mm = Label(f3, text="RS.30  ", bg="Black", fg="white", font=('Anton', 16))
        mm.place(relx=0.6, rely=0.7)

        def close():
            f3.destroy()

        close = Button(f3, text="close", command=close)
        close.place(relx=0.05, rely=0.05, anchor=CENTER)


    def carabt():
        f4 = Frame(bg="Black")
        f4.place(relx=0.3, rely=0.215, width=500, height=500)

        gg = Label(f4, text="Carrot", bg="Black", fg="white", font=('Anton', 24))
        gg.place(relx=0.42, rely=0.05)

        jj = Label(f4, text="Scientific name:- Daucus carota subsp. sativus", bg="Black", fg="white",
                   font=('Anton', 16))
        jj.place(relx=0.1, rely=0.2)

        hh = Label(f4, text="How to cultivate this crop:- ", bg="Black", fg="white", font=('Anton', 16))
        hh.place(relx=0.1, rely=0.3)

        ee = Label(f4, text="Time duration:- 90-100 days ", bg="Black", fg="white", font=('Anton', 16))
        ee.place(relx=0.14, rely=0.4)

        ff = Label(f4, text="Seasons for cultivation:- rabi seasons ", bg="Black", fg="white", font=('Anton', 16))
        ff.place(relx=0.14, rely=0.5)

        hh = Label(f4, text="cost for 1 kg:-  ", bg="Black", fg="white", font=('Anton', 16))
        hh.place(relx=0.1, rely=0.7)

        mm = Label(f4, text="RS.40  ", bg="Black", fg="white", font=('Anton', 16))
        mm.place(relx=0.5, rely=0.7)

        def close():
            f4.destroy()

        close = Button(f4, text="close", command=close)
        close.place(relx=0.05, rely=0.05, anchor=CENTER)


    def beabt():
        f5 = Frame(bg="Black")
        f5.place(relx=0.3, rely=0.215, width=500, height=500)

        gg = Label(f5, text="Beans ", bg="Black", fg="white", font=('Anton', 24))
        gg.place(relx=0.42, rely=0.05)

        jj = Label(f5, text="Scientific name:- Phaseolus vulgaris", bg="Black", fg="white", font=('Anton', 16))
        jj.place(relx=0.1, rely=0.2)

        hh = Label(f5, text="How to cultivate this crop:-", bg="Black", fg="white", font=('Anton', 16))
        hh.place(relx=0.1, rely=0.3)

        ee = Label(f5, text="Time duration:- 40-50 days ", bg="Black", fg="white", font=('Anton', 16))
        ee.place(relx=0.14, rely=0.4)

        ff = Label(f5, text="Seasons for cultivation:- rabi seasons ", bg="Black", fg="white", font=('Anton', 16))
        ff.place(relx=0.14, rely=0.5)

        hh = Label(f5, text="cost for 1 kg:-   ", bg="Black", fg="white", font=('Anton', 16))
        hh.place(relx=0.1, rely=0.7)

        mm = Label(f5, text="RS.30  ", bg="Black", fg="white", font=('Anton', 16))
        mm.place(relx=0.5, rely=0.7)

        def close():
            f5.destroy()

        close = Button(f5, text="close", command=close)
        close.place(relx=0.05, rely=0.05, anchor=CENTER)



    def brabt():
        f6 = Frame(bg="Black")
        f6.place(relx=0.3, rely=0.215, width=500, height=500)

        gg = Label(f6, text="Brinjal", bg="Black", fg="white", font=('Anton', 24))
        gg.place(relx=0.42, rely=0.05)

        jj = Label(f6, text="Scientific name:- Solanum melongena", bg="Black", fg="white", font=('Anton', 16))
        jj.place(relx=0.1, rely=0.2)

        hh = Label(f6, text="How to cultivate this crop:-  ", bg="Black", fg="white", font=('Anton', 16))
        hh.place(relx=0.1, rely=0.3)

        ee = Label(f6, text="Time duration:- 140-150 days ", bg="Black", fg="white", font=('Anton', 16))
        ee.place(relx=0.14, rely=0.4)

        ff = Label(f6,
                   text="Seasons for cultivation:- it can be grown in\n both seasons but, rabi is preffered\n for more profitable yield ",
                   bg="Black", fg="white", font=('Anton', 16))
        ff.place(relx=0.14, rely=0.5)

        hh = Label(f6, text="cost for 1 kg:-   ", bg="Black", fg="white", font=('Anton', 16))
        hh.place(relx=0.1, rely=0.7)

        mm = Label(f6, text="RS.20  ", bg="Black", fg="white", font=('Anton', 16))
        mm.place(relx=0.5, rely=0.7)

        def close():
            f6.destroy()

        close = Button(f6, text="close", command=close)
        close.place(relx=0.05, rely=0.05, anchor=CENTER)




    def tomabt():
        f1 = Frame(bg="black")
        f1.place(relx=0.3, rely=0.215, width=500, height=500)

        gg = Label(f1, text="Tomato",bg="Black",fg="white",font=('Anton',24))
        gg.place(relx=0.42, rely=0.05)

        jj = Label(f1, text="Scientific name:- Solanum lycopersicum",bg="Black",fg="white",font=('Anton',16))
        jj.place(relx=0.1, rely=0.2)

        hh = Label(f1, text="How to cultivate this crop:-",bg="Black",fg="white",font=('Anton',16))
        hh.place(relx=0.1, rely=0.3)

        ee = Label(f1, text="Time duration:- 125 days ",bg="Black",fg="white",font=('Anton',16))
        ee.place(relx=0.14, rely=0.4)

        ff = Label(f1, text="Seasons for cultivation:- both rabi and kharif ",bg="Black",fg="white",font=('Anton',16))
        ff.place(relx=0.14, rely=0.5)

        hh = Label(f1, text="cost for 1 kg:-  ",bg="Black",fg="white",font=('Anton',16))
        hh.place(relx=0.1, rely=0.7)

        mm = Label(f1, text="RS.20  ",bg="Black",fg="white",font=('Anton',16))
        mm.place(relx=0.5, rely=0.7)

        def exit():
            f1.destroy()



        q = Button(f1,text="close",command=exit)
        q.place(relx=0.05,rely=0.05)






    #Button

    cus = Button(main_window9, text="Continue", font=('Merlin', 16), bg='green',command=sum_window)
    cus.place(relx=0.78, rely=0.58, anchor=CENTER)

    tomimg = PhotoImage(file="tomimage.png")
    tomab = Button(main_window9, image = tomimg , font=('Merlin', 16),command=tomabt)
    tomab.place(relx=0.23, rely=0.42, anchor=CENTER)

    onimg = PhotoImage(file="onimg.png")
    onab = Button(main_window9, image=onimg, font=('Merlin', 16), command=oniabt)
    onab.place(relx=0.44, rely=0.42, anchor=CENTER)

    poimg = PhotoImage(file="poimg.png")
    poab = Button(main_window9, image=poimg, font=('Merlin', 16), command=poabt)
    poab.place(relx=0.64, rely=0.42, anchor=CENTER)

    caimg = PhotoImage(file="carimg.png")
    caab = Button(main_window9, image=caimg, font=('Merlin', 16), command=carabt)
    caab.place(relx=0.23, rely=0.72, anchor=CENTER)

    beimg = PhotoImage(file="beimg.png")
    beab = Button(main_window9, image=beimg, font=('Merlin', 16), command=beabt)
    beab.place(relx=0.44, rely=0.72, anchor=CENTER)

    brimg = PhotoImage(file="brimg.png")
    brab = Button(main_window9, image=brimg, font=('Merlin', 16), command=brabt)
    brab.place(relx=0.64, rely=0.72, anchor=CENTER)


    main_window9.mainloop()



def farmerh3():
    main_window10 = Tk()
    main_window10.geometry('1920x1080')


    #Back Ground
    bk = PhotoImage(file="farmerh3.png")
    bk_b = Label(main_window10, image=bk)
    bk_b.place(x=0.5, y=0.5)




    def clear_window():
        main_window10.destroy()


    # Buttons
    cus = Button(main_window10, text="Close", font=('Merlin', 16), bg='green',command=clear_window)
    cus.place(relx=0.8, rely=0.7, anchor=CENTER)




    main_window10.mainloop()


def abt():

    f1 = Frame(bg="Black")
    f1.place(relx=0.1, rely=0.215, width=1200, height=500)

    gg = Label(f1, text="What's Our AIM?",font=("Merlin",24),bg="black",fg="white")
    gg.place(relx=0.37, rely=0.2)

    hh = Label(f1,text="->Farmers, The Backbone of our Nation are being exploited almost all over the country where they \nare not paid what their products desrve.\n->They are being paid very low for their products which inturn are sold in the markets as packages premium products.\n->An estimated 90% of our Indian Farmers are unable to fix a constant price for their vegetables and the crops they produce.\n->So we the KIWI GROUPS, a non profitable organisation are aiming at buying the goods from farmers \nat proper market price and to sell it at the same price to our customers.\n->We also have included the medicinal values of all our products, so do check it out, shop accordingly\n and live a healthy life !!",font=("Merlin",16),bg="black",fg="white")
    hh.place(relx=0.5, rely=0.6,anchor=CENTER)

    def close():
        f1.destroy()

    close = Button(f1, text="close", command=close)
    close.place(relx=0.03, rely=0.05, anchor=CENTER)


#Button

abt = Button(main_window, text= "About",font=('Merlin',16),bg='red',command=abt)
abt.place(relx=0.95, rely=0.05, anchor=CENTER)

sign = Button(main_window, text="Sign Up", font=('Merlin', 16), bg='red', command=sign_up)
sign.place(relx=0.45, rely=0.4, anchor=CENTER)

loi_s = Button(main_window, text="Login", font=('Merlin', 16), bg='red', command=login_new)
loi_s.place(relx=0.6, rely=0.4, anchor=CENTER)


main_window.mainloop()




