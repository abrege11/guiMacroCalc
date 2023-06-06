"""
CREATED BY ABRAHAM BREGE 5/10/2023

"""


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Fitness Center")
        self.master.geometry("800x600")
        self.create_widgets()
    
    def create_widgets(self):
        # Create notebook
        notebook = ttk.Notebook(self.master)
        notebook.grid(row=0, column=0, sticky="nsew")

        # Create Macros page
        macros_frame = ttk.Frame(notebook)
        notebook.add(macros_frame, text="Macros")


        #option menu 1 for activity level
        activitylvl = ['__________________________', 'Little or no exercise, desk job', 'Light exercise or sports 1-3 days a week', 'Moderate exercise or sports 3-5 days a week', 'Hard exercise or sports 6-7 days a week', 'Very hard exercise/sports, physical job']
        self.activitylvl_var = tk.StringVar(value=activitylvl[0])
        activitylvl_dropdown = ttk.OptionMenu(macros_frame, self.activitylvl_var, *activitylvl)


        #option menu 2 for goal
        goal = ['__________________________', 'Lose Weight', 'Gain Weight', 'Maintain Weight']
        self.goal_var = tk.StringVar(value=goal[0])
        goal_dropdown = ttk.OptionMenu(macros_frame, self.goal_var, *goal)


        #initiate the values for the calc function
        self.gender_var = tk.StringVar()
        self.weight_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.heightFT_var = tk.StringVar()
        self.heightIN_var = tk.StringVar()







        #create labels
        gender_label = tk.Label(macros_frame, text="Gender:")
        weight_label = tk.Label(macros_frame, text="Weight in LBS:")
        age_label = tk.Label(macros_frame, text="Age:")
        height_label = tk.Label(macros_frame, text="Enter your height below")
        heightFT_label = tk.Label(macros_frame, text="Feet:")
        heightIN_label = tk.Label(macros_frame, text="Inches:")
        activitylvl_label = tk.Label(macros_frame, text="Activity Level:")
        goal_label = tk.Label(macros_frame, text="Goal:")


        # Create buttons
        self.male_button = tk.Checkbutton(macros_frame, text="Male", variable=self.gender_var, onvalue=1, offvalue=0)
        self.female_button = tk.Checkbutton(macros_frame, text="Female", variable=self.gender_var, onvalue=2, offvalue=0)
        self.calculate_button = tk.Button(macros_frame, text="Calculate", command=self.calculate)


        #Create entry boxes
        self.weight_entry = tk.Entry(macros_frame, textvariable=self.weight_var)
        self.age_entry = tk.Entry(macros_frame, textvariable=self.age_var)
        self.heightFT_entry = tk.Entry(macros_frame, textvariable=self.heightFT_var)
        self.heightIN_entry = tk.Entry(macros_frame, textvariable=self.heightIN_var)

        # Place labels and buttons and entry boxes in grid layout
        gender_label.grid(row=0, column=0, padx=10, pady=10)
        weight_label.grid(row=2, column=0, padx=10, pady=10)
        age_label.grid(row=3, column=0, padx=10, pady=10)
        height_label.grid(row=4, column=0, padx=10, pady=10)
        heightFT_label.grid(row=5, column=0, padx=10, pady=10)
        heightIN_label.grid(row=6, column=0, padx=10, pady=10)
        activitylvl_label.grid(row=7, column=0, padx=10, pady=10)
        goal_label.grid(row=8, column=0, padx=10, pady=10)


        self.male_button.grid(row=0, column=1, padx=10, pady=10)
        self.female_button.grid(row=1, column=1, padx=10, pady=10)
        self.calculate_button.grid(row=9, column=1, padx=10, pady=10)

       
        self.weight_entry.grid(row=2, column=1, padx=10, pady=10)
        self.age_entry.grid(row=3, column=1, padx=10, pady=10)
        self.heightFT_entry.grid(row=5, column=1, padx=10, pady=10)
        self.heightIN_entry.grid(row=6, column=1, padx=10, pady=10)
        activitylvl_dropdown.grid(row=7, column=1, padx=10, pady=10)
        goal_dropdown.grid(row=8, column=1, padx=10, pady=10)


        self.bmr_label = tk.Label(macros_frame, text="")
        self.tdee_label = tk.Label(macros_frame, text="")
        self.dc_label = tk.Label(macros_frame, text="")
        self.dp_label = tk.Label(macros_frame, text="")
        self.df_label = tk.Label(macros_frame, text="")


    #button functions
    def calculate(self):
        #try/catch for the input since it is being parsed
        try:    
            weight = float(self.weight_entry.get())
            age = int(self.age_entry.get())

            height_ft = int(self.heightFT_entry.get()) * 12
            height_in = int(self.heightIN_entry.get())

            #check if weight, age and height are valid
            if weight <= 0 or age <= 0 or height_ft <= 0 or height_in < 0 or height_in >= 12:
                raise ValueError
            
            height = float(height_ft) + float(height_in)

            gender = int(self.gender_var.get())

            #convert the selection of activitylvl to an int that I can use in the eq
            if self.activitylvl_var.get() == '__________________________':
                raise ValueError
            elif self.activitylvl_var.get() == 'Little or no exercise, desk job':
                activity_lvl = 1.2
            elif self.activitylvl_var.get() == 'Light exercise or sports 1-3 days a week':
                activity_lvl = 1.375
            elif self.activitylvl_var.get() == 'Moderate exercise or sports 3-5 days a week':
                activity_lvl = 1.55
            elif self.activitylvl_var.get() == 'Hard exercise or sports 6-7 days a week':
                activity_lvl = 1.725
            elif self.activitylvl_var.get() == 'Very hard exercise/sports, physical job':
                activity_lvl = 1.9

            #convert goal into an into that i can use in the eq
            if self.goal_var.get() == '__________________________':
                raise ValueError
            elif self.goal_var.get() == 'Lose Weight':
                goal = 1
            elif self.goal_var.get() == 'Gain Weight':
                goal = 2
            elif self.goal_var.get() == 'Maintain Weight':
                goal = 3

            #put user input into calculations
            hbBMR = self.harrisBenedictBMR(gender, weight, height, age)
            hbTDEE = self.harrisBenedictTDEE(gender, weight, height, age, activity_lvl)
            msBMR = self.mifflinStJeorBMR(gender, weight, height, age)
            msTDEE = self.mifflinStJeorTDEE(gender, weight, height, age, activity_lvl)


            #average out resutls for most accurate response
            BMR = (hbBMR + msBMR) // 2
            BMRprint = round(BMR, 2)
            TDEE = (hbTDEE + msTDEE) // 2
            TDEEprint = round(TDEE, 2)


            #take goal input and calc the nutrition macros for that
            if goal == 1:
                dailyCal = TDEE - 500

                dailyCarbs = (.4 * dailyCal) / 4
                DCprint = round(dailyCarbs, 2)

                dailyProtien = (.3 * dailyCal) / 4
                DPprint = round(dailyProtien, 2) 

                dailyFat = (.3 * dailyCal) / 9
                DFprint = round(dailyFat, 2)


            elif goal == 2:   
                dailyCal = TDEE + 500

                dailyCarbs = (.5 * dailyCal) / 4 
                DCprint = round(dailyCarbs, 2)

                dailyProtien = (.3 * dailyCal) / 9
                DPprint = round(dailyProtien, 2) 

                dailyFat = (.2 * dailyCal) / 9
                DFprint = round(dailyFat, 2)


            elif goal == 3:
                dailyCal = TDEE

                dailyCarbs = (.45 * dailyCal) / 4
                DCprint = round(dailyCarbs, 2)               
                
                dailyProtien = (.25 * dailyCal) / 4
                DPprint = round(dailyProtien, 2) 
                
                dailyFat = (.3 * dailyCal) / 9 
                DFprint = round(dailyFat, 2)


        #the exception thrown
        except ValueError:
            root.after(0, lambda: messagebox.showerror(title='Invalid Input', message='Please enter valid input.'))


        #declaring the labels of the users results to be set
        self.bmr_label.config(text="BMR: " + str(BMRprint) + " calories")
        self.tdee_label.config(text="TDEE: " + str(TDEEprint) + " calories")
        self.dc_label.config(text="Daily Carbs: " + str(DCprint) + " grams")
        self.dp_label.config(text="Daily Protein: " + str(DPprint) + " grams")
        self.df_label.config(text="Daily Fats: " + str(DFprint) + " grams")

        #declaring the location of the users results
        self.bmr_label.grid(row=0, column=4, padx=10, pady=10)
        self.tdee_label.grid(row=1, column=4, padx=10, pady=10)
        self.dc_label.grid(row=2, column=4, padx=10, pady=10)
        self.dp_label.grid(row=3, column=4, padx=10, pady=10)
        self.df_label.grid(row=4, column=4, padx=10, pady=10)
    

    #first equation used for TDEE
    def harrisBenedictTDEE(self, gender, weight, height, age, activity_lvl):
        
        kgWeight = weight *.45359237
        cmHeight = height * 2.54

        if gender == 1:
            BMR = 88.362 + (13.397 * kgWeight) + (4.799 * cmHeight) - (5.677 * age)
            TDEE = BMR * activity_lvl
            return TDEE
        elif gender == 2:
            BMR = 447.593 + (9.247 * kgWeight) + (3.098 * cmHeight) - (4.330 * age)
            TDEE = BMR * activity_lvl
            return TDEE
    #first equation used for BMR        
    def harrisBenedictBMR(self, gender, weight, height, age):
        
        kgWeight = weight *.45359237
        cmHeight = height * 2.54

        if gender == 1:
            BMR = 88.362 + (13.397 * kgWeight) + (4.799 * cmHeight) - (5.677 * age)
            return BMR
        elif gender == 2:
            BMR = 447.593 + (9.247 * kgWeight) + (3.098 * cmHeight) - (4.330 * age)
            return BMR       
    #second equation used for BMR          
    def mifflinStJeorBMR(self, gender, weight, height, age):
        
        kgWeight = weight *.45359237
        cmHeight = height * 2.54        

        if gender == 1:
            BMR = (10 * kgWeight) + (6.25 * cmHeight) - (5 * age) + 5
            return BMR
        elif gender == 2:
            BMR = (10 * kgWeight) + (6.25 * cmHeight) - (5 * age) - 161
            return BMR
    #second equation used for TDEE        
    def mifflinStJeorTDEE(self, gender, weight, height, age, activity_lvl):
        
        kgWeight = weight *.45359237
        cmHeight = height * 2.54        

        if gender == 1:
            BMR = (10 * kgWeight) + (6.25 * cmHeight) - (5 * age) + 5
            TDEE = BMR * activity_lvl
            return TDEE
        elif gender == 2:
            BMR = (10 * kgWeight) + (6.25 * cmHeight) - (5 * age) - 161
            TDEE = BMR * activity_lvl
            return TDEE 


   
    






root = tk.Tk()
app = MainWindow(root)
app.mainloop()
