#James Dutton


hours = float(raw_input("Please enter number of hours: "))
rate = float(raw_input("Please enter pay per hour: "))
total = hours * rate

if hours <= 40:
    print("Your pay is: " + str(hours * rate))
else:
    OT = hours - 40
    print("Your pay is: " + str((hours - OT) * rate + OT * rate * 1.5))
    
