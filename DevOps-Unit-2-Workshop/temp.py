def temp_list(input_string):
    """Convert comma-separated string to a list of float"""
    temperatures_list=[]
    for temp in input_string.split(","):
        temperatures_list.append(float(temp))
    return temperatures_list

def average_temperature(temperatures):
    """Calculate the average temperature"""
    total = 0
    for temp in temperatures:
        total += temp
    return total/len(temperatures)

def celcius_to_fahrenheit(celcius):
    """Convert celcius to fahrenheit"""
    return celcius * 9/5 + 32

# main
input_string = input("Enter the temperatures in Celcius, separated by commas: ")

# convert the input_string into a list of temperatures
temperatures = temp_list(input_string)

# calculate average temp and print them
avg_temp = average_temperature(temperatures)
print(f"Average Temperature: {avg_temp} C")

# convert the list temp to fahrenheit

temp_in_fahrenheit = []
for temp in temperatures:
    temp_in_fahrenheit.append(celcius_to_fahrenheit(temp))

# print list of temperatures in fahrenheit
for temp in temp_in_fahrenheit:
    print(f"{temp}")


#print(input_string)
#print(temperatures)
#print(avg_temp)