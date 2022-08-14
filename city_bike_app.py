from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)


@app.route('/api/journey', methods=['GET'])
def getData():
    # gets the journey data for this case it only gets  journey data for May
    if request.method=='GET':
        #TODO use pagination to render all the data to broweser
        # For the time being get only the first 1000 raw values
        iter_csv = pd.read_csv('data/citybikes/2021-05.csv', iterator=True, nrows=1000, chunksize=100)
        # Filter the data set so only jonrines with  duration > 10 sec and distance > 10 meter are loaded to the memory
        journey_df = pd.concat([chunk[(chunk['Duration (sec.)'] > 10 ) & (chunk['Covered distance (m)'] > 10)] for chunk in iter_csv])
        
        return {'journey': journey_df.to_dict()}, 200
    
if __name__ == '__main__':
    app.run(debug=True)