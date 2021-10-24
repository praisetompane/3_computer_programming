def fix(workbook, price_reduction_percent):
    sheet = workbook['Sheet1']
    ''' alternatives to access cells
        cell = sheet['a1']
        print(cell.value)
        cell = sheet.cell(1,1)
        print(cell.value)
    '''
    start_row = 2
    price_col = 3
    for row in range(start_row, sheet.max_row + 1):
        cell = sheet.cell(row, price_col)
        price = cell.value
        corrected_price = price - price * price_reduction_percent/100
        cell.value = corrected_price

    return workbook
