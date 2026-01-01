import datetime

final_year = int(input("Enter the final year: "))

current_year = datetime.datetime.now().year

print("Leap years from", current_year, "to", final_year, ":")


for year in range(current_year, final_year + 1):
    # Step 6: Check if the year is a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        # Step 7: Print the leap year
        print(year)