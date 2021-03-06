# Automatic_homework_grading
> You grade the homeworks and exams using some pdf editor [Example](https://www.ilovepdf.com/es/editar-pdf), in an organized way, using folders and this **program write a excel file with all the grades and the final calification**.

## Table of Contents
* [How to use](#How-to-use)
* [Grade method](#Grade-method)
* [References](#References)
<!-- * [License](#license) -->

## How to use
Download these Python Libraries

```sh
pip install fitz
```

```sh
pip install pandas
```

```sh
pip install openpyxl
```

First you need a directory with the program Autograde.py and an excel file **("Lista de Alumnos Fisica III PERIODO Febrero_Junio_2021 Viernes_Final (1).xlsx")** with the names of the students **("Nombre del Alumno")** and their id number **("Matricula")**, you do a sheet for each group, examples: "V6 - Gpo 032" "N1 - Gpo 033" "N3 - Gpo 039"

Nombre del Alumno | Matricula 
--- | --- 
ANGEL RAUL CHAVEZ CARRILLO| 1234567 

You make these subdirectories:
* V6_Exam1
* V6_Exam2
* V6_ExtraordinaryExam
* V6_FinalHomework
* V6_Homework1
* V6_Homework2
* V6_Homework3

In each subdirectory you save the files of students homeworks in pdf files using this format **("chavez_carrillo_angel_raul_1234567_V6.pdf")** don't use these characters: á, é, í, ó  and ú in the file name, to scan the homeworks using camscanner, to grade the homeworks you can use any pdf editor [ilovepdf](https://www.ilovepdf.com/es/editar-pdf), adding this text in the first page **Calificacion 100
Matricula 1234567**

Now you compile and execute the Autograde.py, this program do these files:
* final_gradesN1_Gpo033.xlsx
* final_gradesN3_Gpo039.xlsx
* final_gradesV6_Gpo032.xlsx

I take 9.3 - 10 seconds to grade 1 student (with all their homeworks), using only 7 folders, if you add more files or directories you take more time

I take 17.5 - 18.2 seconds to grade 2 student (with all their homeworks), using only 7 folders, if you add more files or directories you take more time

I take 26.4 - 27.1 seconds to grade 3 student (with all their homeworks), using only 7 folders, if you add more files or directories you take more time

Using Autograde_v1.py I take 4.8 - 5.5 seconds to grade 3 student (with all their homeworks), using only 7 folders, if you add more files or directories you take more time

Using Autograde_v2.py is like  Autograde_v1.py without printing

## Grade method
60 % Homework 1 2 and 3

40 % Exam 1 and 2

10 % Final Homework (extra points)

## References
https://pythonbasics.org/write-excel/

https://www.youtube.com/watch?v=OzTCzucnD3c
