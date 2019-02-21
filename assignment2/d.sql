SELECT COUNT(docid) FROM

(SELECT docid FROM frequency

WHERE term = "law"

UNION

SELECT docid FROM frequency

WHERE term = "legal");