from datetime import date

# Get today's date
today = date.today()

# Format the date as YYYY-MM-DD
formatted_date = today.strftime("%Y-%m-%d")

# Display the formatted date
print("Today's date is:", formatted_date)
