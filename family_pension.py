import mysql.connector
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def convert_years_served(years_served_input, date_of_death):
    years_served = float(years_served_input.split(".")[0])

    if datetime.strptime(date_of_death, "%d/%m/%Y") > datetime(1983, 6, 18):
        if 1 <= int(years_served_input.split(".")[1]) <= 3:
            years_served += 0.0
        elif 4 <= int(years_served_input.split(".")[1]) <= 8:
            years_served += 0.5
        elif 9 <= int(years_served_input.split(".")[1]) <= 11:
            years_served += 1.0
    else:
        if 1 <= int(years_served_input.split(".")[1]) <= 5:
            years_served += 0.0
        elif 6 <= int(years_served_input.split(".")[1]) <= 11:
            years_served += 0.5

    if years_served >= 33.0:
        years_served = 33.0

    return years_served

def handle_harness_yes(service_type, rank, years_served_input, date_of_death, dependent_date_of_birth):
    # Database connection
    db = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Apple#2013",
        database="orop_db"
    )

    family_pension_amount = 0.0
    years_served = convert_years_served(years_served_input, date_of_death)

    dependent_date_of_birth = datetime.strptime(dependent_date_of_birth, '%d/%m/%Y')

    dependent_date_of_birth_80 = (dependent_date_of_birth + relativedelta(years=80)).date()
    dependent_date_of_birth_85 = (dependent_date_of_birth + relativedelta(years=85)).date()
    dependent_date_of_birth_90 = (dependent_date_of_birth + relativedelta(years=90)).date()
    dependent_date_of_birth_95 = (dependent_date_of_birth + relativedelta(years=95)).date()
    dependent_date_of_birth_100 = (dependent_date_of_birth + relativedelta(years=100)).date()

    # Assuming date_of_death is a string in the format 'dd/mm/yyyy'
    date_of_death = datetime.strptime(date_of_death, '%d/%m/%Y')


    pension_end_date_10_years = date_of_death + relativedelta(years=10)
    current_date = datetime.now()
    age = current_date.year - dependent_date_of_birth.year - (
            (current_date.month, current_date.day) < (dependent_date_of_birth.month, dependent_date_of_birth.day)
    )

    current_date_normalized = datetime(current_date.year, current_date.month, current_date.day)
    pension_end_date_10_years_normalized = datetime(pension_end_date_10_years.year, pension_end_date_10_years.month,
                                                     pension_end_date_10_years.day)

    if current_date_normalized <= pension_end_date_10_years_normalized:
        pension_type = "Enhanced Rate of Ordinary Family Pension"
    else:
        pension_type = "Normal Rate of Ordinary Family Pension"

    print(f"Pension Type: {pension_type}")
    print(f"Number of years served: {years_served}")
    print(f"Service type entered: {service_type}")

    cursor = db.cursor()

    # Family Pension Calculation
    table_name = None
    if service_type == "Regular Commissioned Officers Excluding AMC/ADC/RVC/MNS/TA/EC/SSC":
        table_name = "regularcommissionedofficers"
    elif service_type == "Commissioned Officers of AMC/ADC/RVC":
        table_name = "rco_amc_adc_rvc"
    elif service_type == "Commissioned Officers of Territorial Army":
        table_name = "rco_ta"
    elif service_type == "Commissioned Officers of Military Nursing Services":
        table_name = "rco_mns"
    elif service_type == "Regular EC/SSC Officers Other than AMC/ADC/RVC":
        table_name = "ec_ssc"
    elif service_type == "EC/SSC Officers AMC/ADC/RVC doctors":
        table_name = "ec_ssc_amc_adc_rvc"
    elif service_type == "JCOs/ORs including Honorary commisioned officers":
        table_name = "jcos_ors_hco"
    elif service_type == "JCOs/ORs Group X drawing Group Pay Rs.6200 - w.e.f 01.01.2016 applicable for post 01.01.2016 retirees (FOR SPARSH ONLY)":
        table_name = "jcos_groupx"
    elif service_type == "JCOs/ORs of DSC in receipt of 2nd pension":
        table_name = "jcos_dsc"
    elif service_type == "JCOs/ORs of Territorial Army":
        table_name = "jcos_ta"

    # Add other service types and table names as needed
    else:
        print("Invalid service type entered:")

    if table_name:
        try:
            query = f"""
                SELECT DISTINCT rco.*
                FROM {table_name} rco
                JOIN PensionType pt ON rco.pension_type_id = pt.pension_type_id
                JOIN ServiceType st ON rco.service_type_id = st.service_type_id
                WHERE rco.no_of_years_served = %s
                AND pt.pension_type = %s
                AND st.service_type = %s
            """
            params = (years_served, pension_type, service_type)
            cursor.execute(query, params)
            result = cursor.fetchone()

            if result:
                column_names = [desc[0] for desc in cursor.description]
                for i, column_name in enumerate(column_names):
                    if column_name == rank:
                        family_pension_amount = float(result[i])
                        print(f"Your family pension amount is: {family_pension_amount}")
                        break
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            db.close()

        if dependent_date_of_birth_80 <= current_date.date() < dependent_date_of_birth_85:
            additional_pension_amount = family_pension_amount * 0.2  # 20% of the original amount
        elif dependent_date_of_birth_85 <= current_date.date() < dependent_date_of_birth_90:
            additional_pension_amount = family_pension_amount * 0.3  # 30% of the original amount
        elif dependent_date_of_birth_90 <= current_date.date() < dependent_date_of_birth_95:
            additional_pension_amount = family_pension_amount * 0.4  # 40% of the original amount
        elif dependent_date_of_birth_95 <= current_date.date() < dependent_date_of_birth_100:
            additional_pension_amount = family_pension_amount * 0.5  # 50% of the original amount
        elif current_date.date() >= dependent_date_of_birth_100:
            additional_pension_amount = family_pension_amount  # 100% of the original amount
        else:
            print("No additional pension at the moment.")
            additional_pension_amount = 0

        print(f"Additional pension amount: {additional_pension_amount}")
        return family_pension_amount, pension_type, round(additional_pension_amount, 2), age


