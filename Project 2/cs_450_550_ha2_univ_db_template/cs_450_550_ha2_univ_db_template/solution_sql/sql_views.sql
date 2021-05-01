-- query_a
drop view query_a;
create view query_a as
select distinct s.ssn, s.name, s.major, s.status from student s, transcript t
    where s.ssn=t.ssn and t.dcode='CS' and t.cno=530
    order by s.ssn;


-- query_b
drop view query_b;
create view query_b as
select distinct s.ssn, s.name, s.major, s.status from student s, transcript t
    where s.name='John' and s.ssn=t.ssn and t.dcode='CS' and t.cno=530
    order by s.ssn;

-- query_c
drop view query_c;
create view query_c as
select distinct * from student s
    where not exists(select e.ssn from enrollment e
        where e.ssn = s.ssn and exists(select p.pcode, p.pno from prereq p, class c
            where c.class = e.class and p.dcode = c.dcode and p.cno = c.cno and not exists(select t.dcode, t.cno from transcript t
                where t.dcode = p.pcode and t.cno = p.pno and t.ssn = s.ssn and (t.grade = 'A' or t.grade='B'))))
    order by s.ssn;

-- query_d
drop view query_d;
create view query_d as
select distinct * from student s
    where exists(select e.ssn from enrollment e
        where e.ssn = s.ssn and exists(select p.pcode, p.pno from prereq p, class c
            where c.class = e.class and p.dcode = c.dcode and p.cno = c.cno and not exists(select t.dcode, t.cno from transcript t
                where t.dcode = p.pcode and t.cno = p.pno and t.ssn = s.ssn and (t.grade = 'A' or t.grade='B'))))
    order by s.ssn;

-- query_e
drop view query_e;
create view query_e as
select distinct * from student s
    where s.name = 'John' and exists(select e.ssn from enrollment e
        where e.ssn = s.ssn and exists(select p.pcode, p.pno from prereq p, class c
            where c.class = e.class and p.dcode = c.dcode and p.cno = c.cno and not exists(select t.dcode, t.cno from transcript t
                where t.dcode = p.pcode and t.cno = p.pno and t.ssn = s.ssn and (t.grade = 'A' or t.grade='B'))))
    order by s.ssn;

-- query_f
drop view query_f;
create view query_f as
select distinct c.dcode, c.cno from course c
    where not exists(select p.pcode, p.pno from prereq p
        where p.dcode = c.dcode and p.cno = c.cno)
    order by c.dcode,c.cno;

-- query_g
drop view query_g;
create view query_g as
select distinct c.dcode, c.cno from course c
    where exists(select p.pcode, p.pno from prereq p
        where p.dcode = c.dcode and p.cno = c.cno)
    order by c.dcode,c.cno;

-- query_h
drop view query_h;
create view query_h as
select distinct * from class c
    where exists(select p.pcode, p.pno from prereq p
        where p.dcode = c.dcode and p.cno = c.cno)
    order by c.class;

-- query_i
drop view query_i;
create view query_i as
select distinct * from student s
    where not exists(select t.dcode, t.cno from transcript t
        where t.ssn = s.ssn and (t.grade = 'C' or t.grade = 'F'))
    order by s.ssn;

-- query_j
drop view query_j;
create view query_j as
select distinct * from student s
    where exists(select e.ssn from enrollment e, class c, faculty f
        where f.name='Brodsky' and c.instr = f.ssn and e.class = c.class and e.ssn = s.ssn)
    order by s.ssn;

-- query_k
drop view query_k;
create view query_k as
select distinct s.ssn from student s
    where not exists(select c.class from class c
        where not exists(select e.class from enrollment e
            where e.class = c.class and e.ssn=s.ssn)) and exists(select * from enrollment e where e.ssn = s.ssn)
    order by s.ssn;

drop view query_l;
create view query_l as
select distinct s.ssn from student s
    where s.major='CS' and not exists(select c.class from class c
        where c.dcode='MTH' and not exists(select e.class from enrollment e
            where e.class = c.class and e.ssn=s.ssn)) and exists(select * from enrollment e where e.ssn = s.ssn)
    order by s.ssn;
