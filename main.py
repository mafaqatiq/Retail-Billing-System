import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import random, smtplib
root = tk.Tk()
root.title('Retail Billing System')
# root.geometry('1270x680')
root.resizable(False,False)
root.iconbitmap('icon.ico')
 
# global var
cosmetic_price=0.0
grocery_price=0.0
cold_drink_p=0.0
cosmetic_tax=0.0
grocery_tax = 0.0
cold_drink_tax = 0.0

bath_soap_p =140
face_cream_p = 220
face_wash_p=150
hair_spray_p = 350
hair_gel_p=240
body_lotion_p = 350
rice_p = 320
oil_p = 450
dal_p = 85
wheat_p = 330
shugar_p = 440
tea_p = 110
mazaa_p =85
pepsi_p = 35
sprite_p = 120
dew_p = 45
frooti_p = 320
cocacola_p = 140
total_billl=0.0

bill_number=0
# Functionality
def total_bill():
    if name_entry.get()!='' and phone_entry.get()!= '':
        cosmetic_price_entry.delete(0,'end')
        grocery_price_entry.delete(0,'end')
        cold_drink_price.delete(0,'end')
        cosmetic_tax_entry.delete(0,'end')
        grocery_tax_entry.delete(0,'end')
        cold_drink_tax_entry.delete(0,'end')
        bath_soap = float(bath_soap_entry.get())
        face_cream = float(face_cream_entry.get())
        face_wash = float(face_wash_entry.get())
        hair_spray = float(hair_spray_entry.get())
        hair_gel = float(hair_gel_entry.get())
        body_lotion = float(body_lotion_entry.get())
        rice = float(rice_entry.get())
        oil = float(oil_entry.get())
        dal = float(dal_entry.get())
        wheat = float(wheat_entry.get())
        sugar = float(sugar_entry.get())
        tea = float(tea_entry.get())
        mazaa = float(mazaa_entry.get())
        pepsi = float(pepsi_entry.get())
        sprite = float(sprite_entry.get())
        dew = float(dew_entry.get())
        frooti = float(frooti_entry.get())
        cocacola = float(cocacola_entry.get())
        global cosmetic_price
        cosmetic_price= (bath_soap*140) + (face_cream*220) + (face_wash*150) + (hair_spray*350) + (hair_gel*240) + (body_lotion*350) 
        global grocery_price
        grocery_price= (rice*320) + (oil*450) + (dal*85) + (wheat*330) + (sugar*440) + (tea*110) 
        global cold_drink_p
        cold_drink_p= (mazaa*85) + (pepsi*35) + (sprite*120) + (dew*45) + (frooti*320) + (cocacola*140)
        cosmetic_price_entry.insert(0,' '+str(cosmetic_price))
        grocery_price_entry.insert(0,' '+str(grocery_price))
        cold_drink_price.insert(0,' '+str(cold_drink_p))
        global cosmetic_tax
        cosmetic_tax = (cosmetic_price*4)/100
        global grocery_tax
        grocery_tax = (grocery_price*2)/100
        global cold_drink_tax
        cold_drink_tax= (cold_drink_p*1)/100
        cosmetic_tax_entry.insert(0,' '+str(cosmetic_tax))
        grocery_tax_entry.insert(0,' '+str(grocery_tax))
        cold_drink_tax_entry.insert(0,' '+str(cold_drink_tax))
        global total_billl
        total_billl = cosmetic_price+grocery_price+cold_drink_p+cosmetic_tax+grocery_tax+cold_drink_tax
    else:
     messagebox.showerror(title='Error',message='Customer Details are Required!')



