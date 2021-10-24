from app import editor
import openpyxl as xl

workbook = xl.load_workbook('./resources/transactions.xlsx')

price_reduction_percent = 10.00
editor.fix(workbook, price_reduction_percent)
workbook.save('./resources/transactions_corrected.xlsx')