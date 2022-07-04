import re, nltk
print("This function is called parstag. Run it to tag any text.")

verbpres = [u'ā', u'āmuz', u'āvar', u'ār' , u'oft', u'ist', u'bar',
            u'bor', u'band', u'paz', u'par', u'puš', u'xar', u'xāb',
            u'xāh', u'xā', u'xān', u'xun', u'dār', u'dān', u'dun',
            u'dav', u'do\'', u'bin', u'rān', u'run', u'res', u'rav',
            u'zan', u'sāz', u'šor', u'šek',
            u'šenās', u'šnās', u'ferest', u'frest',
            u'foruš', u'fahm', u'kon', u'koš', u'keš', u'gir', u'gu', u'mir', u'nešin',
            u'šin', u'nevis', u'ārā', u'āzār', u'ālā', u'āzmā', u'āfarin', u'āmiz',
            u'āviz', u'afruz', u'afrāz', u'afzā', u'afšār', u'afkan' , u'anbār', u'ambār',
            u'andāz', u'anduz', u'andā', u'engār', u'angiz', u'bāz', u'bāf', u'bāl', u'baxš',
            u'čin', u'xiz', u'šomor', u'šmor', u'gozin', u'gard', u'biz', u'pālā', u'pazir',
            u'parākan', u'pardāz', u'parvar', u'par', u'pendār', u'peivand', u'peyvand',
            u'tāz', u'tāb', u'tavān', u'tun', u'peimā', u'peymā', u'jah', u'ju', u'dar',
            u'dozd', u'duz', u'robā', u'resān', u'resun', u'rah', u'ru', u'ris', u'rub',
            u'riz', u'zodā', u'zi', u'sepār', u'setā', u'sereš', u'sarā', u'suz', u'šetāb',
            u'farmā', u'foruz', u'farib', u'fešār', u'fakan', u'afkan', u'afgan', u'kāh',
            u'kār', u'kan', u'kub', u'godāz', u'gozār', u'zār', u'gozar', u'goriz',
            u'geri', u'gery', u'gaz', u'gozin', u'gard', u'gošā', u'gomār', u'mān',
            u'mun', u'negār', u'negar', u'namā', u'nemā', u'navāz', u'nah', u'nahonb',
            u'nahomb', u'varz', u'vaz', u'yāb', u'xābān']
verbpres_bo = [u'kon', u'gzār', u'gozār', u'gšā', u'gošā', u'koš']
verbpret = [u'āmad', u'umad', u'āmuxt', u'āvord', u'āvard', u'oftād',
            u'istād' , u'bord' , u'borid' , u'bast' , u'bud' , u'goft',
            u'poxt',  u'parid'  , u'pušid' , u'xarid', u'xābid',
            u'xāst', u'xānd', u'xund', u'xord', u'dād' , u'dāšt', u'dānest',
            u'dunest', u'david', u'doid' , u'do\'id', u'did', u'rānd',
            u'rund', u'resid', u'raft', u'zad', u'sāxt', u'šod',
            u'šostan', u'šekast', u'šenāxt', u'šnāxt', u'šenid',
            u'ferestād', u'foruxt', u'fahmid', u'kard', u'košt', u'kešid',
            u'gereft', u'goft', u'mord', u'nešast', u'nevešt', u'ārāst',
            u'āzord', u'ālud', u'āzmud', u'āfarid', u'āmixt', u'āvixt',
            u'afruxt', u'afrāxt', u'afrāšt', u'afzud' , u'afšord',
            u'afkand', u'anbāšt', u'ambāšt', u'andāxt', u'anduxt', u'andud',
            u'engāšt', u'angixt', u'bāxtan', u'bāft', u'bālid', u'baxšid',
            u'baxšud', u'čid', u'xāst', u'šomord', u'gozid', u'gašt',
            u'bixt', u'pālud' , u'paziroft', u'parākand', u'pardāxt' ,
            u'parvard' , u'parid', u'pendāšt' , u'peivast' , u'peyvast'
            , u'tāxt', u'tāft', u'tābid', u'tavānest', u'tunest' ,
            u'peimud', u'peymud', u'jast', u'jost', u'darid', u'dozdid',
            u'duxt', u'robud', u'resānd', u'resund', u'rast', u'rost'
            , u'rešt', u'roft', u'rixt', u'zodud', u'zist', u'sepord',
            u'sotud', u'serešt', u'sorud', u'suxt', u'šetāft', u'farmud',
            u'foruxt', u'fruxt' , u'farift', u'fareft', u'fešord', u'fakand',
            u'afkand', u'afgand' , u'kāst', u'kašt', u'kešt', u'kand',
            u'kuft', u'kubid', u'godāxt', u'gozāšt', u'zāšt', u'gozašt',
            u'gozārd', u'gorixt', u'gerist', u'gazid', u'gozid', u'gašt',
            u'gošud', u'gšud', u'gomāšt', u'mānd', u'mund' , u'mānest',
            u'munest', u'negāšt', u'negarist', u'nemud', u'namud',
            u'navāxt', u'nahād', u'nahoft' , u'varzid', u'vazid', u'yāft', u'xābānd']
imperative = [u'šo', u'šow', u'de', u'ro', u'row', u'šnow', u'šno']
imperative_bo = [u'ro', u'row']
nonimperative = [u'š', u'g', u'd', u'dah', u'šav', u'r', u'rav', u'šenav', u'šnav']
bash = [u'bāš']
dar = [u'dār']

vowels = [u'a',u'ā',u'o',u'u',u'e',u'i']
consonants = [u'b',u'č',u'd',u'f',u'g',u'h',u'j',u'k',u'l',u'm',u'n',u'p',u'q',u'r',u's',u't',u'v',u'x',u'w',u'y',u'z',u'š',u'ž',u'\'']

# ------ imperative -------

imper = []

for w in verbpres:
    imper.append(w)

for w in imperative:
    imper.append(w)

for w in verbpres:
    if w[0] in vowels:
        imper.append(u'biy' + w)

for w in verbpres:
    if w[0] in vowels:
        imper.append(u'bi' + w)

for w in verbpres:
    if w[0] in consonants:
        imper.append(u'be' + w)

for w in imperative:
    imper.append(u'be' + w)

for w in imperative_bo:
    imper.append(u'bo' + w)

for w in bash:
    imper.append(w)

# ------ negative imperative -------

Nimper = []

for w in verbpres:
    if w[0] in vowels:
        Nimper.append(u'nay' + w)

for w in verbpres:
    if w[0] in consonants:
        Nimper.append(u'na' + w)

for w in imperative:
    Nimper.append(u'na' + w)

for w in bash:
    Nimper.append(u'na' + w)

# ---- present subjunctive ----

konj = []

for w in verbpres:
    if w[0] in vowels:
        konj.append(u'biy' + w)

for w in verbpres:
        konj.append(u'bi' + w)

for w in verbpres:
    if w[0] in consonants:
        konj.append(u'be' + w)

for w in nonimperative:
    konj.append(u'be' + w)

for w in verbpres_bo:
        konj.append(u'bo' + w)

for w in verbpres:
    konj.append(w)

for w in nonimperative:
    konj.append(w)

for w in bash:
    konj.append(w)

konj_1s = []

for w in konj:
    if w[-1] in vowels:
        konj_1s.append(w + u'yam')

for w in konj:
    if w[-1] in vowels:
        konj_1s.append(w + u'm')

for w in konj:
    if w[-1] in consonants:
        konj_1s.append(w + u'am')

# - object

konj_1s_o2s = []

for w in konj_1s:
    konj_1s_o2s.append(w + u'et')

for w in konj_1s:
    konj_1s_o2s.append(w + u'at')

konj_1s_o3s = []

for w in konj_1s:
    konj_1s_o3s.append(w + u'eš')

for w in konj_1s:
    konj_1s_o3s.append(w + u'aš')

konj_1s_o1pl = []

for w in konj_1s:
    konj_1s_o1pl.append(w + u'emān')

for w in konj_1s:
    konj_1s_o1pl.append(w + u'emun')


konj_1s_o2pl = []

for w in konj_1s:
    konj_1s_o2pl.append(w + u'etān')

for w in konj_1s:
    konj_1s_o2pl.append(w + u'etun')

konj_1s_o3pl = []

for w in konj_1s:
    konj_1s_o3pl.append(w + u'ešān')

for w in konj_1s:
    konj_1s_o3pl.append(w + u'ešun')


# ----

konj_2s = []

for w in konj:
    if w[-1] in vowels:
        konj_2s.append(w + u'yi')

for w in konj:
    if w[-1] in vowels:
        konj_2s.append(w + u'y')

for w in konj:
        konj_2s.append(w + u'i')

# ---- object

konj_2s_o2s = []

for w in konj_2s:
    konj_2s_o2s.append(w + 'yet')

for w in konj_2s:
    konj_2s_o2s.append(w + 'yat')

konj_2s_o3s = []

for w in konj_2s:
    konj_2s_o3s.append(w + u'eš')

for w in konj_2s:
    konj_2s_o3s.append(w + u'aš')

konj_2s_o1pl = []

for w in konj_2s:
    konj_2s_o1pl.append(w + u'emān')

for w in konj_2s:
    konj_2s_o1pl.append(w + u'emun')


konj_2s_o2pl = []

for w in konj_2s:
    konj_2s_o2pl.append(w + u'etān')

for w in konj_2s:
    konj_2s_o2pl.append(w + u'etun')

konj_2s_o3pl = []

for w in konj_2s:
    konj_2s_o3pl.append(w + u'ešān')

for w in konj_2s:
    konj_2s_o3pl.append(w + u'ešun')

# ----


konj_3s = []

for w in konj:
    if w[-1] in vowels:
        konj_3s.append(w + u'yad')

for w in konj:
    if w[-1] in vowels:
        konj_3s.append(w + u'd')

for w in konj:
    if w[-1] in consonants:
        konj_3s.append(w + u'ad')

for w in konj:
    if w[-1] in consonants:
        konj_3s.append(w + u'e')

# ---- object

konj_3s_o2s = []

for w in konj_3s:
    konj_3s_o2s.append(w + u'et')

for w in konj_3s:
    konj_3s_o2s.append(w + u'at')

konj_3s_o3s = []

for w in konj_3s:
    konj_3s_o3s.append(w + u'eš')

for w in konj_3s:
    konj_3s_o3s.append(w + u'aš')

konj_3s_o1pl = []

for w in konj_3s:
    konj_3s_o1pl.append(w + u'emān')

for w in konj_3s:
    konj_3s_o1pl.append(w + u'emun')


konj_3s_o2pl = []

for w in konj_3s:
    konj_3s_o2pl.append(w + u'etān')

for w in konj_3s:
    konj_3s_o2pl.append(w + u'etun')

konj_3s_o3pl = []

for w in konj_3s:
    konj_3s_o3pl.append(w + u'ešān')

for w in konj_3s:
    konj_3s_o3pl.append(w + u'ešun')

# ----

konj_1pl = []

for w in konj:
    if w[-1] in vowels:
        konj_1pl.append(w + u'yim')

for w in konj:
    if w[-1] in consonants:
        konj_1pl.append(w + u'im')

# ---- object

konj_1pl_o2s = []

for w in konj_1pl:
    konj_1pl_o2s.append(w + u'et')

for w in konj_1pl:
    konj_1pl_o2s.append(w + u'at')

konj_1pl_o3s = []

for w in konj_1pl:
    konj_1pl_o3s.append(w + u'eš')

for w in konj_1pl:
    konj_1pl_o3s.append(w + u'aš')

konj_1pl_o1pl = []

for w in konj_1pl:
    konj_1pl_o1pl.append(w + u'emān')

for w in konj_1pl:
    konj_1pl_o1pl.append(w + u'emun')


konj_1pl_o2pl = []

for w in konj_1pl:
    konj_1pl_o2pl.append(w + u'etān')

for w in konj_1pl:
    konj_1pl_o2pl.append(w + u'etun')

konj_1pl_o3pl = []

for w in konj_1pl:
    konj_1pl_o3pl.append(w + u'ešān')

for w in konj_1pl:
    konj_1pl_o3pl.append(w + u'ešun')

# ----

konj_2pl = []

for w in konj:
    if w[-1] in vowels:
        konj_2pl.append(w + u'yid')

for w in konj:
    if w[-1] in consonants:
        konj_2pl.append(w + u'id')

for w in konj:
    if w[-1] in vowels:
        konj_2pl.append(w + u'yin')

for w in konj:
    if w[-1] in consonants:
        konj_2pl.append(w + u'in')

# ---- object

konj_2pl_o2s = []

for w in konj_2pl:
    konj_2pl_o2s.append(w + u'et')

for w in konj_2pl:
    konj_2pl_o2s.append(w + u'at')

konj_2pl_o3s = []

for w in konj_2pl:
    konj_2pl_o3s.append(w + u'eš')

for w in konj_2pl:
    konj_2pl_o3s.append(w + u'aš')

konj_2pl_o1pl = []

for w in konj_2pl:
    konj_2pl_o1pl.append(w + u'emān')

for w in konj_2pl:
    konj_2pl_o1pl.append(w + u'emun')


konj_2pl_o2pl = []

for w in konj_2pl:
    konj_2pl_o2pl.append(w + u'etān')

for w in konj_2pl:
    konj_2pl_o2pl.append(w + u'etun')

konj_2pl_o3pl = []

