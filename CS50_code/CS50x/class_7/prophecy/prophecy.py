#Code to work with DataBases using slqite3

#connect to roster DB
import sqlite3
con = sqlite3.connect('roster.db')

#The returned Connection Object 'con' represents the connection to the DB on the disk

#To execute SQL commands, we need a cursor:
cur = con.cursor()

#to execute commands, we use the cursor like this
    #res = cur.execute("SELECT * FROM [table_name]")
    #where res is a tuple with one element per column


#Main code to redefine the tables assuming the new tables were already created
    #the SQL commands to create the new tables are in the file schema.sql
def main():

    #load_student_table()
    #load_houses_table()
    student_house_link()

    con.close()


#function to identify unique students from students-table and load them into student table
def load_student_table():
    #select unique student names from student table
    test = 'students'
    cmd = "SELECT DISTINCT student_name \
            FROM " + test
    res = cur.execute(cmd)


    #initialize values
    id = 1 #student id
    data =[]

    #creating a list data() to include the ids and names of students
    for i in res:

        #i[0] contains the student name given the structure of the res dict
        data.append({'id': id, 'student_name': i[0]})   #creates a list with dicts for every student
        id += 1                 #increases the id to continue reading res

    #now we insert student data for all students into the student table using try:
    try:
        cur.execute("BEGIN TRANSACTION")
        cur.executemany("INSERT INTO student VALUES(:id, :student_name)", tuple(data)) #note that list needs to be converted into a tuple
        con.commit()    #INSERT opens a transaction that needs to be commited to change the DB

    except sqlite3.Error:
        print("Insert execution error on student TABLE")

    #check how to place holders to asign values instead of contactenating strings as in python
    #https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders




#function to identify houses and heads from students table and load them into house table
def load_houses_table():

    #select unique houses and heads of houses from students table
    res = cur.execute("SELECT DISTINCT house, head from students")

    #initializes data to load
    id = 1
    data = []

    for i in res:
        data.append({'id': id, 'house_name': i[0], 'house_head': i[1]})
        id += 1
    #print(data)

    #now we insert the data into house table with 'try'
    try:
        cur.execute("BEGIN TRANSACTION")
        cur.executemany("INSERT INTO house VALUES(:id, :house_name, :house_head)", tuple(data))
        con.commit()
    except sqlite3.Error:
        print("Insert Execution Error on house TABLE")

#identify student id and house id for every student in students table
def student_house_link():

    #select student id from students table and house id from house table (using the house defined in students table)
    res = cur.execute("SELECT students.id, house.id from students join house on students.house == house.house_name")

    #initializes data to load
    data = []

    for i in res:
        data.append({'student_id': i[0], 'house_id': i[1]})
    #print(data)

    #now we insert the data into student_house table
    try:
        cur.execute("BEGIN TRANSACTION")
        cur.executemany("INSERT INTO student_house VALUES(:student_id, :house_id)", tuple(data))
        con.commit()
    except sqlite3.Error:
        print("Insert execution Error on student_house TABLE")


main()