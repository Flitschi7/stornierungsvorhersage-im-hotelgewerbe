%pip install r-requirements.txt

from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load('best_model.pkl')
dataframe = pd.read_csv("export_dataframe.csv", sep=";")
model_columns = list(dataframe.columns)  
joblib.dump(model_columns, 'model_columns.pkl') 


def prepare_data(*args):
    total_stay = int(args[0])
    total_guests = int(args[1])
    type_of_meal_plan = args[2]
    required_car_parking_space = int(args[3])
    room_type_reserved = args[4]
    lead_time = int(args[5])
    arrival_month = int(args[6])
    market_segment_type = args[7]
    repeated_guest = int(args[8])
    no_of_previous_cancellations = int(args[9])
    no_of_previous_bookings_not_canceled = int(args[10])
    avg_price_per_room = float(args[11])  
    no_of_special_requests = int(args[12])
  
    data = pd.DataFrame({
        "total_guests": [total_guests],
        "total_stay": [total_stay],
        "type_of_meal_plan": [type_of_meal_plan],
        "required_car_parking_space": [required_car_parking_space],
        "room_type_reserved": [room_type_reserved],
        "lead_time": [lead_time],
        "arrival_month": [arrival_month],
        "market_segment_type": [market_segment_type],
        "repeated_guest": [repeated_guest],
        "no_of_previous_cancellations": [no_of_previous_cancellations],
        "no_of_previous_bookings_not_canceled": [no_of_previous_bookings_not_canceled],
        "avg_price_per_room": [avg_price_per_room],
        "no_of_special_requests": [no_of_special_requests]
    })

    data_encoded = pd.get_dummies(data, columns=['type_of_meal_plan', 'room_type_reserved', 'market_segment_type'])

    for column in model_columns:
        if column not in data_encoded.columns:
            data_encoded[column] = 0

    data_encoded = data_encoded[model_columns]

    return data_encoded

def convert_prediction_to_result(prediction):
    if prediction[0] == 1:
        return "eine"
    else:
        return "keine"

@app.route('/')
def booking_form():
    return render_template('booking_form.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    total_stay = request.form['total_stay']
    total_guests = request.form['total_guests']
    type_of_meal_plan = request.form['type_of_meal_plan']
    required_car_parking_space = request.form['required_car_parking_space']
    room_type_reserved = request.form['room_type_reserved']
    lead_time = request.form['lead_time']
    arrival_month = request.form['arrival_month']
    market_segment_type = request.form['market_segment_type']
    repeated_guest = request.form['repeated_guest']
    no_of_previous_cancellations = request.form['no_of_previous_cancellations']
    no_of_previous_bookings_not_canceled = request.form['no_of_previous_bookings_not_canceled']
    avg_price_per_room = request.form['avg_price_per_room']
    no_of_special_requests = request.form['no_of_special_requests']

    data = prepare_data(
        total_stay, total_guests, type_of_meal_plan, required_car_parking_space,
        room_type_reserved, lead_time, arrival_month,
         market_segment_type, repeated_guest,
        no_of_previous_cancellations, no_of_previous_bookings_not_canceled,
        avg_price_per_room, no_of_special_requests
    )

    prediction = model.predict(data)
    result = convert_prediction_to_result(prediction)
    print(result)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)