for w in konj_2pl:
    konj_2pl_o3pl.append(w + u'ešān')

for w in konj_2pl:
    konj_2pl_o3pl.append(w + u'ešun')

# ----

konj_3pl = []

for w in konj:
    if w[-1] in vowels:
        konj_3pl.append(w + u'yand')

for w in konj:
    if w[-1] in consonants:
        konj_3pl.append(w + u'and')

for w in konj:
    if w[-1] in vowels:
        konj_3pl.append(w + u'yan')

for w in konj:
    if w[-1] in consonants:
        konj_3pl.append(w + u'an')

# ---- object

konj_3pl_o2s = []

for w in konj_3pl:
    konj_3pl_o2s.append(w + u'et')

for w in konj_3pl:
    konj_3pl_o2s.append(w + u'at')

konj_3pl_o3s = []

for w in konj_3pl:
    konj_3pl_o3s.append(w + u'eš')

for w in konj_3pl:
    konj_3pl_o3s.append(w + u'aš')

konj_3pl_o1pl = []

for w in konj_3pl:
    konj_3pl_o1pl.append(w + u'emān')

for w in konj_3pl:
    konj_3pl_o1pl.append(w + u'emun')


konj_3pl_o2pl = []

for w in konj_3pl:
    konj_3pl_o2pl.append(w + u'etān')

for w in konj_3pl:
    konj_3pl_o2pl.append(w + u'etun')

konj_3pl_o3pl = []

for w in konj_3pl:
    konj_3pl_o3pl.append(w + u'ešān')

for w in konj_3pl:
    konj_3pl_o3pl.append(w + u'ešun')


# ------ negative present subjunctive ------


Nkonj = []

for w in verbpres:
    if w[0] in vowels:
        Nkonj.append(u'nay' + w)

for w in verbpres:
    if w[0] in consonants:
        Nkonj.append(u'nay' + w)

for w in verbpres:
    Nkonj.append(u'na' + w)

for w in nonimperative:
    Nkonj.append(u'na' + w)

for w in bash:
    Nkonj.append(u'na' + w)


Nkonj_1s = []

for w in Nkonj:
    if w[-1] in vowels:
        Nkonj_1s.append(w + u'yam')

for w in Nkonj:
    if w[-1] in vowels:
        Nkonj_1s.append(w + u'm')

for w in Nkonj:
    if w[-1] in consonants:
        Nkonj_1s.append(w + u'am')

# ---- object

Nkonj_1s_o2s = []

for w in Nkonj_1s:
    Nkonj_1s_o2s.append(w + u'et')

for w in Nkonj_1s:
    Nkonj_1s_o2s.append(w + u'at')

Nkonj_1s_o3s = []

for w in Nkonj_1s:
    Nkonj_1s_o3s.append(w + u'eš')

for w in Nkonj_1s:
    Nkonj_1s_o3s.append(w + u'aš')

Nkonj_1s_o1pl = []

for w in Nkonj_1s:
    Nkonj_1s_o1pl.append(w + u'emān')

for w in Nkonj_1s:
    Nkonj_1s_o1pl.append(w + u'emun')


Nkonj_1s_o2pl = []

for w in Nkonj_1s:
    Nkonj_1s_o2pl.append(w + u'etān')

for w in Nkonj_1s:
    Nkonj_1s_o2pl.append(w + u'etun')

Nkonj_1s_o3pl = []

for w in Nkonj_1s:
    Nkonj_1s_o3pl.append(w + u'ešān')

for w in Nkonj_1s:
    Nkonj_1s_o3pl.append(w + u'ešun')

# ----

Nkonj_2s = []

for w in Nkonj:
    if w[-1] in vowels:
        Nkonj_2s.append(w + u'yi')

for w in Nkonj:
    if w[-1] in vowels:
        Nkonj_2s.append(w + u'y')

for w in Nkonj:
        Nkonj_2s.append(w + u'i')

# ---- object

Nkonj_2s_o2s = []

for w in Nkonj_2s:
    Nkonj_2s_o2s.append(w + u't')

for w in Nkonj_2s:
    Nkonj_2s_o2s.append(w + u't')

Nkonj_2s_o3s = []

for w in Nkonj_2s:
    Nkonj_2s_o3s.append(w + u'š')

for w in Nkonj_2s:
    Nkonj_2s_o3s.append(w + u'š')

Nkonj_2s_o1pl = []

for w in Nkonj_2s:
    Nkonj_2s_o1pl.append(w + u'mān')

for w in Nkonj_2s:
    Nkonj_2s_o1pl.append(w + u'mun')


Nkonj_2s_o2pl = []

for w in Nkonj_2s:
    Nkonj_2s_o2pl.append(w + u'tān')

for w in Nkonj_2s:
    Nkonj_2s_o2pl.append(w + u'tun')

Nkonj_2s_o3pl = []

for w in Nkonj_2s:
    Nkonj_2s_o3pl.append(w + u'šān')

for w in Nkonj_2s:
    Nkonj_2s_o3pl.append(w + u'šun')

# ----

Nkonj_3s = []

for w in Nkonj:
    if w[-1] in vowels:
        Nkonj_3s.append(w + u'yad')

for w in Nkonj:
    if w[-1] in vowels:
        Nkonj_3s.append(w + u'd')

for w in Nkonj:
    if w[-1] in consonants:
        Nkonj_3s.append(w + u'ad')

for w in Nkonj:
    if w[-1] in consonants:
        Nkonj_3s.append(w + u'e')

# ---- object

Nkonj_3s_o2s = []

for w in Nkonj_3s:
    Nkonj_3s_o2s.append(w + u'et')

for w in Nkonj_3s:
    Nkonj_3s_o2s.append(w + u'at')

Nkonj_3s_o3s = []

for w in Nkonj_3s:
    Nkonj_3s_o3s.append(w + u'eš')

for w in Nkonj_3s:
    Nkonj_3s_o3s.append(w + u'aš')

Nkonj_3s_o1pl = []

for w in Nkonj_3s:
    Nkonj_3s_o1pl.append(w + u'emān')

for w in Nkonj_3s:
    Nkonj_3s_o1pl.append(w + u'emun')


Nkonj_3s_o2pl = []

for w in Nkonj_3s:
    Nkonj_3s_o2pl.append(w + u'etān')

for w in Nkonj_3s:
    Nkonj_3s_o2pl.append(w + u'etun')

Nkonj_3s_o3pl = []

for w in Nkonj_3s:
    Nkonj_3s_o3pl.append(w + u'ešān')

for w in Nkonj_3s:
    Nkonj_3s_o3pl.append(w + u'ešun')

# ----

Nkonj_1pl = []

for w in Nkonj:
    if w[-1] in vowels:
        Nkonj_1pl.append(w + u'yim')

for w in Nkonj:
    if w[-1] in consonants:
        Nkonj_1pl.append(w + u'im')

# ---- object

Nkonj_1pl_o2s = []

for w in Nkonj_1pl:
    Nkonj_1pl_o2s.append(w + u'et')

for w in Nkonj_1pl:
    Nkonj_1pl_o2s.append(w + u'at')

Nkonj_1pl_o3s = []

for w in Nkonj_1pl:
    Nkonj_1pl_o3s.append(w + u'eš')

for w in Nkonj_1pl:
    Nkonj_1pl_o3s.append(w + u'aš')

Nkonj_1pl_o1pl = []

for w in Nkonj_1pl:
    Nkonj_1pl_o1pl.append(w + u'emān')

for w in Nkonj_1pl:
    Nkonj_1pl_o1pl.append(w + u'emun')


Nkonj_1pl_o2pl = []

for w in Nkonj_1pl:
    Nkonj_1pl_o2pl.append(w + u'etān')

for w in Nkonj_1pl:
    Nkonj_1pl_o2pl.append(w + u'etun')

Nkonj_1pl_o3pl = []

for w in Nkonj_1pl:
    Nkonj_1pl_o3pl.append(w + u'ešān')

for w in Nkonj_1pl:
    Nkonj_1pl_o3pl.append(w + u'ešun')

# ----

Nkonj_2pl = []

for w in Nkonj:
    if w[-1] in vowels:
        Nkonj_2pl.append(w + u'yid')

for w in Nkonj:
    if w[-1] in consonants:
        Nkonj_2pl.append(w + u'id')

for w in Nkonj:
    if w[-1] in vowels:
        Nkonj_2pl.append(w + u'yin')

for w in Nkonj:
    if w[-1] in consonants:
        Nkonj_2pl.append(w + u'in')

# ---- object

Nkonj_2pl_o2s = []

for w in Nkonj_2pl:
    Nkonj_2pl_o2s.append(w + u'et')

for w in Nkonj_2pl:
    Nkonj_2pl_o2s.append(w + u'at')

Nkonj_2pl_o3s = []

for w in Nkonj_2pl:
    Nkonj_2pl_o3s.append(w + u'eš')

for w in Nkonj_2pl:
    Nkonj_2pl_o3s.append(w + u'aš')

Nkonj_2pl_o1pl = []

for w in Nkonj_2pl:
    Nkonj_2pl_o1pl.append(w + u'emān')

for w in Nkonj_2pl:
    Nkonj_2pl_o1pl.append(w + u'emun')


Nkonj_2pl_o2pl = []

for w in Nkonj_2pl:
    Nkonj_2pl_o2pl.append(w + u'etān')

for w in Nkonj_2pl:
    Nkonj_2pl_o2pl.append(w + u'etun')

Nkonj_2pl_o3pl = []

for w in Nkonj_2pl:
    Nkonj_2pl_o3pl.append(w + u'ešān')

for w in Nkonj_2pl:
    Nkonj_2pl_o3pl.append(w + u'ešun')

# ----

Nkonj_3pl = []

for w in Nkonj:
    if w[-1] in vowels:
        Nkonj_3pl.append(w + u'yand')

for w in Nkonj:
    if w[-1] in consonants:
        Nkonj_3pl.append(w + u'and')

for w in Nkonj:
    if w[-1] in vowels:
        Nkonj_3pl.append(w + u'yan')

for w in Nkonj:
    if w[-1] in consonants:
        Nkonj_3pl.append(w + u'an')

# ---- object

Nkonj_3pl_o2s = []

for w in Nkonj_3pl:
    Nkonj_3pl_o2s.append(w + u'et')

for w in Nkonj_3pl:
    Nkonj_3pl_o2s.append(w + u'at')

Nkonj_3pl_o3s = []

for w in Nkonj_3pl:
    Nkonj_3pl_o3s.append(w + u'eš')

for w in Nkonj_3pl:
    Nkonj_3pl_o3s.append(w + u'aš')

Nkonj_3pl_o1pl = []

for w in Nkonj_3pl:
    Nkonj_3pl_o1pl.append(w + u'emān')

for w in Nkonj_3pl:
    Nkonj_3pl_o1pl.append(w + u'emun')


Nkonj_3pl_o2pl = []

for w in Nkonj_3pl:
    Nkonj_3pl_o2pl.append(w + u'etān')

for w in Nkonj_3pl:
    Nkonj_3pl_o2pl.append(w + u'etun')

Nkonj_3pl_o3pl = []

for w in Nkonj_3pl:
    Nkonj_3pl_o3pl.append(w + u'ešān')

for w in Nkonj_3pl:
    Nkonj_3pl_o3pl.append(w + u'ešun')

# ----

#------ present indicative ------

indstem = []

for w in verbpres:
    indstem.append(u'mi' + w)

for w in verbpres:
    if w[0] in vowels:
        indstem.append(u'miy' + w)

for w in nonimperative:
    indstem.append(u'mi' + w)

for w in dar:
    indstem.append(w)

# ---

ind_1s = []

for w in indstem:
    if w[-1] in vowels:
        ind_1s.append(w + u'yam')

for w in indstem:
    if w[-1] in vowels:
        ind_1s.append(w + u'm')

for w in indstem:
    if w[-1] in consonants:
        ind_1s.append(w + u'am')

ind_1s.append(u'hastam')

# ---- object

ind_1s_o2s = []

for w in ind_1s:
    ind_1s_o2s.append(w + u'et')

for w in ind_1s:
    ind_1s_o2s.append(w + u'at')

ind_1s_o3s = []

for w in ind_1s:
    ind_1s_o3s.append(w + u'eš')

for w in ind_1s:
    ind_1s_o3s.append(w + u'aš')

ind_1s_o1pl = []

for w in ind_1s:
    ind_1s_o1pl.append(w + u'emān')

for w in ind_1s:
    ind_1s_o1pl.append(w + u'emun')


ind_1s_o2pl = []

for w in ind_1s:
    ind_1s_o2pl.append(w + u'etān')

for w in ind_1s:
    ind_1s_o2pl.append(w + u'etun')

ind_1s_o3pl = []

for w in ind_1s:
    ind_1s_o3pl.append(w + u'ešān')

for w in ind_1s:
    ind_1s_o3pl.append(w + u'ešun')

# ----

ind_2s = []

for w in indstem:
    if w[-1] in vowels:
        ind_2s.append(w + u'yi')

for w in indstem:
    if w[-1] in vowels:
        ind_2s.append(w + u'y')

for w in indstem:
        ind_2s.append(w + u'i')

ind_2s.append(u'hasti')

# ---- object

ind_2s_o2s = []

for w in ind_2s:
    ind_2s_o2s.append(w + u't')

for w in ind_2s:
    ind_2s_o2s.append(w + u't')

ind_2s_o3s = []

