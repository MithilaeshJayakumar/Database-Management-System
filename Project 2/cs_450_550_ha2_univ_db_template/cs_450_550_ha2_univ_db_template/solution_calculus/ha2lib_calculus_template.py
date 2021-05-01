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

    # query_a
    query_a = ra.distinct([ {"tbd": "tbd"} ])

    # query_b
    query_b = ra.distinct([ {"tbd": "tbd"} ])

    # query_c
    query_c = ra.distinct([ {"tbd": "tbd"} ])

    # query_d
    query_d = ra.distinct([ {"tbd": "tbd"} ])

    # query_e
    query_e = ra.distinct([ {"tbd": "tbd"} ])

    # query_f
    query_f = ra.distinct([ {"tbd": "tbd"} ])

    # query_g
    query_g = ra.distinct([ {"tbd": "tbd"} ])

    # query_h
    query_h = ra.distinct([ {"tbd": "tbd"} ])

    # query_i
    query_i = ra.distinct([ {"tbd": "tbd"} ])

    # query_j
    query_j = ra.distinct([ {"tbd": "tbd"} ])

    # query_k
    query_k = ra.distinct([ {"tbd": "tbd"} ])

    # query_l
    query_l = ra.distinct([ {"tbd": "tbd"} ])


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
