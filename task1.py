def temperature(value,unit):
    unit=unit.upper()
    if unit=='C':
        kelvin=value+273.15
        fahrenheit=value*1.8+32
        print(f"{value} Celsius= {fahrenheit:.2f} Fahrenheit")
        print(f"{value} Celsius= {kelvin:.2f} Kelvin")
    elif unit=='F':
        celsius=(value-32)/1.8
        kelvin=(value + 459.67)*5/9
        print(f"{value} Fahrenheit={celsius:.2f} Celsius")
        print(f"{value} Fahrenheit={kelvin:.2f} Kelvin")
    elif unit=='K':
        celsius=value-273.15
        fahrenheit=value*1.8 -459.67
        print(f"{value} Kelvin={celsius:.2f} Celsius")
        print(f"{value} Kelvin={fahrenheit:.2f} Fahrenheit")
    
value=float(input("Enter the temperature value:"))
unit=input("Enter the unit(C for Celsius,F for fahrenheit,k for Kelvin):")
print(temperature(value,unit))
        
    
    
              
