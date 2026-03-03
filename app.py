from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load Model
model = pickle.load(open("house_price_model.pkl", "rb"))

avg_price = 80  # Lakhs

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        sqft = float(request.form['sqft'])
        bath = int(request.form['bath'])
        balcony = int(request.form['balcony'])
        distance = float(request.form['distance'])

        input_data = np.array([[sqft, bath, balcony, distance]])

        prediction = model.predict(input_data)[0]

        # If model predicts in RUPEES
        price_rupees = "{:,.2f}".format(prediction)
        price_lakhs = round(prediction / 1000, 3)

        status = "Affordable" if price_lakhs < avg_price else "Expensive"

        return render_template("index.html",
                            prediction_text=price_lakhs,
                            rupees=price_rupees,
                            status=status)

    except Exception as e:
        return f"Error occurred: {e}"
    
if __name__ == "__main__":
    app.run(debug=True)