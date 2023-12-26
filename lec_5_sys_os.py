import sys, os

print(os.getcwd())

os.system('echo hi!')

# os.system('C:/Users/inf3-12/AppData/Local/Programs/Python/Python311/python.exe c:/Users/inf3-12/Desktop/math_modeling/lec_5_sys_os.py')

print('Python version is:', sys.version)
print(sys.path)
print(sys.platform)

print(dir(sys)) #выводит все функции
print(dir(os)) 