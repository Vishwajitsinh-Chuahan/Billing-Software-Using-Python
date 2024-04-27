# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk

# class Bill_App:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1230x800+0+0")
#         self.root.title("Billing Software")

#         #Product Categories list

#         self.category=["Select Option","Clothing","LifeStyle","Mobiles"]
#         self.subcatClothing=["Pant","T-Shirt","Shirt"]
#         self.pant=["Levis","Mukti","Spykar"]
#         self.price_levis=5000
#         self.price_mukti=7000
#         self.price_spykar=1000

#         self.T_shirt=['Polo','Roadster','JackJones']
#         self.price_polo=1500
#         self.price_Roadster=1800
#         self.price_jackjones=1700

#         self.Shirt=['peter England','Louis Phillipe','park Avenue']
#         self.price_peter=2100
#         self.price_Louis=2700
#         self.price_park=1740

#         self.subcatlifestyle=["Bath Soap","Face Creame","Hair oil"]
#         self.Bath_soap=['LifeBoy','Lux','Santoor','Pearl']
#         self.price_life=float(20)
#         self.price_lux=20
#         self.price_santoor=20
#         self.price_pearl=30

#         self.faceCreame=['Fail&Lovely','Ponds','Olay',"Garnier"]
#         self.price_fail=20
#         self.price_ponds=20
#         self.price_olay=20
#         self.price_garnier=30

#         self.Hairoil=['Parchute','Jashmin','Bajaj']
#         self.price_para=25
#         self.price_jashmin=22
#         self.price_bajaj=30



#         self.subcatMobiles=["Iphone","Semsung","Xione","Reallme","One+"]
#         self.Iphone=['Iphone_x','Iphone_11','Iphone_12']
#         self.price_ix=40000
#         self.price_i11=60000
#         self.price_i12=85000

#         self.xiome=['Redi1','Redme-12','Readmepro']
#         self.price_r11=11000
#         self.price_r12=12000
#         self.price_rpro=9000

#         self.Samsung=['Samsung M16','Samsung M12','Samsung M21']
#         self.price_sm16=16000
#         self.price_sm12=12000
#         self.price_sm21=18000

#         self.readME=['Realme 12','Realme 13','Realme Pro']
#         self.price_rel12=25000
#         self.price_reli3=22000
#         self.price_relpro=35000

#         self.oneplus=['Oneplus1','Oneplus2','Oneplus3']
#         self.price_oe1=45000
#         self.price_one2=60000
#         self.price_one3=45000
       



#         # Load and resize the first image
#         img1 = Image.open("images/m2.jpeg")
#         img1 = img1.resize((250, 130))
#         self.photoimg1 = ImageTk.PhotoImage(img1)

#         # Load and resize the second image
#         img2 = Image.open("images/c1.jpeg")
#         img2 = img2.resize((250, 130))
#         self.photoimg2 = ImageTk.PhotoImage(img2)

#         # Load and resize the third image
#         img3 = Image.open("images/s1.jpeg")
#         img3 = img3.resize((300, 130))
#         self.photoimg3 = ImageTk.PhotoImage(img3)

#         img4 = Image.open("images/mo.jpeg")
#         img4 = img4.resize((500, 130))
#         self.photoimg4 = ImageTk.PhotoImage(img4)

#         img5 = Image.open("images/m1.jpg")
#         img5 = img5.resize((500, 130))
#         self.photoimg5 = ImageTk.PhotoImage(img5)

#         # Create Labels to display the images
#         lb1_img = Label(self.root, image=self.photoimg1)
#         lb1_img.place(x=10, y=10)

#         lb2_img = Label(self.root, image=self.photoimg2)
#         lb2_img.place(x=200, y=10)

#         lb3_img = Label(self.root, image=self.photoimg3)
#         lb3_img.place(x=430, y=10)

#         lb4_img = Label(self.root, image=self.photoimg4)
#         lb4_img.place(x=730, y=10)

#         lb5_img = Label(self.root, image=self.photoimg5)
#         lb5_img.place(x=1020, y=10)
       
