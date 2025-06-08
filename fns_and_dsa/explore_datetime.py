import  datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:",formatted)

def calculate_future_date(daysToAdd):
    future_date = datetime.datetime.now() + datetime.timedelta(days=daysToAdd)
    print("Future date:", future_date.strftime("%Y-%m-%d"))


display_current_datetime()
daysToAdd = int(input("Enter the number of days to add to the current date: "))
calculate_future_date(daysToAdd)