for w in ind_2s:
    ind_2s_o3s.append(w + u'š')

ind_2s_o1pl = []

for w in ind_2s:
    ind_2s_o1pl.append(w + u'mān')

for w in ind_2s:
    ind_2s_o1pl.append(w + u'mun')


ind_2s_o2pl = []

for w in ind_2s:
    ind_2s_o2pl.append(w + u'tān')

for w in ind_2s:
    ind_2s_o2pl.append(w + u'tun')

ind_2s_o3pl = []

for w in ind_2s:
    ind_2s_o3pl.append(w + u'šān')

for w in ind_2s:
    ind_2s_o3pl.append(w + u'šun')

# ----

ind_3s = []

for w in indstem:
    if w[-1] in vowels:
        ind_3s.append(w + u'yad')

for w in indstem:
    if w[-1] in vowels:
        ind_3s.append(w + u'd')

for w in indstem:
    if w[-1] in consonants:
        ind_3s.append(w + u'ad')

for w in indstem:
    if w[-1] in consonants:
        ind_3s.append(w + u'e')

ind_3s.append(u'hast')
ind_3s.append(u'ast')

# ---- object

ind_3s_o2s = []

for w in ind_3s:
    ind_3s_o2s.append(w + u'et')

for w in ind_3s:
    ind_3s_o2s.append(w + u'at')

ind_3s_o3s = []

for w in ind_3s:
    ind_3s_o3s.append(w + u'eš')

for w in ind_3s:
    ind_3s_o3s.append(w + u'aš')

ind_3s_o1pl = []

for w in ind_3s:
    ind_3s_o1pl.append(w + u'emān')

for w in ind_3s:
    ind_3s_o1pl.append(w + u'emun')


ind_3s_o2pl = []

for w in ind_3s:
    ind_3s_o2pl.append(w + u'etān')

for w in ind_3s:
    ind_3s_o2pl.append(w + u'etun')

ind_3s_o3pl = []

for w in ind_3s:
    ind_3s_o3pl.append(w + u'ešān')

for w in ind_3s:
    ind_3s_o3pl.append(w + u'ešun')

# ----

ind_1pl = []

for w in indstem:
    if w[-1] in vowels:
        ind_1pl.append(w + u'yim')

for w in indstem:
    if w[-1] in consonants:
        ind_1pl.append(w + u'im')

ind_1pl.append(u'hastim')

# ---- object

ind_1pl_o2s = []

for w in ind_1pl:
    ind_1pl_o2s.append(w + u'et')

for w in ind_1pl:
    ind_1pl_o2s.append(w + u'at')

ind_1pl_o3s = []

for w in ind_1pl:
    ind_1pl_o3s.append(w + u'eš')

for w in ind_1pl:
    ind_1pl_o3s.append(w + u'aš')

ind_1pl_o1pl = []

for w in ind_1pl:
    ind_1pl_o1pl.append(w + u'emān')

for w in ind_1pl:
    ind_1pl_o1pl.append(w + u'emun')


ind_1pl_o2pl = []

for w in ind_1pl:
    ind_1pl_o2pl.append(w + u'etān')

for w in ind_1pl:
    ind_1pl_o2pl.append(w + u'etun')

ind_1pl_o3pl = []

for w in ind_1pl:
    ind_1pl_o3pl.append(w + u'ešān')

for w in ind_1pl:
    ind_1pl_o3pl.append(w + u'ešun')

# ----

ind_2pl = []

for w in indstem:
    if w[-1] in vowels:
        ind_2pl.append(w + u'yid')

for w in indstem:
    if w[-1] in consonants:
        ind_2pl.append(w + u'id')

for w in indstem:
    if w[-1] in vowels:
        ind_2pl.append(w + u'yin')

for w in indstem:
    if w[-1] in consonants:
        ind_2pl.append(w + u'in')

ind_2pl.append(u'hastid')
ind_2pl.append(u'hastin')

# ---- object

ind_2pl_o2s = []

for w in ind_2pl:
    ind_2pl_o2s.append(w + u'et')

for w in ind_2pl:
    ind_2pl_o2s.append(w + u'at')

ind_2pl_o3s = []

for w in ind_2pl:
    ind_2pl_o3s.append(w + u'eš')

for w in ind_2pl:
    ind_2pl_o3s.append(w + u'aš')

ind_2pl_o1pl = []

for w in ind_2pl:
    ind_2pl_o1pl.append(w + u'emān')

for w in ind_2pl:
    ind_2pl_o1pl.append(w + u'emun')


ind_2pl_o2pl = []

for w in ind_2pl:
    ind_2pl_o2pl.append(w + u'etān')

for w in ind_2pl:
    ind_2pl_o2pl.append(w + u'etun')

ind_2pl_o3pl = []

for w in ind_2pl:
    ind_2pl_o3pl.append(w + u'ešān')

for w in ind_2pl:
    ind_2pl_o3pl.append(w + u'ešun')

# ----

ind_3pl = []

for w in indstem:
    if w[-1] in vowels:
        ind_3pl.append(w + u'yand')

for w in indstem:
    if w[-1] in consonants:
        ind_3pl.append(w + u'and')

for w in indstem:
    if w[-1] in vowels:
        ind_3pl.append(w + u'yan')

for w in indstem:
    if w[-1] in consonants:
        ind_3pl.append(w + u'an')

ind_3pl.append(u'hastand')
ind_3pl.append(u'hastan')

# ---- object

ind_3pl_o2s = []

for w in ind_3pl:
    ind_3pl_o2s.append(w + u'et')

for w in ind_3pl:
    ind_3pl_o2s.append(w + u'at')

ind_3pl_o3s = []

for w in ind_3pl:
    ind_3pl_o3s.append(w + u'eš')

for w in ind_3pl:
    ind_3pl_o3s.append(w + u'aš')

ind_3pl_o1pl = []

for w in ind_3pl:
    ind_3pl_o1pl.append(w + u'emān')

for w in ind_3pl:
    ind_3pl_o1pl.append(w + u'emun')


ind_3pl_o2pl = []

for w in ind_3pl:
    ind_3pl_o2pl.append(w + u'etān')

for w in ind_3pl:
    ind_3pl_o2pl.append(w + u'etun')

ind_3pl_o3pl = []

for w in ind_3pl:
    ind_3pl_o3pl.append(w + u'ešān')

for w in ind_3pl:
    ind_3pl_o3pl.append(w + u'ešun')

# ----

#------ negative present indicative ------

Nindstem = []

for w in verbpres:
    Nindstem.append(u'nemi' + w)

for w in verbpres:
    if w[0] in vowels:
        Nindstem.append(u'nemiy' + w)

for w in nonimperative:
    indstem.append(u'nemi' + w)

for w in dar:
    Nindstem.append(u'na' + w)

# ---

Nind_1s = []

for w in Nindstem:
    if w[-1] in vowels:
        Nind_1s.append(w + u'yam')

for w in Nindstem:
    if w[-1] in vowels:
        Nind_1s.append(w + u'm')

for w in Nindstem:
    if w[-1] in consonants:
        Nind_1s.append(w + u'am')

Nind_1s.append(u'nistam')

# ---- object

Nind_1s_o2s = []

for w in Nind_1s:
    Nind_1s_o2s.append(w + u'et')

for w in Nind_1s:
    Nind_1s_o2s.append(w + u'at')

Nind_1s_o3s = []

for w in Nind_1s:
    Nind_1s_o3s.append(w + u'eš')

for w in Nind_1s:
    Nind_1s_o3s.append(w + u'aš')

Nind_1s_o1pl = []

for w in Nind_1s:
    Nind_1s_o1pl.append(w + u'emān')

for w in Nind_1s:
    Nind_1s_o1pl.append(w + u'emun')


Nind_1s_o2pl = []

for w in Nind_1s:
    Nind_1s_o2pl.append(w + u'etān')

for w in Nind_1s:
    Nind_1s_o2pl.append(w + u'etun')

Nind_1s_o3pl = []

for w in Nind_1s:
    Nind_1s_o3pl.append(w + u'ešān')

for w in Nind_1s:
    Nind_1s_o3pl.append(w + u'ešun')

# ----

Nind_2s = []

for w in Nindstem:
    if w[-1] in vowels:
        Nind_2s.append(w + u'yi')

for w in Nindstem:
    if w[-1] in vowels:
        Nind_2s.append(w + u'y')

for w in Nindstem:
        Nind_2s.append(w + u'i')

Nind_2s.append(u'nisti')

# ---- object

Nind_2s_o2s = []

for w in Nind_2s:
    Nind_2s_o2s.append(w + u't')

for w in Nind_2s:
    Nind_2s_o2s.append(w + u't')

Nind_2s_o3s = []

for w in Nind_2s:
    Nind_2s_o3s.append(w + u'š')

Nind_2s_o1pl = []

for w in Nind_2s:
    Nind_2s_o1pl.append(w + u'mān')

for w in Nind_2s:
    Nind_2s_o1pl.append(w + u'mun')


Nind_2s_o2pl = []

for w in Nind_2s:
    Nind_2s_o2pl.append(w + u'tān')

for w in Nind_2s:
    Nind_2s_o2pl.append(w + u'tun')

Nind_2s_o3pl = []

for w in Nind_2s:
    Nind_2s_o3pl.append(w + u'šān')

for w in Nind_2s:
    Nind_2s_o3pl.append(w + u'šun')

# ----

Nind_3s = []

for w in Nindstem:
    if w[-1] in vowels:
        Nind_3s.append(w + u'yad')

for w in Nindstem:
    if w[-1] in vowels:
        Nind_3s.append(w + u'd')

for w in Nindstem:
    if w[-1] in consonants:
        Nind_3s.append(w + u'ad')

for w in Nindstem:
    if w[-1] in consonants:
        Nind_3s.append(w + u'e')

Nind_3s.append(u'nist')

# ---- object

Nind_3s_o2s = []

for w in Nind_3s:
    Nind_3s_o2s.append(w + u'et')

for w in Nind_3s:
    Nind_3s_o2s.append(w + u'at')

Nind_3s_o3s = []

for w in Nind_3s:
    Nind_3s_o3s.append(w + u'eš')

for w in Nind_3s:
    Nind_3s_o3s.append(w + u'aš')

Nind_3s_o1pl = []

for w in Nind_3s:
    Nind_3s_o1pl.append(w + u'emān')

for w in Nind_3s:
    Nind_3s_o1pl.append(w + u'emun')


Nind_3s_o2pl = []

for w in Nind_3s:
    Nind_3s_o2pl.append(w + u'etān')

for w in Nind_3s:
    Nind_3s_o2pl.append(w + u'etun')

Nind_3s_o3pl = []

for w in Nind_3s:
    Nind_3s_o3pl.append(w + u'ešān')

for w in Nind_3s:
    Nind_3s_o3pl.append(w + u'ešun')

# ----

Nind_1pl = []

for w in Nindstem:
    if w[-1] in vowels:
        Nind_1pl.append(w + u'yim')

for w in Nindstem:
    if w[-1] in consonants:
        Nind_1pl.append(w + u'im')

Nind_1pl.append(u'nistim')

# ---- object

Nind_1pl_o2s = []

for w in Nind_1pl:
    Nind_1pl_o2s.append(w + u'et')

for w in Nind_1pl:
    Nind_1pl_o2s.append(w + u'at')

Nind_1pl_o3s = []

for w in Nind_1pl:
    Nind_1pl_o3s.append(w + u'eš')

for w in Nind_1pl:
    Nind_1pl_o3s.append(w + u'aš')

Nind_1pl_o1pl = []

for w in Nind_1pl:
    Nind_1pl_o1pl.append(w + u'emān')

for w in Nind_1pl:
    Nind_1pl_o1pl.append(w + u'emun')


Nind_1pl_o2pl = []

for w in Nind_1pl:
    Nind_1pl_o2pl.append(w + u'etān')

for w in Nind_1pl:
    Nind_1pl_o2pl.append(w + u'etun')

Nind_1pl_o3pl = []

for w in Nind_1pl:
    Nind_1pl_o3pl.append(w + u'ešān')

for w in Nind_1pl:
    Nind_1pl_o3pl.append(w + u'ešun')

# ----

Nind_2pl = []

for w in Nindstem:
    if w[-1] in vowels:
        Nind_2pl.append(w + u'yid')

for w in Nindstem:
    if w[-1] in consonants:
        Nind_2pl.append(w + u'id')

for w in Nindstem:
    if w[-1] in vowels:
        Nind_2pl.append(w + u'yin')

for w in Nindstem:
    if w[-1] in consonants:
        Nind_2pl.append(w + u'in')

Nind_2pl.append(u'nistid')
Nind_2pl.append(u'nistin')

# ---- object

Nind_2pl_o2s = []

for w in Nind_2pl:
    Nind_2pl_o2s.append(w + u'et')

for w in Nind_2pl:
    Nind_2pl_o2s.append(w + u'at')

Nind_2pl_o3s = []

for w in Nind_2pl:
    Nind_2pl_o3s.append(w + u'eš')

for w in Nind_2pl:
    Nind_2pl_o3s.append(w + u'aš')

Nind_2pl_o1pl = []

for w in Nind_2pl:
    Nind_2pl_o1pl.append(w + u'emān')

for w in Nind_2pl:
    Nind_2pl_o1pl.append(w + u'emun')


Nind_2pl_o2pl = []

for w in Nind_2pl:
    Nind_2pl_o2pl.append(w + u'etān')

