from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder


#initialization of flask
app = Flask(__name__, template_folder='templates')

#load the model created from prediction
model = joblib.load('models/mushroom_tree_model.pkl')

#make a directionary that holds all thepossible categories
feature_mappings = {
    'cap_shape': ['bell', 'conical', 'convex', 'flat', 'knobbed', 'sunken'],
    'cap_surface': ['fibrous', 'grooves', 'scaly', 'smooth'],
    'cap_color': ['brown', 'buff', 'cinnamon', 'gray', 'green', 
                  'pink', 'purple', 'red', 'white', 'yellow'],
    'bruises': ['bruises', 'no bruises'],
    'odor': ['almond', 'anise', 'creosote', 'fishy', 'foul', 
             'musty', 'none', 'pungent', 'spicy'],
    'gill_attachment': ['attached', 'descending', 'free', 'notched'],
    'gill_spacing': ['close', 'crowded', 'distant'],
    'gill_size': ['broad', 'narrow'],
    'gill_color': ['black', 'brown', 'buff', 'chocolate', 'gray', 
                   'green', 'orange', 'pink', 'purple', 'red', 
                   'white', 'yellow'],
    'stalk_shape': ['enlarging', 'tapering'],
    'stalk_surface_above_ring': ['fibrous', 'scaly', 'silky', 'smooth'],
    'stalk_surface_below_ring': ['fibrous', 'scaly', 'silky', 'smooth'],
    'stalk_color_above_ring': ['brown', 'buff', 'cinnamon', 'gray', 
                               'orange', 'pink', 'red', 'white', 'yellow'],
    'stalk_color_below_ring': ['brown', 'buff', 'cinnamon', 'gray', 
                               'orange', 'pink', 'red', 'white', 'yellow'],
    'veil_color': ['brown', 'orange', 'white', 'yellow'],
    'ring_number': ['none', 'one', 'two'],
    'ring_type': ['cobwebby', 'evanescent', 'flaring', 'large', 'none', 
                  'pendant', 'sheathing', 'zone'],
    'spore_print_color': ['black', 'brown', 'buff', 'chocolate', 'green', 
                          'orange', 'purple', 'white', 'yellow'],
    'population': ['abundant', 'clustered', 'numerous', 'scattered', 
                   'several', 'solitary'],
    'habitat': ['grasses', 'leaves', 'meadows', 'paths', 'urban', 
                'waste', 'woods']
}

#creates a dictionary of LabelEncoder from feature_mapping
encoders = {feature: LabelEncoder().fit(values) for feature, values in feature_mappings.items()}

# GET (to load the page) and POST (to handle form submissions)
@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        features = [
            request.form.get("cap_shape"),
            request.form.get("cap_surface"),
            request.form.get("cap_color"),
            request.form.get("bruises"),
            request.form.get("odor"),
            request.form.get("gill_attachment"),
            request.form.get("gill_spacing"),
            request.form.get("gill_size"),
            request.form.get("gill_color"),
            request.form.get("stalk_shape"),
            request.form.get("stalk_surface_above_ring"),
            request.form.get("stalk_surface_below_ring"),
            request.form.get("stalk_color_above_ring"),
            request.form.get("stalk_color_below_ring"),
            request.form.get("veil_color"),
            request.form.get("ring_number"),
            request.form.get("ring_type"),
            request.form.get("spore_print_color"),
            request.form.get("population"),
            request.form.get("habitat"),
        ]

        #loops through the selected features and encodes them into numeric values.
        encoded_features = []

        for feature, feature_name in zip(features, feature_mappings.keys()):
            encoder = encoders[feature_name]  # Get the pre-trained encoder for this feature
            encoded_value = encoder.transform([feature])[0]  # Transform the feature to its encoded value
            encoded_features.append(encoded_value)

        #creating a data frame for the encoded features becasue the tree is trained in data fram
        encoded_features_df = pd.DataFrame([encoded_features], columns=model.feature_names_in_)

        print("Encoded Features: ", encoded_features_df)

        #making the prediction, 0 means edible and 1 means poisonous
        prediction = model.predict(encoded_features_df)[0]
        result = "Edible" if prediction == 0 else "Poisonous"

        return render_template("index.html", prediction_text=f"Your mushroom is: {result}")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

