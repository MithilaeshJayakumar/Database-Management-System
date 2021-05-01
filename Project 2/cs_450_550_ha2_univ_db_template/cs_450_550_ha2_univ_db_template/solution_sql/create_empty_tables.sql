create table department (
   dcode varchar2(15),
   dname varchar2(50),
   chair number(10),
   primary key(dcode) 
); 

create table course (
   dcode varchar2(15),
   cno number(3),
   title varchar2(50),
   units number(2),
   primary key(dcode, cno)
   --foreign key(dcode) references department(dcode)
); 

create table prereq (
   dcode varchar2(15),
   cno number(3),
   pcode varchar2(15),
   pno number(3),
   primary key(dcode, cno, pcode, pno)
   --foreign key(dcode, cno) references course(dcode, cno),
   --foreign key(pcode, pno) references course(dcode, cno)
); 

create table faculty (
   ssn number(10),
   name varchar2(50),
   dcode varchar2(15),
   rank varchar2(25),
   primary key(ssn)
   --foreign key(dcode) references department(dcode)
); 

create table class (
   class number(3),
   dcode varchar2(15),
   cno number(3),
   instr number(10),
   primary key(class)
   --foreign key(dcode, cno) references course(dcode, cno),
   --foreign key(instr) references faculty(ssn)
); 

create table student (
   ssn number(10),
   name varchar2(50),
   major varchar2(15),
   status varchar2(15),
   primary key(ssn)
   --foreign key(major) references department(dcode)
); 

create table enrollment (
   class number(3),
   ssn number(10),
   primary key(class, ssn)
   --foreign key(class) references class(class),
   --foreign key(ssn) references student(ssn)
); 

create table transcript (
   dcode varchar2(15),
   cno number(3),
   ssn number(10),
   grade varchar2(2),
   primary key(dcode, cno, ssn)
   --foreign key(dcode, cno) references course(dcode, cno),
   --foreign key(ssn) references student(ssn)
); 
