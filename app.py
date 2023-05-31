from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    height = float(request.form['height']) / 100  # convert cm to m
    weight = float(request.form['weight'])
    bmi = weight / (height ** 2)
    bmi_category = get_bmi_category(bmi)
    return render_template('result.html', bmi=bmi, bmi_category=bmi_category)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Normal weight'
    elif bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

if __name__ == '__main__':
    app.run()
