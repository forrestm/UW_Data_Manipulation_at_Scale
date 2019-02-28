import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    # wordsls = []
    key = record[0]
    value = record[1]
    # words = value.split()
    # for w in words:
      # if w not in wordsls:
        # wordsls.append(w)
    mr.emit_intermediate(key, 1)

def reducer(key, list_of_values):
    # idorder = 0
    # iditems = []
    # for counter, item in enumerate(list_of_values):
    #   if item[0] == 'order':
    #     idorder = counter
    #   elif item[0] == 'line_item':
    #     iditems.append(counter)
    # for ids in iditems:
    #   out = []
    #   ordered = list_of_values[idorder]

    #   for k in range(10):
    #     out.append(ordered[k])

    #   somes = list_of_values[ids]

    #   for i in range(17):
    #     out.append(somes[i])
    length = len(list_of_values)
    keyandlength = (key, length)

    mr.emit(keyandlength)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
