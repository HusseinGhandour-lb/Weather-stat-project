#import needed libraries
import requests
import time
import csv
import os

#api key and a url to test the countries
url_test = 'http://api.openweathermap.org/data/2.5/weather?q=france,&appid=69d023182d7ca5fe26c94743b6168acc&units=metric'
API_KEY = "69d023182d7ca5fe26c94743b6168acc"

#countries to extracts it data
countries = {'europe':['france','england','germany'],
             'north_europe':['sweden','norway','finland']}

#check if the file existis
file_exists = os.path.isfile("wether_data.csv")

#open the file and save the data


with open("wether_data.csv", mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    if not file_exists:
        writer.writerow(['continent', 'country', 'temperature', 'temperature_sense', 
                        'humidity', 'pressure', 'speed', 'clouds', 'clock', 'date'])

    #loop over the countries in the dict
    for continent, region  in countries.items():
        for country in region:
            
            #sending request to website to get all the needed data
            try:
                url = f"http://api.openweathermap.org/data/2.5/weather?q={country},&appid={API_KEY}&units=metric"
                response = requests.get(url)    
                
                if response.status_code == 200:
                    data = response.json()
        
                    temp = data['main']['temp']
                    temp_feels = data['main']['feels_like']
                    humidity = data['main']['humidity']
                    pressure = data['main']['pressure']
                    speed = data['wind']['speed']
                    clouds = data['clouds']['all']
                    clock = time.strftime("%H:%M:%S", time.localtime())
                    date = time.strftime("%y-%m-%d", time.localtime())
                    
                    #write the extracted data line by line in csv file
                    writer.writerow([continent,country,temp,temp_feels,humidity,
                                    pressure,speed,clouds,clock,date])
                    
                    time.sleep(2)
                    
                else:
                    print(response.status_code)
            
            #to catch an error while sending request       
            except Exception as e:
                print(f"error: {e}, at {country}")
                        
            except KeyError as e:
                print(f'error2: {e}')
                
print('Done! :)')