import openpyxl

excel = openpyxl.load_workbook('일용직 지명원.xlsx')

sheet = excel.active

sheet.title = 'Test_2'

excel.save('Test_2.xlsx')