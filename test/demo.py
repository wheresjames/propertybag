#!/usr/bin/env python3

import propertybag as pb

Log = print

# Init with kw args
bag = pb.Bag(a='b', c='d')
Log(bag.toJson(True))                   # > {
                                        # >   "a": "b",
                                        # >   "c": "d"
                                        # > }

bag.b.c.d.e = 42
Log(bag.toJson())                       # > {"a": "b", "c": "d", "b": {"c": {"d": {"e": 42}}}}

# Init with dict
bag = pb.Bag({'a':'b', 'c':'d'})
Log(bag)                                # > {"a": "b", "c": "d"}

# Init with both
bag = pb.Bag({'a':'b'}, c='d')
Log(bag)                                # > {"a": "b", "c": "d"}

# Set deep value
bag.d.e.f.g.h = 42
Log(bag)                                # > {"a": "b", "c": "d", "d": {"e": {"f": {"g": {"h": 42}}}}}

# Read deep value
Log(bag.d.e.f.g.h)                      # > 42
try:
    Log(bag.e.f.g.h.i)                  # > Throws ValueError() exception
except ValueError as e:
    Log(e)                              # > Value not set

# If you don't want exceptions thrown
bag_nt = pb.Bag({'a': 'b'}, '')
Log(bag_nt.d.e.f.g.i)                   # > ''

# Use get/set for compound keys
bag.set("d.e.f.g.h", 43)
Log(bag.get("d.e.f.g.h"))               # > 43
Log(bag.get("d.e.f.g.i", "default"))    # > "default"


# Iterate
Log('--------------------------------------------')
for k,v in bag.items():
    Log(k, v)

Log('--------------------------------------------')
for k in bag:
    Log(k)

Log('--------------------------------------------')
for v in bag.values():
    Log(v)
