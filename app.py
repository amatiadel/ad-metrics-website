from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    num_entries = 1
    results = None
    summary = None
    error = None

    if request.method == 'POST':
        action = request.form.get('action')
        num_entries = int(request.form.get('num_entries', 1))

        if action == 'update':
            return render_template('index.html', num_entries=num_entries)

        elif action == 'calculate':
            try:
                results = []
                total_budget_no_vat = 0
                total_budget_with_vat = 0
                total_clicks = 0

                for i in range(num_entries):
                    budget = float(request.form[f'budget_{i}'])
                    clicks = float(request.form[f'clicks_{i}'])

                    budget_no_vat = budget / 1.2
                    cpc_no_vat = budget_no_vat / clicks if clicks > 0 else 0

                    total_budget_no_vat += budget_no_vat
                    total_budget_with_vat += budget
                    total_clicks += clicks

                    results.append({
                        'row': f'Row {i + 1}',
                        'cpc_no_vat': round(cpc_no_vat, 2),
                        'budget_no_vat': round(budget_no_vat, 2),
                        'budget_with_vat': round(budget, 2),
                        'clicks': int(clicks)
                    })

                summary = {
                    'total_budget_no_vat': round(total_budget_no_vat, 2),
                    'total_budget_with_vat': round(total_budget_with_vat, 2),
                    'total_clicks': int(total_clicks)
                }

            except (ValueError, KeyError):
                error = "Пожалуйста, введите действительные числовые значения"

    return render_template('index.html', num_entries=num_entries, results=results, summary=summary, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)