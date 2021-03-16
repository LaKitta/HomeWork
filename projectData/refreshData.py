import sqlite3
import pandas as pd

# init DB connection
conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()

# refresh dataProfit.csv
revenue_col = ['project','revenue_total','expense_total','profit']
cur.execute('SELECT project, sum(revenue), sum(expense), sum(revenue) - sum(expense) FROM (SELECT project AS project, expense AS expense, 0 AS revenue FROM projectExpense UNION SELECT project AS project, 0 AS expense, revenue*1.06 AS revenue FROM projectRevenue AS foo) GROUP BY project')
result1 = pd.DataFrame(cur, columns=revenue_col)
result1.to_csv('dataProfit.csv',index=False)

# refresh dataExpense.csv
expense_col = ['project','billDate','expense','category', 'partner']
cur.execute('SELECT project, billDate, expense, category, partner FROM projectExpense')
result2 = pd.DataFrame(cur, columns=expense_col)
result2.to_csv('dataExpense.csv',index=False)

# disconnet to DB
cur.close()
conn.close()