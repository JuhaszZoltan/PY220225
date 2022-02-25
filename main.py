import module as m

diakok = []

for sor in open('diakok.txt', encoding="utf-8"):
    diakok.append(m.Diak(sor))

# for d in diakok:
#     if 'B' in d.vezetek_nev or 'b' in d.vezetek_nev:
#         print(f'{d.vezetek_nev} {d.kereszt_nev}')

for d in diakok:
    print(d.nem)