# Week 01 - Data Cleaning & Preparation

## Project Overview
This project is part of the DecodeLabs Data Analytics Internship - Project 1.

The objective of this week was to clean a raw dataset and prepare it for analysis by handling missing values, duplicate records, incorrect formats, and inconsistent text values.

The final output is a clean and reliable dataset that can be used for Exploratory Data Analysis in Week 02.

---

## Files Included

| File Name | Description |
|---|---|
| `Dataset for Data Analytics.xlsx` | Original raw dataset provided for the project |
| `data.project` | Python code / notebook file used for data cleaning in VS Code |
| `Decode_Project1_Final_Output.xlsx` | Final cleaned Excel output containing the cleaned dataset and reports |
| `README.md` | Documentation file explaining the project |

---

## Tools Used

- Python
- Pandas
- OpenPyXL
- VS Code
- Excel

---

## Cleaning Tasks Performed

The following data cleaning steps were completed:

1. Loaded the raw Excel dataset using Python.
2. Created a backup copy of the original dataset before cleaning.
3. Checked dataset shape, column names, and data types.
4. Identified missing values.
5. Filled missing `CouponCode` values with `NO_COUPON`.
6. Checked and removed duplicate `OrderID` records if found.
7. Cleaned text columns by removing extra spaces.
8. Standardized text formatting for categorical columns.
9. Converted the `Date` column into a proper date format.
10. Converted numeric columns into correct numeric data types.
11. Recalculated `TotalPrice` using:

```python
TotalPrice = Quantity * UnitPrice
```

12. Verified the final dataset quality.
13. Exported the cleaned dataset and reports to Excel.

---

## Final Validation Results

| Check | Result |
|---|---:|
| Missing Values | 0 |
| Duplicate OrderID | 0 |
| Incorrect Date Formats | 0 |
| TotalPrice Calculation Errors | 0 |

---

## Output File Structure

The final Excel file `Decode_Project1_Final_Output.xlsx` contains the following sheets:

| Sheet Name | Description |
|---|---|
| `Cleaned Dataset` | Final cleaned dataset |
| `Data Quality Report` | Summary of data quality checks |
| `Missing Report` | Missing value summary |
| `Change Log` | List of cleaning actions performed |

---

## How to Run the Code

1. Open the project folder in VS Code.
2. Make sure the following files are in the same folder:

```text
Dataset for Data Analytics.xlsx
data.project
```

3. Open the Python file / notebook.
4. Run the code from top to bottom.
5. The final output file will be generated as:

```text
Decode_Project1_Final_Output.xlsx
```

---

## Key Learning Outcomes

Through this project, I practiced:

- Reading Excel files using Python.
- Identifying and handling missing values.
- Detecting duplicate records.
- Cleaning and standardizing text values.
- Converting dates and numeric columns to correct formats.
- Creating a data quality report.
- Documenting changes using a change log.

---

## Project Status

Completed successfully.
