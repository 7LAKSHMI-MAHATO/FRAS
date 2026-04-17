from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #first image
        img1=Image.open(r"D:\FRAS python\images\1.png")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimage1)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #second image
        img2=Image.open(r"D:\FRAS python\images\2.png")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimage2)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #third image
        img4=Image.open(r"D:\FRAS python\images\3.jpg")
        img4=img4.resize((550,130),Image.Resampling.LANCZOS)

        self.photoimage3=ImageTk.PhotoImage(img4)
        f_lbl=Label(self.root,image=self.photoimage3)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #bg image
        img=Image.open(r"D:\FRAS python\images\bg.png")
        img=img.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimage)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label (bg_img,text="STUDENT MANAGMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)   

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=12,y=55,width=1500,height=600) 

        #left side label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold")) 
        Left_frame.place(x=10,y=10,width=760,height=580)   

        img_left=Image.open(r"D:\FRAS python\images\traning 8.jpg")
        img_left=img_left.resize((750,130),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimage)
        f_lbl.place(x=5,y=0,width=750,height=130)


        #right side label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold")) 
        Right_frame.place(x=780,y=10,width=660,height=580)            

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
           