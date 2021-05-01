import sys
sys.path.append('..')

import lib.rel_algebra_calculus.rel_algebra_calculus as ra
# note: you can use ra.imply(a,b) which expresses a --> b (a implies b)

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
    # Your set creater functions or other helper functions (if needed)


    # ---------------------------------------------------------------
    # Your queries
    def studSatCourseAB(s,dcode,cno):
        result = any([
                t["ssn"] == s["ssn"] and
                t["dcode"] == dcode and
                t["cno"] == cno and
                (t["grade"] == "A" or t["grade"] == "B")
                for t in transcript
        ])
        return result

    def studSatPrereqs(s, dcode, cno):
        result = all([
            studSatCourseAB(s,p["pcode"],p["pno"])
            for p in prereq
            if p["dcode"] == dcode and p["cno"] == cno
        ])
        return result

    # query_a
    query_a = [
        s
        for s in student
        if any([
            (t["dcode"] == "CS" and t["cno"] == 530  and t["ssn"] == s["ssn"])
            for t in transcript
        ])
    ]

    # query_b
    query_b = [
        s
        for s in student
        if s["name"] == "John"
        if any([
            (t["dcode"] == "CS" and t["cno"] == 530  and t["ssn"] == s["ssn"])
            for t in transcript
        ])
    ]
    #query_b = ra.distinct([ "tbd" ])

    # query_c
    query_c = [
        s
        for s in student
        if not(any([
            e["ssn"] == s["ssn"] and
                e["class"] == c["class"] and
                not(studSatPrereqs(s, c["dcode"], c["cno"] ))     # s sat'd all  prereqs of class c  )
            for e in enrollment
            for c in class_
        ]))  
    ]
    #query_c = ra.distinct([ "tbd" ])

    # query_d
    query_d = [
        s
        for s in student
        if any([
            e["ssn"] == s["ssn"] and
                e["class"] == c["class"] and
                not( studSatPrereqs(s, c["dcode"], c["cno"] ))     # s sat'd all  prereqs of class c  )
            for e in enrollment
            for c in class_
        ])          # s is enrolled in a class
    ]
    #query_d = ra.distinct([ "tbd" ])

    # query_e
    query_e = [
        s
        for s in student
        if s["name"] == "John"
        if any([
            e["ssn"] == s["ssn"] and
                e["class"] == c["class"] and
                not( studSatPrereqs(s, c["dcode"], c["cno"] ))     # s sat'd all  prereqs of class c  )
            for e in enrollment
            for c in class_
        ])          # s is enrolled in a class
    ]
    #query_e = ra.distinct([ "tbd" ])

    # query_f
    query_f = [
        {"dcode":c["dcode"],"cno":c["cno"]}
        for c in course
        if not(any([
                c["dcode"] == p["dcode"] and c["cno"] == p["cno"]
                for p in prereq
                ]))
    ]
    query_f.sort(key= lambda t: [t["dcode"],t["cno"]])
    #query_f = ra.distinct([ "tbd" ])

    # query_g
    #query_g = ra.distinct([ "tbd" ])
    query_g = [
            {"dcode":c["dcode"],"cno":c["cno"]}
            for c in course
            if any([
                    c["dcode"] == p["dcode"] and c["cno"] == p["cno"]
                    for p in prereq
                    ])
    ]
    query_g.sort(key= lambda t: [t["dcode"],t["cno"]])

    # query_h
    #query_h = ra.distinct([ "tbd" ])
    query_h = query_h = [
        c
        for c in class_
        if  any([
            c["dcode"] == p["dcode"] and c["cno"] == p["cno"] #p is a prereq
            for p in prereq
            #offered this semester and has prereqs
        ])
    ]
    query_h.sort(key= lambda t: [t["class"],t["dcode"],t["cno"]])

    # query_i
    #query_i = ra.distinct([ "tbd" ])
    query_i = [
            s
            for s in student
            if not(any([
                    t["ssn"] == s["ssn"] and (t["grade"] == "C" or t["grade"] == "F")
                    for t in transcript
                    ]))
    ]

    # query_j
    #query_j = ra.distinct([ "tbd" ])
    query_j = [
            s
            for s in student
            if any([
                    f["name"] == "Brodsky" and c["instr"] == f["ssn"] and e["class"] == c["class"] and e["ssn"] == s["ssn"]
                    for f in faculty
                    for c in class_
                    for e in enrollment
                    ])
    ]

    # query_k
    #query_k = ra.distinct([ "tbd" ])
    def checking(cl,ssn):
        res = any([
                e["class"] == cl and e["ssn"] == ssn
                for e in enrollment
                ])
        return res
    query_k = [
            {"ssn":s["ssn"]}
            for s in student
            if all([
                    checking(c["class"],s["ssn"])
                    for c in class_
                    ]) and len(class_) > 0
            ]

    # query_l
    #query_l = ra.distinct([ "tbd" ])
    def check2(cl,ssn):
        res = any([
                e["class"] == cl and e["ssn"] == ssn
                for e in enrollment
                ])
        return res
    
    query_l = [
            {"ssn":s["ssn"]}
            for s in student
            if s["major"] == "CS"
            if all([
                    check2(c["class"],s["ssn"])
                    for c in class_
                    if c["dcode"] == "MTH"
                    ]) and len(class_) > 0
            
            ]


    # ---------------------------------------------------------------
    # Some post-processing which you do not need to worry about
    # Do not change anything after this

    ra.sortTable(query_a,["ssn"])
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
        "query_l": query_l,

    })
