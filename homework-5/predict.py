import pickle

from flask import Flask
from flask import request, jsonify

app = Flask("clientscore")

model_file = "model1.bin"
dv_file = "dv.bin"

with open(model_file, "rb") as f_in_model: #read binary
    model = pickle.load(f_in_model)

with open(dv_file, "rb") as f_in_dv: #read binary
    dv = pickle.load(f_in_dv)

@app.route('/predict', methods=['POST'])

def predict():
    client = request.get_json()

    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0,1]

    return jsonify(float(y_pred))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