def clear_data():
    cosmetic_price_entry.delete(0,'end')
    grocery_price_entry.delete(0,'end')
    cold_drink_price.delete(0,'end')
    cosmetic_tax_entry.delete(0,'end')
    grocery_tax_entry.delete(0,'end')
    cold_drink_tax_entry.delete(0,'end')
    cosmetic_price_entry.insert(0,' 0.0')
    grocery_price_entry.insert(0,' 0.0')
    cold_drink_price.insert(0,' 0.0')
    cosmetic_tax_entry.insert(0,' 0.0')
    grocery_tax_entry.insert(0,' 0.0')
    cold_drink_tax_entry.insert(0,' 0.0')

    bath_soap_entry.delete(0,'end')
    face_wash_entry.delete(0,'end')
    face_cream_entry.delete(0,'end')
    hair_spray_entry.delete(0,'end')
    hair_gel_entry.delete(0,'end')
    body_lotion_entry.delete(0,'end')
    rice_entry.delete(0,'end')
    oil_entry.delete(0,'end')
    dal_entry.delete(0,'end')
    wheat_entry.delete(0,'end')
    sugar_entry.delete(0,'end')
    tea_entry.delete(0,'end')
    mazaa_entry.delete(0,'end')
    pepsi_entry.delete(0,'end')
    sprite_entry.delete(0,'end')
    dew_entry.delete(0,'end')
    frooti_entry.delete(0,'end')
    cocacola_entry.delete(0,'end')
    bath_soap_entry.insert(0,'0')
    face_wash_entry.insert(0,'0')
    face_cream_entry.insert(0,'0')
    hair_spray_entry.insert(0,'0')
    hair_gel_entry.insert(0,'0')
    body_lotion_entry.insert(0,'0')
    rice_entry.insert(0,'0')
    oil_entry.insert(0,'0')
    dal_entry.insert(0,'0')
    wheat_entry.insert(0,'0')
    sugar_entry.insert(0,'0')
    tea_entry.insert(0,'0')
    mazaa_entry.insert(0,'0')
    pepsi_entry.insert(0,'0')
    sprite_entry.insert(0,'0')
    dew_entry.insert(0,'0')
    frooti_entry.insert(0,'0')
    cocacola_entry.insert(0,'0')
    txt_area.delete("1.0", "end")  # Clear the text area
    name_entry.delete(0,'end')
    phone_entry.delete(0,'end')
    bill_entry.delete(0,'end')

def generate_bill():
    if name_entry.get() == '' and phone_entry.get()=='':
        messagebox.showerror(title='Error',message='Customer Details are Required!')
    elif (cosmetic_price_entry.get()=='' or cosmetic_price_entry.get()==' 0.0') and (grocery_price_entry.get()=='' or grocery_price_entry.get()==' 0.0') and (cold_drink_tax_entry.get()==''or cold_drink_tax_entry.get()==' 0.0'):
        messagebox.showerror(title='Error',message='No Product Selected!')
    else:    
        global bill_number
        bill_number = random.randint(500,1500)
        txt_area.delete("1.0", "end")  # Clear the text area
        txt_area.insert('end','\t    ** Welcome Customer **\n\n')
        txt_area.insert('end',f' Bill Number : {bill_number}\n')
        txt_area.insert('end',f' Customer Name : {name_entry.get()}\n')
        txt_area.insert('end',f' Phone Number : {phone_entry.get()}\n')
        txt_area.insert('end',' =========================================\n')
        txt_area.insert('end',' Products\t\t   QTY\t\t    Price\n')
        txt_area.insert('end',' =========================================\n')
        global cosmetic_tax
        global grocery_tax
        global cold_drink_tax
        entry_list = [bath_soap_entry,face_cream_entry,face_wash_entry,hair_spray_entry,hair_gel_entry,body_lotion_entry,
                      rice_entry,oil_entry,dal_entry,wheat_entry,sugar_entry,tea_entry,mazaa_entry,
                      pepsi_entry,sprite_entry,dew_entry,frooti_entry,cocacola_entry]
        label_list = ['Bath Soap','Face Cream','Face Wash','Hair Spray','Hair Gel','Body Lotion',
                      'Rice','Oil','Daal','Wheat','Sugar','Tea','Mazaa','Pepsi','Sprite','Dew','Frooti',
                      'Coca Cola']
        price_list = [140,220,150,350,240,350,320,450,85,330,440,110,85,35,120,45,320,140]
        index_list=[]
        a=0
        for i in entry_list:
            if i.get()=='0':
                a=a+1
            else:
                index_list.append(a)
                a=a+1
        
        for i in index_list:
            product = label_list[i]
            quantity = int(entry_list[i].get())
            price = price_list[i] * quantity
            txt_area.insert('end',f' {product}\t\t   {quantity}\t\t    {price}\n')
        txt_area.insert('end',' -----------------------------------------\n')
        txt_area.insert('end',f' Cosmetic Tax :\t\t\t\t    {cosmetic_tax}\n')
        txt_area.insert('end',f' Grocery Tax :\t\t\t\t    {grocery_tax}\n')
        txt_area.insert('end',f' Cold Drink Tax :\t\t\t\t    {cold_drink_tax}\n\n')
        global total_billl
        round_bill= round(total_billl,1)
        txt_area.insert('end',f' Total Bill :\t\t\t\t   {round_bill}\n')
        txt_area.insert('end',' -----------------------------------------\n')

        


