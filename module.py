class Diak:
    def __init__(self, sor: str):
        v = sor.strip().split(' ')
        self.vezetek_nev = v[0]
        self.kereszt_nev = v[1]
        self.magassag = int(v[2])
        self.suly = float(v[3].replace(',', '.'))
        self.nem = v[4]