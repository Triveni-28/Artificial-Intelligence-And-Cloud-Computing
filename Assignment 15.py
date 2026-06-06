""" Assignment of 12th march """ 


"""

                Weather
               /      \
           Sunny      Rainy
            /           \
       Humidity?        Windy?
      /    \           /      \
   High   Normal     Yes      No
    |        |        |       |
  Don't     Play   Don't    Play
   Play            Playweather = input("Enter weather (sunny/rainy): ").lower()

"""

""" Assignment of 12th march """

"""
                Weather
               /      \
           Sunny      Rainy
            /           \
       Humidity?        Windy?
      /    \           /      \
   High   Normal     Yes      No
    |        |        |       |
  Don't     Play   Don't    Play
   Play
"""

weather = input("Enter weather (sunny/rainy): ").lower()

if weather == "sunny":
    humidity = input("Enter humidity (high/normal): ").lower()
    
    if humidity == "high":
        print("Decision: Don't Play")
    else:
        print("Decision: Play")

elif weather == "rainy":
    wind = input("Is it windy? (yes/no): ").lower()
    
    if wind == "yes":
        print("Decision: Don't Play")
    else:
        print("Decision: Play")

else:
    print("Weather condition not recognized")


