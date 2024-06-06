from flask import Flask, request, render_template

app = Flask(__name__)

def from_celsius(C):
    F = (C * 9 / 5) + 32
    K = C + 273.15
    return F, K

def from_fahrenheit(F):
    C = (5 / 9) * (F - 32)
    K = C + 273.15
    return C, K

def from_kelvin(K):
    C = K - 273.15
    F = (C * 9 / 5) + 32
    return C, F

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    scale = request.form['scale']
    temp = float(request.form['temperature'])
    
    if scale == 'Celsius':
        F, K = from_celsius(temp)
        result = f"Fahrenheit = {F}, Kelvin = {K}"
    elif scale == 'Fahrenheit':
        C, K = from_fahrenheit(temp)
        result = f"Celsius = {C}, Kelvin = {K}"
    elif scale == 'Kelvin':
        C, F = from_kelvin(temp)
        result = f"Celsius = {C}, Fahrenheit = {F}"
    else:
        result = "Invalid choice."

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