#         lbl_title = Label(self.root,text="BILLING SOFTWARE USIGN PYTHON",font=("times new roman",35,"bold"),bg="white",fg="red")
#         lbl_title.place(x=0,y=130,width=1530,height=45)

#         Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
#         Main_Frame.place(x=0,y=175,width=1530,height=620)

#         # Customer LabelFrame

#         Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
#         Cust_Frame.place(x=10,y=5,width=350,height=140)

#         self.lbl_mobile=Label(Cust_Frame,text="Mobile No.",font=("times new roman",10,"bold"),bg="white")
#         self.lbl_mobile.grid(row=0,column=0,stick=W,padx=5,pady=2)

#         self.entry_mob=ttk.Entry(Cust_Frame,font=("times new roman",10,"bold"),width=24)
#         self.entry_mob.grid(row=0,column=1)

#         self.lblcustname=Label(Cust_Frame,font=('times new roman',10,'bold'),bg="white",text="Customer Name",bd=4)
#         self.lblcustname.grid(row=1,column=0,sticky=W,padx=5,pady=2)

#         self.txtcustname=ttk.Entry(Cust_Frame,font=('times new roman',10,'bold'),width=24)
#         self.txtcustname.grid(row=1,column=1,sticky=W,padx=5,pady=2)

#         self.lblemail=Label(Cust_Frame,font=('times new roman',10,'bold'),bg="white",text="Email",bd=4)
#         self.lblemail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

#         self.lblemail=ttk.Entry(Cust_Frame,font=('times new roman',10,'bold'),width=24)
#         self.lblemail.grid(row=2,column=1,sticky=W,padx=5,pady=2)

#         Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
#         Product_Frame.place(x=370,y=5,width=600,height=140)

#         #Category
#         self.lblcategory=Label(Product_Frame,font=('times new roman',10,'bold'),bg="white",text="Select Categories",bd=4)
#         self.lblcategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

#         self.combo_category=ttk.Combobox(Product_Frame,values=self.category,font=('times new roman',10,'bold'),width=24,state="readonly")
#         self.combo_category.current(0)
#         self.combo_category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
#         self.combo_category.bind("<<CommboboxSelected>>",self.Categories)

#         #Product name
#         self.lblproductname=Label(Product_Frame,font=('times new roman',10,'bold'),bg="white",text="Product Name",bd=4)
#         self.lblproductname.grid(row=1,column=0,sticky=W,padx=5,pady=2)

#         self.comboproudct=ttk.Combobox(Product_Frame,font=('times new roman',10,'bold'),width=24,state="readonly")
#         self.comboproudct.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        

#         #price
#         self.lblprice=Label(Product_Frame,font=('times new roman',10,'bold'),bg="white",text="Price",bd=4)
#         self.lblprice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

#         self.combo_price=ttk.Combobox(Product_Frame,font=('times new roman',10,'bold'),width=24,state="readonly")
#         self.combo_price.grid(row=0,column=3,sticky=W,padx=5,pady=2)

#         #sub category
#         self.lblsubcategory=Label(Product_Frame,font=('times new roman',10,'bold'),bg="white",text="Subcategory",bd=4)
#         self.lblsubcategory.grid(row=2,column=0,sticky=W,padx=5,pady=2)

#         self.combo_subcategory=ttk.Combobox(Product_Frame,value=[""],font=('times new roman',10,'bold'),width=24,state="readonly")
#         self.combo_subcategory.grid(row=2,column=1,sticky=W,padx=5,pady=2)
#         self.combo_subcategory.bind("<<ComboboxSelected>>",self.Product_add)

#         #qty
#         self.lblqty=Label(Product_Frame,font=('times new roman',10,'bold'),bg="white",text="Quantitty",bd=4)
#         self.lblqty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

#         self.combo_qty=ttk.Combobox(Product_Frame,font=('times new roman',10,'bold'),width=24,state="readonly")
#         self.combo_qty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

#         #Middle name
#         Middle_Frame=Frame(Main_Frame,bd=10)
#         Middle_Frame.place(x=10,y=150,width=980,height=340)

