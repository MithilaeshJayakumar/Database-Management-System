jsoniq version "3.0";
module namespace mm = "lib/reporting/reportForStudent.jq";
import module namespace file = "http://expath.org/ns/file";
import module namespace math = "http://www.w3.org/2005/xpath-functions/math";
import module namespace r= "http://zorba.io/modules/random";
declare namespace ann = "http://zorba.io/annotations";
declare function mm:imply($lhs as boolean, $rhs as boolean) as boolean {
   (not($lhs) or $rhs)
};
(:
declare variable $mm:univDB := parse-json(file:read-text("sampleUnivDB.json"));
:)

declare function mm:reportForStudent($studentOut,$correctOut) {

let $allDBs := keys($correctOut)
let $noDBs := count($allDBs)
let $allQueries := distinct-values(
  for $d in $allDBs, $q in keys($correctOut.$d)
  return $q
  )
let $noQueries := count($allQueries)
let $perQueryReport := [
  for $q in $allQueries
  let $perDB := [
        for $d in $allDBs
        let $studentAns := $studentOut.$d.$q,
            $correctAns := $correctOut.$d.$q
            return {query: $q, db: $d, correct: deep-equal($studentAns,$correctAns)}
        ]
  let $correct := every $e in $perDB[] satisfies $e.correct
  return {query: $q, correct: $correct, perDBreport: $perDB}
  ]
let $noCorrectQueries:= count(
    for $e in $perQueryReport[]
    where $e.correct
    return $e
    )
return {
  correctQueries: $noCorrectQueries,
  outOf: $noQueries,
  perQueryReport: $perQueryReport
  }
};
