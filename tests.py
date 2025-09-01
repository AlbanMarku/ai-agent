from functions.get_files_info import get_files_info
from functions.get_files_info import get_file_content

result1 = get_file_content("calculator", "main.py")
print("Result for current directory:")
print(result1)

result2 = get_file_content("calculator", "pkg/calculator.py")
print("Result for 'pkg' directory:")
print(result2)

result3 = get_file_content("calculator", "/bin/cat")
print("Result for '/bin' directory:")
print(result3)

result4 = get_file_content("calculator", "pkg/does_not_exist.py")
print("Result for '../' directory:")
print(result4)