for w in Nind_2pl:
    Nind_2pl_o2pl.append(w + u'etun')

Nind_2pl_o3pl = []

for w in Nind_2pl:
    Nind_2pl_o3pl.append(w + u'ešān')

for w in Nind_2pl:
    Nind_2pl_o3pl.append(w + u'ešun')

# ----

Nind_3pl = []

for w in Nindstem:
    if w[-1] in vowels:
        Nind_3pl.append(w + u'yand')

for w in Nindstem:
    if w[-1] in consonants:
        Nind_3pl.append(w + u'and')

for w in Nindstem:
    if w[-1] in vowels:
        Nind_3pl.append(w + u'yan')

for w in Nindstem:
    if w[-1] in consonants:
        Nind_3pl.append(w + u'an')

Nind_3pl.append(u'nistand')
Nind_3pl.append(u'nistan')

# ---- object

Nind_3pl_o2s = []

for w in Nind_3pl:
    Nind_3pl_o2s.append(w + u'et')

for w in Nind_3pl:
    Nind_3pl_o2s.append(w + u'at')

Nind_3pl_o3s = []

for w in Nind_3pl:
    Nind_3pl_o3s.append(w + u'eš')

for w in Nind_3pl:
    Nind_3pl_o3s.append(w + u'aš')

Nind_3pl_o1pl = []

for w in Nind_3pl:
    Nind_3pl_o1pl.append(w + u'emān')

for w in Nind_3pl:
    Nind_3pl_o1pl.append(w + u'emun')


Nind_3pl_o2pl = []

for w in Nind_3pl:
    Nind_3pl_o2pl.append(w + u'etān')

for w in Nind_3pl:
    Nind_3pl_o2pl.append(w + u'etun')

Nind_3pl_o3pl = []

for w in Nind_3pl:
    Nind_3pl_o3pl.append(w + u'ešān')

for w in Nind_3pl:
    Nind_3pl_o3pl.append(w + u'ešun')

# ----

# ------ preterit --------

pret_1s = []

for w in verbpret:
    pret_1s.append(w + u'am')

# ---- object

pret_1s_o2s = []

for w in pret_1s:
    pret_1s_o2s.append(w + u'et')

for w in pret_1s:
    pret_1s_o2s.append(w + u'at')

pret_1s_o3s = []

for w in pret_1s:
    pret_1s_o3s.append(w + u'eš')

for w in pret_1s:
    pret_1s_o3s.append(w + u'aš')

pret_1s_o1pl = []

for w in pret_1s:
    pret_1s_o1pl.append(w + u'emān')

for w in pret_1s:
    pret_1s_o1pl.append(w + u'emun')


pret_1s_o2pl = []

for w in pret_1s:
    pret_1s_o2pl.append(w + u'etān')

for w in pret_1s:
    pret_1s_o2pl.append(w + u'etun')

pret_1s_o3pl = []

for w in pret_1s:
    pret_1s_o3pl.append(w + u'ešān')

for w in pret_1s:
    pret_1s_o3pl.append(w + u'ešun')

# ----

pret_2s = []

for w in verbpret:
        pret_2s.append(w + u'i')

# ---- object

pret_2s_o2s = []

for w in pret_2s:
    pret_2s_o2s.append(w + u't')

for w in pret_2s:
    pret_2s_o2s.append(w + u't')

pret_2s_o3s = []

for w in pret_2s:
    pret_2s_o3s.append(w + u'š')

pret_2s_o1pl = []

for w in pret_2s:
    pret_2s_o1pl.append(w + u'mān')

for w in pret_2s:
    pret_2s_o1pl.append(w + u'mun')


pret_2s_o2pl = []

for w in pret_2s:
    pret_2s_o2pl.append(w + u'tān')

for w in pret_2s:
    pret_2s_o2pl.append(w + u'tun')

pret_2s_o3pl = []

for w in pret_2s:
    pret_2s_o3pl.append(w + u'šān')

for w in pret_2s:
    pret_2s_o3pl.append(w + u'šun')

# ----

pret_3s = []

for w in verbpret:
    pret_3s.append(w)

# ---- object

pret_3s_o2s = []

for w in pret_3s:
    pret_3s_o2s.append(w + u'et')

for w in pret_3s:
    pret_3s_o2s.append(w + u'at')

pret_3s_o3s = []

for w in pret_3s:
    pret_3s_o3s.append(w + u'eš')

for w in pret_3s:
    pret_3s_o3s.append(w + u'aš')

pret_3s_o1pl = []

for w in pret_3s:
    pret_3s_o1pl.append(w + u'emān')

for w in pret_3s:
    pret_3s_o1pl.append(w + u'emun')


pret_3s_o2pl = []

for w in pret_3s:
    pret_3s_o2pl.append(w + u'etān')

for w in pret_3s:
    pret_3s_o2pl.append(w + u'etun')

pret_3s_o3pl = []

for w in pret_3s:
    pret_3s_o3pl.append(w + u'ešān')

for w in pret_3s:
    pret_3s_o3pl.append(w + u'ešun')

# ----

pret_1pl = []

for w in verbpret:
    pret_1pl.append(w + u'im')

# ---- object

pret_1pl_o2s = []

for w in pret_1pl:
    pret_1pl_o2s.append(w + u'et')

for w in pret_1pl:
    pret_1pl_o2s.append(w + u'at')

pret_1pl_o3s = []

for w in pret_1pl:
    pret_1pl_o3s.append(w + u'eš')

for w in pret_1pl:
    pret_1pl_o3s.append(w + u'aš')

pret_1pl_o1pl = []

for w in pret_1pl:
    pret_1pl_o1pl.append(w + u'emān')

for w in pret_1pl:
    pret_1pl_o1pl.append(w + u'emun')


pret_1pl_o2pl = []

for w in pret_1pl:
    pret_1pl_o2pl.append(w + u'etān')

for w in pret_1pl:
    pret_1pl_o2pl.append(w + u'etun')

pret_1pl_o3pl = []

for w in pret_1pl:
    pret_1pl_o3pl.append(w + u'ešān')

for w in pret_1pl:
    pret_1pl_o3pl.append(w + u'ešun')

# ----

pret_2pl = []

for w in verbpret:
    pret_2pl.append(w + u'id')

for w in verbpret:
    pret_2pl.append(w + u'in')

# ---- object

pret_2pl_o2s = []

for w in pret_2pl:
    pret_2pl_o2s.append(w + u'et')

for w in pret_2pl:
    pret_2pl_o2s.append(w + u'at')

pret_2pl_o3s = []

for w in pret_2pl:
    pret_2pl_o3s.append(w + u'eš')

for w in pret_2pl:
    pret_2pl_o3s.append(w + u'aš')

pret_2pl_o1pl = []

for w in pret_2pl:
    pret_2pl_o1pl.append(w + u'emān')

for w in pret_2pl:
    pret_2pl_o1pl.append(w + u'emun')


pret_2pl_o2pl = []

for w in pret_2pl:
    pret_2pl_o2pl.append(w + u'etān')

for w in pret_2pl:
    pret_2pl_o2pl.append(w + u'etun')

pret_2pl_o3pl = []

for w in pret_2pl:
    pret_2pl_o3pl.append(w + u'ešān')

for w in pret_2pl:
    pret_2pl_o3pl.append(w + u'ešun')

# ----

pret_3pl = []

for w in verbpret:
    pret_3pl.append(w + u'and')


# ---- object

pret_3pl_o2s = []

for w in pret_3pl:
    pret_3pl_o2s.append(w + u'et')

for w in pret_3pl:
    pret_3pl_o2s.append(w + u'at')

pret_3pl_o3s = []

for w in pret_3pl:
    pret_3pl_o3s.append(w + u'eš')

for w in pret_3pl:
    pret_3pl_o3s.append(w + u'aš')

pret_3pl_o1pl = []

for w in pret_3pl:
    pret_3pl_o1pl.append(w + u'emān')

for w in pret_3pl:
    pret_3pl_o1pl.append(w + u'emun')


pret_3pl_o2pl = []

for w in pret_3pl:
    pret_3pl_o2pl.append(w + u'etān')

for w in pret_3pl:
    pret_3pl_o2pl.append(w + u'etun')

pret_3pl_o3pl = []

for w in pret_3pl:
    pret_3pl_o3pl.append(w + u'ešān')

for w in pret_3pl:
    pret_3pl_o3pl.append(w + u'ešun')

# ----

# ---- negative preterit -----

Nverbpret = []

for w in verbpret:
    if w[0] in vowels:
        Nverbpret.append(u'nay' + w)

for w in verbpret:
    if w[0] in consonants:
        Nverbpret.append(u'na' + w)

# ---

Npret_1s = []

for w in Nverbpret:
    Npret_1s.append(w + u'am')

# ---- object

Npret_1s_o2s = []

for w in Npret_1s:
    Npret_1s_o2s.append(w + u'et')

for w in Npret_1s:
    Npret_1s_o2s.append(w + u'at')

Npret_1s_o3s = []

for w in Npret_1s:
    Npret_1s_o3s.append(w + u'eš')

for w in Npret_1s:
    Npret_1s_o3s.append(w + u'aš')

Npret_1s_o1pl = []

for w in Npret_1s:
    Npret_1s_o1pl.append(w + u'emān')

for w in Npret_1s:
    Npret_1s_o1pl.append(w + u'emun')


Npret_1s_o2pl = []

for w in Npret_1s:
    Npret_1s_o2pl.append(w + u'etān')

for w in Npret_1s:
    Npret_1s_o2pl.append(w + u'etun')

Npret_1s_o3pl = []

for w in Npret_1s:
    Npret_1s_o3pl.append(w + u'ešān')

for w in Npret_1s:
    Npret_1s_o3pl.append(w + u'ešun')

# ----

Npret_2s = []

for w in Nverbpret:
        Npret_2s.append(w + u'i')

# ---- object

Npret_2s_o2s = []

for w in Npret_2s:
    Npret_2s_o2s.append(w + u't')

for w in Npret_2s:
    Npret_2s_o2s.append(w + u't')

Npret_2s_o3s = []

for w in Npret_2s:
    Npret_2s_o3s.append(w + u'š')

Npret_2s_o1pl = []

for w in Npret_2s:
    Npret_2s_o1pl.append(w + u'mān')

for w in Npret_2s:
    Npret_2s_o1pl.append(w + u'mun')


Npret_2s_o2pl = []

for w in Npret_2s:
    Npret_2s_o2pl.append(w + u'tān')

for w in Npret_2s:
    Npret_2s_o2pl.append(w + u'tun')

Npret_2s_o3pl = []

for w in Npret_2s:
    Npret_2s_o3pl.append(w + u'šān')

for w in Npret_2s:
    Npret_2s_o3pl.append(w + u'šun')

# ----

Npret_3s = []

for w in Nverbpret:
    Npret_3s.append(w)

# ---- object

Npret_3s_o2s = []

for w in Npret_3s:
    Npret_3s_o2s.append(w + u'et')

for w in Npret_3s:
    Npret_3s_o2s.append(w + u'at')

Npret_3s_o3s = []

for w in Npret_3s:
    Npret_3s_o3s.append(w + u'eš')

for w in Npret_3s:
    Npret_3s_o3s.append(w + u'aš')

Npret_3s_o1pl = []

for w in Npret_3s:
    Npret_3s_o1pl.append(w + u'emān')

for w in Npret_3s:
    Npret_3s_o1pl.append(w + u'emun')


Npret_3s_o2pl = []

for w in Npret_3s:
    Npret_3s_o2pl.append(w + u'etān')

for w in Npret_3s:
    Npret_3s_o2pl.append(w + u'etun')

Npret_3s_o3pl = []

for w in Npret_3s:
    Npret_3s_o3pl.append(w + u'ešān')

for w in Npret_3s:
    Npret_3s_o3pl.append(w + u'ešun')

# ----

Npret_1pl = []

for w in Nverbpret:
    Npret_1pl.append(w + u'im')

# ---- object

Npret_1pl_o2s = []

for w in Npret_1pl:
    Npret_1pl_o2s.append(w + u'et')

for w in Npret_1pl:
    Npret_1pl_o2s.append(w + u'at')

Npret_1pl_o3s = []

for w in Npret_1pl:
    Npret_1pl_o3s.append(w + u'eš')

for w in Npret_1pl:
    Npret_1pl_o3s.append(w + u'aš')

Npret_1pl_o1pl = []

for w in Npret_1pl:
    Npret_1pl_o1pl.append(w + u'emān')

for w in Npret_1pl:
    Npret_1pl_o1pl.append(w + u'emun')


Npret_1pl_o2pl = []

for w in Npret_1pl:
    Npret_1pl_o2pl.append(w + u'etān')

for w in Npret_1pl:
    Npret_1pl_o2pl.append(w + u'etun')

Npret_1pl_o3pl = []

for w in Npret_1pl:
    Npret_1pl_o3pl.append(w + u'ešān')

for w in Npret_1pl:
    Npret_1pl_o3pl.append(w + u'ešun')

# ----

Npret_2pl = []

for w in Nverbpret:
    Npret_2pl.append(w + u'id')

for w in Nverbpret:
    Npret_2pl.append(w + u'in')

# ---- object

Npret_2pl_o2s = []

for w in Npret_2pl:
    Npret_2pl_o2s.append(w + u'et')

for w in Npret_2pl:
    Npret_2pl_o2s.append(w + u'at')

