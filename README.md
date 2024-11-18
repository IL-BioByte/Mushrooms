### Project Overview
As more people explore the outdoors and take up foraging, the risk of consuming poisonous mushrooms has become a growing concern. 
For many, distinguishing between edible and toxic mushrooms can be challenging, especially when there’s a lack of knowledge or experience. 
In fact, some mushrooms can look remarkably similar, and misidentification can have dangerous consequences.

The Mushroom Edibility Predictor is a practical tool that uses decision tree to help user determine whether a mushroom is edible or poisonous based on its physical characteristics. 
By analyzing features like cap shape, color, odor, and spore print, the model classifies mushrooms into two categories: safe to eat or harmful. 
The idea is to make it easy for anyone to learn about mushroom safety, whether they're foraging in the wild or just curious about different species.

You can try the application here: [Mushroom Edibility Predictor](https://mushrooms-itve.onrender.com/)

### Data Source
This dataset is sourced from the UCI Machine Learning Repository, and consists of more than 8000 mushroom samples.

### Data Description - Key Features

1. Edible: The mushroom is safe to eat.
1. Poisonous: The mushroom is harmful and potentially toxic.
1. Cap shape: The shape of the mushroom's cap.
1. Cap surface: The texture of the mushroom’s cap. 
1. Cap color: The color of the mushroom’s cap.
1. Bruises: Indicates whether the mushroom bruises when handled. 
1. Odor: The odor of the mushroom. 
1. Gill attachment: How the gills are attached to the stem.
1. Gill spacing: The spacing between the gills. 
1. Gill size: The size of the gills. 
1. Gill color: The color of the gills. 
1. Stalk shape: The shape of the stalk.
1. Stalk root: The root-like structure of the stalk.
1. Stalks urface above ring, stalk surface below ring, stalk color above ring, stalk color below ring: The color below the stalk’s ring.
1. Veil color: The color of the veil.
1. Ring number: The number of rings on the stalk.
1. Ring type: The type of ring.
1. Spore print color: The color of the mushroom’s spore print.
1. Population: The population density of the mushroom in the area. 
1. Habitat: The type of environment where the mushroom is found.

### Model Evaluation and Performance
The Mushroom Edibility Predictor was built using a Decision Tree classifier, which excels at making clear decisions based on the features provided. 
The model achieved 100% accuracy on the training dataset, which initially seemed like a great result. 
However, to ensure that this high accuracy reflects real-world performance, we evaluated the model using a confusion matrix.
This matrix indicates that the model correctly classified every mushroom sample—no false positives (edible mushrooms wrongly classified as poisonous) or false negatives (poisonous mushrooms wrongly classified as edible). 
![image](https://github.com/user-attachments/assets/d02bff9d-c21d-4754-806b-841f5cf5dafe)


### User Interface (UI)
The Mushroom Edibility Predictor was designed with a simple and intuitive user interface to make it easy for users to interact with the model and make predictions. 


   
