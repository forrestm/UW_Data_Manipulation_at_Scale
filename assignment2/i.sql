SELECT MAX(data) FROM (
SELECT SUM(A.count * B.count) data FROM

(SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count)

A,

(SELECT * FROM frequency)

B

WHERE A.term = B.term
GROUP BY B.docid);