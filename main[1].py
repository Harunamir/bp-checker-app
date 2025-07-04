from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html>
  <head>
    <title>Blood Pressure Checker</title>
    <style>
      body { font-family: Arial; padding: 30px; background-color: #f2f2f2; }
      .container { background: white; padding: 20px; border-radius: 10px; max-width: 400px; margin: auto; }
      input[type=number] { width: 100%; padding: 8px; margin: 5px 0 10px; }
      button { padding: 10px 15px; background-color: #007BFF; color: white; border: none; border-radius: 5px; }
    </style>
  </head>
  <body>
    <div class="container">
      <h2>Blood Pressure Checker</h2>
      <form method="post">
        <label>Systolic Pressure:</label>
        <input type="number" name="systolic" required><br>
        <label>Diastolic Pressure:</label>
        <input type="number" name="diastolic" required><br>
        <button type="submit">Check</button>
      </form>
      {% if result %}
        <h3>Result:</h3>
        <p><strong>Status:</strong> {{ result }}</p>
      {% endif %}
    </div>
  </body>
</html>
"""

def check_blood_pressure(systolic, diastolic):
    if systolic < 90 or diastolic < 60:
        return "Low Blood Pressure (Hypotension)"
    elif 90 <= systolic < 120 and 60 <= diastolic < 80:
        return "Normal Blood Pressure"
    elif 120 <= systolic < 130 and diastolic < 80:
        return "Elevated Blood Pressure"
    elif 130 <= systolic < 140 or 80 <= diastolic < 90:
        return "High Blood Pressure Stage 1 (Hypertension)"
    elif 140 <= systolic or 90 <= diastolic:
        return "High Blood Pressure Stage 2 (Hypertension)"
    else:
        return "Consult a doctor"

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        systolic = int(request.form['systolic'])
        diastolic = int(request.form['diastolic'])
        result = check_blood_pressure(systolic, diastolic)
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)
