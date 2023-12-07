import collections

data = [
    'start-A',
    'start-b',
    'A-c',
    'A-b',
    'b-d',
    'A-end',
    'b-end',
]
# data = [
#     'dc-end',
#     'HN-start',
#     'start-kj',
#     'dc-start',
#     'dc-HN',
#     'LN-dc',
#     'HN-end',
#     'kj-sa',
#     'kj-HN',
#     'kj-dc',
# ]
# data = [
#     'fs-end',
#     'he-DX',
#     'fs-he',
#     'start-DX',
#     'pj-DX',
#     'end-zg',
#     'zg-sl',
#     'zg-pj',
#     'pj-he',
#     'RW-he',
#     'fs-DX',
#     'pj-RW',
#     'zg-RW',
#     'start-pj',
#     'he-WI',
#     'zg-he',
#     'pj-fs',
#     'start-RW',
# ]
# data = [
#     'mx-IQ',
#     'mx-HO',
#     'xq-start',
#     'start-HO',
#     'IE-qc',
#     'HO-end',
#     'oz-xq',
#     'HO-ni',
#     'ni-oz',
#     'ni-MU',
#     'sa-IE',
#     'IE-ni',
#     'end-sa',
#     'oz-sa',
#     'MU-start',
#     'MU-sa',
#     'oz-IE',
#     'HO-xq',
#     'MU-xq',
#     'IE-end',
#     'MU-mx',
# ]
paths = collections.defaultdict(set)
for row in data:
    a, b = row.split('-')
    paths[a].add(b)
    paths[b].add(a)


def visit1(visited, room, path=None):
    if not path:
        path = []
    path.append(room)
    visited.add(room)
    if room == 'end':
        yield path
    for next_room in paths[room]:
        if next_room.isupper() or next_room not in visited:
            yield from visit1(visited.copy(), next_room, path=path[:])


# def visit2(visited, room, path=None):
#     if not path:
#         path = []
#     path.append(room)
#     visited.add(room)
#     if room == 'end':
#         yield path
#     for next_room in paths[room]:
#         if next_room.isupper() or next_room not in visited:
#             yield from visit1(visited.copy(), next_room, path=path[:])


s = 0
for v in visit1(set(), 'start'):
    s += 1
print('part 1:', s)
