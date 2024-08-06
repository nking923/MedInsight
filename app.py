from flask import app, render_template, request


@app.route('/search', methods=['POST'])
def search():
    drug_name = request.form['drug_name']
    min_rating = float(request.form['min_rating']) if request.form['min_rating'] else 0
    max_rating = float(request.form['max_rating']) if request.form['max_rating'] else 10
    start_date = request.form['start_date']
    end_date = request.form['end_date']

    # Filter based on drug name
    results = df[df['drugName'].str.contains(drug_name, case=False, na=False)] # type: ignore
    
    # Filter based on rating range
    results = results[(results['rating'] >= min_rating) & (results['rating'] <= max_rating)]
    
    # Filter based on date range
    if start_date:
        results = results[results['date'] >= start_date]
    if end_date:
        results = results[results['date'] <= end_date]

    return render_template('results.html', drug_name=drug_name, results=results.to_dict(orient='records'))
