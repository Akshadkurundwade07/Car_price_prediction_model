from flask import Flask, render_template
import pandas as pd 

app = Flask(__name__)
car = pd.read_csv('cleaned_car.csv')

@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    car_models = car['model'].unique()
    year = car['year'].unique()
    fuel_type = car['fuel_type'].unique()
    return render_template('index.html', companies=companies, car_models=car_models, year=year, fuel_type=fuel_type)

if __name__ == "__main__":
    app.run(debug=True)
