import streamlit as st
import numpy as np


# Markdown and Headings
html_temp = """ 
<div style="background-color: lightblue; padding: 16px">
<h2 style="color: black; text-align: center;">Drex Dang Financial Statement Template (IFRS Standard) Web App</h2>
</div>
"""


st.markdown(html_temp, unsafe_allow_html=True)
st.write('')
st.write('')
st.markdown("##### A Simple Financial Statement Computation App\n##### Let's Ascertain The Performance Of Your Business Entity")

# Input Fields for Income Statement
st.subheader("Income Statement")
revenue = st.number_input("Total Revenue", step=1.0, format="%f")
cost_of_goods_sold = st.number_input("Cost of Goods Sold (COGS)", step=1.0, format="%f")
operating_expenses = st.number_input("Operating Expenses", step=1.0, format="%f")
income_tax = st.number_input("Income Tax", step=1.0, format="%f")
other_income = st.number_input("Other Income", step=1.0, format="%f")
other_expenses = st.number_input("Other Expenses", step=1.0, format="%f")

# Calculate Income Statement
gross_profit = revenue - cost_of_goods_sold
operating_profit = gross_profit - operating_expenses
net_profit = operating_profit + other_income - other_expenses - income_tax

# Input Fields for Statement of Financial Position
st.subheader("Statement of Financial Position")
assets = st.number_input("Total Assets", step=1.0, format="%f")
liabilities = st.number_input("Total Liabilities", step=1.0, format="%f")
equity = assets - liabilities

# Input Fields for Statement of Changes in Equity
st.subheader("Statement of Changes in Equity")
opening_equity = st.number_input("Opening Equity", step=1.0, format="%f")
net_profit_or_loss = net_profit  # Use net profit from the income statement
additional_investments = st.number_input("Additional Investments", step=1.0, format="%f")
dividends = st.number_input("Dividends", step=1.0, format="%f")
closing_equity = opening_equity + net_profit_or_loss + additional_investments - dividends

# Input Fields for Cash Flow Statement
st.subheader("Cash Flow Statement")
cash_inflows_operating = st.number_input("Cash Inflows from Operating Activities", step=1.0, format="%f")
cash_outflows_operating = st.number_input("Cash Outflows from Operating Activities", step=1.0, format="%f")
cash_inflows_investing = st.number_input("Cash Inflows from Investing Activities", step=1.0, format="%f")
cash_outflows_investing = st.number_input("Cash Outflows from Investing Activities", step=1.0, format="%f")
cash_inflows_financing = st.number_input("Cash Inflows from Financing Activities", step=1.0, format="%f")
cash_outflows_financing = st.number_input("Cash Outflows from Financing Activities", step=1.0, format="%f")

# Calculate Cash Flow Statement
net_cash_flow_operating = cash_inflows_operating - cash_outflows_operating
net_cash_flow_investing = cash_inflows_investing - cash_outflows_investing
net_cash_flow_financing = cash_inflows_financing - cash_outflows_financing

# Display Financial Statements
st.header("Comprehensive Financial Statements (IFRS Compliant)")

# Income Statement
st.subheader("Income Statement")
st.write(f"Total Revenue: {revenue}")
st.write(f"Cost of Goods Sold (COGS): {cost_of_goods_sold}")
st.write(f"Gross Profit: {gross_profit}")
st.write(f"Operating Expenses: {operating_expenses}")
st.write(f"Income Tax: {income_tax}")
st.write(f"Other Income: {other_income}")
st.write(f"Other Expenses: {other_expenses}")
st.write(f"Operating Profit: {operating_profit}")
st.write(f"Net Profit Or Loss: {net_profit}")

# Statement of Financial Position
st.subheader("Statement of Financial Position")
st.write(f"Total Assets: {assets}")
st.write(f"Total Liabilities: {liabilities}")
st.write(f"Total Equity: {equity}")

# Statement of Changes in Equity
st.subheader("Statement of Changes in Equity")
st.write(f"Opening Equity: {opening_equity}")
st.write(f"Net Profit or Loss: {net_profit_or_loss}")
st.write(f"Additional Investments: {additional_investments}")
st.write(f"Dividends: {dividends}")
st.write(f"Closing Equity: {closing_equity}")

# Cash Flow Statement
st.subheader("Cash Flow Statement")
st.write("Operating Activities")
st.write(f"Net Cash Inflows: {net_cash_flow_operating}")
st.write("Investing Activities")
st.write(f"Net Cash Inflows: {net_cash_flow_investing}")
st.write("Financing Activities")
st.write(f"Net Cash Inflows: {net_cash_flow_financing}")
