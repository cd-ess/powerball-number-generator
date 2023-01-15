# powerball.py
import random

"""Return randomly generated Powerball ticket numbers.
The result should look like this:

~~~~~~POWERBALL~~~~~~
┌───────────────┐───┐
| 55 63 28 20 47| 17|
└───────────────└───┘"""
# Declare an empty list and append 5 randomly generated integers from 1 to 69.
five_numbers = []
while len(five_numbers) < 5:
    number = random.randint(1,69)
    if number not in five_numbers:
        five_numbers.append(number)

# Sort the list, convert the integers to strings and pad it with 0 if it is less than 2 digits long. (01, 02, 03, etc...)
five_numbers.sort() 
five_numbers = [str(x).zfill(2) for x in five_numbers]

# Generate powerball number, 1 to 26, convert to string, pad with 0.
powerball_number = str(random.randint(1, 26)).zfill(2)

# Create a header for the ticket
ticket_header = " POWERBALL ".center(23, "~")

print(ticket_header)
print("┌────────────────┐────┐")
print("|", five_numbers[0], five_numbers[1], five_numbers[2], five_numbers[3], five_numbers[4], "|", powerball_number, "|")
print("└────────────────└────┘")
