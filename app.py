# app.py
# Dylan Todd
# Created: 12.04.23
# Updated: 12.04.23

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extract parameters from form
        market_condition = float(request.form.get('market_condition', 0))
        vacancy_rate = float(request.form.get('vacancy_rate', 0))
        construction_delay = int(request.form.get('construction_delay', 0))

        # Run the stress test simulation
        simulation_result = run_stress_test(market_condition, vacancy_rate, construction_delay)

        # Display results
        return render_template('result.html', simulation_result=simulation_result)
    return render_template('index.html')

def run_stress_test(market_condition, vacancy_rate, construction_delay):
    # Simplified logic for stress test simulation
    # Placeholder for more complex calculations
    impact_score = market_condition * 0.5 + vacancy_rate * 0.3 + construction_delay * 0.2
    return max(min(impact_score, 100), 0)  # Score between 0 and 100

if __name__ == '__main__':
    app.run(debug=True)