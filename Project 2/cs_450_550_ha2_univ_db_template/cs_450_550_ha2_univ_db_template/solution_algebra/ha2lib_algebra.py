import sys
sys.path.append('..')

import lib.rel_algebra_calculus.rel_algebra_calculus as ra


def ha2(univDB):
    tables = univDB["tables"]
    department = tables["department"]
    course = tables["course"]
    prereq = tables["prereq"]
    # class may be a reserved word - check
    class_ = tables["class"]
    faculty = tables["faculty"]
    student = tables["student"]
    enrollment = tables["enrollment"]
    transcript = tables["transcript"]

    # ---------------------------------------------------------------
    # Your condition functions or other helper functions (if needed)


    # ---------------------------------------------------------------
    # Your queries

    # query_a
    cs530_lamda = lambda x: x["dcode"] == "CS" and x["cno"] == 530
    cs530 = ra.sel(transcript,cs530_lamda)
    r1 = ra.join(cs530,student)
    res = ra.proj(r1,['ssn','name','major','status'])
    query_a = res


    # query_b
    cs530_lamda = lambda x: x["dcode"] == "CS" and x["cno"] == 530
    cs530 = ra.sel(transcript,cs530_lamda)
    s1 = ra.proj(cs530,['ssn'])
    name_lamda = lambda x: x['name'] == "John"
    s2 = ra.sel(student,name_lamda)
    s3 = ra.join(s1,s2)
    query_b = ra.proj(s3,['ssn','name','major','status'])

    # query_c
    r1 = ra.join(enrollment,class_)
    r2 = ra.join(r1,prereq)
    r3 = ra.proj(r2,['ssn','pcode','pno'])
    std_have_prereq = ra.ren(r3,{'pcode':'dcode','pno':'cno'})

    t1 = ra.proj(ra.join(std_have_prereq,transcript),['ssn','dcode','cno'])
    #students who have no transcripts for prerequisite courses
    no_trans = ra.proj(ra.diff(std_have_prereq,t1),['ssn'])

    r5 = ra.join(std_have_prereq,transcript)        
    grade_lambda = lambda x: x['grade'] == 'C' or x['grade'] == 'F'
    r6 = ra.proj( ra.sel(r5,grade_lambda),['ssn'])
    final = ra.diff(ra.proj(student,['ssn']), ra.union(no_trans,r6))
    query_c = ra.join( final,student)


    # query_d
    r1 = ra.join(enrollment,class_)
    r2 = ra.join(r1,prereq)
    r3 = ra.proj(r2,['ssn','pcode','pno'])
    std_have_prereq = ra.ren(r3,{'pcode':'dcode','pno':'cno'})

    t1 = ra.proj(ra.join(std_have_prereq,transcript),['ssn','dcode','cno'])
    #students who have no transcripts for prerequisite courses
    no_trans = ra.proj(ra.diff(std_have_prereq,t1),['ssn'])

    r5 = ra.join(std_have_prereq,transcript)        
    grade_lambda = lambda x: x['grade'] == 'C' or x['grade'] == 'F'
    #students who have C or F for prereq course in transcripts
    r6 = ra.proj( ra.sel(r5,grade_lambda),['ssn'])
    query_d = ra.join( ra.union(no_trans,r6),student)

    # query_e
    e_lambda = lambda x: x['name'] == 'John'
    r1 = ra.proj(ra.sel(student,e_lambda),['ssn'])
    r2 = ra.join(ra.join(ra.join(r1,enrollment),class_),prereq)
    r3 = ra.proj(r2,['ssn','pcode','pno'])
    #All the prerequisites of students named 'John' they must satisfy
    All_prereq = ra.ren(r3,{'pcode':'dcode','pno':'cno'})

    t1 = ra.proj(ra.join(r3,transcript),['ssn','dcode','cno'])
    #Prereqs for which there are no transcripts
    no_trans = ra.proj(ra.diff(All_prereq,t1),['ssn'])
    r4 = ra.join(All_prereq,transcript)
    #prereqs in which they got a grade of C or F
    e2_lambda = lambda x: x['grade'] == 'C' or x['grade'] == 'F'
    r5 = ra.proj(ra.sel(r4,e2_lambda),['ssn'])
    query_e = ra.join( ra.union(no_trans,r5),student)

	


    # query_f
    r1 = ra.proj(course,['dcode','cno'])
    r2 = ra.proj(prereq,['dcode','cno'])
    query_f = ra.diff(r1,r2)

    # query_g
    query_g = ra.proj(prereq,['dcode','cno'])

    # query_h
    query_h = ra.proj(ra.join(class_,prereq),['class','dcode','cno','instr'])

    # query_i
    i_lambda = lambda x: x['grade'] == 'C' or x['grade'] == 'F'
    r2 = ra.proj(ra.sel(transcript,i_lambda),['ssn'])
    query_i = ra.diff(student,ra.join(r2,student))

    # query_j
    j_lambda = lambda x: x['name'] == 'Brodsky'
    prof = ra.ren(ra.proj(ra.sel(faculty,j_lambda),['ssn']),{'ssn':'instr'})
    enrolled = ra.proj(ra.join(ra.join(prof,class_),enrollment),['ssn'])
    query_j = ra.join(enrolled,student)

    #query_k
    r1 = ra.proj(class_,['class'])
    query_k = ra.div(enrollment,r1,['class'])

    #query_l
    l1_lambda = lambda x: x['dcode'] == "MTH"
    all_math_classes = ra.proj(ra.sel(class_,l1_lambda),['class'])
    l2_lambda = lambda x: x['major'] == "CS"
    all_cs_stud = ra.sel(student,l2_lambda)
    r3 = ra.proj(ra.join(all_cs_stud,enrollment),['class','ssn'])
    query_l = ra.div(r3,all_math_classes,['class'])


    # ---------------------------------------------------------------
    # Some post-processing which you do not need to worry about
    # Do not change anything after this

    query_a = ra.distinct(query_a)
    query_b = ra.distinct(query_b)
    query_c = ra.distinct(query_c)
    query_d = ra.distinct(query_d)
    query_e = ra.distinct(query_e)
    query_f = ra.distinct(query_f)
    query_g = ra.distinct(query_g)
    query_h = ra.distinct(query_h)
    query_i = ra.distinct(query_i)
    query_j = ra.distinct(query_j)
    query_k = ra.distinct(query_k)
    query_l = ra.distinct(query_l)


    ra.sortTable(query_a,["ssn"])
    ra.sortTable(query_b,["ssn"])
    ra.sortTable(query_c, ['ssn'])
    ra.sortTable(query_d, ['ssn'])
    ra.sortTable(query_e, ['ssn'])
    ra.sortTable(query_f, ['dcode', 'cno'])
    ra.sortTable(query_g, ['dcode', 'cno'])
    ra.sortTable(query_h, ['class'])
    ra.sortTable(query_i, ['ssn'])
    ra.sortTable(query_j, ['ssn'])
    ra.sortTable(query_k, ['ssn'])
    ra.sortTable(query_l, ['ssn'])

    return({
        "query_a": query_a,
        "query_b": query_b,
        "query_c": query_c,
        "query_d": query_d,
        "query_e": query_e,
        "query_f": query_f,
        "query_g": query_g,
        "query_h": query_h,
        "query_i": query_i,
        "query_j": query_j,
        "query_k": query_k,
        "query_l": query_l
    })
