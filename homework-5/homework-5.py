import pickle

model_file = "model1.bin"
dv_file = "dv.bin"

with open(model_file, "rb") as f_in_model: #read binary
    model = pickle.load(f_in_model)

with open(dv_file, "rb") as f_in_dv: #read binary
    dv = pickle.load(f_in_dv)

client = {
    "job": "management", 
    "duration": 400, 
    "poutcome": "success"
}

X = dv.transform([client])
probability = model.predict_proba(X)[:,1]

print(probability)