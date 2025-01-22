"""
My github repo can be viewed here: https://github.com/dho1115/Create-basic-HTML-page-using-PYTHON---
"""


try:
   #Information that will be displayed onto index.html.
   companyName= input ("Input the Company Name!!! ")
   name = input("Input your name!!! ");
   jobTitle = input("Input your job title!!! ");

   HTML_file = open("./index.html", "w"); #File for WRITING ('w').

   #HTML elements for index.html file.
   htmlElements = ["<!DOCTYPE html>", "<html lang=\"en\">", 
                   "<meta charset=\"UTF-8\">", "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">", 
                   "<title>CREATED FROM PYTHON!!!</title>", 
                   "<head>", 
                   "</head>", 
                   "<body style='background-color: beige; padding: 0px; margin: 0px; box-sizing: border-box'>", 
                   f"<header style='border-bottom: 3.5px solid black; background-color: whitesmoke; text-align: center'>\n<h3>Future Homepage of...</h3>\n <h1><span style='color: red; -webkit-text-stroke: 1px red;'>{companyName}</span><h1></header>",
                   "<div style=\"padding: 1%; margin: 1%; border: 1px solid black; background-color: yellow \">"
                   f"<h1>NAME: {name}</h1>", 
                   f"<h3>JOB TITLE: {jobTitle}</h3>",
                   "</div>",
                   "<script type=\"text/Javascript\">",
                   "alert('WEBSITE IN PROGRESS... MAY OR MAY NOT BE COMPLETED.')",
                   "</script>",
                   "</body>", 
                   "</html>"
                   ];

   for i in htmlElements:
      HTML_file.write(f"{i}\n") #Iterate Through htmlElements and write each element (i) onto index.html. The \n is for aesthetics.
   
   HTML_file.close()

except FileNotFoundError as fnfe:
   print(f"The file is not found: {fnfe}!!!");

except Exception as exc:
   print(f"An exception occurred: {exc}.");