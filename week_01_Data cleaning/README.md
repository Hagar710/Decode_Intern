# DecodeLabs Data Analytics Internship - Project 2: Exploratory Data Analysis (EDA)

## Project Objective

The objective of this project is to perform Exploratory Data Analysis (EDA) on the cleaned dataset from Project 1 in order to understand patterns, trends, distributions, outliers, and business insights.

Project 2 focuses on transforming a clean static dataset into meaningful observations that can support business decisions.

## Tools Used

- Python
- Pandas
- Matplotlib
- Google Colab
- Excel output report

## Dataset Overview

| Metric | Value |
|---|---:|
| Number of Rows | 1,200 |
| Number of Columns | 14 |
| Missing Values | 0 |
| Duplicate Rows | 0 |
| Duplicate OrderID | 0 |
| Unique Orders | 1,200 |
| Unique Customers | 1,189 |
| Unique Products | 7 |
| Total Revenue | 1,264,761.96 |
| Average Order Value | 1,053.97 |
| Date Range | 2023-01-01 to 2025-06-30 |
| Invalid Dates | 0 |

## Methodology

1. Loaded the cleaned dataset from Project 1.
2. Verified data quality before analysis.
3. Calculated descriptive statistics for numeric columns.
4. Analyzed distributions using mean, median, skewness, histograms, and boxplots.
5. Detected outliers using the IQR method.
6. Analyzed categorical variables including Product, Payment Method, Order Status, Referral Source, and Coupon Code.
7. Analyzed monthly and yearly revenue trends.
8. Performed Pearson correlation analysis between numerical variables.
9. Summarized the key observations and business recommendations.

## Executive Summary

The dataset contains 1,200 clean order records with no missing values, no duplicate OrderIDs, and no invalid dates. Total revenue is 1,264,761.96 with an average order value of 1,053.97.

The analysis shows that TotalPrice is right-skewed, meaning that most orders are low-to-medium value while a small number of high-value orders increase the average. Only 8 TotalPrice outliers were detected, representing 0.67% of the dataset. These outliers appear to be meaningful high-value transactions rather than errors.

Chair and Printer are the strongest products by revenue. Instagram is the strongest referral channel. However, Cancelled and Returned orders together represent 41.41% of all orders, which is the most important business risk found in the analysis.

## Key Findings

### 1. Data Quality

The dataset is reliable for EDA. It contains 0 missing values, 0 duplicate rows, 0 duplicate OrderIDs, and 0 invalid dates.

### 2. Revenue Overview

Total revenue equals 1,264,761.96 across 1,200 unique orders. The average order value is 1,053.97.

### 3. Distribution Analysis

Quantity, UnitPrice, and ItemsInCart are approximately balanced. TotalPrice is right-skewed because the mean is 1,053.97 while the median is 823.62. The skewness value is 0.89.

This indicates that a small number of high-value orders are raising the average.

### 4. Outlier Analysis

Using the IQR method, only TotalPrice contains outliers. There are 8 TotalPrice outliers, representing 0.67% of all records.

These were not removed because they may represent real high-value customer transactions rather than data entry errors.

### 5. Product Analysis

Chair generated the highest revenue at 195,620.11. Printer is almost equal at 195,612.61, followed by Laptop at 192,126.56.

Phone has the lowest revenue at 151,722.39 and may need further investigation.

### 6. Payment Method Analysis

Revenue is relatively balanced across payment methods. Credit Card is the highest revenue method at 263,847.63, followed by Online at 262,442.94 and Cash at 259,786.29.

This suggests that customers are using multiple payment methods without one method dominating heavily.

### 7. Order Status Analysis

Cancelled orders represent 20.83% of all orders, while Returned orders represent 20.58%. Together, Cancelled and Returned orders represent 41.41%.

This is a critical business observation and may indicate issues related to fulfillment, delivery, customer expectations, product quality, or return policy behavior.

### 8. Referral Source Analysis

Instagram is the strongest referral source by revenue at 275,285.45. Email follows with 261,808.55. Referral is the lowest source at 226,815.58.

This suggests that Instagram and Email may be the strongest channels for customer acquisition or sales generation.

### 9. Coupon Analysis

Coupon usage is fairly balanced. FREESHIP is the most used coupon with 313 orders, followed by NO_COUPON with 309 orders, WINTER15 with 292 orders, and SAVE10 with 286 orders.

FREESHIP being the top coupon suggests that customers may respond slightly better to free shipping than discount codes.

### 10. Trend Analysis

The best month by revenue is 2024-06 with 68,068.54 in revenue, 53 orders, and an average order value of 1,284.31.

The weakest month is 2023-04 with 27,751.71 in revenue, 31 orders, and an average order value of 895.22.

Yearly revenue was:

| Year | Revenue | Order Count |
|---|---:|---:|
| 2023 | 552,643.24 | 510 |
| 2024 | 480,235.87 | 459 |
| 2025 | 231,882.85 | 231 |

Important note: 2025 only includes data until June, so it should not be directly compared with complete years.

### 11. Correlation Analysis

The strongest positive relationship is between TotalPrice and UnitPrice with a correlation of 0.72. Quantity also has a positive relationship with TotalPrice at 0.62.

Quantity and ItemsInCart have a correlation of 0.65, which suggests that larger baskets tend to include higher quantities.

Correlation does not prove causation. These relationships should be treated as clues for further investigation.

## Business Recommendations

1. **Investigate Cancelled and Returned Orders**  
   Since Cancelled and Returned orders represent 41.41%, the company should review return reasons, cancellation causes, delivery process, product descriptions, and customer expectations.

2. **Focus on Strong Referral Channels**  
   Instagram and Email are the strongest revenue channels. Marketing efforts should prioritize these channels while improving the performance of Referral.

3. **Analyze High-Value Orders**  
   The 8 TotalPrice outliers may represent VIP customers or premium transactions. These should be investigated rather than removed.

4. **Improve Low-Revenue Products**  
   Phone has the lowest revenue among products. The company should review its pricing, visibility, promotions, and customer demand.

5. **Test Coupon Strategy**  
   FREESHIP is the most used coupon. The company should test whether free shipping generates better conversion or higher order value than percentage discounts.

6. **Replicate Strong Monthly Performance**  
   June 2024 was the strongest month. The company should investigate whether campaigns, seasonality, or product mix drove this performance.

## Files Included

- `project2_eda.ipynb` or `project2_eda.py`: Python code used for the analysis.
- `Decode_Project2_EDA_Report.xlsx`: Final Excel report with analysis tables.
- `charts/`: Folder containing visualizations.
- `README.md`: Project explanation, methodology, findings, and recommendations.

## How to Run

1. Open the notebook in Google Colab or Jupyter Notebook.
2. Upload the cleaned dataset from Project 1.
3. Run all cells from top to bottom.
4. The notebook will generate the EDA report and charts.

## Final Conclusion

The EDA shows that the dataset is clean, stable, and suitable for business analysis. The strongest signals are the right-skewed TotalPrice distribution, high-value order outliers, strong revenue from Chair and Printer, strong referral performance from Instagram, and the high combined rate of cancelled and returned orders. The most important business action is to investigate cancellation and return behavior while protecting high-performing products and acquisition channels.
