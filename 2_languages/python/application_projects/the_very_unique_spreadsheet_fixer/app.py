from app import editor
import openpyxl as xl


price_reduction_percent = 10.00
try:
    workbook = xl.load_workbook('./resources/transactions.xlsx')
    editor.fix(workbook, price_reduction_percent)
    workbook.save('./resources/transactions_corrected.xlsx')
except FileNotFoundError as e:
    print(f'failed to open file, because we could not find it. full stack trace {e}')
except Exception as e:
    print(f'an error occurred while applying fix. full stack trace {e}')