def handle_harness_no(service_type, rank, years_served_input, date_of_death, date_of_birth, date_of_discharge, dependent_date_of_birth):
    # Database connection
    db = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Apple#2013",
        database="orop_db"
    )

    years_served = convert_years_served(years_served_input, date_of_discharge)
    family_pension_amount = 0.0

    dependent_date_of_birth = datetime.strptime(dependent_date_of_birth, '%d/%m/%Y')

    dependent_date_of_birth_80 = (dependent_date_of_birth + relativedelta(years=80)).date()
    dependent_date_of_birth_85 = (dependent_date_of_birth + relativedelta(years=85)).date()
    dependent_date_of_birth_90 = (dependent_date_of_birth + relativedelta(years=90)).date()
    dependent_date_of_birth_95 = (dependent_date_of_birth + relativedelta(years=95)).date()
    dependent_date_of_birth_100 = (dependent_date_of_birth + relativedelta(years=100)).date()


    # Assuming date_of_death is a string in the format 'dd/mm/yyyy'
    date_of_death = datetime.strptime(date_of_death, '%d/%m/%Y')

    # Assuming date_of_discharge is a string in the format 'dd/mm/yyyy'
    date_of_discharge = datetime.strptime(date_of_discharge, '%d/%m/%Y')

    # Assuming date_of_birth is a string in the format 'dd/mm/yyyy'
    date_of_birth = datetime.strptime(date_of_birth, '%d/%m/%Y')

    # Calculate the pension end date 7 years from the date of death using relativedelta
    pension_end_date_7_years = date_of_death + relativedelta(years=7)

    # Calculate the pension end date when the person attains age 67 using relativedelta
    pension_end_date_age_67 = date_of_birth + relativedelta(years=67)

    # Determine the final pension end date as the minimum of the two
    final_pension_end_date = min(pension_end_date_7_years, pension_end_date_age_67)

    # Calculate the current date
    current_date = datetime.now()

    age = current_date.year - dependent_date_of_birth.year - (
            (current_date.month, current_date.day) < (dependent_date_of_birth.month, dependent_date_of_birth.day)
    )

    # Normalize dates to midnight
    current_date_normalized = datetime(current_date.year, current_date.month, current_date.day)
    final_pension_end_date_normalized = datetime(final_pension_end_date.year, final_pension_end_date.month, final_pension_end_date.day)

    # Check if the current date is less than or equal to the final pension end date
    if current_date_normalized <= final_pension_end_date_normalized:
        pension_type = "Enhanced Rate of Ordinary Family Pension"
    else:
        pension_type = "Normal Rate of Ordinary Family Pension"

    # Display the results
    print(f"Final Pension End Date: {final_pension_end_date.strftime('%d/%m/%Y')}")
    print(f"Pension Type: {pension_type}")

    cursor = db.cursor()
    # Family Pension Calculation
    table_name = None
    if service_type == "Regular Commissioned Officers Excluding AMC/ADC/RVC/MNS/TA/EC/SSC":
        table_name = "regularcommissionedofficers"
    elif service_type == "Commissioned Officers of AMC/ADC/RVC":
        table_name = "rco_amc_adc_rvc"
    elif service_type == "Commissioned Officers of Territorial Army":
        table_name = "rco_ta"
    elif service_type == "Commissioned Officers of Military Nursing Services":
        table_name = "rco_mns"
    elif service_type == "Regular EC/SSC Officers Other than AMC/ADC/RVC":
        table_name = "ec_ssc"
    elif service_type == "EC/SSC Officers AMC/ADC/RVC doctors":
        table_name = "ec_ssc_amc_adc_rvc"
    elif service_type == "JCOs/ORs including Honorary commisioned officers":
        table_name = "jcos_ors_hco"
    elif service_type == "JCOs/ORs Group X drawing Group Pay Rs.6200 - w.e.f 01.01.2016 applicable for post 01.01.2016 retirees (FOR SPARSH ONLY)":
        table_name = "jcos_groupx"
    elif service_type == "JCOs/ORs of DSC in receipt of 2nd pension":
        table_name = "jcos_dsc"
    elif service_type == "JCOs/ORs of Territorial Army":
        table_name = "jcos_ta"

    # Add other service types and table names as needed
    else:
        print("Invalid service type:")

    print(f"Your pension type value is: {pension_type}")

    if table_name:
        try:
            query = f"""
                SELECT DISTINCT rco.*
                FROM {table_name} rco
                JOIN PensionType pt ON rco.pension_type_id = pt.pension_type_id
                JOIN ServiceType st ON rco.service_type_id = st.service_type_id
                WHERE rco.no_of_years_served = %s
                AND pt.pension_type = %s
                AND st.service_type = %s
            """
            params = (years_served, pension_type, service_type)
            cursor.execute(query, params)
            result = cursor.fetchone()

            if result:
                column_names = [desc[0] for desc in cursor.description]
                for i, column_name in enumerate(column_names):
                    if column_name == rank:
                        family_pension_amount = float(result[i])
                        print(f"Your family pension amount is: {family_pension_amount}")
                        break
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            db.close()

        if dependent_date_of_birth_80 <= current_date.date() < dependent_date_of_birth_85:
            additional_pension_amount = family_pension_amount * 0.2  # 20% of the original amount
        elif dependent_date_of_birth_85 <= current_date.date() < dependent_date_of_birth_90:
            additional_pension_amount = family_pension_amount * 0.3  # 30% of the original amount
        elif dependent_date_of_birth_90 <= current_date.date() < dependent_date_of_birth_95:
            additional_pension_amount = family_pension_amount * 0.4  # 40% of the original amount
        elif dependent_date_of_birth_95 <= current_date.date() < dependent_date_of_birth_100:
            additional_pension_amount = family_pension_amount * 0.5  # 50% of the original amount
        elif current_date.date() >= dependent_date_of_birth_100:
            additional_pension_amount = family_pension_amount  # 100% of the original amount
        else:
            print("No additional pension at the moment.")
            additional_pension_amount = 0

        print(f"Additional pension amount: {additional_pension_amount}")
        return family_pension_amount, pension_type, round(additional_pension_amount, 2), age