# CityBikeApp

### Description of the project: 
This is part of pre-assignment project for [Solita Dev Academy Finland fall 2022.](https://github.com/solita/dev-academy-2022-fall-exercise)

The idea is create an API that will display the journy made by city bikes in the Helsinki Capital area.

The app is written using pythonn programing language. It  uses Flask web application framework to build the web app and  pandas liberary to read csv files

### Prerequisites: 
To run the application, it requires Flask web application frame work and  pandas liberary
Please install them first and make sure the Flask is running well. It is recomended to create 
a virtual environment and install the required liberaies spcific to this app.
### Configurations: 
Data set is larger than github recommended data size (i.e. 68.35 MB). So, it is not part of this repo but you can download first the dataset from 
this link and put it inside /data/citybikes/ directory.
### How to run the project? 
To run the application first clone this repo and cd to CityBikeApp direcotry. ``
Form the direcotry export FLASK_APP=city_bike_app.py. Then execute flask run
The app will run in the localhost with 50000 port address: http://127.0.0.1:5000 
Use the above address to test it in the browser  using full url address in http://127.0.0.1:5000/api/journey
The above GET request should resturn a dictionary containing    
   -"Departure station name", "Return station name","Covered distance (m)" in km and "Duration (sec.)" in minutes




### TODO: 
 - Implement Paginination so that all data will be displayed 
 - Connect to the database instade of loading to memory
 git filter-branch -f --index-filter 'git rm --cached --ignore-unmatch fixtures/11_user_answer.json'
