# -*- coding: UTF-8 -*-
d = {
    "lodDist": 100.0,
    "SmallCull": 0.04,
    "DostCull": 500.0,
    "trilinear": 40,
    "farclip": 477}
w = max(map(len, d.keys()))
for k,v in d.items():
    print k.ljust(w), ':', v
 
d = {
    "lodDist": 100.0,
    "SmallCull": 0.04,
    "DostCull": 500.0,
    "trilinear": 40,
    "farclip": 477}
w = str(max(map(len, d.keys())))
for k,v in d.items():
    print format(k, '<' + w), ':', v 