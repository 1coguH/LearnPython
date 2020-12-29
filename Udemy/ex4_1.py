# $0.51 per hour 

# cost of one server per day
HourCost = 0.51
DaylyCost = (HourCost * 24.0 )
number_of_days = float(input ("How many days wil you be rumming your server?"))
number_of_servers = float(input ("how many servers do you want?"))
print ("Your server will cost ${}" .format (number_of_days * DaylyCost * number_of_servers))

#cost per month
Monthly_Cost = (DaylyCost * 365.4 / 12.0)
Number_of_months = float(input ("How many months will you be running your server?"))
Amount_of_servers =  float(input ("How many servers will you be using?"))
print ("Your server will cost ${}" .format (Number_of_months * Monthly_Cost * Amount_of_servers))

#how many days for a certain amount of money 
money = float (input ("how much money do you have?"))
servers = float (input ("how many servers do you want?"))
print ("Your can run your servers for {} days" .format (DaylyCost * servers / money ))