#         img10 = Image.open("images/w.jpeg")
#         img10 = img10.resize((490, 340))
#         self.photoimg10 = ImageTk.PhotoImage(img10)

#         # Load and resize the third image
#         img11 = Image.open("images/perfume.jpg")
#         img11 = img11.resize((490, 340))
#         self.photoimg11 = ImageTk.PhotoImage(img11)


#         Midd1_img = Label(Middle_Frame, image=self.photoimg10)
#         Midd1_img.place(x=0, y=0,width=490,height=340)

#         Midd2_img = Label(Middle_Frame, image=self.photoimg11)
#         Midd2_img.place(x=490, y=0,width=490,height=340)


#         #search
#         Search_frame=Frame(Main_Frame,bd=2,bg="white")
#         Search_frame.place(x=1020,y=10)

#         self.lblbill=Label(Search_frame,font=('times new roman',10,'bold'),bg="red",text="Bill Number",bd=4)
#         self.lblbill.grid(row=0,column=1,sticky=W,padx=5,pady=2)

#         self.txt_Entry_Search =ttk.Entry(Search_frame,font=('arial',10,'bold'),width=24)
#         self.txt_Entry_Search.grid(row=0,column=2,sticky=W,padx=2,pady=2)

#         self.Btnsearch=Button(Search_frame,height=2,text="Search",font=('arial',10,'bold'),bg="orangered",fg="white",width=8,cursor="hand2")
#         self.Btnsearch.grid(row=0,column=3)


#         #Rightframe bill area
#         RightlabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
#         RightlabelFrame.place(x=1000,y=45,width=480,height=440)

#         scroll_y=Scrollbar(RightlabelFrame,orient=VERTICAL)
#         self.textarea=Text(RightlabelFrame,yscrollcommand=scroll_y.set,font=("times new roman",12,"bold"),bg="white",fg="blue")
#         scroll_y.pack(side=RIGHT,fill=Y)
#         scroll_y.config(command=self.textarea.yview)
#         self.textarea.pack(fill=BOTH,expand=1)


         

#         #bil couter
#         bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
#         bottom_Frame.place(x=0,y=485,width=1520,height=120)

#         self.lblsubtotal=Label(bottom_Frame,font=('times new roman',10,'bold'),bg="white",text="Sub Total",bd=4)
#         self.lblsubtotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)
#         self.entrysubtotal=ttk.Entry(bottom_Frame,font=('times new roman',10,'bold'),width=24)
#         self.entrysubtotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

#         self.lbltax=Label(bottom_Frame,font=('times new roman',10,'bold'),bg="white",text="Gov Tax",bd=4)
#         self.lbltax.grid(row=1,column=0,sticky=W,padx=5,pady=2)
#         self.entrytax=ttk.Entry(bottom_Frame,font=('times new roman',10,'bold'),width=24)
#         self.entrytax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

#         self.lbltxtamount=Label(bottom_Frame,font=('times new roman',10,'bold'),bg="white",text="Total",bd=4)
#         self.lbltxtamount.grid(row=2,column=0,sticky=W,padx=5,pady=2)
#         self.entrytxtamount=ttk.Entry(bottom_Frame,font=('times new roman',10,'bold'),width=24)
#         self.entrytxtamount.grid(row=2,column=1,sticky=W,padx=5,pady=2)

#         #button Frame
#         Button_Frame=Frame(bottom_Frame,bd=2,bg="white")
#         Button_Frame.place(x=320,y=0)

#         self.btnaddTocart=Button(Button_Frame,height=2,text="Add to Cart",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
#         self.btnaddTocart.grid(row=0,column=0)

#         self.btngenerate=Button(Button_Frame,height=2,text="Generate Bill",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
#         self.btngenerate.grid(row=0,column=1)

#         self.btnsave=Button(Button_Frame,height=2,text="Save Bill",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
#         self.btnsave.grid(row=0,column=2)

#         self.btnexit=Button(Button_Frame,height=2,text="Print",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
#         self.btnexit.grid(row=0,column=3)
        