def print_bill():
    if (cosmetic_price_entry.get()=='' or cosmetic_price_entry.get()==' 0.0') and (grocery_price_entry.get()=='' or grocery_price_entry.get()==' 0.0') and (cold_drink_tax_entry.get()==''or cold_drink_tax_entry.get()==' 0.0'):
        messagebox.showerror(title='Error',message='No Product Selected!')
    else:
        messagebox.askyesno(title='Confirmation',message='Do you want to save the bill?')
        bill = txt_area.get("1.0", "end")
        file_path = f"E:\GUI Projects\P5 - Retail Billing System\Bills\{bill_number}.txt"
        
        f = open(file_path, "w")
        f.write(bill)
        f.close()
        messagebox.showinfo(title='Success', message=f'Bill No.{bill_number} saved successfully!')


def load_file(file_path):
    with open(file_path, "r") as file:
        txt_area.delete("1.0", "end")  # Clear existing content
        txt_area.insert("1.0", file.read())

def search_bill():
    folder_path = "E:/GUI Projects/P5 - Retail Billing System/Bills"  # Replace with the path to the folder
    number = bill_entry.get()
    target_file_name = f"{number}.txt"    # Replace with the name of the file you're searching for

    target_file_path = folder_path + "/" + target_file_name

    try:
        load_file(target_file_path)
    except FileNotFoundError:
        txt_area.delete("1.0", "end")
        txt_area.insert("1.0", "File not found!")


def send_email():

    def send():
        try:
            ob = smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(sender_email_entry.get(),sender_password_entry.get())
            message = txt.get(1.0,'end')
            ob.sendmail(sender_email_entry.get(),recipient_email_entry.get(),message)
            ob.quit()
            messagebox.showinfo('Success','Bill is successfully sent')
        except:
             messagebox.showerror('Error','Something went wrong!')
      
    if txt_area.get(1.0,'end') == '\n':
        messagebox.showerror('Error','Bill is empty!')
    else:
        mail_window = tk.Toplevel()
        mail_window.title('Send Gmail') 
        mail_window.geometry('500x700')
        mail_window.config(bg='gray20')
        mail_window.resizable(False,False)
        header_lbl = tk.Label(mail_window,text='Gmail',
                        font=('times new roman',30,'bold'),fg='gold',bg='gray20',bd=5,relief='groove')
        header_lbl.pack(fill='x')

        sender_frame = tk.LabelFrame(mail_window,text='Sender',fg='gold',bg='gray20',bd=5,relief='groove',font=('times new roman',15,'bold'))
        sender_frame.pack(fill='x',pady=(5,5),padx=30)    

        sender_email_lbl = tk.Label(sender_frame,text="Email Address",fg='white',bg='gray20',font=('times new roman',15,'bold'))
        sender_email_lbl.grid(row=0,column=0,padx=(20,25),pady=15,sticky='w')
        sender_email_entry = tk.Entry(sender_frame,width=25,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))
        sender_email_entry.grid(row=0,column=1,padx=(0,20),pady=15)

        sender_password_lbl = tk.Label(sender_frame,text="Password",fg='white',bg='gray20',font=('times new roman',15,'bold'))
        sender_password_lbl.grid(row=1,column=0,padx=(20,25),pady=(0,15),sticky='w')
        sender_password_entry = tk.Entry(sender_frame,width=25,fg='black',show='*',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))
        sender_password_entry.grid(row=1,column=1,padx=(0,20),pady=(0,15))

        recipient_frame = tk.LabelFrame(mail_window,text='Recipient',fg='gold',bg='gray20',bd=5,relief='groove',font=('times new roman',15,'bold'))
        recipient_frame.pack(fill='x',pady=(5,25),padx=30)  
        recipient_email_lbl = tk.Label(recipient_frame,text="Email Address",fg='white',bg='gray20',font=('times new roman',15,'bold'))
        recipient_email_lbl.grid(row=0,column=0,padx=(20,25),pady=15,sticky='w')
        recipient_email_entry = tk.Entry(recipient_frame,width=25,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))
        recipient_email_entry.grid(row=0,column=1,padx=(0,20),pady=15)   
        message_lbl = tk.Label(recipient_frame,text="Message",fg='white',bg='gray20',font=('times new roman',15,'bold'))
        message_lbl.grid(row=1,column=0,padx=(20,25),pady=15,sticky='w',columnspan=2)
        
        txt = tk.Text(recipient_frame,height=15,width=44,yscrollcommand=scroll.set,font=('time new roman',9,'bold'))
        txt.grid(row=2,column=0,columnspan=2,pady=(0,15)) 
        txt.delete(1.0,'end')
        txt.insert('end',txt_area.get(1.0,'end'))


        send_btn = tk.Button(mail_window,command=send,text='Send',fg='black',width=15,bg='white',bd=5,font=('times new roman',12,'bold'))
        send_btn.pack()
        
        mail_window.mainloop()
    

