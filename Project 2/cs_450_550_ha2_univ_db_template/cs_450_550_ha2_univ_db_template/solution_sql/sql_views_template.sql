-- query_a
drop view query_a;
create view query_a as
select distinct s.ssn as ssn, s.name as name, s.major as major, s.status as status
from student s, transcript t
where s.ssn = t.ssn and t.dcode = "CS" and t.cno = 530
order by s.ssn;

-- query_b
drop view query_b;
create view query_b as
select distinct s.ssn as ssn, s.name as name, s.major as major, s.status as status
from student s, transcript t
where s.ssn = t.ssn and s.name = "John" and t.dcode = "CS" and t.cno = 530
order by s.ssn;

-- query_c
drop view query_c;
create view query_c as
select distinct s.ssn as ssn, s.name as name, s.major as major, s.status as status
from student s
where NOT EXISTS (
-- all prereqs
  ( select dcode = p.pcode, cno = p.pno
    from enrolled e, class c, prereq p
    where s.ssn = e.ssn and e.class = c.class and c.dcode = p.dcode and c.cno = p.cno
  )
  MINUS
-- all courses taken w/A or B
  ( select
    from transcripts t
    where t.ssn = s.ssn and (t.grade = 'A' or t.grade = 'B')
  )
)
order by s.ssn;

-- query_d
drop view query_d;
create view query_d as
select distinct s.ssn as ssn, s.name as name, s.major as major, s.status as status
from student s, enrolled e, class c
where s.ssn = e.ssn and  e.class = c.class and EXISTS (
-- all prereqs for this class
  ( select dcode = p.pcode, cno = p.pno
    from prereq p
    where c.dcode = p.dcode and c.cno = p.cno
  )
  MINUS
-- all courses taken w/A or B
  ( select
    from transcripts t
    where t.ssn = s.ssn and (t.grade = 'A' or t.grade = 'B')
  )
)
order by s.ssn;

-- query_e
drop view query_e;
create view query_e as
select distinct s.ssn as ssn, s.name as name, s.major as major, s.status as status
from student s, enrolled e, class c
where s.name = 'John' and s.ssn = e.ssn and  e.class = c.class and EXISTS (
-- all prereqs for this class
  ( select dcode = p.pcode, cno = p.pno
    from prereq p
    where c.dcode = p.dcode and c.cno = p.cno
  )
  MINUS
-- all courses taken w/A or B
  ( select
    from transcripts t
    where t.ssn = s.ssn and (t.grade = 'A' or t.grade = 'B')
  )
)
order by s.ssn;

-- query_f
drop view query_f;
create view query_f as
select distinct c.dcode, c.cno
from course co
where NOT EXISTS (
  select *
  from prereq p
  where p.dcode = co.dcode and p.cno = co.cno
)
order by c.dcode, c.cno;

-- query_g
drop view query_g;
create view query_g as
select distinct p.dcode, p.cno
from prereq p
order by p.dcode, p.cno;

-- query_h
drop view query_h;
create view query_h as
select distinct c.*
from class c, prereq p
where c.dcode = p.dcode and c.cno = p.cno
order by c.class;

-- query_i
drop view query_i;
create view query_i as
select distinct s.*
from student s
where NOT EXISTS (
-- courses taken by s.ssn with the grade that is neither A nor B
  select *
  from transcript t
  where t.ssn = s.ssn and not(t.grade = 'A' or t.grade = 'B')
)
order by s.ssn;

-- query_j
drop view query_j;
create view query_j as
select s.* from student s

    order by s.ssn;

-- query_k
drop view query_k;
create view query_k as
select e.ssn from enrollment e

    order by e.ssn

drop view query_l;
create view query_l as
select e.ssn from enrollment e


    order by e.ssn
