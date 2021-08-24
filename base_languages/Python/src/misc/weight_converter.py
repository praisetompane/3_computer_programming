weight = float(input("Weight: "))
unit_type = input("K for Kg or L lbs: ")

if unit_type.upper() == "K":
    print("Weight in lbs: %s" % str(weight/0.45))
elif unit_type.upper() == "L":
    kg_to_lbs_ratio = 2.205
    print("Weight in Kg: %s" % str(weight/kg_to_lbs_ratio))
else:
    print("Invalid weight unit supplied")