from collections import defaultdict
from copy import deepcopy
import music21

def make_vec_table(points):
    # point_point_vec = defaultdict(dict)
    vec_point = defaultdict(list)
    keys = sorted(points)
    for i, row in enumerate(keys):
        for j, col in enumerate(keys):
            if i <= j:
                continue
            v = tuple( [row[k] - col[k] for k in range( len( row ) )] )
            # point_point_vec[row][col] = v
            vec_point[v].append(col)
    return vec_point

def extract_patterns(vec_table):
    return [sorted(p, key=lambda x: x[1]) for p in vec_table.values() if len(p) > 1]

score = music21.converter.parse('bf1i.krn')
# notes = [(ord(n.pitch.step) - ord('A'), n.offset) for n in score.flat.notes if isinstance(n, music21.note.Note)]
notes = [(ord(n.pitch.step) - ord('A'), n.offset) for n in score.parts[0].notes if isinstance(n, music21.note.Note)]

notes = []
tup2note = {}
for n in score.flat.notes:
    if isinstance( n, music21.note.Note ):
        descriptor = (ord( n.pitch.step ) - ord( 'A' ), n.offset)
        notes.append(descriptor)
        tup2note[descriptor] = n

sample = [(1,1), (1,3), (2,1), (2,2), (2,3), (3,2)]

vec2points = make_vec_table(notes)
mtps = extract_patterns(vec2points)
for p in mtps:
    print p
# top5 = sorted(mtps, key=lambda x: x[-1][1] - x[0][1])[:1000]
# atleast5 = sorted([p for p in top5 if len(p) >= 5], key=lambda x: len(x))
# for p in atleast5:
#     print p
# best = atleast5[-1]
# keep = [tup2note[t] for t in best]
# for part in score.parts:
#     for note in part.flat.notes:
#         if note in keep:
#             note.addLyric('la')
# score.show()



