**Affordable House Price Estimator**

This project estimates house prices based on a few simple property details and tells the user whether the house is affordable or expensive compared to the median price in the dataset. The goal is to give a quick, data‑driven price estimate that can assist buyers, owners, or agents during basic decision‑making.
The work is implemented in Python using pandas, NumPy, scikit‑learn, and visualizations with Matplotlib and Seaborn.

**Features**
The model uses the following inputs:

Total square footage of the house
Number of bathrooms
Number of balconies
Distance to the nearest metro station (in meters, within a realistic range)

**Output:**

Estimated house price in lakhs
Estimated house price in rupees
Label: “Affordable” or “Expensive” based on the median price in the dataset

**Tech Stack**

Python
pandas, NumPy
Matplotlib, Seaborn
scikit‑learn (RobustScaler, train_test_split, LinearRegression)
**Linear Regression is used as a simple, interpretable baseline model for price estimation.**

**How It Works**

**1) Data Loading**

 Load the cleaned housing data CSV file.
 Keep only the required columns: total_sqft, bath, balcony, and price.
 Remove rows with missing values to avoid issues during training Feature Engineering
Add a new feature distance_metro using random integers between 200 and 5000 to represent distance to the nearest metro in meters.
This feature reflects how connectivity can influence house prices.
​
**2) Exploratory Data Analysis (EDA)**

Inspect the shape and first few rows of the dataset.
Use the IQR (Interquartile Range) method to detect outliers in all numeric columns.
Plot boxplots for each feature to visually inspect outliers.
Plot a Bar chart of mean values to get a quick overview of the data distribution.
​



Define X as the input features: total_sqft, bath, balcony, distance_metro.
Define y as the target variable: price.
Use RobustScaler to scale the features, which handles outliers better by using median and IQR instead of mean and standard deviation.​
Split the data into training and testing sets (80% train, 20% test) using train_test_split.

**3) Model Training and Evaluation**

Train a LinearRegression model on the scaled training data.
Print the feature coefficients to understand how each feature affects the estimated price.
Calculate the R² score on the test set to measure how well the model explains the variation in prices. Similar house price estimation models often use R² as the main performance metric.

**4) User Interaction and Estimation**

Take user input from the console for:
Square footage
Number of bathrooms
Number of balconies
Distance to the nearest metro (meters)
Scale the input using the same RobustScaler fitted earlier.
Estimate the house price using the trained model.
Convert the estimated price from lakhs to rupees and display both.
Compare the estimated price with the median price from the dataset and classify it as “Affordable” or “Expensive”.

**How to Run**

Clone or download the project folder.
Make sure the CSV file path in the code matches the location of your cleaned data file.
**Bengaluru_House_Data_Cleaned (1).csv** # Dataset

**Install the required Python libraries:**
bash
**pip install pandas numpy matplotlib seaborn scikit-learn**
Run the script or notebook:
bash
python main.py
or open the notebook in Jupyter/Colab and run all cells.

When prompted, enter:

1)Square footage
2)Number of bathrooms
3)Number of balconies
4)Distance to metro (in meters)

The model will print the estimated price and whether it is affordable or expensive.

​
