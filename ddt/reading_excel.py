'''

STEP1   :   import xlrd
STEP2   :   open the excel workbook
STEP3   :   open the worksheet


'''

# import xlrd
#
# path = r'C:\Users\Ramya\PycharmProjects\Sel-A3-1-3PM-Sep15\files_\candidates_info.xlsx'
#
# ## open the excel
# workbook = xlrd.open_workbook(path)
# # print(workbook)             ## Book object
#
# ## open the worksheet
# worksheet = workbook.sheet_by_name('a3_data')
# # print(worksheet)            ## Sheet object
#
# ##
# rows = worksheet.get_rows()
# # print(rows)                 ## generator object
#
# # for ele in rows:
# #     print(ele)
# #
# # ## [text:'name', text:'place', text:'phone_num']
# # ## [text:'Chidambri', text:'Chennai', number:9080706050.0]
# # ## [text:'Shivaleela', text:'Hyderabad', number:9181716151.0]
# # ## [text:'Harsha', text:'Mumbai', number:9282726252.0]
# # ## [text:'Jayashree', text:'Bengaluru', number:9383736353.0]
#
# ##--------------------------------------------------------------------------------------
# #
# # for ele in rows:
# #     print(ele[0], ele[1], ele[2])
# #
# # ## text:'name' text:'place' text:'phone_num'
# # ## text:'Chidambri' text:'Chennai' number:9080706050.0
# # ## text:'Shivaleela' text:'Hyderabad' number:9181716151.0
# # ## text:'Harsha' text:'Mumbai' number:9282726252.0
# # ## text:'Jayashree' text:'Bengaluru' number:9383736353.0
#
# ##--------------------------------------------------------------------------------------
#
# for ele in rows:
#     print(ele[0].value, ele[1].value, ele[2].value)

#########################################################################################################

import xlrd

path = r'C:\Users\Ramya\PycharmProjects\Sel-A3-1-3PM-Sep15\files_\testdata.xlsx'


def excel_read():
    workbook = xlrd.open_workbook(path)                 ## book object
    worksheet = workbook.sheet_by_name('reg_data')      ## sheet object
    rows = worksheet.get_rows()                         ## generator object

    header = next(rows)
    reg = {}
    for ele in rows:
        reg[ele[0].value] = ele[1].value

    return reg      ## {'firstname': 'James', 'lastname': 'Watt', 'email_id': 'james@gmail.com', 'password': 'james@12345'}




















































