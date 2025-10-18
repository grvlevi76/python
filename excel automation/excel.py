#automation of excel sheet
#checkout gfg for more
import openpyxl as xl
wb = xl.load_workbook("money_excel.xlsx")
sheet = wb.active

for money_col in sheet.iter_cols(min_col=2,max_col=2,values_only=True):
    pass

for i in range(2,5):
    cell = "C"+str(i)
    sheet[cell] = money_col[i-1] +100

wb.save("money_excel(1).xlsx")