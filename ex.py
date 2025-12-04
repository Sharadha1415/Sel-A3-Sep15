# if 10%2==0:
#     print("even")

#-------------------------------------------
#
# num = int(input("Enter the number : "))
# if num%2==0:
#     print("even")
# else:
#     print("odd")

# #-------------------------------------------
#
# for num in range(1, 10):
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")

# #-------------------------------------------
#
# def even_odd():
#     for num in range(1, 10):
#         if num%2==0:
#             print("even")
#         else:
#             print("odd")

#-------------------------------------------

# class Numbers:
#
#     def even_odd(self, start, end):
#         for num in range(start, end):
#             if num%2==0:
#                 print("even")
#             else:
#                 print("odd")

# for i in range(2, 50):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)






# import pytest
# from selenium import webdriver
#
# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     driver.get('')
#     yield driver
#
# ## setup --> driver
#
# def test_case1(setup):
#     setup.find_element('xpath', 'value')
#
# def test_case2(setup):
#     setup.find_element('xpath', 'value')

##########################################################################

'''
*   git --version       --> Check the git version
*   To add username     --> git config --global user.name username
*   To add email        --> git config --global user.email email_id

To check the username and password
*   git config user.name    --> Display username
*   git config user.email   --> Display email

*   To change the cmd prompt path --> cd <path of the project>

*   Initialize the repository   --> git init

*   Create a new directory  --> mkdir dirname
*   To remove the directory --> rmdir dirname

*   To check the status of the git  -->     git status

*   To add files to the staging area    --> git add filename
    To add all the files                --> git add .

*   To remove the files from the staging area   --> git rm --cached filename

*   To commit   --> git commit -m "descriptive message"

*   To check all the commits    --> git log
                                --> git log --oneline
                                The above command gives short commit ID followed by message

*   To check the commit --> git checkout checkout-ID
*   To delete the specific commit   --->    git revert checkout-ID
    The above command deletes the commit from the project, but it will be present in the git
*   To delete the commit permanently    --> git reset checkout-ID

*   To push the code    --> git push repo_url master

*   To clone            --> git clone repo_url

*   To pull             --> git pull


'''






















































