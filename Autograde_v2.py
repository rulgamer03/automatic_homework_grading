import fitz
import os
import argparse
import pandas as pd
import openpyxl

def grade_method(a,b,c,d,e,f):
	return 0.6 * (d+e+f)/3 + 0.4*(a+b)/2+0.1*c # These is the formula to obtain the final grad


def extractinfo(pdf_documet): # with the pdf we obtain the grade and the id number 
	document = fitz.open(pdf_documet)
	# print(f"Numero de paginas: {documento.pageCount}")
	page = document.loadPage(0) # pagina 0
	text = page.getText("text")
	# print(text)
	text = text.replace('\n','_')
	text = text.replace(' ','_')
	grade = text.split('_')[1]
	id_number = text.split('_')[3]
	# print(text)
	return grade, id_number

path = '.' # All is in the same directory
dir_content = os.listdir(path)
path_dir_content = [os.path.join(path, doc) for doc in dir_content] #docs in the path
folders = [folder for folder in path_dir_content if os.path.isdir(folder)] #folders in the path

'''
for folder in folders:
	print(folder) 
	path = folder
	dir_content = os.listdir(path)
	path_dir_content = [os.path.join(path, doc) for doc in dir_content]
	docs = [doc for doc in path_dir_content if os.path.isfile(doc)]
'''

docs = []
for folder in folders: # for folder in the list of folders obtain the docs 
	path = folder
	dir_content = os.listdir(path)
	path_dir_content = [os.path.join(path, doc) for doc in dir_content]
	docs += [doc for doc in path_dir_content if os.path.isfile(doc)]

columns_names = [] # The names of the columns that we want in the excel
columns_names.append('Id Number') 
columns_names.append('Student name')  

"""
xl = pd.ExcelFile('Lista de Alumnos Fisica III PERIODO Febrero_Junio_2021 Viernes_Final (1).xlsx')

xl.sheet_names  # see all sheet names

print(xl.sheet_names)
print()
df = pd.read_excel('Lista de Alumnos Fisica III PERIODO Febrero_Junio_2021 Viernes_Final (1).xlsx', sheet_name=xl.sheet_names[0])
# print(f'{df}')
# print(df.columns.ravel())
print(df['Nombre del Alumno'].tolist())
print()
print(df['Matricula'].tolist())
print()
"""


# here 
def obtain_the_columns(): # we obtain the columns 
	for folder in folders: # with the names of the folders we obtain the names of the homeworks
		homework_name = folder.split('_')[-1]
		if homework_name not in columns_names and homework_name!='ExtraordinaryExam': # if the homework is not in columns_names and if is not the extraordinary exam we add it later
			columns_names.append(homework_name)

"""
	for doc in docs:
		grade, id_num = extractinfo(doc)
		# print(grade) # we need to find the id number in the excel file, with the name of the doc know which homework is 
		# we change the value of the id number using the name of the document 
		id_number=int(doc.split('_')[-2])
		hour_of_the_class = doc.split('_')[-1].split('.')[0]
		homework_name = doc.split('\\')[1].split('_')[1]
		if homework_name not in columns_names and homework_name!='ExtraordinaryExam':
			columns_names.append(homework_name)
		# print(homework_name)
		# print(hour_of_the_class)
		# print(id_number)
		# print("------")
"""


def give_grade(some_id_number, some_homework_name, some_hour_of_the_class): # given this information we return the grade 
	for doc in docs:
		aux = doc.split('_')[1].split('\\')[0]
		if aux == some_homework_name:
			grade, id_num = extractinfo(doc)
			# print(grade) # we need to find the id number in the excel file, with the name of the doc know which homework is 
			# we change the value of the id number using the name of the document 
			id_number=int(doc.split('_')[-2])
			hour_of_the_class = doc.split('_')[-1].split('.')[0]
			homework_name = doc.split('\\')[1].split('_')[1]
			if homework_name not in columns_names and homework_name!='ExtraordinaryExam':
				columns_names.append(homework_name)
			# print(homework_name)
			# print(hour_of_the_class)
			# print(id_number)
			# print("------")
			if homework_name == some_homework_name and hour_of_the_class ==  some_hour_of_the_class and id_number == some_id_number:
				return grade
	return 0

# id number may be given by the name of the file
obtain_the_columns() # we obtain the columns 



