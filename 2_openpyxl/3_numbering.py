import openpyxl

input_wb = openpyxl.load_workbook('정리필요 일용직 지명원.xlsx')
input_ws = input_wb.active

for row in range(2, input_ws.max_row + 1) :
    if input_ws[f'B{row}'].value:
        input_ws[f'A{row}'] = row - 1

input_wb.save('일용직 지명원_numbering.xlsx')