from jinja2 import Environment, PackageLoader
import os
import requests
from datetime import datetime
 
#Getting Data From The URL
response = requests.get('http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22')
data = response.json()

time_of_data = datetime.fromtimestamp(data['dt'])
#xcur_temp = 

#Putting the Data in The Template and Generating Output
env = Environment(loader=PackageLoader('app'))
template = env.get_template('index.html')
 
root = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(root, 'output.html')
 
with open(filename, 'w') as fh:
    fh.write(template.render(
        h1 = data['name'],
        current_temperature = data['main']['temp'],
        sky_info = data['weather'][0]['description'].title(),
        obtained_at = time_of_data,
        city = data['name'],
        weather = data['weather'][0]['main'],
        description = data['weather'][0]['description'].capitalize(),
        curr_temp = data['main']['temp'],
        max_temp = data['main']['temp_max'],
        min_temp = data['main']['temp_min'],
        pressure = data['main']['pressure'],
        humidity = data['main']['humidity'],
        visibility = data['visibility'],
    ))