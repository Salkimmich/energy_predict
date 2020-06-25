import numpy as np
import os
from flask import Flask, jsonify, request, render_template
from joblib import load


app = Flask(__name__)

model = load('model.joblib')


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = [request.form.get('relative_compactness'),
                request.form.get('surface_area'),
                request.form.get('wall_area'),
                request.form.get('roof_area'),
                request.form.get('overall_height'),
                request.form.get('orientation'),
                request.form.get('glazing_area'),
                request.form.get('glazing_area_distribution')
                ]

        data = np.array([np.asarray(data, dtype=float)])

        # Use the predict method of the model to
        # get the prediction for unseen data
        result = model.predict(data)
        prediction = f'Heating load: {np.round(result[0][0], 3)} , Cooling load: {np.round(result[0][1], 3)}'
        return render_template('index.html', pred=prediction)
    else:
        return render_template('index.html', pred='')


@app.route('/api-predict', methods=['POST'])
def results():

    # Request data as json
    req_data = request.get_json(force=True)

    # Use the predict method of the model to
    # get the prediction for unseen data
    prediction = model.predict([np.array(list(req_data.values()))])

    # return the result back in json
    return jsonify({"heating_load": np.round(prediction[0][0], 3),
                    "cooling_load": np.round(prediction[0][1], 3)})


# Start the server, continuously listen to requests.
# If it doesn't show in browser go to
# localhost:5000
if __name__ == "__main__":
    app.run(host='0.0.0.0')
