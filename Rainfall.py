def get_rainfall():
    rain_dict = {}
    while True:
        city_name = input('City name').strip()

        if not city_name:
            break
        
        rain = int(input('How much rain ').strip())
        rain_dict[city_name] = rain_dict.get(city_name,0) + rain

    for city , rain in rain_dict.items():
        print(city,': ',rain)

get_rainfall()
    

        