Npret_2pl_o3s = []

for w in Npret_2pl:
    Npret_2pl_o3s.append(w + u'eš')

for w in Npret_2pl:
    Npret_2pl_o3s.append(w + u'aš')

Npret_2pl_o1pl = []

for w in Npret_2pl:
    Npret_2pl_o1pl.append(w + u'emān')

for w in Npret_2pl:
    Npret_2pl_o1pl.append(w + u'emun')


Npret_2pl_o2pl = []

for w in Npret_2pl:
    Npret_2pl_o2pl.append(w + u'etān')

for w in Npret_2pl:
    Npret_2pl_o2pl.append(w + u'etun')

Npret_2pl_o3pl = []

for w in Npret_2pl:
    Npret_2pl_o3pl.append(w + u'ešān')

for w in Npret_2pl:
    Npret_2pl_o3pl.append(w + u'ešun')

# ----

Npret_3pl = []

for w in Nverbpret:
    Npret_3pl.append(w + u'and')


# ---- object

Npret_3pl_o2s = []

for w in Npret_3pl:
    Npret_3pl_o2s.append(w + u'et')

for w in Npret_3pl:
    Npret_3pl_o2s.append(w + u'at')

Npret_3pl_o3s = []

for w in Npret_3pl:
    Npret_3pl_o3s.append(w + u'eš')

for w in Npret_3pl:
    Npret_3pl_o3s.append(w + u'aš')

Npret_3pl_o1pl = []

for w in Npret_3pl:
    Npret_3pl_o1pl.append(w + u'emān')

for w in Npret_3pl:
    Npret_3pl_o1pl.append(w + u'emun')


Npret_3pl_o2pl = []

for w in Npret_3pl:
    Npret_3pl_o2pl.append(w + u'etān')

for w in Npret_3pl:
    Npret_3pl_o2pl.append(w + u'etun')

Npret_3pl_o3pl = []

for w in Npret_3pl:
    Npret_3pl_o3pl.append(w + u'ešān')

for w in Npret_3pl:
    Npret_3pl_o3pl.append(w + u'ešun')

# ----

# ----- present participle ------

prespart = []

for w in verbpres:
    if w[-1] in vowels:
        prespart.append(w + u'yān')

for w in verbpres:
    if w[-1] in consonants:
        prespart.append(w + u'ān')

# ----- negative present participle -----

Nprespart = []

for w in prespart:
    if w[0] in vowels:
        Nprespart.append(u'nay' + w)

for w in prespart:
    if w[0] in consonants:
        Nprespart.append(u'na' + w)

# ---- imperfect -----

verbimp = []

for w in verbpret:
    if w[0] in vowels:
        verbimp.append(u'miy' + w)

for w in verbpret:
        verbimp.append(u'mi' + w)

# ---

imp_1s = []

for w in verbimp:
    imp_1s.append(w + u'am')

# ---- object

imp_1s_o2s = []

for w in imp_1s:
    imp_1s_o2s.append(w + u'et')

for w in imp_1s:
    imp_1s_o2s.append(w + u'at')

imp_1s_o3s = []

for w in imp_1s:
    imp_1s_o3s.append(w + u'eš')

for w in imp_1s:
    imp_1s_o3s.append(w + u'aš')

imp_1s_o1pl = []

for w in imp_1s:
    imp_1s_o1pl.append(w + u'emān')

for w in imp_1s:
    imp_1s_o1pl.append(w + u'emun')


imp_1s_o2pl = []

for w in imp_1s:
    imp_1s_o2pl.append(w + u'etān')

for w in imp_1s:
    imp_1s_o2pl.append(w + u'etun')

imp_1s_o3pl = []

for w in imp_1s:
    imp_1s_o3pl.append(w + u'ešān')

for w in imp_1s:
    imp_1s_o3pl.append(w + u'ešun')

# ----

imp_2s = []

for w in verbimp:
        imp_2s.append(w + u'i')

# ---- object

imp_2s_o2s = []

for w in imp_2s:
    imp_2s_o2s.append(w + u't')

for w in imp_2s:
    imp_2s_o2s.append(w + u't')

imp_2s_o3s = []

for w in imp_2s:
    imp_2s_o3s.append(w + u'š')

imp_2s_o1pl = []

for w in imp_2s:
    imp_2s_o1pl.append(w + u'mān')

for w in imp_2s:
    imp_2s_o1pl.append(w + u'mun')


imp_2s_o2pl = []

for w in imp_2s:
    imp_2s_o2pl.append(w + u'tān')

for w in imp_2s:
    imp_2s_o2pl.append(w + u'tun')

imp_2s_o3pl = []

for w in imp_2s:
    imp_2s_o3pl.append(w + u'šān')

for w in imp_2s:
    imp_2s_o3pl.append(w + u'šun')

# ----

imp_3s = []

for w in verbimp:
    imp_3s.append(w)

# ---- object

imp_3s_o2s = []

for w in imp_3s:
    imp_3s_o2s.append(w + u'et')

for w in imp_3s:
    imp_3s_o2s.append(w + u'at')

imp_3s_o3s = []

for w in imp_3s:
    imp_3s_o3s.append(w + u'eš')

for w in imp_3s:
    imp_3s_o3s.append(w + u'aš')

imp_3s_o1pl = []

for w in imp_3s:
    imp_3s_o1pl.append(w + u'emān')

for w in imp_3s:
    imp_3s_o1pl.append(w + u'emun')


imp_3s_o2pl = []

for w in imp_3s:
    imp_3s_o2pl.append(w + u'etān')

for w in imp_3s:
    imp_3s_o2pl.append(w + u'etun')

imp_3s_o3pl = []

for w in imp_3s:
    imp_3s_o3pl.append(w + u'ešān')

for w in imp_3s:
    imp_3s_o3pl.append(w + u'ešun')

# ----

imp_1pl = []

for w in verbimp:
    imp_1pl.append(w + u'im')

# ---- object

imp_1pl_o2s = []

for w in imp_1pl:
    imp_1pl_o2s.append(w + u'et')

for w in imp_1pl:
    imp_1pl_o2s.append(w + u'at')

imp_1pl_o3s = []

for w in imp_1pl:
    imp_1pl_o3s.append(w + u'eš')

for w in imp_1pl:
    imp_1pl_o3s.append(w + u'aš')

imp_1pl_o1pl = []

for w in imp_1pl:
    imp_1pl_o1pl.append(w + u'emān')

for w in imp_1pl:
    imp_1pl_o1pl.append(w + u'emun')


imp_1pl_o2pl = []

for w in imp_1pl:
    imp_1pl_o2pl.append(w + u'etān')

for w in imp_1pl:
    imp_1pl_o2pl.append(w + u'etun')

imp_1pl_o3pl = []

for w in imp_1pl:
    imp_1pl_o3pl.append(w + u'ešān')

for w in imp_1pl:
    imp_1pl_o3pl.append(w + u'ešun')

# ----

imp_2pl = []

for w in verbimp:
    imp_2pl.append(w + u'id')

for w in verbimp:
    imp_2pl.append(w + u'in')

# ---- object

imp_2pl_o2s = []

for w in imp_2pl:
    imp_2pl_o2s.append(w + u'et')

for w in imp_2pl:
    imp_2pl_o2s.append(w + u'at')

imp_2pl_o3s = []

for w in imp_2pl:
    imp_2pl_o3s.append(w + u'eš')

for w in imp_2pl:
    imp_2pl_o3s.append(w + u'aš')

imp_2pl_o1pl = []

for w in imp_2pl:
    imp_2pl_o1pl.append(w + u'emān')

for w in imp_2pl:
    imp_2pl_o1pl.append(w + u'emun')


imp_2pl_o2pl = []

for w in imp_2pl:
    imp_2pl_o2pl.append(w + u'etān')

for w in imp_2pl:
    imp_2pl_o2pl.append(w + u'etun')

imp_2pl_o3pl = []

for w in imp_2pl:
    imp_2pl_o3pl.append(w + u'ešān')

for w in imp_2pl:
    imp_2pl_o3pl.append(w + u'ešun')

# ----

imp_3pl = []

for w in verbimp:
    imp_3pl.append(w + u'and')

for w in verbimp:
    imp_3pl.append(w + u'an')

# ---- object

imp_3pl_o2s = []

for w in imp_3pl:
    imp_3pl_o2s.append(w + u'et')

for w in imp_3pl:
    imp_3pl_o2s.append(w + u'at')

imp_3pl_o3s = []

for w in imp_3pl:
    imp_3pl_o3s.append(w + u'eš')

for w in imp_3pl:
    imp_3pl_o3s.append(w + u'aš')

imp_3pl_o1pl = []

for w in imp_3pl:
    imp_3pl_o1pl.append(w + u'emān')

for w in imp_3pl:
    imp_3pl_o1pl.append(w + u'emun')


imp_3pl_o2pl = []

for w in imp_3pl:
    imp_3pl_o2pl.append(w + u'etān')

for w in imp_3pl:
    imp_3pl_o2pl.append(w + u'etun')

imp_3pl_o3pl = []

for w in imp_3pl:
    imp_3pl_o3pl.append(w + u'ešān')

for w in imp_3pl:
    imp_3pl_o3pl.append(w + u'ešun')

# ----

# --- negative imperfect

Nverbimp = []

for w in verbpret:
    if w[0] in vowels:
        Nverbimp.append(u'nemiy' + w)

for w in verbpret:
        Nverbimp.append(u'nemi' + w)

# ---

Nimp_1s = []

for w in Nverbimp:
    Nimp_1s.append(w + u'am')

# ---- object

Nimp_1s_o2s = []

for w in Nimp_1s:
    Nimp_1s_o2s.append(w + u'et')

for w in Nimp_1s:
    Nimp_1s_o2s.append(w + u'at')

Nimp_1s_o3s = []

for w in Nimp_1s:
    Nimp_1s_o3s.append(w + u'eš')

for w in Nimp_1s:
    Nimp_1s_o3s.append(w + u'aš')

Nimp_1s_o1pl = []

for w in Nimp_1s:
    Nimp_1s_o1pl.append(w + u'emān')

for w in Nimp_1s:
    Nimp_1s_o1pl.append(w + u'emun')


Nimp_1s_o2pl = []

for w in Nimp_1s:
    Nimp_1s_o2pl.append(w + u'etān')

for w in Nimp_1s:
    Nimp_1s_o2pl.append(w + u'etun')

Nimp_1s_o3pl = []

for w in Nimp_1s:
    Nimp_1s_o3pl.append(w + u'ešān')

for w in Nimp_1s:
    Nimp_1s_o3pl.append(w + u'ešun')

# ----

Nimp_2s = []

for w in Nverbimp:
        Nimp_2s.append(w + u'i')

# ---- object

Nimp_2s_o2s = []

for w in Nimp_2s:
    Nimp_2s_o2s.append(w + u't')

for w in Nimp_2s:
    Nimp_2s_o2s.append(w + u't')

Nimp_2s_o3s = []

for w in Nimp_2s:
    Nimp_2s_o3s.append(w + u'š')

Nimp_2s_o1pl = []

for w in Nimp_2s:
    Nimp_2s_o1pl.append(w + u'mān')

for w in Nimp_2s:
    Nimp_2s_o1pl.append(w + u'mun')


Nimp_2s_o2pl = []

for w in Nimp_2s:
    Nimp_2s_o2pl.append(w + u'tān')

for w in Nimp_2s:
    Nimp_2s_o2pl.append(w + u'tun')

Nimp_2s_o3pl = []

for w in Nimp_2s:
    Nimp_2s_o3pl.append(w + u'šān')

for w in Nimp_2s:
    Nimp_2s_o3pl.append(w + u'šun')

# ----

Nimp_3s = []

for w in Nverbimp:
    Nimp_3s.append(w)

# ---- object

Nimp_3s_o2s = []

for w in Nimp_3s:
    Nimp_3s_o2s.append(w + u'et')

for w in Nimp_3s:
    Nimp_3s_o2s.append(w + u'at')

Nimp_3s_o3s = []

for w in Nimp_3s:
    Nimp_3s_o3s.append(w + u'eš')

for w in Nimp_3s:
    Nimp_3s_o3s.append(w + u'aš')

Nimp_3s_o1pl = []

for w in Nimp_3s:
    Nimp_3s_o1pl.append(w + u'emān')

for w in Nimp_3s:
    Nimp_3s_o1pl.append(w + u'emun')


Nimp_3s_o2pl = []

for w in Nimp_3s:
    Nimp_3s_o2pl.append(w + u'etān')

for w in Nimp_3s:
    Nimp_3s_o2pl.append(w + u'etun')

Nimp_3s_o3pl = []

for w in Nimp_3s:
    Nimp_3s_o3pl.append(w + u'ešān')

for w in Nimp_3s:
    Nimp_3s_o3pl.append(w + u'ešun')

# ----

Nimp_1pl = []

for w in Nverbimp:
    Nimp_1pl.append(w + u'im')

# ---- object

Nimp_1pl_o2s = []

for w in Nimp_1pl:
    Nimp_1pl_o2s.append(w + u'et')

for w in Nimp_1pl:
    Nimp_1pl_o2s.append(w + u'at')

Nimp_1pl_o3s = []

for w in Nimp_1pl:
    Nimp_1pl_o3s.append(w + u'eš')

for w in Nimp_1pl:
    Nimp_1pl_o3s.append(w + u'aš')

