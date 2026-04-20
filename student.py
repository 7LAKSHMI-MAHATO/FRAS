from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #first image
        img1=Image.open(r"images\1.png")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimage1)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #second image
        img2=Image.open(r"images\2.png")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimage2)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #third image
        img4=Image.open(r"images\3.jpg")
        img4=img4.resize((550,130),Image.Resampling.LANCZOS)

        self.photoimage3=ImageTk.PhotoImage(img4)
        f_lbl=Label(self.root,image=self.photoimage3)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #bg image
        img=Image.open(r"images\bg.png")
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

        img_left=Image.open(r"images\traning 8.jpg")
        img_left=img_left.resize((750,130),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimage)
        f_lbl.place(x=5,y=0,width=750,height=130)

        #current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current cource information",font=("times new roman",12,"bold")) 
        current_course_frame.place(x=5,y=135,width=760,height=125)   

        #department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg='white')
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",13,"bold"))
        dep_combo['values']=("Select Depatments",'computer','it','civil','mechanical')
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #course
        course_label=Label(current_course_frame,text='Course',font=("times new roman",13,'bold'),bg='white')
        course_label.grid(row=0,column=2,padx=10,sticky=W) 

        course_combo=ttk.Combobox(current_course_frame,font=("times new roman",13,'bold'),width=20)     
        course_combo['values']=("Select course",'FF','SE','TE','BE')
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=10,sticky=W)

        #year
        
        year_label = Label(current_course_frame, text="Year",font=('times new roman',13,'bold'), bg='white')
        year_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame,
                          font=('times new roman',13,'bold'), width=20)
        year_combo['values'] = ("Select year",'1','2','3','4')
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=10, sticky=W)
         
        #Semester
        semester_label = Label(current_course_frame, text='Semester',font=("times new roman",13,'bold'), bg='white')
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,font=("times new roman",13,'bold'), width=20)
        semester_combo['values'] = ("Select semester",'1','2','3','4')
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=10, sticky=W)

        #class student information
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="class student information",font=("times new roman",12,"bold")) 
        class_Student_frame.place(x=5,y=250,width=760,height=300)   

        
        #student id
        studentId_label=Label(class_Student_frame,text='StudentID',font=("times new roman",13,'bold'),bg='white') 
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",13,'bold'))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)

        #studen name
        studentName_label=Label(class_Student_frame,text='StudentName',font=("times new roman",13,'bold'),bg='white') 
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",13,'bold'))
        studentID_entry.grid(row=0,column=3,padx=10,sticky=W)

        #class division
        class_div_label=Label(class_Student_frame,text='classdivision',font=("times new roman",13,'bold'),bg='white') 
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        class_div_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",13,'bold'))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll no
        roll_no_label=Label(class_Student_frame,text='roll no',font=("times new roman",13,'bold'),bg='white') 
        roll_no_label.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",13,'bold'))
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        #Gender
        gender_label=Label(class_Student_frame,text='Gender',font=("times new roman",13,'bold'),bg='white') 
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",13,'bold'))
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #dob
        dob_label=Label(class_Student_frame,text='dob',font=("times new roman",13,'bold'),bg='white') 
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(class_Student_frame, width=20, font=("times new roman",13,'bold'))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
      
        #email
        email_label=Label(class_Student_frame,text='email',font=("times new roman",13,'bold'),bg='white') 
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",13,'bold'))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
      
        #phone no
        phone_div_label=Label(class_Student_frame,text='phone no',font=("times new roman",13,'bold'),bg='white') 
        phone_div_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        phone_div_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",13,'bold'))
        phone_div_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #address
        class_div_label=Label(class_Student_frame,text='address',font=("times new roman",13,'bold'),bg='white') 
        class_div_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        class_div_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",13,'bold'))
        class_div_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
      
        #teacher name
        class_div_label=Label(class_Student_frame,text='Teacher name',font=("times new roman",13,'bold'),bg='white') 
        class_div_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        class_div_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",13,'bold'))
        class_div_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
     
              
              
              
              
              
              
              
              
              
      

        #right side label frame
        # Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),bg='white') 
        # Right_frame.place(x=780,y=10,width=660,height=580)            

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
           