columns_names.append('Final Grade')
columns_names.append('ExtraordinaryExam')


"""
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor = random.randint(-10, 30) # Rango de los numeros aleatorios
        matriz[i].append(valor)
"""
number_of_grades = len(columns_names)-1 # 9

xl = pd.ExcelFile('Lista de Alumnos Fisica III PERIODO Febrero_Junio_2021 Viernes_Final (1).xlsx') # Open the excel file

for sheets in xl.sheet_names: # for sheets Lista de Alumnos Fisica III PERIODO Febrero_Junio_2021 Viernes_Final (1).xlsx 
	df = pd.read_excel('Lista de Alumnos Fisica III PERIODO Febrero_Junio_2021 Viernes_Final (1).xlsx', sheet_name=sheets)
	# print(sheets)
	hour_of_the_class_by_sheet_name = sheets.split(' ')[0]  # with the name of the sheet we obtain the hour of the class
	# print(hour_of_the_class_by_sheet_name)
	id_numbers = df['Matricula'].tolist() # we obtain the id numbers from the Lista de Alumnos Fisica III
	students = df['Nombre del Alumno'].tolist() # same for students 
	matrix = [] # with the id, name, grades 
	columns_numbers = number_of_grades +1 # 9 + 1 = 10
	rows_number = len(students) # number of students

	for i in range(rows_number):
		matrix.append([])
		for j in range(columns_numbers):
			# ['Id Number', 'Student name', 'Exam1', 'Exam2', 'FinalHomework', 'Homework1', 'Homework2', 'Homework3', 'Final Grade', 'ExtraordinaryExam']
			if j == 0: # is the id_number
				matrix[i].append(id_numbers[i])
			elif j == 1: # is the name 
				matrix[i].append(students[i].lower().replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u'))
				# In the nexts lines we append the int value of the calification using the function give_grade
				# The Final grade use the function grade_method (just a formula)
			elif j == 2:
				matrix[i].append(int(give_grade(id_numbers[i], 'Exam1', hour_of_the_class_by_sheet_name))) 
			elif j == 3:
				matrix[i].append(int(give_grade(id_numbers[i], 'Exam2', hour_of_the_class_by_sheet_name)))
			elif j == 4:
				matrix[i].append(int(give_grade(id_numbers[i], 'FinalHomework', hour_of_the_class_by_sheet_name))) 
			elif j == 5:
				matrix[i].append(int(give_grade(id_numbers[i], 'Homework1', hour_of_the_class_by_sheet_name)))
			elif j == 6:
				matrix[i].append(int(give_grade(id_numbers[i], 'Homework2', hour_of_the_class_by_sheet_name)))
			elif j == 7:
				matrix[i].append(int(give_grade(id_numbers[i], 'Homework3', hour_of_the_class_by_sheet_name)))
			elif j == 8:
				matrix[i].append(int(grade_method(float(matrix[i][2]),float(matrix[i][3]),float(matrix[i][4]),float(matrix[i][5]),float(matrix[i][6]),float(matrix[i][7]))))
			elif j == 9:
				matrix[i].append(int(give_grade(id_numbers[i], 'ExtraordinaryExam', hour_of_the_class_by_sheet_name)))

	df = pd.DataFrame(matrix,
                  index=None, columns=columns_names) 
	# print(df) # index=None are the numbers 0 1 2 3 ... in the excel file  // columns are the list columns name // and the information is the matrix
	df.to_excel('final_grades'+sheets.replace(' ','').replace('-','_')+'.xlsx', sheet_name=sheets) # save the excel




	# print(matrix)
	# print()
	# print()

	"""
	print()
	print(df['Nombre del Alumno'].tolist())
	print()
	print(df['Matricula'].tolist())
	print()
	"""

"""
something = []
for i in range(0,9):
	something.append(i)

df = pd.DataFrame([something, something, something,],
                  index=['  ', '   ', '  '], columns=columns_names)

print(df)

df.to_excel('pandas_to_excel.xlsx', sheet_name='new_sheet_name')

# print(df)
"""


# print(folders)
# print(docs)
# print(columns_names)



# grade, id_num = extractinfo("chavez_carrillo_angel_raul_1234567_V6.pdf")
# print(grade, id_num) # 100 and 1234567
