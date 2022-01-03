print("How many Kilometers did you cycle today?")
kms = input()
miles = float(kms)/1.60934
rounded_miles = round(miles, 2)
print(f"Your {kms} km ride was {rounded_miles} miles")
