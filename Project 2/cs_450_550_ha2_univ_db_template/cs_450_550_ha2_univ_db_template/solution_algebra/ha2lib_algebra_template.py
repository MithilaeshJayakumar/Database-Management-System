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
    query_a = [ {"tbd": "tbd"}]

    # query_b
    query_b = [{"tbd": "tbd"}]

    # query_c
    query_c = [{"tbd": "tbd"}]

    # query_d
    query_d = [{"tbd": "tbd"}]

    # query_e
    query_e = [{"tbd": "tbd"}]

    # query_f
    query_f = [{"tbd": "tbd"}]

    # query_g
    query_g = [{"tbd": "tbd"}]

    # query_h
    query_h = [{"tbd": "tbd"}]

    # query_i
    query_i = [{"tbd": "tbd"}]

    # query_j
    query_j = [{"tbd": "tbd"}]

    # query_k
    query_k = [{"tbd": "tbd"}]

    #query_l
    query_l = [{"tbd": "tbd"}]

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
