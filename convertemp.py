def displayWelcome():
    
    print('This program will convert a range of tempratures')
    print('Enter (F) to convert Fahrenheit to Celcius')
    print('Enter (C) to convert Celsius to Fahrenheit\n')
    
def getConvertTo():
    
    which = input('Enter selection: ')
    while which != 'F' and which != 'C':
        which = input('Enter selection: ')
        
    return which
    
def displayFahrenToCelsius(start, end):
    
    print('\n Degrees', ' Degrees')
    print('Fahrenheit', 'Celsius')
    
    for temp in range(start, end +1):
        converted_temp = (temp - 32) * 5/9
        print(' ', format(temp, '4.1f'), ' ', format(converted_temp, '4.1f'))
        
def displayCelsiusToFahren(start, end):
    
    print('\n Degrees', ' Degrees')
    print(' Celsius', 'Fahrenheit')
    
    for temp in range(start, end + 1):
        converted_temp = (9/5 * temp) + 32
        print(' ', format(temp, '4.1f'), ' ', format(converted_temp, '4.1f'))
        
# ---- main

# Display program welcome
displayWelcome()

# Get which conversion from user
which = getConvertTo()

# Get range of tempratures to convert
temp_start = int(input('Enter starting temprature to convert: '))
temp_end = int(input('Enter ending temprature to convert: '))

# Display range of converted tempratures
if which == 'F':
    displayFahrenToCelsius(temp_start, temp_end)
else:
    displayCelsiusToFahren(temp_start, temp_end)
