import openpyxl as xl

wb = xl.load_workbook('transactions.xlsx')
sheet = wb['Sheet1']
cell = sheet['a1']
cell = sheet.cell(1, 1)

for row in range(2, sheet.max_row + 1): #first argument indicates starting point of row
    cell = sheet.cell(row, 3) #The second argument identifies number of the column
    corrected_price = cell.value * 0.9
    corrected_cell = sheet.cell(row, 4)
    corrected_cell.value = corrected_price

wb.save('transactions2.xlsx')



