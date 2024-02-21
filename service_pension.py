import mysql.connector
from datetime import datetime
from dateutil.relativedelta import relativedelta

def convert_years_served(years_served_input, date_of_discharge):
    years_served = float(years_served_input.split(".")[0])

    if datetime.strptime(date_of_discharge, "%d/%m/%Y") > datetime(1983, 6, 18):
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

    return years_served

def calculate_service_pension_no_disability(service_type, rank, years_served_input, date_of_birth, date_of_discharge, disability):
    db = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Apple#2013",
        database="orop_db"
    )

    years_served = convert_years_served(years_served_input, date_of_discharge)
    date_of_birth = datetime.strptime(date_of_birth, '%d/%m/%Y')
    
    date_of_birth_80 = (date_of_birth + relativedelta(years=80)).date()
    date_of_birth_85 = (date_of_birth + relativedelta(years=85)).date()
    date_of_birth_90 = (date_of_birth + relativedelta(years=90)).date()
    date_of_birth_95 = (date_of_birth + relativedelta(years=95)).date()
    date_of_birth_100 = (date_of_birth + relativedelta(years=100)).date()
    
    cursor = db.cursor()

    # Service Pension Calculation
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

    if table_name:
        pension_type = "Retiring Pension/Service Pension"
        query = f"""
            SELECT DISTINCT rco.*
            FROM {table_name} rco
            JOIN PensionType pt ON rco.pension_type_id = pt.pension_type_id
            JOIN ServiceType st ON rco.service_type_id = st.service_type_id
            WHERE rco.no_of_years_served = %s
            AND pt.pension_type = %s
            AND st.service_type = %s
        """
        cursor.execute(query, (years_served, pension_type, service_type))
        result = cursor.fetchone()

        if result:
            column_names = [desc[0] for desc in cursor.description]
            for i in range(len(column_names)):
                if column_names[i] == rank:
                    service_pension_amount = float(result[i])
                    break

        cursor.close()

    current_date = datetime.now().date()
    age = current_date.year - date_of_birth.year - ((current_date.month, current_date.day) < (date_of_birth.month, date_of_birth.day))

    if disability.lower() == "no" and pension_type == "Retiring Pension/Service Pension":
        print(f"Pension amount: {service_pension_amount}")

        if date_of_birth_80 <= current_date < date_of_birth_85:
            additional_pension_amount = service_pension_amount * 0.2  # 20% of the original amount
        elif date_of_birth_85 <= current_date < date_of_birth_90:
            additional_pension_amount = service_pension_amount * 0.3  # 30% of the original amount
        elif date_of_birth_90 <= current_date < date_of_birth_95:
            additional_pension_amount = service_pension_amount * 0.4  # 40% of the original amount
        elif date_of_birth_95 <= current_date < date_of_birth_100:
            additional_pension_amount = service_pension_amount * 0.5  # 50% of the original amount
        elif current_date >= date_of_birth_100:
            additional_pension_amount = service_pension_amount  # 100% of the original amount
        else:
            print("No additional pension at the moment.")
            additional_pension_amount = 0

        print(f"Additional pension amount: {additional_pension_amount}")
        return service_pension_amount, round(additional_pension_amount, 2), age

    else:
        print("Invalid service type provided.")
        return None

    db.close()

def calculate_service_pension_with_disability(service_type, rank, years_served_input, date_of_birth, date_of_discharge, disability, disability_percentage):
    # Database connection
    db = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Apple#2013",
        database="orop_db"
    )

    years_served = convert_years_served(years_served_input, date_of_discharge)
    date_of_birth = datetime.strptime(date_of_birth, '%d/%m/%Y')
    
    date_of_birth_80 = (date_of_birth + relativedelta(years=80)).date()
    date_of_birth_85 = (date_of_birth + relativedelta(years=85)).date()
    date_of_birth_90 = (date_of_birth + relativedelta(years=90)).date()
    date_of_birth_95 = (date_of_birth + relativedelta(years=95)).date()
    date_of_birth_100 = (date_of_birth + relativedelta(years=100)).date()
    
    cursor = db.cursor()

    # Service Pension Calculation
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

    if table_name:
        pension_type = "Retiring Pension/Service Pension"
        query = f"""
            SELECT DISTINCT rco.*
            FROM {table_name} rco
            JOIN PensionType pt ON rco.pension_type_id = pt.pension_type_id
            JOIN ServiceType st ON rco.service_type_id = st.service_type_id
            WHERE rco.no_of_years_served = %s
            AND pt.pension_type = %s
            AND st.service_type = %s
        """
        cursor.execute(query, (years_served, pension_type, service_type))
        result = cursor.fetchone()

        if result:
            column_names = [desc[0] for desc in cursor.description]
            for i in range(len(column_names)):
                if column_names[i] == rank:
                    service_pension_amount = float(result[i])

        # Disability Pension Calculation (if applicable)
        disability_pension_amount = 0.0
        if disability.lower() == "yes":
            pension_type = "Disability Pension"
            
            cursor.execute(query, (years_served, pension_type, service_type))
            result = cursor.fetchone()

            if result:
                column_names = [desc[0] for desc in cursor.description]
                for i in range(len(column_names)):
                    if column_names[i] == rank:
                        if disability_percentage <= 50:
                            disability_pension_amount = service_pension_amount * 0.5
                        elif 50 < disability_percentage <= 75:
                            disability_pension_amount = service_pension_amount * 0.75
                        else:
                            disability_pension_amount = service_pension_amount

        cursor.close()

    # Check if disability is "yes"
    if disability.lower() == "yes":
        current_date = datetime.now().date()
        age = current_date.year - date_of_birth.year - ((current_date.month, current_date.day) < (date_of_birth.month, date_of_birth.day))

    if date_of_birth_80 <= current_date < date_of_birth_85:
        additional_service_pension_amount = service_pension_amount * 0.2  # 20% of the original amount
        additional_disability_pension_amount = disability_pension_amount * 0.2  # 20% of the original amount
    elif date_of_birth_85 <= current_date < date_of_birth_90:
        additional_service_pension_amount = service_pension_amount * 0.3  # 30% of the original amount
        additional_disability_pension_amount = disability_pension_amount * 0.3  # 30% of the original amount
    elif date_of_birth_90 <= current_date < date_of_birth_95:
        additional_service_pension_amount = service_pension_amount * 0.4  # 40% of the original amount
        additional_disability_pension_amount = disability_pension_amount * 0.4  # 40% of the original amount
    elif date_of_birth_95 <= current_date < date_of_birth_100:
        additional_service_pension_amount = service_pension_amount * 0.5  # 50% of the original amount
        additional_disability_pension_amount = disability_pension_amount * 0.5  # 50% of the original amount
    elif current_date >= date_of_birth_100:
        additional_service_pension_amount = service_pension_amount  # 100% of the original amount
        additional_disability_pension_amount = disability_pension_amount  # 100% of the original amount
    else:
        print("No additional pension at the moment.")
        return service_pension_amount, disability_pension_amount, 0, 0, age # Return original service_pension_amount with 0 additional pension

    print(f"Additional pension amount for service element: {additional_service_pension_amount}")
    print(f"Additional pension amount for disability element: {additional_disability_pension_amount}")
    return service_pension_amount, disability_pension_amount, round(additional_service_pension_amount, 2), round(additional_disability_pension_amount, 2), age

    print("Invalid service type provided.")
    return None  # Or raise an exception or handle the invalid case accordingly

    # Close the database connection
    db.close()
