import csv

filename = "sales.csv"

def read_csv(filename):
    data = []
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

def get_sales_figures(sales_data):
    sales_list = []
    for row in sales_data:
        sales_list.append(int(row["sales"]))
    
    return sales_list

def calculate_total_sales(sales):
    return sum(sales)

if input(f"Current file is {filename}, do you want to change filename? (y/n) ").lower() == 'y':
    filename = input("Enter new filename: ")

sales_data = read_csv(filename)
print(f"Sales Data:\n{sales_data}\n")

monthly_sales_list = get_sales_figures(sales_data)
print(f"Monthly Sales:\n{monthly_sales_list}\n")

total_sales = calculate_total_sales(monthly_sales_list)
print(f"Total Sales:\n{total_sales}\n")
