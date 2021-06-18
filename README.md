# Automatic_homework_grading
> You grade the homeworks and exams using some pdf editor [Example](https://www.ilovepdf.com/es/editar-pdf), in an organized way, using folders and this **program write a excel file with all the grades and the final calification**.

## Table of Contents
* [How to use?](#How to use)
* [References](#References)
<!-- * [License](#license) -->

## How to use
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

In each subdirectory you save the files of students homeworks in pdf files using this format **("chavez_carrillo_angel_raul_1234567_V6.pdf")** don't use these characters: á, é, í, ó  and ú in the file name, to scan the homeworks using camscanner, to grade the homeworks you can use any pdf editor [Example](https://www.ilovepdf.com/es/editar-pdf), adding this text in the first page **Calificacion 100
Matricula 1234567**

Now you compile and execute the Autograde.py, this program do these files:
* final_gradesN1_Gpo033.xlsx
* final_gradesN3_Gpo039.xlsx
* final_gradesV6_Gpo032.xlsx

