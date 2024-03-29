# -*- coding: utf-8 -*-
"""atliq.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rTuxBe-UAbxzMB8KH3LL04FeUUokrok3

Loan_ID: A unique loan ID.
Gender: Either male or female.
Married: Weather Married(yes) or Not Married(No).
Dependents: Number of persons depending on the client.
Education: Applicant Education(Graduate or Undergraduate).
Self_Employed: Self-employed (Yes/No).
ApplicantIncome: Applicant income.
CoapplicantIncome: Co-applicant income.
LoanAmount: Loan amount in thousands.
Loan_Amount_Term: Terms of the loan in months.
Credit_History: Credit history meets guidelines.
Property_Area: Applicants are living either Urban, Semi-Urban or Rural.

Loan_Status: Loan approved (Y/N). # target variable
"""

df[df['Gender'] == 'M']['LoanAmount'].mean()

# Property_Area wise median value of Income
# Property_Area wise max value of loan
# median of income and max of loan amount

"""
property_Type max
urb
se
ru
"""

df[df.group_by('Property_Area')]['ApplicantIncome'].median()

# create a new column which is percentage of loanamount to annual_income


def getPercentage(loanamount, annual_income):
    return loanamount / annual_income

df['percentage'] =  df.apply(getPercentage, df[['loanamount', 'annual_income'])

SELECT candidate_id FROM (SELECT * tablename WHERE skill in ('Python', 'Tableau', 'PostgreSQL')) agg=GROUPBY(COUNT) candidate_id WHERE agg = 3;

# for 2023, get max prices for each category

SELECT MAX(spend) FROM tablename WHERE transaction_date[5:10] = '2023' GROUPBY category;