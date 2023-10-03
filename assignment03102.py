def computepay(hours, rate):
    try :
        hours = float(hours)
        rate = float(rate)
    except ValueError :
        print("Error : Please enter numeric values for hours and rate.")
        return
    
    if hours > 40:
        overtime_hours = hours - 40
        regular_pay = 40 * rate
        overtime_pay = overtime_hours * rate * 1.5
        total_pay = regular_pay + overtime_pay
    else :
        total_pay = hours * rate
    
    return total_pay


hours = input("Enter hours worked : ")
rate = input("Enter hourly rate :")
salary = computepay(hours, rate)
if salary is not None :
    print("Total salary : " + str(salary))