import random, re
random.seed(2026)
POOLS = {}      # pool -> list of (en, hi)
QS = []         # raw questions

def _pool_add(pool, en, hi):
    if not pool: return
    L = POOLS.setdefault(pool, [])
    if (en, hi) not in L: L.append((en, hi))

def _rows(s):
    for line in s.strip().split("\n"):
        line = line.strip()
        if line and not line.startswith("#"):
            yield [x.strip() for x in line.split("|")]

def T(cat, pool, rows, qen, qhi, qen_r=None, qhi_r=None, kpool=None):
    """Template table. rows: k_en|k_hi|v_en|v_hi. qen uses {k}; reverse uses {v}."""
    rs = list(_rows(rows))
    vals = [r[2] for r in rs]
    keys_pool = f"_k{len(QS)}_{pool}"
    for r in rs:
        _pool_add(pool, r[2], r[3])
        _pool_add(keys_pool, r[0], r[1])
        if kpool: _pool_add(kpool, r[0], r[1])
    for r in rs:
        QS.append(dict(cat=cat, en=qen.format(k=r[0], v=r[2]), hi=qhi.format(k=r[1], v=r[3]),
                       a=(r[2], r[3]), pool=pool, dist=None, tp=pool))
        if qen_r and vals.count(r[2]) == 1:
            QS.append(dict(cat=cat, en=qen_r.format(k=r[0], v=r[2]), hi=qhi_r.format(k=r[1], v=r[3]),
                           a=(r[0], r[1]), pool=keys_pool, dist=None, tp=pool))

def F(cat, pool, rows):
    """One-off facts. rows: qen|qhi|aen|ahi[|d1;d2;d3]  ('=' for ahi => same as en; d 'x/y' = en/hi)"""
    for r in _rows(rows):
        qen, qhi, aen, ahi = r[0], r[1], r[2], r[3]
        if ahi == "=": ahi = aen
        dist = None
        if len(r) > 4 and r[4]:
            dist = []
            for d in r[4].split(";"):
                d = d.strip()
                if "/" in d and not re.fullmatch(r"[\d/]+", d):
                    e, h = [x.strip() for x in d.split("/", 1)]
                else:
                    e = h = d
                dist.append((e, h))
        else:
            _pool_add(pool, aen, ahi)
        QS.append(dict(cat=cat, en=qen, hi=qhi, a=(aen, ahi), pool=pool, dist=dist, tp=pool))

def finalize():
    out, seen = [], set()
    for q in QS:
        key = re.sub(r"\W+", " ", (q["en"]+" "+q["hi"]).lower()).strip()
        if key in seen: continue
        seen.add(key)
        if q["dist"]:
            d = q["dist"]
        else:
            cands = [x for x in POOLS.get(q["pool"], []) if x[0] != q["a"][0]]
            if len(cands) < 3:
                raise SystemExit(f"Pool too small: {q['pool']} for {q['en']}")
            d = random.sample(cands, 3)
        d = [x for x in d if x[0] != q["a"][0]][:3]
        if len(d) < 3: raise SystemExit("bad distractors: " + q["en"])
        out.append(dict(tp=q["tp"], cat=q["cat"], en=q["en"], hi=q["hi"], a=q["a"], d=d))
    return out

def X(cat, en, hi, a, d, tp):
    QS.append(dict(cat=cat, en=en, hi=hi, a=(a, a), pool=None, dist=[(x, x) for x in d], tp=tp))
