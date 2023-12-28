# Write function bmi that calculates body mass index (bmi = weight / height2).

# if bmi <= 18.5 return "Underweight"

# if bmi <= 25.0 return "Normal"

# if bmi <= 30.0 return "Overweight"

# if bmi > 30 return "Obese"

# my solution: 

def bmi(weight, height):
    bmi = weight / height**2
    
    if bmi <= 18.5:
        return 'Underweight'
    elif bmi <= 25.0:
        return 'Normal'
    elif bmi <= 30.0:
        return 'Overweight'
    else:
        return 'Obese'
    

# other cool solution I found on the code wars solutions page: 

def bmi(weight, height):
    b = weight / height ** 2
    #using boolean operations to see if 'b' is greater than the number. If 'b' is greater, it will be true which will equal '1'. the sum of all the options will be 0,1,2,3 which indicates the index. 
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]