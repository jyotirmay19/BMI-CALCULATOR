from tkinter import *

def calculate_bmi():
    weight = float(e1.get())  
    height = float(e2.get()) 
    if height == 0 or weight == 0:
        result_label.config(text=f'Please Enter a valid Parameters.')
    else:
        bmi = (weight / (height ** 2))*10000    
    if bmi<18.5:    
         result_label.config(text=f'Your BMI is {bmi:.2f} and You Have Underweight')
    elif bmi>=18.5 and bmi<=24.9:
         result_label.config(text=f'Your BMI is {bmi:.2f} and You Have Healthy weight')
    elif bmi>=25 and bmi<=29.9:
         result_label.config(text=f'Your BMI is {bmi:.2f} and You Have Overweight')  
    else:
         result_label.config(text=f'Your BMI is {bmi:.2f} and You Have Obesity')  
             
    
master = Tk()
master.title("BMI CALCULATOR")
master.geometry("400x150")


Label(master, text='Enter Your Weight [Kg]').grid(row=0)
Label(master, text='Enter Your Height [cm]').grid(row=2)

e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=2, column=1)

calculate_button = Button(master, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=3, columnspan=2)

result_label = Label(master, text='   ',font=("Arial", 10))
result_label.grid(row=6, columnspan=2)

mainloop()