Nimp_1pl_o1pl = []

for w in Nimp_1pl:
    Nimp_1pl_o1pl.append(w + u'emān')

for w in Nimp_1pl:
    Nimp_1pl_o1pl.append(w + u'emun')


Nimp_1pl_o2pl = []

for w in Nimp_1pl:
    Nimp_1pl_o2pl.append(w + u'etān')

for w in Nimp_1pl:
    Nimp_1pl_o2pl.append(w + u'etun')

Nimp_1pl_o3pl = []

for w in Nimp_1pl:
    Nimp_1pl_o3pl.append(w + u'ešān')

for w in Nimp_1pl:
    Nimp_1pl_o3pl.append(w + u'ešun')

# ----

Nimp_2pl = []

for w in Nverbimp:
    Nimp_2pl.append(w + u'id')

for w in Nverbimp:
    Nimp_2pl.append(w + u'in')

# ---- object

Nimp_2pl_o2s = []

for w in Nimp_2pl:
    Nimp_2pl_o2s.append(w + u'et')

for w in Nimp_2pl:
    Nimp_2pl_o2s.append(w + u'at')

Nimp_2pl_o3s = []

for w in Nimp_2pl:
    Nimp_2pl_o3s.append(w + u'eš')

for w in Nimp_2pl:
    Nimp_2pl_o3s.append(w + u'aš')

Nimp_2pl_o1pl = []

for w in Nimp_2pl:
    Nimp_2pl_o1pl.append(w + u'emān')

for w in Nimp_2pl:
    Nimp_2pl_o1pl.append(w + u'emun')


Nimp_2pl_o2pl = []

for w in Nimp_2pl:
    Nimp_2pl_o2pl.append(w + u'etān')

for w in Nimp_2pl:
    Nimp_2pl_o2pl.append(w + u'etun')

Nimp_2pl_o3pl = []

for w in Nimp_2pl:
    Nimp_2pl_o3pl.append(w + u'ešān')

for w in Nimp_2pl:
    Nimp_2pl_o3pl.append(w + u'ešun')

# ----

Nimp_3pl = []

for w in Nverbimp:
    Nimp_3pl.append(w + u'and')

for w in Nverbimp:
    Nimp_3pl.append(w + u'an')


# ---- object

Nimp_3pl_o2s = []

for w in Nimp_3pl:
    Nimp_3pl_o2s.append(w + u'et')

for w in Nimp_3pl:
    Nimp_3pl_o2s.append(w + u'at')

Nimp_3pl_o3s = []

for w in Nimp_3pl:
    Nimp_3pl_o3s.append(w + u'eš')

for w in Nimp_3pl:
    Nimp_3pl_o3s.append(w + u'aš')

Nimp_3pl_o1pl = []

for w in Nimp_3pl:
    Nimp_3pl_o1pl.append(w + u'emān')

for w in Nimp_3pl:
    Nimp_3pl_o1pl.append(w + u'emun')


Nimp_3pl_o2pl = []

for w in Nimp_3pl:
    Nimp_3pl_o2pl.append(w + u'etān')

for w in Nimp_3pl:
    Nimp_3pl_o2pl.append(w + u'etun')

Nimp_3pl_o3pl = []

for w in Nimp_3pl:
    Nimp_3pl_o3pl.append(w + u'ešān')

for w in Nimp_3pl:
    Nimp_3pl_o3pl.append(w + u'ešun')

# ----

# ------ past participle ----

pretpart = []

for w in verbpret:
    pretpart.append(w + u'e')

# ---- perfective ---

perf = []

for w in pretpart:
    perf.append(w)

for w in pretpart:
    perf.append(w + u'\'')

perf_1s = []

for w in perf:
    perf_1s.append(w + u'am')

perf_2s = []

for w in perf:
    perf_2s.append(w + u'i')

perf_3s = []

for w in perf:
    perf_3s.append(w + u'ast')

perf_1pl = []

for w in perf:
    perf_1pl.append(w + u'im')

perf_2pl = []

for w in perf:
    perf_2pl.append(w + u'id')

for w in perf:
    perf_2pl.append(w + u'in')

perf_3pl = []

for w in perf:
    perf_3pl.append(w + u'and')

for w in perf:
    perf_3pl.append(w + u'and')


# ----- negative past participle -----

Npretpart = []

for w in pretpart:
    if w[0] in vowels:
        Npretpart.append(u'nay' + w)

for w in pretpart:
    if w[0] in consonants:
        Npretpart.append(u'na' + w)

# ---- negative perfective ----

Nperf = []

for w in Npretpart:
    Nperf.append(w)

for w in Npretpart:
    Nperf.append(w + u'\'')

Nperf_1s = []

for w in Nperf:
    Nperf_1s.append(w + u'am')

Nperf_2s = []

for w in Nperf:
    Nperf_2s.append(w + u'i')

Nperf_3s = []

for w in Nperf:
    Nperf_3s.append(w + u'ast')

Nperf_1pl = []

for w in Nperf:
    Nperf_1pl.append(w + u'im')

Nperf_2pl = []

for w in Nperf:
    Nperf_2pl.append(w + u'id')

for w in Nperf:
    Nperf_2pl.append(w + u'in')

Nperf_3pl = []

for w in Nperf:
    Nperf_3pl.append(w + u'and')

for w in Nperf:
    Nperf_3pl.append(w + u'and')

# ---- past narrative ----

pastnarr = []

for w in perf:
    if w[0] in vowels:
        pastnarr.append(u'miy' + w)

for w in perf:
    pastnarr.append(u'mi' + w)

pastnarr_1s = []

for w in pastnarr:
    pastnarr_1s.append(w + u'am')

pastnarr_2s = []

for w in pastnarr:
    pastnarr_2s.append(w + u'i')

pastnarr_3s = []

for w in pastnarr:
    pastnarr_3s.append(w + u'ast')

pastnarr_1pl = []

for w in pastnarr:
    pastnarr_1pl.append(w + u'im')

pastnarr_2pl = []

for w in pastnarr:
    pastnarr_2pl.append(w + u'id')

for w in pastnarr:
    pastnarr_2pl.append(w + u'in')

pastnarr_3pl = []

for w in pastnarr:
    pastnarr_3pl.append(w + u'and')

for w in pastnarr:
    pastnarr_3pl.append(w + u'and')

# ---- negative past narrative ----

Npastnarr = []

for w in pastnarr:
    Npastnarr.append(u'ne' + w)

Npastnarr_1s = []

for w in Npastnarr:
    Npastnarr_1s.append(w + u'am')

Npastnarr_2s = []

for w in Npastnarr:
    Npastnarr_2s.append(w + u'i')

Npastnarr_3s = []

for w in Npastnarr:
    Npastnarr_3s.append(w + u'ast')

Npastnarr_1pl = []

for w in Npastnarr:
    Npastnarr_1pl.append(w + u'im')

Npastnarr_2pl = []

for w in Npastnarr:
    Npastnarr_2pl.append(w + u'id')

for w in Npastnarr:
    Npastnarr_2pl.append(w + u'in')

Npastnarr_3pl = []

for w in Npastnarr:
    Npastnarr_3pl.append(w + u'and')

for w in Npastnarr:
    Npastnarr_3pl.append(w + u'and')

# ---- infinitive ----

infinitive = []

for w in verbpret:
    infinitive.append(w + u'an')

# ---- negative infinitive ----

Ninfinitive = []

for w in infinitive:
    if w[0] in vowels:
        Ninfinitive.append(u'nay' + w)

for w in infinitive:
    if w[0] in consonants:
        Ninfinitive.append(u'na' + w)

# -----------