# --------------->> GUI Phase
header_lbl = tk.Label(root,text='Retail Billing System',
                      font=('times new roman',30,'bold'),fg='gold',bg='gray20',bd=12,relief='groove')
header_lbl.pack(fill='x')

# Customer Details
customer_detail_frame = tk.LabelFrame(root,text='Customer Details',fg='gold',bg='gray20',bd=12,relief='groove',font=('times new roman',15,'bold'))
customer_detail_frame.pack(fill='x',pady=5)
name_lbl = tk.Label(customer_detail_frame,text='Name',fg='white',bg='gray20',font=('times new roman',15,'bold'))
name_lbl.grid(row=0,column=0,padx=(30,25))
name_entry = tk.Entry(customer_detail_frame,width=26,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))
name_entry.grid(row=0,column=1,padx=(0,20))

phone_lbl = tk.Label(customer_detail_frame,text='Phone Number',fg='white',bg='gray20',font=('times new roman',15,'bold'))
phone_lbl.grid(row=0,column=2,padx=(0,25))
phone_entry = tk.Entry(customer_detail_frame,width=26,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))
phone_entry.grid(row=0,column=3,padx=(0,20))

bill_lbl = tk.Label(customer_detail_frame,text='Bill Number',fg='white',bg='gray20',font=('times new roman',15,'bold'))
bill_lbl.grid(row=0,column=4,padx=(0,25))
bill_entry = tk.Entry(customer_detail_frame,width=26,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))
bill_entry.grid(row=0,column=5,padx=(0,25),pady=15)

search_btn = tk.Button(customer_detail_frame,command=search_bill,text='Search',fg='black',width=10,bg='white',bd=5,font=('times new roman',12,'bold'))
search_btn.grid(row=0,column=6)


# Middle Frame
mid_frame = tk.Frame(root)
mid_frame.pack(fill='x')

# cosmetics frame
cosmetics_frame = tk.LabelFrame(mid_frame,text='Cosmetics',fg='gold',bg='gray20',bd=12,relief='groove',font=('times new roman',15,'bold'))
cosmetics_frame.grid(row=0,column=0)

bath_soap_lbl = tk.Label(cosmetics_frame,text='Bath Soap',fg='white',bg='gray20',font=('times new roman',15,'bold'))
bath_soap_lbl.grid(row=0,column=0,sticky='w',padx=10,pady=9)
bath_soap_entry = tk.Spinbox(cosmetics_frame,width=11,from_=0,to=100,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))

bath_soap_entry.grid(row=0,column=1,padx=(10,25),pady=9)

face_cream_lbl = tk.Label(cosmetics_frame,text='Face Cream',fg='white',bg='gray20',font=('times new roman',15,'bold'))
face_cream_lbl.grid(row=1,column=0,sticky='w',padx=10,pady=9)
face_cream_entry = tk.Spinbox(cosmetics_frame,from_=0,to=100,width=11,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))

