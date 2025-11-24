'''
To write into the excel files, we use openpyxl

'''

from openpyxl import Workbook

## create the new excel workbook
excel_workbook = Workbook()

## initialize the worksheet
worksheet = excel_workbook.active

## set the title for the worksheet(optional)
worksheet.title = 'personal_info'

## enter the data
worksheet['A1'] = 'name'
worksheet['B1'] = 'place'
worksheet['C1'] = 'phone_num'
worksheet['D1'] = 'email_id'

data_list = [
    ['Vibha', 'Germany', 9080706050, 'vibha@gmail.com'],
    ['Shivaleela', 'Hyderabad', 9181716151, 'shivaleela@gmail.com'],
    ['Jayashree', 'Bengaluru', 9282726252, 'jaya@gmail.com'],
    ['Pragya', 'Mysuru', 9384756478, 'pragya@gmail.com']
]

for row in data_list:
    worksheet.append(row)

# ## save the excel_file
# excel_workbook.save('A3_candidates.xlsx')

## To save the excel file in different location
excel_workbook.save(r'C:\Users\Ramya\PycharmProjects\Sel-A3-1-3PM-Sep15\files_\a3.xlsx')
















































