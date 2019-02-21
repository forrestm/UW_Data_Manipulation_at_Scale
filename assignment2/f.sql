SELECT COUNT(docid) FROM

(SELECT docid FROM frequency

WHERE term = 'world'

INTERSECT

SELECT docid FROM frequency

WHERE term = 'transactions');