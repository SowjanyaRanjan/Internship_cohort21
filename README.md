**Bengaluru House Price Prediction
Predicts house prices in Bengaluru using Linear Regression. You give it the square footage, number of bathrooms, and balconies — it gives you a price estimate in Lakhs.**

**Dataset**
Using Bengaluru_House_Data_Cleaned.csv — a pre-cleaned dataset of Bengaluru real estate listings. The three features used for training are total_sqft, bath, and balcony, with price as the target.
**Libraries used**
pandas, numpy
scikit-learn (LinearRegression, RobustScaler, train_test_split)

**What the notebook does**
Loads the data, picks the relevant features, splits into train/test (80/20), scales with RobustScaler (chosen because housing data has a lot of outliers), fits a linear regression model, and checks performance with MAE and R² score.
At the end there's a small input section where you type in sqft, bathrooms, and balconies and it prints out the predicted price.

**Running it**
Open in Google Colab or Jupyter. Make sure the dataset is at /content/Bengaluru_House_Data_Cleaned.csv or update the path. Run all cells top to bottom.

**Sample output**
Enter Total Square Feet: 1200
Enter Number of Bathrooms: 2
Enter Number of Balconies: 1

Estimated House Price: 85.47 Lakhs
Predicted Price: ₹ 8,547,000

**Things to keep in mind**
**The model only uses 3 features so accuracy is limited**. Adding location data would probably improve it a lot. The dataset also needs to already be cleaned before loading — **there's no preprocessing in this notebook.**
