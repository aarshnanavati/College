
city_temp = {}
n = int(input("Enter the number for dicitionary:"))

for i in range(n):
    city = input("Enter the name of city : ")
    temp = float(input("Enter the temperature "))
    city_temp[city] =  temp

cleaned_city = {}
for city,temp in city_temp.items():
    if 15 <= temp <= 40 : 
        cleaned_city[city] = temp

print(cleaned_city)