#         self.btnclear=Button(Button_Frame,height=2,text="Clear",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
#         self.btnclear.grid(row=0,column=4)

#         self.btnexit=Button(Button_Frame,height=2,text="Exit",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
#         self.btnexit.grid(row=0,column=5)

#     def Categories(self,event=""):
#         if self.category.get()=="Clothing":
#             self.combo_subcategory.config(value=self.subcatClothing)
#             self.combo_subcategory.current(0)

#         if self.category.get()=="LifeStyle":
#             self.combo_subcategory.config(value=self.subcatlifestyle)
#             self.combo_subcategory.current(0)

#         if self.category.get()=="Mobiles":
#             self.combo_subcategory.config(value=self.subcatMobiles)
#             self.combo_subcategory.current(0)

#     def Product_add(self,event=""):
#         if self.combo_subcategory.get()=="Pant":
#             self.comboproudct.config(value=self.pant)
#             self.comboproudct.current(0)

        


          


# if __name__ == '__main__':
#     root = Tk()
#     obj = Bill_App(root)
#     root.mainloop()



from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random,os
from tkinter import messagebox
import tempfile
from time import strftime

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1230x800+0+0")
        self.root.title("Billing Software")

        #variable
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,10000)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        self.l=IntVar()




        #Product Categories list

        self.category=["Select Option","Clothing","LifeStyle","Mobiles"]
        self.subcatClothing=["Pant","T-Shirt","Shirt"]
        self.pant=["Levis","Mufti","Spykar"]
        self.price_levis=5000
        self.price_mufti=7000
        self.price_spykar=1000

        self.T_shirt=['Polo','Roadster','JackJones']
        self.price_polo=1500
        self.price_Roadster=1800
        self.price_jackjones=1700

        self.Shirt=['peter England','Louis Phillipe','park Avenue']
        self.price_peter=2100
        self.price_Louis=2700
        self.price_park=1740

        self.subcatlifestyle=["Bath Soap","Face Creame","Hair oil"]
        self.Bath_soap=['LifeBoy','Lux','Santoor','Pearl']
        self.price_life=float(20)
        self.price_lux=20
        self.price_santoor=20
        self.price_pearl=30

        self.faceCreame=['Fail&Lovely','Ponds','Olay',"Garnier"]
        self.price_fail=20
        self.price_ponds=20
        self.price_olay=20
        self.price_garnier=30

        self.Hairoil=['Parchute','Jashmin','Bajaj']
        self.price_para=25
        self.price_jashmin=22
        self.price_bajaj=30



        self.subcatMobiles=["Iphone","Semsung","Xiome","Realme","One+"]
        self.Iphone=['Iphone_x','Iphone_11','Iphone_12']
        self.price_ix=40000
        self.price_i11=60000
        self.price_i12=85000

        self.xiome=['Redi1','Redme-12','Readmepro']
        self.price_r11=11000
        self.price_r12=12000
        self.price_rpro=9000

        self.Samsung=['Samsung M16','Samsung M12','Samsung M21']
        self.price_sm16=16000
        self.price_sm12=12000
        self.price_sm21=18000

        self.readME=['Realme 12','Realme 13','Realme Pro']
        self.price_rel12=25000
        self.price_reli3=22000
        self.price_relpro=35000

        self.oneplus=['Oneplus1','Oneplus2','Oneplus3']
        self.price_oe1=45000
        self.price_one2=60000
        self.price_one3=45000
       

        # Load and resize the first image
        img1 = Image.open("images/m2.jpeg")
        img1 = img1.resize((250, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # Load and resize the second image
        img2 = Image.open("images/c1.jpeg")
        img2 = img2.resize((250, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # Load and resize the third image
        img3 = Image.open("images/s1.jpeg")
        img3 = img3.resize((300, 130))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        img4 = Image.open("images/mo.jpeg")
        img4 = img4.resize((500, 130))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        img5 = Image.open("images/m1.jpg")
        img5 = img5.resize((500, 130))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        # Create Labels to display the images
        lb1_img = Label(self.root, image=self.photoimg1)
        lb1_img.place(x=10, y=10)

        lb2_img = Label(self.root, image=self.photoimg2)
        lb2_img.place(x=200, y=10)

        lb3_img = Label(self.root, image=self.photoimg3)
        lb3_img.place(x=430, y=10)

        lb4_img = Label(self.root, image=self.photoimg4)
        lb4_img.place(x=730, y=10)

        lb5_img = Label(self.root, image=self.photoimg5)
        lb5_img.place(x=1020, y=10)
       
        lbl_title = Label(self.root,text="BILLING SOFTWARE USIGN PYTHON",font=("times new roman",35,"bold"),bg="white",fg="red")
        lbl_title.place(x=0,y=130,width=1530,height=45)

        def time():
            # lbl=string()
            string =strftime('%H:%M:%S %p')
            self.lbl.config(text=string)
            self.lbl.after(1000,time)
        self.lbl=Label(lbl_title,font=('times new roman',16,'bold'),background='white',foreground='blue')
        self.lbl.place(x=0,y=0,width=120,height=45)
        time()

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)

        # Customer LabelFrame

        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lbl_mobile=Label(Cust_Frame,text="Mobile No.",font=("times new roman",10,"bold"),bg="white")
        self.lbl_mobile.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("times new roman",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        self.lblcustname=Label(Cust_Frame,font=('times new roman',10,'bold'),bg="white",text="Customer Name",bd=4)
        self.lblcustname.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtcustname=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=('times new roman',10,'bold'),width=24)
        self.txtcustname.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblemail=Label(Cust_Frame,font=('times new roman',10,'bold'),bg="white",text="Email",bd=4)
        self.lblemail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.lblemail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=('times new roman',10,'bold'),width=24)
        self.lblemail.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=600,height=140)

        #Category
        self.lblcategory=Label(Product_Frame,font=('times new roman',10,'bold'),bg="white",text="Select Categories",bd=4)
        self.lblcategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.combo_category=ttk.Combobox(Product_Frame,values=self.category,font=('times new roman',10,'bold'),width=24,state="readonly")
        self.combo_category.current(0)
        self.combo_category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.combo_category.bind("<<ComboboxSelected>>",self.Categories)

        #Product name
        self.lblproductname=Label(Product_Frame,font=('times new roman',10,'bold'),bg="white",text="Product Name",bd=4)
        self.lblproductname.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.comboproudct=ttk.Combobox(Product_Frame,textvariable=self.product,font=('times new roman',10,'bold'),width=24,state="readonly")
        self.comboproudct.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.comboproudct.bind("<<ComboboxSelected>>",self.price)
        

        #price
        self.lblprice=Label(Product_Frame,font=('times new roman',10,'bold'),bg="white",text="Price",bd=4)
        self.lblprice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.combo_price=ttk.Combobox(Product_Frame,textvariable=self.prices,font=('times new roman',10,'bold'),width=24,state="readonly")
        self.combo_price.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        #sub category
        self.lblsubcategory=Label(Product_Frame,font=('times new roman',10,'bold'),bg="white",text="Subcategory",bd=4)
        self.lblsubcategory.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.combo_subcategory=ttk.Combobox(Product_Frame,font=('times new roman',10,'bold'),width=24,state="readonly")
        self.combo_subcategory.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.combo_subcategory.bind("<<ComboboxSelected>>",self.Product_add)

        #qty
        self.lblqty=Label(Product_Frame,font=('times new roman',10,'bold'),bg="white",text="Quantitty",bd=4)
        self.lblqty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.combo_qty=ttk.Entry(Product_Frame,textvariable=self.qty,font=('times new roman',10,'bold'),width=24)
        self.combo_qty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        #Middle name
        Middle_Frame=Frame(Main_Frame,bd=10)
        Middle_Frame.place(x=10,y=150,width=980,height=340)

        img10 = Image.open("images/w.jpeg")
        img10 = img10.resize((490, 340))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        # Load and resize the third image
        img11 = Image.open("images/perfume.jpg")
        img11 = img11.resize((490, 340))
        self.photoimg11 = ImageTk.PhotoImage(img11)


        Midd1_img = Label(Middle_Frame, image=self.photoimg10)
        Midd1_img.place(x=0, y=0,width=490,height=340)

        Midd2_img = Label(Middle_Frame, image=self.photoimg11)
        Midd2_img.place(x=490, y=0,width=490,height=340)


        #search
        Search_frame=Frame(Main_Frame,bd=2,bg="white")
        Search_frame.place(x=1020,y=10)

        self.lblbill=Label(Search_frame,font=('times new roman',10,'bold'),bg="red",text="Bill Number",bd=4)
        self.lblbill.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.txt_Entry_Search =ttk.Entry(Search_frame,textvariable=self.search_bill,font=('arial',10,'bold'),width=24)
        self.txt_Entry_Search.grid(row=0,column=2,sticky=W,padx=2,pady=2)

        self.Btnsearch=Button(Search_frame,command=self.find_bill,height=2,text="Search",font=('arial',10,'bold'),bg="orangered",fg="white",width=8,cursor="hand2")
        self.Btnsearch.grid(row=0,column=3)


        #Rightframe bill area
        RightlabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightlabelFrame.place(x=1000,y=45,width=480,height=440)

        scroll_y=Scrollbar(RightlabelFrame,orient=VERTICAL)
        self.textarea=Text(RightlabelFrame,yscrollcommand=scroll_y.set,font=("times new roman",12,"bold"),bg="white",fg="blue")
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)


         

        #bil couter
        bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        bottom_Frame.place(x=0,y=485,width=1520,height=120)

        self.lblsubtotal=Label(bottom_Frame,font=('times new roman',10,'bold'),bg="white",text="Sub Total",bd=4)
        self.lblsubtotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.entrysubtotal=ttk.Entry(bottom_Frame,textvariable=self.sub_total,font=('times new roman',10,'bold'),width=24)
        self.entrysubtotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lbltax=Label(bottom_Frame,font=('times new roman',10,'bold'),bg="white",text="Gov Tax",bd=4)
        self.lbltax.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.entrytax=ttk.Entry(bottom_Frame,textvariable=self.tax_input,font=('times new roman',10,'bold'),width=24)
        self.entrytax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lbltxtamount=Label(bottom_Frame,font=('times new roman',10,'bold'),bg="white",text="Total",bd=4)
        self.lbltxtamount.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        self.entrytxtamount=ttk.Entry(bottom_Frame,textvariable=self.total,font=('times new roman',10,'bold'),width=24)
        self.entrytxtamount.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #button Frame
        Button_Frame=Frame(bottom_Frame,bd=2,bg="white")
        Button_Frame.place(x=320,y=0)

        self.btnaddTocart=Button(Button_Frame,command=self.AddItem,height=2,text="Add to Cart",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.btnaddTocart.grid(row=0,column=0)

        self.btngenerate=Button(Button_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.btngenerate.grid(row=0,column=1)

        self.btnsave=Button(Button_Frame,command=self.save_bill,height=2,text="Save Bill",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.btnsave.grid(row=0,column=2)

        self.btnprint=Button(Button_Frame,command=self.print,height=2,text="Print",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.btnprint.grid(row=0,column=3)
        
        self.btnclear=Button(Button_Frame,command=self.bill_clear,height=2,text="Clear",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.btnclear.grid(row=0,column=4)

        self.btnexit=Button(Button_Frame,command=self.root.destroy,height=2,text="Exit",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.btnexit.grid(row=0,column=5)

        self.welcome()

        self.l=[]
    
    #=========================================Function DEclaration======================
    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)

        if self.product.get()=="":
            messagebox.showerror("Error","Please Select the proeduct Name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t\t{self.qty.get()}\t\t\t{self.m}")
            self.sub_total.set(str('RS.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l))- (self.prices.get()))*Tax)/100)))))

    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please ADD to cart Product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n==================================================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n==================================================")

   
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want save the bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('Save Bill/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} save Succssfully")
            f1.close()

    def print(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def find_bill(self):
        found="no"
        for i in os.listdir("Save Bill/"):
            if i.split(".",)[0]==self.search_bill.get():
                f1=open(f'Save Bill/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=="no":
            messagebox.showerror("Error","Invalid Bill No")

    def bill_clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_email.set("")
        self.c_phon.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.qty.set("")
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()


    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t Welcome CodeWithkiram Mini Mall")
        self.textarea.insert(END,f"\n Bill Number: {self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number: {self.c_phon.get()}")
        self.textarea.insert(END,f"\n Customer E-Mail: {self.c_email.get()}")

        self.textarea.insert(END,"\n==================================================")

        self.textarea.insert(END,f"\n Products\t\t\tQTY\t\t\tPrice")
        self.textarea.insert(END,"\n==================================================\n")

   


    def Categories(self,event=""):
        if self.combo_category.get()=="Clothing":
            self.combo_subcategory.config(values=self.subcatClothing)
            self.combo_subcategory.current(0)

        elif self.combo_category.get()=="LifeStyle":
            self.combo_subcategory.config(values=self.subcatlifestyle)
            self.combo_subcategory.current(0)

        elif self.combo_category.get()=="Mobiles":
            self.combo_subcategory.config(values=self.subcatMobiles)
            self.combo_subcategory.current(0)

    def Product_add(self,event=""):
        if self.combo_subcategory.get()=="Pant":
            self.comboproudct.config(values=self.pant)
            self.comboproudct.current(0)

        if self.combo_subcategory.get()=="T-Shirt":
            self.comboproudct.config(values=self.T_shirt)
            self.comboproudct.current(0)

        if self.combo_subcategory.get()=="Shirt":
            self.comboproudct.config(values=self.Shirt)
            self.comboproudct.current(0)

       #Lifestyle
        if self.combo_subcategory.get()=="Bath Soap":  
            self.comboproudct.config(values=self.Bath_soap)
            self.comboproudct.current(0)

        if self.combo_subcategory.get()=="Face Creame":
            self.comboproudct.config(values=self.faceCreame)
            self.comboproudct.current(0)

        if self.combo_subcategory.get()=="Hair oil":
            self.comboproudct.config(values=self.Hairoil)
            self.comboproudct.current(0)

        #mobile
        if self.combo_subcategory.get()=="Iphone":
            self.comboproudct.config(values=self.Iphone)
            self.comboproudct.current(0)

        if self.combo_subcategory.get()=="Semsung":
            self.comboproudct.config(values=self.Samsung)
            self.comboproudct.current(0)

        if self.combo_subcategory.get()=="Xiome":
            self.comboproudct.config(values=self.xiome)
            self.comboproudct.current(0)

        if self.combo_subcategory.get()=="Realme":
            self.comboproudct.config(values=self.readME)
            self.comboproudct.current(0)

        if self.combo_subcategory.get()=="One+":
            self.comboproudct.config(values=self.oneplus)
            self.comboproudct.current(0)

    
    def price(self,event=""):
        #pant
        if self.comboproudct.get()=="Levis":
            self.combo_price.config(values=self.price_levis)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.comboproudct.get()=="Mufti":
            self.combo_price.config(values=self.price_mufti)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.comboproudct.get()=="Spykar":
            self.combo_price.config(values=self.price_spykar)
            self.combo_price.current(0)
            self.qty.set(1)

        #T-shirt
        #self.T_shirt=['Polo','Roadster','JackJones']
        if self.comboproudct.get()=="Polo":
            self.combo_price.config(values=self.price_polo)
            self.combo_price.current(0)
            self.qty.set(1)
        if self.comboproudct.get()=="Roadster":
            self.combo_price.config(values=self.price_Roadster)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.comboproudct.get()=="JackJones":
            self.combo_price.config(values=self.price_jackjones)
            self.combo_price.current(0)
            self.qty.set(1)

        #shirt
        #self.Shirt=['peter England','Louis Phillipe','park Avenue']
        if self.comboproudct.get()=="peter England":
            self.combo_price.config(values=self.price_peter)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.comboproudct.get()=="Louis Phillipe":
            self.combo_price.config(values=self.price_Louis)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.comboproudct.get()=="park Avenue":
            self.combo_price.config(values=self.price_park)
            self.combo_price.current(0)
            self.qty.set(1)

        #lifestyle
        #bath soap
        #self.Bath_soap=['LifeBoy','Lux','Santoor','Pearl']
        if self.comboproudct.get()=="LifeBoy":
            self.combo_price.config(values=self.price_life)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.comboproudct.get()=="Lux":
            self.combo_price.config(values=self.price_lux)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.comboproudct.get()=="Santoor":
            self.combo_price.config(values=self.price_santoor)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.comboproudct.get()=="Pearl":
            self.combo_price.config(values=self.price_pearl)
            self.combo_price.current(0)
            self.qty.set(1)

        # Face cream
        #  self.faceCreame=['Fail&Lovely','Ponds','Olay',"Garnier"]

        if self.comboproudct.get()=="Fail&Lovely":
            self.combo_price.config(values=self.price_fail)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.comboproudct.get()=="Ponds":
            self.combo_price.config(values=self.price_ponds)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.comboproudct.get()=="Olay":
            self.combo_price.config(values=self.price_olay)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.comboproudct.get()=="Garnier":
            self.combo_price.config(values=self.price_garnier)
            self.combo_price.current(0)
            self.qty.set(1)

        #hair oil
        #  self.Hairoil=['Parchute','Jashmin','Bajaj']
        if self.comboproudct.get()=="Parchute":
            self.combo_price.config(values=self.price_para)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.comboproudct.get()=="Jashmin":
            self.combo_price.config(values=self.price_jashmin)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.comboproudct.get()=="Bajaj":
            self.combo_price.config(values=self.price_bajaj)
            self.combo_price.current(0)
            self.qty.set(1)

        #mobiles
        #iphone
        #self.Iphone=['Iphone_x','Iphone_11','Iphone_12']
        if self.comboproudct.get()=="Iphone_x":
            self.combo_price.config(values=self.price_ix)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.comboproudct.get()=="Iphone_11":
            self.combo_price.config(values=self.price_i11)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.comboproudct.get()=="Iphone_12":
            self.combo_price.config(values=self.price_i12)
            self.combo_price.current(0)
            self.qty.set(1)

        #samsung
        #  self.Samsung=['Samsung M16','Samsung M12','Samsung M21']
        if self.comboproudct.get()=="Samsung M16":
            self.combo_price.config(values=self.price_sm16)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.comboproudct.get()=="Samsung M12":
            self.combo_price.config(values=self.price_sm12)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.comboproudct.get()=="Samsung M21":
            self.combo_price.config(values=self.price_sm21)
            self.combo_price.current(0)
            self.qty.set(1)

        #Realme
        # self.readME=['Realme 12','Realme 13','Realme Pro']
        if self.comboproudct.get()=="Realme 12":
            self.combo_price.config(values=self.price_r12)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.comboproudct.get()=="Realme 13":
            self.combo_price.config(values=self.price_reli3)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.comboproudct.get()=="Realme Pro":
            self.combo_price.config(values=self.price_relpro)
            self.combo_price.current(0)
            self.qty.set(1)

        #xiome
        #  self.xiome=['Redi1','Redme-12','Readmepro']
        if self.comboproudct.get()=="Redi1":
            self.combo_price.config(values=self.price_r11)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.comboproudct.get()=="Redme 12":
            self.combo_price.config(values=self.price_r12)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.comboproudct.get()=="Readmepro":
            self.combo_price.config(values=self.price_rpro)
            self.combo_price.current(0)
            self.qty.set(1)

        #oneplus
        # self.oneplus=['Oneplus1','Oneplus2','Oneplus3']
        if self.comboproudct.get()=="Oneplus1":
            self.combo_price.config(values=self.price_oe1)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.comboproudct.get()=="Oneplus2":
            self.combo_price.config(values=self.price_one2)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.comboproudct.get()=="Oneplus3":
            self.combo_price.config(values=self.price_one3)
            self.combo_price.current(0)
            self.qty.set(1)




        

        


if __name__ == '__main__':
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()