def parstag():
    textin = input('Write your text here: ')
    



    global output
    output = []
    text = textin.lower()
    text1 = re.sub(u'\.',u' . ',text)
    text2 = re.sub(u'\,',u' , ',text1)
    text3 = re.sub(u'\"',u' " ',text2)
    text4 = re.sub(u'\!',u' ! ',text3)
    text5 = re.sub(u'ḥ',u'h',text4)
    text6 = re.sub(u'-',u'',text5)
    text7 = re.sub(u'c',u'č',text6)
    text8 = re.sub(u'ṣ',u's',text7)
    text9 = re.sub(u'ẓ',u'z',text8)
    textA = re.sub(u'ẕ',u'z',text9)
    textB = re.sub(u'xvā',u'xā',textA)
    textC = re.sub(u'ṭ',u't',textB)
    textD = re.sub(u'ō',u'ow',textC)
    textE = re.sub(u'ġ',u'q',textD)
    textF = re.sub(u':',u' :',textE)
    textG = re.sub(u'xvo',u'xo',textF)
    textH = re.sub(u'ō',u'ow',textG)
    textI = re.sub(u'ż',u'z',textH)
    textJ = re.sub(u'\?',u' ? ',textI)
    textK = re.sub(u'  ',u' ',textJ)
    
    frag = textK.split(' ')
    for w in frag:
        if w in imper:
            output.append(w + '/IMPER')
        elif w in Nimper:
            output.append(w + '/negIMPER')
        elif w in konj_1s:
            output.append(w + '/SUB_1s')
        elif w in konj_1s_o2s:
            output.append(w + '/SUB_1s_obj2s')
        elif w in konj_1s_o3s:
            output.append(w + '/SUB_1s_obj3s')
        elif w in konj_1s_o1pl:
            output.append(w + '/SUB_1s_obj1pl')
        elif w in konj_1s_o2pl:
            output.append(w + '/SUB_1s_obj2pl')
        elif w in konj_1s_o3pl:
            output.append(w + '/SUB_1s_obj3pl')
        elif w in konj_2s:
            output.append(w + '/SUB_2s')
        elif w in konj_2s_o2s:
            output.append(w + '/SUB_2s_obj2s')
        elif w in konj_2s_o3s:
            output.append(w + '/SUB_2s_obj3s')
        elif w in konj_2s_o1pl:
            output.append(w + '/SUB_2s_obj1pl')
        elif w in konj_2s_o2pl:
            output.append(w + '/SUB_2s_obj2pl')
        elif w in konj_2s_o3pl:
            output.append(w + '/SUB_2s_obj3pl')
        elif w in konj_3s:
            output.append(w + '/SUB_3s')
        elif w in konj_3s_o2s:
            output.append(w + '/SUB_3s_obj2s')
        elif w in konj_3s_o3s:
            output.append(w + '/SUB_3s_obj3s')
        elif w in konj_3s_o1pl:
            output.append(w + '/SUB_3s_obj1pl')
        elif w in konj_3s_o2pl:
            output.append(w + '/SUB_3s_obj2pl')
        elif w in konj_3s_o3pl:
            output.append(w + '/SUB_3s_obj3pl')
        elif w in konj_1pl:
            output.append(w + '/SUB_1pl')
        elif w in konj_1pl_o2s:
            output.append(w + '/SUB_1pl_obj2s')
        elif w in konj_1pl_o3s:
            output.append(w + '/SUB_1pl_obj3s')
        elif w in konj_1pl_o1pl:
            output.append(w + '/SUB_1pl_obj1pl')
        elif w in konj_1pl_o2pl:
            output.append(w + '/SUB_1pl_obj2pl')
        elif w in konj_1pl_o3pl:
            output.append(w + '/SUB_1pl_obj3pl')
        elif w in konj_2pl:
            output.append(w + '/SUB_2pl')
        elif w in konj_2pl_o2s:
            output.append(w + '/SUB_2pl_obj2s')
        elif w in konj_2pl_o3s:
            output.append(w + '/SUB_2pl_obj3s')
        elif w in konj_2pl_o1pl:
            output.append(w + '/SUB_2pl_obj1pl')
        elif w in konj_2pl_o2pl:
            output.append(w + '/SUB_2pl_obj2pl')
        elif w in konj_2pl_o3pl:
            output.append(w + '/SUB_2pl_obj3pl')
        elif w in konj_3pl:
            output.append(w + '/SUB_3pl')
        elif w in konj_3pl_o2s:
            output.append(w + '/SUB_3pl_obj2s')
        elif w in konj_3pl_o3s:
            output.append(w + '/SUB_3pl_obj3s')
        elif w in konj_3pl_o1pl:
            output.append(w + '/SUB_3pl_obj1pl')
        elif w in konj_3pl_o2pl:
            output.append(w + '/SUB_3pl_obj2pl')
        elif w in konj_3pl_o3pl:
            output.append(w + '/SUB_3pl_obj3pl')
        elif w in Nkonj_1s:
            output.append(w + '/negSUB_1s')
        elif w in Nkonj_1s_o2s:
            output.append(w + '/negSUB_1s_obj2s')
        elif w in Nkonj_1s_o3s:
            output.append(w + '/negSUB_1s_obj3s')
        elif w in Nkonj_1s_o1pl:
            output.append(w + '/negSUB_1s_obj1pl')
        elif w in Nkonj_1s_o2pl:
            output.append(w + '/negSUB_1s_obj2pl')
        elif w in Nkonj_1s_o3pl:
            output.append(w + '/negSUB_1s_obj3pl')
        elif w in Nkonj_2s:
            output.append(w + '/negSUB_2s')
        elif w in Nkonj_2s_o2s:
            output.append(w + '/negSUB_2s_obj2s')
        elif w in Nkonj_2s_o3s:
            output.append(w + '/negSUB_2s_obj3s')
        elif w in Nkonj_2s_o1pl:
            output.append(w + '/negSUB_2s_obj1pl')
        elif w in Nkonj_2s_o2pl:
            output.append(w + '/negSUB_2s_obj2pl')
        elif w in Nkonj_2s_o3pl:
            output.append(w + '/negSUB_2s_obj3pl')
        elif w in Nkonj_3s:
            output.append(w + '/negSUB_3s')
        elif w in Nkonj_3s_o2s:
            output.append(w + '/negSUB_3s_obj2s')
        elif w in Nkonj_3s_o3s:
            output.append(w + '/negSUB_3s_obj3s')
        elif w in Nkonj_3s_o1pl:
            output.append(w + '/negSUB_3s_obj1pl')
        elif w in Nkonj_3s_o2pl:
            output.append(w + '/negSUB_3s_obj2pl')
        elif w in Nkonj_3s_o3pl:
            output.append(w + '/negSUB_3s_obj3pl')
        elif w in Nkonj_1pl:
            output.append(w + '/negSUB_1pl')
        elif w in Nkonj_1pl_o2s:
            output.append(w + '/negSUB_1pl_obj2s')
        elif w in Nkonj_1pl_o3s:
            output.append(w + '/negSUB_1pl_obj3s')
        elif w in Nkonj_1pl_o1pl:
            output.append(w + '/negSUB_1pl_obj1pl')
        elif w in Nkonj_1pl_o2pl:
            output.append(w + '/negSUB_1pl_obj2pl')
        elif w in Nkonj_1pl_o3pl:
            output.append(w + '/negSUB_1pl_obj3pl')
        elif w in Nkonj_2pl:
            output.append(w + '/negSUB_2pl')
        elif w in Nkonj_2pl_o2s:
            output.append(w + '/negSUB_2pl_obj2s')
        elif w in Nkonj_2pl_o3s:
            output.append(w + '/negSUB_2pl_obj3s')
        elif w in Nkonj_2pl_o1pl:
            output.append(w + '/negSUB_2pl_obj1pl')
        elif w in Nkonj_2pl_o2pl:
            output.append(w + '/negSUB_2pl_obj2pl')
        elif w in Nkonj_2pl_o3pl:
            output.append(w + '/negSUB_2pl_obj3pl')
        elif w in Nkonj_3pl:
            output.append(w + '/negSUB_3pl')
        elif w in Nkonj_3pl_o2s:
            output.append(w + '/negSUB_3pl_obj2s')
        elif w in Nkonj_3pl_o3s:
            output.append(w + '/negSUB_3pl_obj3s')
        elif w in Nkonj_3pl_o1pl:
            output.append(w + '/negSUB_3pl_obj1pl')
        elif w in Nkonj_3pl_o2pl:
            output.append(w + '/negSUB_3pl_obj2pl')
        elif w in Nkonj_3pl_o3pl:
            output.append(w + '/negSUB_3pl_obj3pl')
        elif w in ind_1s:
            output.append(w + '/PRESIND_1s')
        elif w in ind_1s_o2s:
            output.append(w + '/PRESIND_1s_obj2s')
        elif w in ind_1s_o3s:
            output.append(w + '/PRESIND_1s_obj3s')
        elif w in ind_1s_o1pl:
            output.append(w + '/PRESIND_1s_obj1pl')
        elif w in ind_1s_o2pl:
            output.append(w + '/PRESIND_1s_obj2pl')
        elif w in ind_1s_o3pl:
            output.append(w + '/PRESIND_1s_obj3pl')
        elif w in ind_2s:
            output.append(w + '/PRESIND_2s')
        elif w in ind_2s_o2s:
            output.append(w + '/PRESIND_2s_obj2s')
        elif w in ind_2s_o3s:
            output.append(w + '/PRESIND_2s_obj3s')
        elif w in ind_2s_o1pl:
            output.append(w + '/PRESIND_2s_obj1pl')
        elif w in ind_2s_o2pl:
            output.append(w + '/PRESIND_2s_obj2pl')
        elif w in ind_2s_o3pl:
            output.append(w + '/PRESIND_2s_obj3pl')
        elif w in ind_3s:
            output.append(w + '/PRESIND_3s')
        elif w in ind_3s_o2s:
            output.append(w + '/PRESIND_3s_obj2s')
        elif w in ind_3s_o3s:
            output.append(w + '/PRESIND_3s_obj3s')
        elif w in ind_3s_o1pl:
            output.append(w + '/PRESIND_3s_obj1pl')
        elif w in ind_3s_o2pl:
            output.append(w + '/PRESIND_3s_obj2pl')
        elif w in ind_3s_o3pl:
            output.append(w + '/PRESIND_3s_obj3pl')
        elif w in ind_1pl:
            output.append(w + '/PRESIND_1pl')
        elif w in ind_1pl_o2s:
            output.append(w + '/PRESIND_1pl_obj2s')
        elif w in ind_1pl_o3s:
            output.append(w + '/PRESIND_1pl_obj3s')
        elif w in ind_1pl_o1pl:
            output.append(w + '/PRESIND_1pl_obj1pl')
        elif w in ind_1pl_o2pl:
            output.append(w + '/PRESIND_1pl_obj2pl')
        elif w in ind_1pl_o3pl:
            output.append(w + '/PRESIND_1pl_obj3pl')
        elif w in ind_2pl:
            output.append(w + '/PRESIND_2pl')
        elif w in ind_2pl_o2s:
            output.append(w + '/PRESIND_2pl_obj2s')
        elif w in ind_2pl_o3s:
            output.append(w + '/PRESIND_2pl_obj3s')
        elif w in ind_2pl_o1pl:
            output.append(w + '/PRESIND_2pl_obj1pl')
        elif w in ind_2pl_o2pl:
            output.append(w + '/PRESIND_2pl_obj2pl')
        elif w in ind_2pl_o3pl:
            output.append(w + '/PRESIND_2pl_obj3pl')
        elif w in ind_3pl:
            output.append(w + '/PRESIND_3pl')
        elif w in ind_3pl_o2s:
            output.append(w + '/PRESIND_3pl_obj2s')
        elif w in ind_3pl_o3s:
            output.append(w + '/PRESIND_3pl_obj3s')
        elif w in ind_3pl_o1pl:
            output.append(w + '/PRESIND_3pl_obj1pl')
        elif w in ind_3pl_o2pl:
            output.append(w + '/PRESIND_3pl_obj2pl')
        elif w in ind_3pl_o3pl:
            output.append(w + '/PRESIND_3pl_obj3pl')
        elif w in Nind_1s:
            output.append(w + '/negPRESIND_1s')
        elif w in Nind_1s_o2s:
            output.append(w + '/negPRESIND_1s_obj2s')
        elif w in Nind_1s_o3s:
            output.append(w + '/negPRESIND_1s_obj3s')
        elif w in Nind_1s_o1pl:
            output.append(w + '/negPRESIND_1s_obj1pl')
        elif w in Nind_1s_o2pl:
            output.append(w + '/negPRESIND_1s_obj2pl')
        elif w in Nind_1s_o3pl:
            output.append(w + '/negPRESIND_1s_obj3pl')
        elif w in Nind_2s:
            output.append(w + '/negPRESIND_2s')
        elif w in Nind_2s_o2s:
            output.append(w + '/negPRESIND_2s_obj2s')
        elif w in Nind_2s_o3s:
            output.append(w + '/negPRESIND_2s_obj3s')
        elif w in Nind_2s_o1pl:
            output.append(w + '/negPRESIND_2s_obj1pl')
        elif w in Nind_2s_o2pl:
            output.append(w + '/negPRESIND_2s_obj2pl')
        elif w in Nind_2s_o3pl:
            output.append(w + '/negPRESIND_2s_obj3pl')
        elif w in Nind_3s:
            output.append(w + '/negPRESIND_3s')
        elif w in Nind_3s_o2s:
            output.append(w + '/negPRESIND_3s_obj2s')
        elif w in Nind_3s_o3s:
            output.append(w + '/negPRESIND_3s_obj3s')
        elif w in Nind_3s_o1pl:
            output.append(w + '/negPRESIND_3s_obj1pl')
        elif w in Nind_3s_o2pl:
            output.append(w + '/negPRESIND_3s_obj2pl')
        elif w in Nind_3s_o3pl:
            output.append(w + '/negPRESIND_3s_obj3pl')
        elif w in Nind_1pl:
            output.append(w + '/negPRESIND_1pl')
        elif w in Nind_1pl_o2s:
            output.append(w + '/negPRESIND_1pl_obj2s')
        elif w in Nind_1pl_o3s:
            output.append(w + '/negPRESIND_1pl_obj3s')
        elif w in Nind_1pl_o1pl:
            output.append(w + '/negPRESIND_1pl_obj1pl')
        elif w in Nind_1pl_o2pl:
            output.append(w + '/negPRESIND_1pl_obj2pl')
        elif w in Nind_1pl_o3pl:
            output.append(w + '/negPRESIND_1pl_obj3pl')
        elif w in Nind_2pl:
            output.append(w + '/negPRESIND_2pl')
        elif w in Nind_2pl_o2s:
            output.append(w + '/negPRESIND_2pl_obj2s')
        elif w in Nind_2pl_o3s:
            output.append(w + '/negPRESIND_2pl_obj3s')
        elif w in Nind_2pl_o1pl:
            output.append(w + '/negPRESIND_2pl_obj1pl')
        elif w in Nind_2pl_o2pl:
            output.append(w + '/negPRESIND_2pl_obj2pl')
        elif w in Nind_2pl_o3pl:
            output.append(w + '/negPRESIND_2pl_obj3pl')
        elif w in Nind_3pl:
            output.append(w + '/negPRESIND_3pl')
        elif w in Nind_3pl_o2s:
            output.append(w + '/negPRESIND_3pl_obj2s')
        elif w in Nind_3pl_o3s:
            output.append(w + '/negPRESIND_3pl_obj3s')
        elif w in Nind_3pl_o1pl:
            output.append(w + '/negPRESIND_3pl_obj1pl')
        elif w in Nind_3pl_o2pl:
            output.append(w + '/negPRESIND_3pl_obj2pl')
        elif w in Nind_3pl_o3pl:
            output.append(w + '/negPRESIND_3pl_obj3pl')
        elif w in pret_1s:
            output.append(w + '/PRET_1s')
        elif w in pret_1s_o2s:
            output.append(w + '/PRET_1s_obj2s')
        elif w in pret_1s_o3s:
            output.append(w + '/PRET_1s_obj3s')
        elif w in pret_1s_o1pl:
            output.append(w + '/PRET_1s_obj1pl')
        elif w in pret_1s_o2pl:
            output.append(w + '/PRET_1s_obj2pl')
        elif w in pret_1s_o3pl:
            output.append(w + '/PRET_1s_obj3pl')
        elif w in pret_2s:
            output.append(w + '/PRET_2s')
        elif w in pret_2s_o2s:
            output.append(w + '/PRET_2s_obj2s')
        elif w in pret_2s_o3s:
            output.append(w + '/PRET_2s_obj3s')
        elif w in pret_2s_o1pl:
            output.append(w + '/PRET_2s_obj1pl')
        elif w in pret_2s_o2pl:
            output.append(w + '/PRET_2s_obj2pl')
        elif w in pret_2s_o3pl:
            output.append(w + '/PRET_2s_obj3pl')
        elif w in pret_3s:
            output.append(w + '/PRET_3s')
        elif w in pret_3s_o2s:
            output.append(w + '/PRET_3s_obj2s')
        elif w in pret_3s_o3s:
            output.append(w + '/PRET_3s_obj3s')
        elif w in pret_3s_o1pl:
            output.append(w + '/PRET_3s_obj1pl')
        elif w in pret_3s_o2pl:
            output.append(w + '/PRET_3s_obj2pl')
        elif w in pret_3s_o3pl:
            output.append(w + '/PRET_3s_obj3pl')
        elif w in pret_1pl:
            output.append(w + '/PRET_1pl')
        elif w in pret_1pl_o2s:
            output.append(w + '/PRET_1pl_obj2s')
        elif w in pret_1pl_o3s:
            output.append(w + '/PRET_1pl_obj3s')
        elif w in pret_1pl_o1pl:
            output.append(w + '/PRET_1pl_obj1pl')
        elif w in pret_1pl_o2pl:
            output.append(w + '/PRET_1pl_obj2pl')
        elif w in pret_1pl_o3pl:
            output.append(w + '/PRET_1pl_obj3pl')
        elif w in pret_2pl:
            output.append(w + '/PRET_2pl')
        elif w in pret_2pl_o2s:
            output.append(w + '/PRET_2pl_obj2s')
        elif w in pret_2pl_o3s:
            output.append(w + '/PRET_2pl_obj3s')
        elif w in pret_2pl_o1pl:
            output.append(w + '/PRET_2pl_obj1pl')
        elif w in pret_2pl_o2pl:
            output.append(w + '/PRET_2pl_obj2pl')
        elif w in pret_2pl_o3pl:
            output.append(w + '/PRET_2pl_obj3pl')
        elif w in pret_3pl:
            output.append(w + '/PRET_3pl')
        elif w in pret_3pl_o2s:
            output.append(w + '/PRET_3pl_obj2s')
        elif w in pret_3pl_o3s:
            output.append(w + '/PRET_3pl_obj3s')
        elif w in pret_3pl_o1pl:
            output.append(w + '/PRET_3pl_obj1pl')
        elif w in pret_3pl_o2pl:
            output.append(w + '/PRET_3pl_obj2pl')
        elif w in pret_3pl_o3pl:
            output.append(w + '/PRET_3pl_obj3pl')
        elif w in Npret_1s:
            output.append(w + '/negPRET_1s')
        elif w in Npret_1s_o2s:
            output.append(w + '/negPRET_1s_obj2s')
        elif w in Npret_1s_o3s:
            output.append(w + '/negPRET_1s_obj3s')
        elif w in Npret_1s_o1pl:
            output.append(w + '/negPRET_1s_obj1pl')
        elif w in Npret_1s_o2pl:
            output.append(w + '/negPRET_1s_obj2pl')
        elif w in Npret_1s_o3pl:
            output.append(w + '/negPRET_1s_obj3pl')
        elif w in Npret_2s:
            output.append(w + '/negPRET_2s')
        elif w in Npret_2s_o2s:
            output.append(w + '/negPRET_2s_obj2s')
        elif w in Npret_2s_o3s:
            output.append(w + '/negPRET_2s_obj3s')
        elif w in Npret_2s_o1pl:
            output.append(w + '/negPRET_2s_obj1pl')
        elif w in Npret_2s_o2pl:
            output.append(w + '/negPRET_2s_obj2pl')
        elif w in Npret_2s_o3pl:
            output.append(w + '/negPRET_2s_obj3pl')
        elif w in Npret_3s:
            output.append(w + '/negPRET_3s')
        elif w in Npret_3s_o2s:
            output.append(w + '/negPRET_3s_obj2s')
        elif w in Npret_3s_o3s:
            output.append(w + '/negPRET_3s_obj3s')
        elif w in Npret_3s_o1pl:
            output.append(w + '/negPRET_3s_obj1pl')
        elif w in Npret_3s_o2pl:
            output.append(w + '/negPRET_3s_obj2pl')
        elif w in Npret_3s_o3pl:
            output.append(w + '/negPRET_3s_obj3pl')
        elif w in Npret_1pl:
            output.append(w + '/negPRET_1pl')
        elif w in Npret_1pl_o2s:
            output.append(w + '/negPRET_1pl_obj2s')
        elif w in Npret_1pl_o3s:
            output.append(w + '/negPRET_1pl_obj3s')
        elif w in Npret_1pl_o1pl:
            output.append(w + '/negPRET_1pl_obj1pl')
        elif w in Npret_1pl_o2pl:
            output.append(w + '/negPRET_1pl_obj2pl')
        elif w in Npret_1pl_o3pl:
            output.append(w + '/negPRET_1pl_obj3pl')
        elif w in Npret_2pl:
            output.append(w + '/negPRET_2pl')
        elif w in Npret_2pl_o2s:
            output.append(w + '/negPRET_2pl_obj2s')
        elif w in Npret_2pl_o3s:
            output.append(w + '/negPRET_2pl_obj3s')
        elif w in Npret_2pl_o1pl:
            output.append(w + '/negPRET_2pl_obj1pl')
        elif w in Npret_2pl_o2pl:
            output.append(w + '/negPRET_2pl_obj2pl')
        elif w in Npret_2pl_o3pl:
            output.append(w + '/negPRET_2pl_obj3pl')
        elif w in Npret_3pl:
            output.append(w + '/negPRET_3pl')
        elif w in Npret_3pl_o2s:
            output.append(w + '/negPRET_3pl_obj2s')
        elif w in Npret_3pl_o3s:
            output.append(w + '/negPRET_3pl_obj3s')
        elif w in Npret_3pl_o1pl:
            output.append(w + '/negPRET_3pl_obj1pl')
        elif w in Npret_3pl_o2pl:
            output.append(w + '/negPRET_3pl_obj2pl')
        elif w in Npret_3pl_o3pl:
            output.append(w + '/negPRET_3pl_obj3pl')
        elif w in imp_1s:
            output.append(w + '/IMP_1s')
        elif w in imp_1s_o2s:
            output.append(w + '/IMP_1s_obj2s')
        elif w in imp_1s_o3s:
            output.append(w + '/IMP_1s_obj3s')
        elif w in imp_1s_o1pl:
            output.append(w + '/IMP_1s_obj1pl')
        elif w in imp_1s_o2pl:
            output.append(w + '/IMP_1s_obj2pl')
        elif w in imp_1s_o3pl:
            output.append(w + '/IMP_1s_obj3pl')
        elif w in imp_2s:
            output.append(w + '/IMP_2s')
        elif w in imp_2s_o2s:
            output.append(w + '/IMP_2s_obj2s')
        elif w in imp_2s_o3s:
            output.append(w + '/IMP_2s_obj3s')
        elif w in imp_2s_o1pl:
            output.append(w + '/IMP_2s_obj1pl')
        elif w in imp_2s_o2pl:
            output.append(w + '/IMP_2s_obj2pl')
        elif w in imp_2s_o3pl:
            output.append(w + '/IMP_2s_obj3pl')
        elif w in imp_3s:
            output.append(w + '/IMP_3s')
        elif w in imp_3s_o2s:
            output.append(w + '/IMP_3s_obj2s')
        elif w in imp_3s_o3s:
            output.append(w + '/IMP_3s_obj3s')
        elif w in imp_3s_o1pl:
            output.append(w + '/IMP_3s_obj1pl')
        elif w in imp_3s_o2pl:
            output.append(w + '/IMP_3s_obj2pl')
        elif w in imp_3s_o3pl:
            output.append(w + '/IMP_3s_obj3pl')
        elif w in imp_1pl:
            output.append(w + '/IMP_1pl')
        elif w in imp_1pl_o2s:
            output.append(w + '/IMP_1pl_obj2s')
        elif w in imp_1pl_o3s:
            output.append(w + '/IMP_1pl_obj3s')
        elif w in imp_1pl_o1pl:
            output.append(w + '/IMP_1pl_obj1pl')
        elif w in imp_1pl_o2pl:
            output.append(w + '/IMP_1pl_obj2pl')
        elif w in imp_1pl_o3pl:
            output.append(w + '/IMP_1pl_obj3pl')
        elif w in imp_2pl:
            output.append(w + '/IMP_2pl')
        elif w in imp_2pl_o2s:
            output.append(w + '/IMP_2pl_obj2s')
        elif w in imp_2pl_o3s:
            output.append(w + '/IMP_2pl_obj3s')
        elif w in imp_2pl_o1pl:
            output.append(w + '/IMP_2pl_obj1pl')
        elif w in imp_2pl_o2pl:
            output.append(w + '/IMP_2pl_obj2pl')
        elif w in imp_2pl_o3pl:
            output.append(w + '/IMP_2pl_obj3pl')
        elif w in imp_3pl:
            output.append(w + '/IMP_3pl')
        elif w in imp_3pl_o2s:
            output.append(w + '/IMP_3pl_obj2s')
        elif w in imp_3pl_o3s:
            output.append(w + '/IMP_3pl_obj3s')
        elif w in imp_3pl_o1pl:
            output.append(w + '/IMP_3pl_obj1pl')
        elif w in imp_3pl_o2pl:
            output.append(w + '/IMP_3pl_obj2pl')
        elif w in imp_3pl_o3pl:
            output.append(w + '/IMP_3pl_obj3pl')
        elif w in Nimp_1s:
            output.append(w + '/negIMP_1s')
        elif w in Nimp_1s_o2s:
            output.append(w + '/negIMP_1s_obj2s')
        elif w in Nimp_1s_o3s:
            output.append(w + '/negIMP_1s_obj3s')
        elif w in Nimp_1s_o1pl:
            output.append(w + '/negIMP_1s_obj1pl')
        elif w in Nimp_1s_o2pl:
            output.append(w + '/negIMP_1s_obj2pl')
        elif w in Nimp_1s_o3pl:
            output.append(w + '/negIMP_1s_obj3pl')
        elif w in Nimp_2s:
            output.append(w + '/negIMP_2s')
        elif w in Nimp_2s_o2s:
            output.append(w + '/negIMP_2s_obj2s')
        elif w in Nimp_2s_o3s:
            output.append(w + '/negIMP_2s_obj3s')
        elif w in Nimp_2s_o1pl:
            output.append(w + '/negIMP_2s_obj1pl')
        elif w in Nimp_2s_o2pl:
            output.append(w + '/negIMP_2s_obj2pl')
        elif w in Nimp_2s_o3pl:
            output.append(w + '/negIMP_2s_obj3pl')
        elif w in Nimp_3s:
            output.append(w + '/negIMP_3s')
        elif w in Nimp_3s_o2s:
            output.append(w + '/negIMP_3s_obj2s')
        elif w in Nimp_3s_o3s:
            output.append(w + '/negIMP_3s_obj3s')
        elif w in Nimp_3s_o1pl:
            output.append(w + '/negIMP_3s_obj1pl')
        elif w in Nimp_3s_o2pl:
            output.append(w + '/negIMP_3s_obj2pl')
        elif w in Nimp_3s_o3pl:
            output.append(w + '/negIMP_3s_obj3pl')
        elif w in Nimp_1pl:
            output.append(w + '/negIMP_1pl')
        elif w in Nimp_1pl_o2s:
            output.append(w + '/negIMP_1pl_obj2s')
        elif w in Nimp_1pl_o3s:
            output.append(w + '/negIMP_1pl_obj3s')
        elif w in Nimp_1pl_o1pl:
            output.append(w + '/negIMP_1pl_obj1pl')
        elif w in Nimp_1pl_o2pl:
            output.append(w + '/negIMP_1pl_obj2pl')
        elif w in Nimp_1pl_o3pl:
            output.append(w + '/negIMP_1pl_obj3pl')
        elif w in Nimp_2pl:
            output.append(w + '/negIMP_2pl')
        elif w in Nimp_2pl_o2s:
            output.append(w + '/negIMP_2pl_obj2s')
        elif w in Nimp_2pl_o3s:
            output.append(w + '/negIMP_2pl_obj3s')
        elif w in Nimp_2pl_o1pl:
            output.append(w + '/negIMP_2pl_obj1pl')
        elif w in Nimp_2pl_o2pl:
            output.append(w + '/negIMP_2pl_obj2pl')
        elif w in Nimp_2pl_o3pl:
            output.append(w + '/negIMP_2pl_obj3pl')
        elif w in Nimp_3pl:
            output.append(w + '/negIMP_3pl')
        elif w in Nimp_3pl_o2s:
            output.append(w + '/negIMP_3pl_obj2s')
        elif w in Nimp_3pl_o3s:
            output.append(w + '/negIMP_3pl_obj3s')
        elif w in Nimp_3pl_o1pl:
            output.append(w + '/negIMP_3pl_obj1pl')
        elif w in Nimp_3pl_o2pl:
            output.append(w + '/negIMP_3pl_obj2pl')
        elif w in Nimp_3pl_o3pl:
            output.append(w + '/negIMP_3pl_obj3pl')
        elif w in prespart:
            output.append(w + '/PRESPART')
        elif w in Nprespart:
            output.append(w + '/negPRESPART')
        elif w in pretpart:
            output.append(w + '/PRETPART')
        elif w in perf_1s:
            output.append(w + '/PERF_1s')
        elif w in perf_2s:
            output.append(w + '/PERF_2s')
        elif w in perf_3s:
            output.append(w + '/PERF_3s')
        elif w in perf_1pl:
            output.append(w + '/PERF_1pl')
        elif w in perf_2pl:
            output.append(w + '/PERF_2pl')
        elif w in perf_3pl:
            output.append(w + '/PERF_3pl')
        elif w in Npretpart:
            output.append(w + '/negPRETPART')
        elif w in Nperf_1s:
            output.append(w + '/negPERF_1s')
        elif w in Nperf_2s:
            output.append(w + '/negPERF_2s')
        elif w in Nperf_3s:
            output.append(w + '/negPERF_3s')
        elif w in Nperf_1pl:
            output.append(w + '/negPERF_1pl')
        elif w in Nperf_2pl:
            output.append(w + '/negPERF_2pl')
        elif w in Nperf_3pl:
            output.append(w + '/negPERF_3pl')
        elif w in pastnarr_1s:
            output.append(w + '/PASTNARR_1s')
        elif w in pastnarr_2s:
            output.append(w + '/PASTNARR_2s')
        elif w in pastnarr_3s:
            output.append(w + '/PASTNARR_3s')
        elif w in pastnarr_1pl:
            output.append(w + '/PASTNARR_1pl')
        elif w in pastnarr_2pl:
            output.append(w + '/PASTNARR_2pl')
        elif w in pastnarr_3pl:
            output.append(w + '/PASTNARR_3pl')
        elif w in Npastnarr_1s:
            output.append(w + '/negPASTNARR_1s')
        elif w in Npastnarr_2s:
            output.append(w + '/negPASTNARR_2s')
        elif w in Npastnarr_3s:
            output.append(w + '/negPASTNARR_3s')
        elif w in Npastnarr_1pl:
            output.append(w + '/negPASTNARR_1pl')
        elif w in Npastnarr_2pl:
            output.append(w + '/negPASTNARR_2pl')
        elif w in Npastnarr_3pl:
            output.append(w + '/negPASTNARR_3pl')
        elif w in infinitive:
            output.append(w + '/INFINIT')
        elif w in Ninfinitive:
            output.append(w + '/negINFINIT')
        else:
            output.append(w + ' ')
    out_p = ' '.join(output)
    print(out_p)
                


parstag()
