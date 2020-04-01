from flask import Flask , request , jsonify
app = Flask(__name__)

from covid19indialocator_Copy import *


@app.route('/')
@app.route('/tracker/' , methods=['GET'])
def get_nearest_case():
        pin_code = request.args.get('pinCode')
        Latitude = request.args.get('latitude')
        Longitude = request.args.get('longitude')
        if Latitude is not None and Longitude is not None and len(Latitude)>0 and len(Longitude)>0:
            # query_info = {'Lat':float(Latitude) , 'Lng' : float(Longitude)}
            (mindist, cases, district, state , Lat, Lng) = get_nearest_case_with_geoloc(Latitude , Longitude)
        else:
            (mindist, cases, district, state , Lat, Lng) = get_nearest_case_with_pincode(pin_code)
            
        nearbyCase = False;
        if mindist<=2 :
             nearbyCase = True;
        response = jsonify({
            'present_in_locality':nearbyCase,
            'minDist': str(mindist),
            'cases' : str(cases),
            'district' : district,
            'state' : state,
            'lat' : str(Lat),
            'lng' : str(Lng),
        })
        response.status_code=200
        return response
        #print(location)

if __name__ == "__main__":
    app.run(debug=True)
