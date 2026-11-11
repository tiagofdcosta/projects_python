print("welcome to tip calculator!")
bill = float(input("Whats the total bill? € "))
percentage = int(input("Whats the percentage do you prefer? "))
tip = percentage / 100 + 1
people = int(input("How many people will pay? "))
total_coast_per_people = bill * tip / people
final = round(total_coast_per_people, 2)
print(f"The total coast per person is = {final} €")
