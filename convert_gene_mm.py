import re

#These two functions are adapted from: https://github.com/sahoo00/BoNE/blob/master/SMaRT/MacUtils.py
def getGroupsMm(gene_groups):
    cfile = "./gene_db/ensembl-GRCh38.p13-100-hs-mm.txt"
    fp = open(cfile, "r")
    mmdict = {}
    for line in fp:
        line = line.strip();
        ll = re.split("\t", line);
        if len(ll) > 3 and ll[2] != '' and ll[3] != '':
            g = ll[3]
            if g not in mmdict:
                mmdict[g] = []
            mmdict[g] += [ll[2]]
    fp.close();

    gene_groups_mm = []
    for s in gene_groups:
        s1 = set()
        for g in s:
            if g in mmdict:
                for k in mmdict[g]:
                    s1.add(k)
        gene_groups_mm.append(s1)
    return gene_groups_mm

def getGroupsHs(gene_groups):
    cfile = "./gene_db/ensembl-GRCm38.p6-100-mm-hs.txt"
    fp = open(cfile, "r")
    mmdict = {}
    for line in fp:
        line = line.strip();
        ll = re.split("\t", line);
        if len(ll) > 3 and ll[1] != '' and ll[2] != '':
            g = ll[1]
            if g not in mmdict:
                mmdict[g] = []
            mmdict[g] += [ll[2]]
    fp.close();

    gene_groups_hs = []
    for s in gene_groups:
        s1 = set()
        for g in s:
            if g in mmdict:
                for k in mmdict[g]:
                    s1.add(k)
        gene_groups_hs.append(s1)
    return gene_groups_hs