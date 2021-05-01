create view query_1 as
select s.ssn from student s
	where not exists(select c.dcode, c.cno from course c where c.dcode = 'CS'
			minus select t.dcode, t.cno from transcript t where t.ssn = s.ssn)
	order by s.ssn;

create view query_2 as
select c.dcode, c.cno from course c
	where c.units >= all (select c2.units from course c2)
	order by c.dcode, c.cno;

-- query_c

drop view query_c;
create view query_c as
select distinct s.ssn as ssn, s.name as name, s.major as major, s.status as status
from student s
where NOT EXISTS (
-- A: all prereqs of all classes that s.ssn is enrolled in
	( select p.pcode as dcode,   p.pno as cno
		from class c, enrollment e, prereq p
		where s.ssn = e.ssn and c.class = e.class and c.dcode = p.dcode and c.cno = p.cno
	)
	MINUS
-- B: all courses in transcript for student s.ssn with the grade of A or B
	(

	)
)

drop view query_i;
create view query_i as
select
from student s
where NOT EXISTS (
-- compute all courses in transcript for student s.ssn where the grade is neither A nor B
	select *
	from transcript t
	where t.ssn = s.ssn and not(t.grade = 'A' or t.grade = 'B')
)

-- A is a subset of B:
-- B: the set of courses in which s.ssn received A or B
-- A: the set of all courses s.ssn has taken (in transcript)

drop view query_l;
create view query_l as
select distinct e.ssn
from enrollment e, student s
where e.ssn = s.ssn and s.major = 'CS' and NOT EXISTS (
-- A: set of all math classes
	(

	)
	MINUS
-- B: set of all classes in which s.ssn is enrolled in 
	(

	)

)


order by e.ssn
