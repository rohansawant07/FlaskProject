# FlaskProject
CRUD Application using Flask and MySQL
install python 3.8

pip install Flask

install mysql 8.0
login into mysql using command line
username='root'
password='root'
create database MyDB;
create table user_table(email varchar(40) primary key, fullname varchar(40), companyname varchar(40), phone varchar(10));

pip install flaskext.mysql

extract Internship.zip
run on command line with
'python app.py'
Endpoints:
1. To create- You can enter the details in the first screen and click on save button.If you enter the details correctly you will recieve a message 'Employees added successfully'.
2. To read- The newly created row will be displayed in the table on the first screen
3. To update - You can press the edit button in the table ,on the record you want to edit . You will be redirected to a new update window. Edit the details and press update button.
4. To delete - You can press the delete button in the table, on the record you want to delete.
