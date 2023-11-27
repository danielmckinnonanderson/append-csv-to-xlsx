import pandas as pd
import argparse


def append_to_excel(csv_file_path, excel_file_path):
    # Load content from both files
    csv_content = pd.read_csv(csv_file_path)
    excel_content = pd.read_excel(excel_file_path)
    
    # Combine CSV content & Excel content
    # TODO - Perform processing here if CSV content does not have
    #        exact same headers / configuration as Excel file.
    combined = pd.concat([ excel_content, csv_content ], ignore_index = True)

    # Write updated content back to file
    combined.to_excel(excel_file_path, index=False)


if __name__ == "__main__":
    # Parse args to get CSV & Excel file paths
    parser = argparse.ArgumentParser(description="Append data from a CSV file to an Excel spreadsheet")
    parser.add_argument("csv_file_path", help="Path to the CSV file (input)")
    parser.add_argument("excel_file_path", help="Path to the Excel file which the data will be appended to")

    args = parser.parse_args()

    # Do the damn thing
    append_to_excel(args.csv_file_path, args.excel_file_path)



