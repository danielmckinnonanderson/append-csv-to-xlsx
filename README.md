# Append CSV to Excel document

Quick script for appending the entire content of a CSV file to an existing Excel document.

If the CSV file does not have the same exact columns / column names as Excel doc, intermediate processing will need to be added.


## Quick start

1. Install deps (pandas)
```
pip3 install pandas
```

2. (Optional) For ease of use, move the script to the same directory as your CSV & Excel files.

3. If your CSV file does not contain same structure as Excel file, update script with intermediate processing.
This is a "draw the rest of the owl" step.

4. Run the script.
```
# On MacOS / Linux
python3 ./append-csv.py ./<path to your csv file>.csv ./<path to your excel file>.xlsx
```

```
# On Windows Command Prompt
python3 .\append-csv.py .\<path to your csv file>.csv .\<path to your excel file>.xlsx
```