face_cream_entry.grid(row=1,column=1,padx=(10,25),pady=9)

face_wash_lbl = tk.Label(cosmetics_frame,text='Face Wash',fg='white',bg='gray20',font=('times new roman',15,'bold'))
face_wash_lbl.grid(row=2,column=0,sticky='w',padx=10,pady=9)
face_wash_entry = tk.Spinbox(cosmetics_frame,from_=0,to=100,width=11,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))

face_wash_entry.grid(row=2,column=1,padx=(10,25),pady=9)

hair_spray_lbl = tk.Label(cosmetics_frame,text='Hair Spray',fg='white',bg='gray20',font=('times new roman',15,'bold'))
hair_spray_lbl.grid(row=3,column=0,sticky='w',padx=10,pady=9)
hair_spray_entry = tk.Spinbox(cosmetics_frame,from_=0,to=100,width=11,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))

hair_spray_entry.grid(row=3,column=1,padx=(10,25),pady=9)

hair_gel_lbl = tk.Label(cosmetics_frame,text='Hair Gel',fg='white',bg='gray20',font=('times new roman',15,'bold'))
hair_gel_lbl.grid(row=4,column=0,sticky='w',padx=10,pady=9)
hair_gel_entry = tk.Spinbox(cosmetics_frame,from_=0,to=100,width=11,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))

hair_gel_entry.grid(row=4,column=1,padx=(10,25),pady=9)

body_lotion_lbl = tk.Label(cosmetics_frame,text='Body Lotion',fg='white',bg='gray20',font=('times new roman',15,'bold'))
body_lotion_lbl.grid(row=5,column=0,sticky='w',padx=10,pady=9)
body_lotion_entry = tk.Spinbox(cosmetics_frame,width=11,from_=0,to=100,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))

body_lotion_entry.grid(row=5,column=1,padx=(10,25),pady=9)

# Grocery Frame
grocery_frame = tk.LabelFrame(mid_frame,text='Grocery',fg='gold',bg='gray20',bd=12,relief='groove',font=('times new roman',15,'bold'))
grocery_frame.grid(row=0,column=1,padx=5)

rice_lbl = tk.Label(grocery_frame,text='Rice',fg='white',bg='gray20',font=('times new roman',15,'bold'))
rice_lbl.grid(row=0,column=0,sticky='w',padx=(15,10),pady=9)
rice_entry = tk.Spinbox(grocery_frame,from_=0,to=100,width=11,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))

rice_entry.grid(row=0,column=1,padx=(10,50),pady=9)

oil_lbl = tk.Label(grocery_frame,text='Oil',fg='white',bg='gray20',font=('times new roman',15,'bold'))
oil_lbl.grid(row=1,column=0,sticky='w',padx=(15,10),pady=9)
oil_entry = tk.Spinbox(grocery_frame,from_=0,to=100,width=11,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))
oil_entry.grid(row=1,column=1,padx=(10,50),pady=9)

dal_lbl = tk.Label(grocery_frame,text='Daal',fg='white',bg='gray20',font=('times new roman',15,'bold'))
dal_lbl.grid(row=2,column=0,sticky='w',padx=(15,10),pady=9)
dal_entry = tk.Spinbox(grocery_frame,from_=0,to=100,width=11,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))
dal_entry.grid(row=2,column=1,padx=(10,50),pady=9)

wheat_lbl = tk.Label(grocery_frame,text='Wheat',fg='white',bg='gray20',font=('times new roman',15,'bold'))
wheat_lbl.grid(row=3,column=0,sticky='w',padx=(15,10),pady=9)
wheat_entry = tk.Spinbox(grocery_frame,from_=0,to=100,width=11,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))

wheat_entry.grid(row=3,column=1,padx=(10,50),pady=9)

sugar_lbl = tk.Label(grocery_frame,text='Sugar',fg='white',bg='gray20',font=('times new roman',15,'bold'))
sugar_lbl.grid(row=4,column=0,sticky='w',padx=(15,10),pady=9)
sugar_entry = tk.Spinbox(grocery_frame,from_=0,to=100,width=11,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))

