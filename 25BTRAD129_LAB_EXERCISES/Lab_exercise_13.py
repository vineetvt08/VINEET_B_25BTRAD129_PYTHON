import csv

def generate_payroll(filename):
    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            print("\nPAYROLL SUMMARY")
            print("-" * 75)
            print(f"{'ID':<10}{'Name':<12}{'Gross':>12}{'Deductions':>15}{'Net Salary':>15}")
            print("-" * 75)
            
            for employee in reader:
                try:
                    basic = float(employee["basic_salary"])
                    hra = float(employee["hra"])
                    da = float(employee["da"])
                    pf_rate = float(employee["pf_rate"])
                    tax_rate = float(employee["tax_rate"])
                    
                    gross = basic + hra + da
                    pf = basic * pf_rate / 100
                    tax = gross * tax_rate / 100
                    deductions = pf + tax
                    net_salary = gross - deductions
                    
                    print(
                        f"{employee['employee_id']:<10}"
                        f"{employee['name']:<12}"
                        f"{gross:>12.2f}"
                        f"{deductions:>15.2f}"
                        f"{net_salary:>15.2f}"
                    )
                except (ValueError, KeyError):
                    print("Skipping a record with invalid or missing data.")
                    
    except FileNotFoundError:
        print("Error: employees.csv was not found.")
    except OSError as error:
        print(f"Unable to read the CSV file: {error}")

generate_payroll("employees.csv")
