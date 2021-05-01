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

    def is_cs(x):
        return x["dcode"] == "CS"

    # ---------------------------------------------------------------
    # Your queries

    # students who have taken (according to transcript) a CS course


    # Student who have taken all CS courses (i.e. all cs courses must be in transcript)
    transcript_proj = ra.proj(transcript, ['dcode', 'cno', 'ssn'])
    cs_only = ra.sel(course, is_cs)
    cs_only = ra.sel(course,  lambda x: x["dcode"] == "CS")
    cs_only_proj = ra.proj(cs_only, ['dcode', 'cno'])
    student_ssn = ra.proj(student, ['ssn'])
    all_combination = ra.prod(cs_only_proj, student_ssn)
    student_did_not_all_cs = ra.diff(all_combination, transcript_proj)
    query_a = ra.diff(student_ssn, student_did_not_all_cs)

    # Course with highest units
    course1 = ra.proj(course, ['dcode', 'cno', 'units'])
    course2 = ra.ren(course1, {'dcode': 'dcode2', 'cno':'cno2', 'units':'units2'})
    course_x_course2 = ra.prod(course, course2)
    cond_lower_units = lambda x: x['units'] < x['units2']
    course_lower_units = ra.sel(course_x_course2, cond_lower_units)
    course_lower_units = ra.proj(course_lower_units, ['dcode', 'cno'])
    all_courses = ra.proj(course, ['dcode', 'cno'])
    query_b = ra.diff(all_courses,course_lower_units)

# query_c

    r1 = ra.join(enrollment,class_)
    r2 = ra.join(r1, prereq)
    r3 = ra.proj(r2, ["ssn", "pcode", "pno"])
    SP = ra.ren(r3, {"pcode": "dcode", "pno": "cno"} )
    # student prereqs over the schema (ssn, dcode, cno)

    cond_a_or_b = lambda t: (t["grade"] == "A" or t["grade"] == "B")
    r4 = ra.sel(transcript, cond_a_or_b)
    ST = ra.proj(r4, ["ssn","dcode", "cno"])

    NOT = ra.proj( ra.diff(SP,ST),  ["ssn"] )
    YES = ra.diff( ra.proj(student, ["ssn"]),  NOT)
    query_c = ra.join(student, YES)


    # ---------------------------------------------------------------
    # Some post-processing which you do not need to worry about
    # It is safe to not change anything after this

    return({
        "query_a": query_a,
        "query_b": query_b,
        "query_c": query_c

    })


# -------------------------------------------------------------------
# IGNORE CODE AFTER THIS
# YOU DO NOT NEED TO HAVE THIS PART IN YOUR SOLUTION FILE
# -------------------------------------------------------------------

if __name__ == '__main__':
    import json
    f = open("../testDBs/db1.json", "r")
    db1 = json.loads(f.read())
    x = ha2(db1)
