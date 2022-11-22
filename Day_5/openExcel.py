# import openpyxl module
import openpyxl

# Give the location of the file
path = "C:\\Users\\P.Purushothaman\\OneDrive - Shell\\EUC_Solution_Automation\\Daily\\Development\\09_Alteryx\\00_Dev\\01_Pradeep\\00_Dev_Files\\01_Input\\ITM3P.xlsx"

# to open the workbook
# workbook object is created
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active

# print the total number of rows
print(sheet_obj.max_row)
