# Create a program to read product details from a CSV file. Handle file not found, incorrect CSV format,
# and empty file errors with different exception blocks.

import csv

def read_product_details(filename):
    try:
        # Try to open the CSV file
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)

            # Check if file has no content
            if file.tell() == 0:  # or simply check if list(reader) is empty
                raise Exception("⚠️ The file is empty!")

            # Check if CSV headers are missing or incorrect
            expected_headers = {'ProductID', 'ProductName', 'Price'}
            if not expected_headers.issubset(reader.fieldnames or []):
                raise ValueError("❌ Incorrect CSV format! Headers must be: ProductID, ProductName, Price")

            print("\n📦 Product Details:")
            print("---------------------------")
            for row in reader:
                print(f"ID: {row['ProductID']}, Name: {row['ProductName']}, Price: ₹{row['Price']}")

    except FileNotFoundError:
        print("❌ Error: File not found! Please check the filename and path.")
    except ValueError as ve:
        print(f"❌ Error: {ve}")
    except Exception as e:
        print(f"⚠️ Error: {e}")
    else:
        print("\n✅ File read successfully!")
    finally:
        print("\n--- End of program ---")

# Example usage
filename = input("Enter CSV filename (e.g., products.csv): ")
read_product_details(filename)
