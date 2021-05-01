# author: Alex Brodsky, brodsky@gmu.edu
#--------------------------------------------------------------------------
import copy
import json
import importlib.util

#-------------------------------------------------------------------------
def imply(lhs,rhs):
    return((not lhs) or rhs)

#--------------------------------------------------------------------------

def merge(dictSeq):
    merged = dict()
    for i in dictSeq:
        merged.update(i)
    return merged
#--------------------------------------------------------------
'''
a relational instance (table) is represented as
a list of python dictionaries, each representing a relatonal tuple.
All relational tuples must have the same schema
example:
  [
      {
        "dcode": "C",
        "dname": "culture",
        "chair": 4
      },
      {
        "dcode": "History",
        "dname": "history",
        "chair": 9
      }
  ]

'''
#----------------------------------------------------------------------
# checks if two relational tuples are identical

def equal(t1,t2):
    attrs1 = set(t1.keys())
    attrs2 = set(t2.keys())
    if attrs1.issubset(attrs2) and attrs2.issubset(attrs1):
        return all([ t1[a] == t2[a] for a in attrs1])
    return "ra_error: equal: schemas not compatible"

#----------------------------------------------------------------------
# removes duplicate tuples from a table

def distinct(table):
    tuples = list()
    for t in table:
        if all([ not(equal(s,t)) for s in tuples]):
            tuples.append(t)
    if len(tuples) > 0:
            sortTable(tuples, tuples[0].keys())
    return tuples
#---------------------------------------------------------------------
# sort lexicographically by attached list of attributes
# table is a (possibly empty) table; sortBy is a list of attributes by which the
# table is to be sorted, e.g., ["dcode","cno"]

def sortTable(table,sortBy):
    def sf(t):
        return ([t[a] for a in sortBy if a in t])
    table.sort(key=sf)
    return table

#----------------------------------------------------------------------
# table1, table2: schemas are compatible if either table is empty, or, if both
# are non-empty, they must be identical

def areSchemasCompatible(table1,table2):
    if len(table1) == 0 or len(table2) == 0:
        return True
    schema1set = table1[0].keys()
    schema2set = table2[0].keys()
    return schema1set.issubset(schema2set) and schema2set.issubset(schema1set)

#----------------------------------------------------------------------
# table1 and/or table2 can be empty

def isSubTable(table1,table2):
    isSubset = all([
        any([ equal(t1,t2) for t2 in table2])
        for t1 in table1
    ])
    return isSubset
#----------------------------------------------------------------------
# table: an input table, can be empty
# cond: is a Bool function on a tuple

def sel(table,cond):
    result = [ t.copy() for t in table if cond(t) ]
    return distinct(result)

#------------------------------------------------------------------------
# table: an input table, can be empty
# attrList is a list of attributes, e.g., ["ssn","dcode","cno"]

def proj(table,attrList):
    tuples = list()
    for t in table:
        tuple = merge([ { a: t[a]} for a in attrList])
        tuples.append(tuple)
    return distinct(tuples)

#---------------------------------------------------------------------------------
# table: an input table, can be empty
# renameList is of the form {A1:B1,..., An:Bn}

def ren(table, renameList):
    tuples = list()
    for t in table:
        tuple = t.copy()
        renTuple = merge([ {renameList[a]: t[a]} for a in renameList.keys()])
        tuple.update(renTuple)
        for a in renameList.keys():
            tuple.pop(a)
        tuples.append(tuple)
    return distinct(tuples)

#---------------------------------------------------------------------------------
# table1, table2: tables to be naturally joined; one or both can be empty
# may or may not have common attributes

def join(table1, table2):
    tuples = list()
    for t in table1:
        for s in table2:
            tAttrs = set(t.keys())
            sAttrs = set(s.keys())
            commonAttrs = tAttrs.intersection(sAttrs)
            if all([t[a] == s[a]  for a in commonAttrs]):
                newTuple = merge([t,s])
                tuples.append(newTuple)
    return distinct(tuples)

#----------------------------------------------------------------------------------
# table1, table2: operands of cross-product; must not have common attributes
def prod(table1,table2):
    tuples = list()
    for t in table1:
        for s in table2:
            tAttrs = set(t.keys())
            sAttrs = set(s.keys())
            commonAttrs = tAttrs.intersection(sAttrs)
            if len(commonAttrs) > 0:
                return "ra_error: prod: schemas not disjoint"
            if all([t[a] == s[s]  for a in commonAttrs]):
                newTuple = merge([t,s])
                tuples.append(newTuple)
    return distinct(tuples)

#---------------------------------------------------------------------------------
# table1, table2: operands of union; must have compatible schemas

def union(table1, table2):
    if not(areSchemasCompatible):
        return "ra_error: union: schemas not compatible"
    tuples = list()
    tuples.extend(table1)
    tuples.extend(table2)
    return distinct(tuples)

#----------------------------------------------------------------------------------
# table1, table2: operands of diff; must have compatible schemas

def diff(table1, table2):
    if not(areSchemasCompatible):
        return "ra_error: diff: schemas not compatible"
    tuples = list()
    for t in table1:
        if all([not(equal(t,s)) for s in table2]):
            tuples.append(t)
    return distinct(tuples)

#-----------------------------------------------------------------------------------
# table1, table2: operands of intersect; must have compatible schemas

def intersect(table1, table2):
    if not(areSchemasCompatible):
        return "ra_error: intersect: schemas not compatible"
    tuples = list()
    for t in table1:
        if any([equal(t,s) for s in table2]):
            tuples.append(t)
    return distinct(tuples)

#-----------------------------------------------------------------------------------
# table1, table2: operands of RA div; one or both can be empty
# table2schema: a list of attributes in table2; needed for the case that table2 is empty,
#               and table1 is not empty (to know the schema of the result)

def div(table1, table2, table2schema):
# first case when table1 is empty
    if len(table1) == 0:
        return table1.copy()
    schema1 = set(table1[0].keys())
    schema2 = set(table2schema)
    if not(schema2.issubset(schema1)):
        return "ra_error:div: table2 schema is not a subset of table1 schema"
    resSchema = schema1.difference(schema2)
    resDomain = proj(table1,resSchema)

# next is the case when table1 is not empty, but table2 is empty
    if len(table2) == 0:
        return resDomain

# this is the main case when both tables are not empty
    tuples = list()
    for t in resDomain:
        tAssocTuples = [
            merge([ {a: t1[a] } for a in schema2 ])
            for t1 in table1
            if all([
                t[b] == t1[b]
                for b in resSchema
            ])
        ]
        if isSubTable(table2,tAssocTuples):
            tuples.append(t)
    return distinct(tuples)

#-----------------------------------------------------------------------------------
