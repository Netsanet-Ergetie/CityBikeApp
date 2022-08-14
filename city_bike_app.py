from flask import Flask, request
import pandas as pd

app = Flask(__name__)

# Converts distance in metter to KM
def convert_meter_to_km(distance):
        return round(float(distance)/1000, 2)

# Converts Duration in seconds to minutes
def convert_second_to_minutes(seconds):
        return round(float(seconds)/60, 2)

def getJourny(journey_df):
    # For each journy return
    # "Departure station name"
    # "Return station name"
    #"Covered distance (m)" in km
    # "Duration (sec.)" in minutes
    journey_df['Covered distance (km)'] = journey_df.apply(lambda row: convert_meter_to_km(row['Covered distance (m)']), axis=1)
    journey_df['Duration (minute)'] = journey_df.apply(lambda row: convert_meter_to_km(row['Duration (sec.)']), axis=1)
    return journey_df[["Departure station name","Return station name","Covered distance (km)", "Duration (minute)"]]

@app.route('/api/journey', methods=['GET'])
def getData():
    # gets the journey data for this case it only gets  journey data for May
    if request.method=='GET':
        #TODO use pagination to render all the data to broweser
        # For the time being get only the first 1000 raw values
        fields = ["Departure station name","Return station name","Covered distance (m)", "Duration (sec.)"]

        iter_csv = pd.read_csv('data/citybikes/2021-05.csv', iterator=True, nrows=1000, usecols=fields, chunksize=100)
       
        # Filter the data set so only jonrines with  duration > 10 sec and distance > 10 meter are loaded to the memory
        journey_df = pd.concat([chunk[(chunk['Duration (sec.)'] > 10 ) & (chunk['Covered distance (m)'] > 10)] for chunk in iter_csv])
                
        journey_df = getJourny(journey_df)

        return {'journey': journey_df.to_dict()}, 200
    
if __name__ == '__main__':
    app.run(debug=True)