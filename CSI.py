karakteristike = {
    'hair': {
        'black': 'CCAGCAATCGC',
        'brown': 'GCCAGTGCCG',
        'blonde': 'TTAGCTATCGC'
    },
    'face': {
        'square': 'GCCACGG',
        'round': 'ACCACAA',
        'oval': 'AGGCCTCA'
    },
    'eyes': {
        'blue': 'TTGTGGTGGC',
        'green': 'GGGAGGTGGC',
        'brown': 'AAGTAGTGAC'
    },
    'gender': {
        'female': 'TGAAGGACCTTC',
        'male': 'TGCAGGAACTTC'
    },
    'race': {
        'white': 'AAAACCTCA',
        'black': 'CGACTACAG',
        'asian': 'CGCGGGCCG'
    }
}

osumljenci = {
    'Eva': {
        'hair': 'blonde',
        'face': 'oval',
        'eyes': 'blue',
        'gender': 'female',
        'race': 'white'
    },
    'Larisa': {
        'hair': 'brown',
        'face': 'oval',
        'eyes': 'brown',
        'gender': 'female',
        'race': 'white'
    },
    'Matej': {
        'hair': 'black',
        'face': 'oval',
        'eyes': 'blue',
        'gender': 'male',
        'race': 'white'
    },
    'Miha': {
        'hair': 'brown',
        'face': 'square',
        'eyes': 'green',
        'gender': 'male',
        'race': 'white'
    }
}

dna_datoteka = open('dna.txt', 'r')
dna = dna_datoteka.read()
dna_datoteka.close()

osumljenec = {}

for key, value in karakteristike.iteritems():
    for karakteristika, sekvenca in value.iteritems():
        if dna.find(sekvenca) != -1:
            osumljenec[key] = karakteristika
            break

ime = ''

for n, value in osumljenci.iteritems():
    trenutno_ime = ''

    for k, v in value.iteritems():
        if osumljenec[k] == v:
            trenutno_ime = n
        else:
            trenutno_ime = ''
            break

    if trenutno_ime:
        ime = trenutno_ime
        break

print "Ime osumljenca je %s." % ime