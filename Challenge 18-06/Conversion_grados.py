celsius = int(input('Ingresa grados Celcius '))

celsius_a_fahrenheit = lambda celsius: (celsius * 9/5) + 32
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit")