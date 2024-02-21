from flask import Flask, render_template, request, redirect, url_for
from service_pension import calculate_service_pension_no_disability, calculate_service_pension_with_disability
from family_pension import handle_harness_yes,handle_harness_no
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def pension_type():
    return render_template('pensiontype.html')

@app.route('/next_page', methods=['POST'])
def next_page():
    pensionType = request.form['pensionType']

    if pensionType == "service":
        return render_template('next_page.html', pensionType=pensionType)
    elif pensionType == "family":
        return render_template('harnessnew.html', pensionType=pensionType)
    else:
        return render_template('error_page.html', message="Invalid pensionType")

@app.route('/family_pension_result', methods=['POST'])
def family_pension_result():
    harness = request.form['died-in-harness']
    service_type = request.form['serviceType']
    rank = request.form['rank']
    years_served_input = request.form['yearsServed'] + '.' + request.form['monthsServed']
    date_of_death = request.form['date-of-death']
    date_of_death = datetime.strptime(date_of_death, '%Y-%m-%d')

    # Format the datetime object to 'DD/MM/YYYY' string
    formatted_date_death_str = date_of_death.strftime('%d/%m/%Y')

    dependent_date_of_birth = request.form['dependent-date-of-birth']
    dependent_date_of_birth = datetime.strptime(dependent_date_of_birth, '%Y-%m-%d')

    # Format the datetime object to 'DD/MM/YYYY' string
    formatted_dependent_date_birth_str = dependent_date_of_birth.strftime('%d/%m/%Y')


    if harness.lower() == "yes":
        family_pension_amount, pension_type, additional_pension_amount, age = handle_harness_yes(service_type, rank, years_served_input, formatted_date_death_str, formatted_dependent_date_birth_str)
        return render_template('family_pension_result.html', pension_type = pension_type, family_pension_amount=family_pension_amount, additional_pension_amount = additional_pension_amount, age = age)
    elif harness.lower() == "no":
        date_of_birth = request.form['date-of-birth']
        date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')

        # Format the datetime object to 'DD/MM/YYYY' string
        formatted_date_birth_str = date_of_birth.strftime('%d/%m/%Y')
 
        date_of_discharge = request.form['date-of-discharge']
        date_of_discharge = datetime.strptime(date_of_discharge, '%Y-%m-%d')

        # Format the datetime object to 'DD/MM/YYYY' string
        formatted_date_str = date_of_discharge.strftime('%d/%m/%Y')

        family_pension_amount, pension_type, additional_pension_amount, age = handle_harness_no(service_type, rank, years_served_input, formatted_date_death_str, formatted_date_birth_str, formatted_date_str, formatted_dependent_date_birth_str)
        return render_template('family_pension_result.html', pension_type = pension_type, family_pension_amount=family_pension_amount, additional_pension_amount = additional_pension_amount, age = age)

@app.route('/submit_page', methods=['POST'])
def submit_page():
    service_type = request.form['service_type']
    rank = request.form['rank']
    years_served_input = request.form['years'] + '.' + request.form['months']
    date_of_birth = request.form['date_of_birth']
    date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')

    # Format the datetime object to 'DD/MM/YYYY' string
    formatted_date_birth_str = date_of_birth.strftime('%d/%m/%Y')

    date_of_discharge = request.form['date_of_discharge']
    date_of_discharge = datetime.strptime(date_of_discharge, '%Y-%m-%d')

    # Format the datetime object to 'DD/MM/YYYY' string
    formatted_date_str = date_of_discharge.strftime('%d/%m/%Y')
    disability = request.form['disability']

    if disability.lower() == "no":
        service_pension_amount, additional_pension_amount, age = calculate_service_pension_no_disability(service_type, rank, years_served_input, formatted_date_birth_str, formatted_date_str, disability)
        return render_template('submit_page.html', disability=disability, service_pension_amount=service_pension_amount, additional_pension_amount = additional_pension_amount, age = age)

    elif disability.lower() == "yes":
        disability_percentage = request.form['disability_percentage']
        disability_percentage = float(disability_percentage.rstrip('%'))

        service_pension_amount, disability_pension_amount, additional_service_pension_amount, additional_disability_pension_amount, age = calculate_service_pension_with_disability(
            service_type, rank, years_served_input, formatted_date_birth_str, formatted_date_str, disability, disability_percentage
        )

        return render_template('submit_page.html', disability=disability, service_pension_amount=service_pension_amount, disability_pension_amount=disability_pension_amount, additional_service_pension_amount = additional_service_pension_amount, additional_disability_pension_amount = additional_disability_pension_amount, age = age)

    return render_template('error_page.html', message="Invalid disability status")

if __name__ == '__main__':
    app.run(debug=True)
