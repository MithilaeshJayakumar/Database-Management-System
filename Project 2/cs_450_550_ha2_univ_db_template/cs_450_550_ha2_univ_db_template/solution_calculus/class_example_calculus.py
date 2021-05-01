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
    # Your set creater functions or other helper functions (if needed)


    # ---------------------------------------------------------------
    # Your queries
    '''
    def studentTookCS530(s):
        for t in transcript:
            if t["dcode"] == "CS" and t["cno"] == 530  and t["ssn"] == s["ssn"]:
               return True
        return False



    query_a = list()
    for s in student:
        if studentTookCS530(s):
            query_a.append(s)
    '''
    def studSatCourseAB(s,dcode,cno):
        # s took course (dcode,cno) and received A or B
        result = any([
                t["ssn"] == s["ssn"] and
                t["dcode"] == dcode and
                t["cno"] == cno and
                (t["grade"] == "A" or t["grade"] == "B")
                for t in transcript
        ])
        return result

    def studSatPrereqs(s, dcode, cno):
        # s sat'd all prereqs of (dcode,cno)
        # for every prereq (pcode,pno) of (dcode,cno), s sat'd it w/A or B
        result = all([
            #bool cond for a prereq
            studSatCourseAB(s,p["pcode"],p["pno"])
            for p in prereq
            if p["dcode"] == dcode and p["cno"] == cno
        ])
#        print("\n\ns :", s["ssn"], "dcode :", dcode, "cno :", cno, "result :", result)
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
    # find all ssn's of student who have taken CS 530 and received A


    # query_b
    query_b = [

    ]

    # query_c
    query_c = []

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

    # query_f
    query_f = []

    # query_g
    query_g = []

    # query_h
    query_h = query_h = [
        c
        for c in class_
        if  any([
            c["dcode"] == p["dcode"] and c["cno"] == p["cno"] #p is a prereq
            for p in prereq
            #offered this semester and has prereqs
        ])
    ]
    '''
    def classKey(t):
        return [t["class"],t["dcode"],t["cno"]]
    query_h.sort(key= classKey )
    '''
    query_h.sort(key= lambda t: [t["class"],t["dcode"],t["cno"]])

    # query_i
    query_i = []

    # query_j
    query_j = []

    query_e = ra.distinct([ s
        for s in student
        if s["name"] == 'John'
        if any([
            ( s["ssn"] == e["ssn"] and
              e["class"] == c["class"] and
              prereqNotSat(s["ssn"], c["dcode"], c["cno"])
            )
            for e in enrollment
            for c in class_
        ])
    ])

    query_k = ra.distinct([
        { "ssn": e["ssn"]}
        for e in enrollment
        if all([
            any([
                ( e["ssn"] == e1["ssn"] and
                  e1["class"] == c["class"]
                )
                e1 in enrollment
            ])
            for c in class_
        ])

    ])
# find students (from students table) who are enrolled in all classes
    modified_query_k = [ { "ssn": e["ssn"]}
        for s in student
        if all([
                any([
                    ( e["ssn"] == s["ssn"] and
                      e["class"] == c["class"]
                    )
                    for e in enrollment
                ])
            for c in class_
        ])

    ]
# query l:
  query_l = ra.distinct([
       s["ssn"]
       for s in student
       if s["major"] == "CS"
       if any([
           e["ssn"] == s["ssn"]
           for e in enrollment
       ])
       if all([
           imply( c["dcode"] == "MTH"),
               any([
                   ( e1["ssn"] == s["ssn"] and
                     e1["class"] == c["class"]
                   )
                   for e1 in enrollment
               ])
           for c in class_
       ])

  ])

    # ---------------------------------------------------------------
    # Some post-processing which you do not need to worry about
    # Do not change anything after this

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
        "query_j": query_j
    })
