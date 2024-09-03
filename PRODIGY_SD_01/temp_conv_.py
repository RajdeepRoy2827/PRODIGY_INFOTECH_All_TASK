#BUILDING A TEMPERATURE CONVERSION PROGRAM
scale = input("Choose the temperature scale Celsius or Fahrenheit or Kelvin (C/F/K): ")
temp = float(input("Enter the temperature you want to convert : "))

if scale == "C":
    temp_f = (temp * 9) / 5 + 32
    print(f"The temperature in fahrenheit is : {temp_f} °f", end=" & ")
    temp_k = (temp + 273.15)
    print(f"Kelvin is : {temp_k} k")        #To print the fahrenheit and kelvin temperature!
elif scale == "F":
    temp_c = (temp - 32) * 5 / 9
    print(f"The temperature in celsius is : {temp_c} °c", end=" & ")
    temp_k = (temp - 32) * 5 / 9 + 273.15
    print(f"Kelvin is : {temp_k} k")        #To print the Celsius and Kelvin temperatue!
elif scale == "K":
    temp_c = (temp - 273.15)
    print(f"The temperature in celsius is : {temp_c} °c", end=" & ")
    temp_f = (temp - 273.15) * 9 / 5 + 32
    print(f"Fahrenheit is : {temp_f} °f")   #To print the Celsius and Fahrenheit temperature!
else:
    print(f"{scale} is  an invalid scale of measurement!!")
