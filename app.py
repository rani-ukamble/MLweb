from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the model
my_model = joblib.load("marks_model")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        hrs = float(request.form['hours'])
        prediction = my_model.predict([[hrs]])
        return render_template('index.html', prediction_text=f'Your future marks will be {prediction[0]}')

if __name__ == '__main__':
    app.run(debug=True)
