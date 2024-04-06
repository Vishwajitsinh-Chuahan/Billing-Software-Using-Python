from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1230x800+0+0")
        self.root.title("Billing Software")

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

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)

        # Customer LabelFrame

        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lbl_mobile=Label(Cust_Frame,text="Mobile No.",font=("times new roman",10,"bold"),bg="white")
        self.lbl_mobile.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,font=("times new roman",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        self.lblcustname=Label(Cust_Frame,font=('times new roman',10,'bold'),bg="white",text="Customer Name",bd=4)
        self.lblcustname.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtcustname=ttk.Entry(Cust_Frame,font=('times new roman',10,'bold'),width=24)
        self.txtcustname.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblemail=Label(Cust_Frame,font=('times new roman',10,'bold'),bg="white",text="Email",bd=4)
        self.lblemail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.lblemail=ttk.Entry(Cust_Frame,font=('times new roman',10,'bold'),width=24)
        self.lblemail.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=600,height=140)

        #sub category
        self.lblcategory=Label(Product_Frame,font=('times new roman',10,'bold'),bg="white",text="Select Categories",bd=4)
        self.lblcategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.combo_category=ttk.Combobox(Product_Frame,font=('times new roman',10,'bold'),width=24,state="readonly")
        self.combo_category.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        #Product name
        self.lblproductname=Label(Product_Frame,font=('times new roman',10,'bold'),bg="white",text="Product Name",bd=4)
        self.lblproductname.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.comboproudct=ttk.Combobox(Product_Frame,font=('times new roman',10,'bold'),width=24,state="readonly")
        self.comboproudct.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        #price
        self.lblprice=Label(Product_Frame,font=('times new roman',10,'bold'),bg="white",text="Price",bd=4)
        self.lblprice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.combo_price=ttk.Combobox(Product_Frame,font=('times new roman',10,'bold'),width=24,state="readonly")
        self.combo_price.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        #sub category
        self.lblsubcategory=Label(Product_Frame,font=('times new roman',10,'bold'),bg="white",text="Subcategory",bd=4)
        self.lblsubcategory.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.combo_subcategory=ttk.Combobox(Product_Frame,font=('times new roman',10,'bold'),width=24,state="readonly")
        self.combo_subcategory.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #qty
        self.lblqty=Label(Product_Frame,font=('times new roman',10,'bold'),bg="white",text="Quantitty",bd=4)
        self.lblqty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.combo_qty=ttk.Combobox(Product_Frame,font=('times new roman',10,'bold'),width=24,state="readonly")
        self.combo_qty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

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
        self.entrysubtotal=ttk.Entry(bottom_Frame,font=('times new roman',10,'bold'),width=24)
        self.entrysubtotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lbltax=Label(bottom_Frame,font=('times new roman',10,'bold'),bg="white",text="Gov Tax",bd=4)
        self.lbltax.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.entrytax=ttk.Entry(bottom_Frame,font=('times new roman',10,'bold'),width=24)
        self.entrytax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lbltxtamount=Label(bottom_Frame,font=('times new roman',10,'bold'),bg="white",text="Total",bd=4)
        self.lbltxtamount.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        self.entrytxtamount=ttk.Entry(bottom_Frame,font=('times new roman',10,'bold'),width=24)
        self.entrytxtamount.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #button Frame
        Button_Frame=Frame(bottom_Frame,bd=2,bg="white")
        Button_Frame.place(x=320,y=0)

        self.btnaddTocart=Button(Button_Frame,height=2,text="Add to Cart",font=('arial',10,'bold'),bg="orangered",fg="white",width=15)
        self.btnaddTocart.grid(row=0,column=0)

        self.btngenerate=Button(Button_Frame,height=2,text="Generate Bill",font=('arial',10,'bold'),bg="orangered",fg="white")
        self.btngenerate.grid(row=0,column=1)

        self.btnsave=Button(Button_Frame,height=2,text="Save Bill",font=('arial',10,'bold'),bg="orangered",fg="white")
        self.btnsave.grid(row=0,column=2)

        self.btnexit=Button(Button_Frame,height=2,text="Print",font=('arial',10,'bold'),bg="orangered",fg="white")
        self.btnexit.grid(row=0,column=3)
        
        self.btnclear=Button(Button_Frame,height=2,text="Clear",font=('arial',10,'bold'),bg="orangered",fg="white")
        self.btnclear.grid(row=0,column=4)

        self.btnexit=Button(Button_Frame,height=2,text="Exit",font=('arial',10,'bold'),bg="orangered",fg="white")
        self.btnexit.grid(row=0,column=5)


if __name__ == '__main__':
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()




