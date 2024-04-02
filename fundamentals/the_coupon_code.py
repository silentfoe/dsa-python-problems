# Your online store likes to give out coupons for special occasions. Some customers try to cheat the system by entering invalid codes or using expired coupons.

# Task
# Your mission:
# Write a function called checkCoupon which verifies that a coupon code is valid and not expired.

# A coupon is no more valid on the day AFTER the expiration date. All dates will be passed as strings in this format: "MONTH DATE, YEAR".

# Examples:
# checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")  == True
# checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")  == False

# my solution: 

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    
    #listing months in order to index
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    #setting up format for the dates to compare 
    curr_date = current_date.replace(',','').split()
    ex_date = expiration_date.replace(',','').split()

    if type(entered_code) != type(correct_code):
        return False
    
    if entered_code != correct_code:
        return False
    
    if int(ex_date[2]) > int(curr_date[2]):
        return True
    
    if int(ex_date[2]) < int(curr_date[2]):
        return False
    
    if months.index(ex_date[0]) < months.index(curr_date[0]):
        return False
    
    if curr_date[0] == ex_date[0] and int(ex_date[1]) < int(curr_date[1]):
        return False
    

    
    return True


# very clever solutions found on the solutions page: 


#1
import datetime
def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code is correct_code:
        return(datetime.datetime.strptime(current_date,'%B %d, %Y') <= datetime.datetime.strptime(expiration_date,'%B %d, %Y'))
    return False

#2
import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    strptime = datetime.datetime.strptime
    format = "%B %d, %Y"
    return strptime(current_date, format) <= strptime(expiration_date, format) and\
                             entered_code is correct_code