sugar_entry.grid(row=4,column=1,padx=(10,50),pady=9)

tea_lbl = tk.Label(grocery_frame,text='Tea',fg='white',bg='gray20',font=('times new roman',15,'bold'))
tea_lbl.grid(row=5,column=0,sticky='w',padx=(15,10),pady=9)
tea_entry = tk.Spinbox(grocery_frame,from_=0,to=100,width=11,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))
tea_entry.grid(row=5,column=1,padx=(10,50),pady=9)

# Cold drink Frame
cold_drink_frame = tk.LabelFrame(mid_frame,text='Cold Drinks',fg='gold',bg='gray20',bd=12,relief='groove',font=('times new roman',15,'bold'))
cold_drink_frame.grid(row=0,column=2,padx=5)

mazaa_lbl = tk.Label(cold_drink_frame,text='Mazaa',fg='white',bg='gray20',font=('times new roman',15,'bold'))
mazaa_lbl.grid(row=0,column=0,sticky='w',padx=10,pady=9)
mazaa_entry = tk.Spinbox(cold_drink_frame,from_=0,to=100,width=11,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))
mazaa_entry.grid(row=0,column=1,padx=(10,25),pady=9)

pepsi_lbl = tk.Label(cold_drink_frame,text='Pepsi',fg='white',bg='gray20',font=('times new roman',15,'bold'))
pepsi_lbl.grid(row=1,column=0,sticky='w',padx=10,pady=9)
pepsi_entry = tk.Spinbox(cold_drink_frame,from_=0,to=100,width=11,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))
pepsi_entry.grid(row=1,column=1,padx=(10,25),pady=9)

sprite_lbl = tk.Label(cold_drink_frame,text='Sprite',fg='white',bg='gray20',font=('times new roman',15,'bold'))
sprite_lbl.grid(row=2,column=0,sticky='w',padx=10,pady=9)
sprite_entry = tk.Spinbox(cold_drink_frame,from_=0,to=100,width=11,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))
sprite_entry.grid(row=2,column=1,padx=(10,25),pady=9)

dew_lbl = tk.Label(cold_drink_frame,text='Dew',fg='white',bg='gray20',font=('times new roman',15,'bold'))
dew_lbl.grid(row=3,column=0,sticky='w',padx=10,pady=9)
dew_entry = tk.Spinbox(cold_drink_frame,from_=0,to=100,width=11,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))
dew_entry.grid(row=3,column=1,padx=(10,25),pady=9)

frooti_lbl = tk.Label(cold_drink_frame,text='Frooti',fg='white',bg='gray20',font=('times new roman',15,'bold'))
frooti_lbl.grid(row=4,column=0,sticky='w',padx=10,pady=9)
frooti_entry = tk.Spinbox(cold_drink_frame,from_=0,to=100,width=11,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))
frooti_entry.grid(row=4,column=1,padx=(10,25),pady=9)

cocacola_lbl = tk.Label(cold_drink_frame,text='Coca Cola',fg='white',bg='gray20',font=('times new roman',15,'bold'))
cocacola_lbl.grid(row=5,column=0,sticky='w',padx=10,pady=9)
cocacola_entry = tk.Spinbox(cold_drink_frame,from_=0,to=100,width=11,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))
cocacola_entry.grid(row=5,column=1,padx=(10,25),pady=9)


# bill frame
bill_frame = tk.Frame(mid_frame,bd=12,relief='groove')
bill_frame.grid(row=0,column=3)
bill_area_lbl = tk.Label(bill_frame,text='Bill Area',fg='gold',bg='grey20',font=('times new roman',15,'bold'))
bill_area_lbl.pack(fill='x')
scroll = tk.Scrollbar(bill_frame,orient='vertical')
scroll.pack(side='right',fill='y')

txt_area = tk.Text(bill_frame,height=17,width=43,yscrollcommand=scroll.set)
txt_area.pack()
scroll.config(command=txt_area.yview)

# bottom frame
bottom_frame = tk.LabelFrame(root,text='Bill Menue',fg='gold',bg='gray20',bd=12,relief='groove',font=('times new roman',15,'bold'))
bottom_frame.pack(fill='x',pady=5)

