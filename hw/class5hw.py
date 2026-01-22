# age=int(input("Enter your age: "))
# isStudent = input("are you a student: ")
# baseTicket = 200
# studentDiscount = 0
# if age <12:
#     ageDiscount= baseTicket * 50/100
# finalTicketPrice = baseTicket - ageDiscount
# if isStudent == "yes":
#     studentDiscount = finalTicketPrice * 20/100
# finalTicketPrice = finalTicketPrice - studentDiscount
# print(f"""
#       base ticket         : {baseTicket}
#       age discount        : {ageDiscount}
#       student discount    : {studentDiscount}
#       ----------------------------------
#       final price         : {finalTicketPrice}
      
# """)

#Assignment 3
unitOfElectricity = int(input("How many units of electricity did you use? "))
cost = 0
if unitOfElectricity >= 0 and unitOfElectricity <= 100:
    bill = unitOfElectricity * 5
if unitOfElectricity >= 101 and unitOfElectricity <= 300:
    bill = unitOfElectricity * 7
if unitOfElectricity > 300:
    bill = unitOfElectricity * 10
if bill > 1500:
    cost = bill * 8/100
finalBill = bill + cost
print(f"""
      unit of electricity     :    {unitOfElectricity}
      surcharge               :    {cost}
      ------------------------------------------------
      final bill              :    {finalBill}
      
      """)