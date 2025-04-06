height = float(input("Enter your height in meter: "))
weight = int(input("Enter your weight in kg: "))

bmi_cal =  weight / height ** 2

if bmi_cal < 18.5 :
    print(f"Your bmi is {bmi_cal} and you are underweight.")
elif bmi_cal >= 18.5 and bmi_cal < 25:
    print(f"Your bmi is {bmi_cal} and you are normal weight.")
elif bmi_cal >= 25 and bmi_cal < 30 :  
    print(f"Your bmi is {bmi_cal} and you are slightly overweight.") 
elif bmi_cal >= 30 and bmi_cal < 35 :  
    print(f"Your bmi is {bmi_cal} and you are slightly overweight.") 
else:
    print(f"Your bmi is {bmi_cal} and you are need clinical obvse ")        

