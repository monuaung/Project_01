from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox,filedialog

root=Tk()



root.geometry("400x500")

# Title
root.title("Sign Up Form")

# Icon Image
Image=PhotoImage(file="D:\\Monu Class\\5pm\\python coding\\2.0 GUI\\aaaa.png")
root.iconphoto(False,Image)

Label(root,text="Sign Up Form",font=("Times",20,"bold"),fg="red",bg="yellow").pack()

# Name
Label(root,text="Full Name:",font=("Times",14,"bold"),fg="blue").pack()
name_entry=Entry(root,width=30,font=("Times",12,"bold"))
name_entry.pack()

# DOB
Label(root,text="DOB(dd/mm/yyyy):",font=("Times",14,"bold"),fg="blue").pack()
dob_entry=Entry(root,width=30,font=("Times",12,"bold"))
dob_entry.pack()

# Gender
gender_var=IntVar()
Label(root,text="Gender:",font=("Times",14,"bold"),fg="blue").pack()
r1=Radiobutton(root,text="Male",variable=gender_var,font=("Times",12,"bold"),value=1)
r2=Radiobutton(root,text="Female",variable=gender_var,font=("Times",12,"bold"),value=2)
r1.pack()
r2.pack()

#Nationality
Label(root,text="Nationality:",font=("Times",14,"bold"),fg="blue").pack()
Nationality_list=["Indian","Others"]
nationality_var=StringVar()
nationality_var.set("Select a Nationality")
country_entry=OptionMenu(root,nationality_var,*Nationality_list)
country_entry.config(width=30,font=("Times",12,"bold"))
country_entry.pack()

#Qulification
Label(root,text="Highest Qulification:",font=("Times",14,"bold"),fg="blue").pack()
Qulification_list=["Bachelor of Computer Application","Master of Computer Application","B.Tech","M.Tech"]
qualification_var=StringVar()
qualification_var.set("Select Highest Qulification")
qualification_entry=OptionMenu(root,qualification_var,*Qulification_list)
qualification_entry.config(width=30,font=("Times",12,"bold"))
qualification_entry.pack()

#Upload
def upload_file():
    file = filedialog.askopenfile()
    data=file.read()
    # data.
    # print(file.name)
    f=open(r"D:\Monu Class\5pm\python coding\2.0 GUI\Projects\Uploaded_File\test1.txt",'w')
    f.write(data)



    # upload.config(text="File Uploaded" + file_path)
    # file_path = filedialog.asksaveasfilename()


upload = Label(root, text="No File Uploaded")
upload.pack()
upload_button=Button(root,text="Upload File",command=upload_file)
upload_button.pack()

# Disclaimer
Label(root,text="Disclaimer:",font=("Times",14,"bold"),fg="blue").pack()
disclaimer_var = BooleanVar()
disclaimer_check = Checkbutton(root, text="I accept disclaimer", variable = disclaimer_var)
disclaimer_check.pack()


def submit_form():
    name = name_entry.get()
    dob = dob_entry.get()
    gender = gender_var.get()
    nationality = nationality_var.get()
    qualification = qualification_var.get()
    disclaimer = disclaimer_var.get()

    def gender_print():
        if gender==1:
            return "Male"
        elif gender==2:
            return "Female"
    
    def disclaimer_print():
        if disclaimer==True:
            return "Accepted"
        elif disclaimer==False:
            return "Not Accepted"


    print("Name : ",name)
    print("DOB : ",dob)
    print("Gender :",gender_print())
    print("Nationality :",nationality)
    print("Qulification : ",qualification)
    print("Disclaimer Accepted : ",disclaimer_print())


# Submit Button
submit_button = Button(root,text="Enter",bg="green",fg="white",font=("Time",12,"bold"),width=30,command=submit_form)
submit_button.pack(pady=0)

# Space Label
# space_label = Label(root,text="",height=1)
# space_label.pack()

# Exit Button
exit_button = Button(root,text="Exit",bg="red",fg="white",font=("Time",12,"bold"),width=30)
exit_button.pack(pady=0)

root.mainloop()
