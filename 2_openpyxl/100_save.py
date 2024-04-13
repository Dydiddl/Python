import openpyxl

excel = openpyxl.Workbook()

sheet = excel.active

sheet.title = 'Test_1'

excel.save('Test.xlsx')