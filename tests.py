from functions.get_files_info import get_files_info
from functions.get_files_info import get_file_content
from functions.write_file_info import write_file

result1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print("Result for current directory:")
print(result1)

result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print("Result for 'pkg' directory:")
print(result2)

result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print("Result for '/bin' directory:")
print(result3)