cosmetic_price_lbl = tk.Label(bottom_frame,text='Cosmetic Price',fg='white',bg='gray20',font=('times new roman',15,'bold'))
cosmetic_price_lbl.grid(row=0,column=0,padx=(10,10),sticky='w',pady=5)
cosmetic_price_entry = tk.Entry(bottom_frame,width=15,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))
cosmetic_price_entry.grid(row=0,column=1,padx=(0,20),pady=5)

grocery_price_lbl = tk.Label(bottom_frame,text='Grocery Price',fg='white',bg='gray20',font=('times new roman',15,'bold'))
grocery_price_lbl.grid(row=1,column=0,padx=(10,10),sticky='w',pady=5)
grocery_price_entry = tk.Entry(bottom_frame,width=15,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))
grocery_price_entry.grid(row=1,column=1,padx=(0,20),pady=5)

cold_drink_price_lbl = tk.Label(bottom_frame,text='Cold Drink Price',fg='white',bg='gray20',font=('times new roman',15,'bold'))
cold_drink_price_lbl.grid(row=2,column=0,padx=(10,10),sticky='w',pady=5)
cold_drink_price = tk.Entry(bottom_frame,width=15,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))
cold_drink_price.grid(row=2,column=1,padx=(0,20),pady=5)

cosmetic_tax_lbl = tk.Label(bottom_frame,text='Cosmetic Tax',fg='white',bg='gray20',font=('times new roman',15,'bold'))
cosmetic_tax_lbl.grid(row=0,column=2,padx=(10,10),sticky='w',pady=5)
cosmetic_tax_entry = tk.Entry(bottom_frame,width=15,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))
cosmetic_tax_entry.grid(row=0,column=3,padx=(0,20),pady=5)

grocery_tax_lbl = tk.Label(bottom_frame,text='Grocery Tax',fg='white',bg='gray20',font=('times new roman',15,'bold'))
grocery_tax_lbl.grid(row=1,column=2,padx=(10,10),sticky='w',pady=5)
grocery_tax_entry = tk.Entry(bottom_frame,width=15,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))
grocery_tax_entry.grid(row=1,column=3,padx=(0,20),pady=5)

cold_drink_tax_lbl = tk.Label(bottom_frame,text='Cold Drink Tax',fg='white',bg='gray20',font=('times new roman',15,'bold'))
cold_drink_tax_lbl.grid(row=2,column=2,padx=(10,10),sticky='w',pady=5)
cold_drink_tax_entry = tk.Entry(bottom_frame,width=15,fg='black',bg='white',bd=5,relief='groove',font=('times new roman',12,'bold'))
cold_drink_tax_entry.grid(row=2,column=3,padx=(0,20),pady=5)

# Button Frames
bottom_in_frame = tk.Frame(bottom_frame,bg='white',bd=5,relief='groove')
bottom_in_frame.grid(row=0,column=4,rowspan=3)
total_btn = tk.Button(bottom_in_frame,pady=10,padx=20,text='Total',command=total_bill,font=('arial',14,'bold'),fg='gold',bg='grey20',bd=5,relief='groove')
total_btn.grid(row=0,column=0,padx=7)
bill_btn = tk.Button(bottom_in_frame,pady=10,command = generate_bill,padx=20,text='Bill',font=('arial',14,'bold'),fg='gold',bg='grey20',bd=5,relief='groove')
bill_btn.grid(row=0,column=1,padx=7)
email_btn = tk.Button(bottom_in_frame,pady=10,padx=20,text='Email',command=send_email,font=('arial',14,'bold'),fg='gold',bg='grey20',bd=5,relief='groove')
email_btn.grid(row=0,column=2,padx=7)
print_btn = tk.Button(bottom_in_frame,pady=10,padx=20,text='Print',command=print_bill,font=('arial',14,'bold'),fg='gold',bg='grey20',bd=5,relief='groove')
print_btn.grid(row=0,column=3,padx=7)
clear_btn = tk.Button(bottom_in_frame,pady=10,padx=20,command= clear_data,text='Clear',font=('arial',14,'bold'),fg='gold',bg='grey20',bd=5,relief='groove')
clear_btn.grid(row=0,column=4,padx=7)

root.mainloop()