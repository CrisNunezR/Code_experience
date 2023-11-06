--Create a table for students
CREATE TABLE student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TXT NOT NULL
);

--create table for houses
CREATE TABLE house (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    house_name TXT NOT NULL,
    house_head TXT NOT NULL
);

--create table to link students and houses
CREATE TABLE student_house (
    student_id INTEGER,
    house_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES student(id),
    FOREIGN KEY (house_id) REFERENCES house(id)
);

--geet student id and house id from students table by collecting house name from students table
SELECT students.id, house.id from
    students join house on students.house == house.house_name;


--Populate data
SELECT * FROM students;

--DELETE FROM student;

--drop TABLE sqlite_sequence;
--drop TABLE house;

SELECT DISTINCT house, head
    from students;
