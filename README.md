# sywtltc_chapter_3_5
Types and Typeful programming

Makes use of the [sympy symbolic](http://www.sympy.org/en/index.html) math library for geometry.

To install on Linux
```
sudo pip install -r REQUIREMENTS.txt
```

The system tries to read in geo fences from a file, and gps data from another file, and report out what gps coordinates
fall within our geo fences.

There's a bug though. I'm currently getting this result:

Does polygon [(1.0, 0.0), (1.0, 1.0), (0.0, 1.0), (0.0, 0.0)]  contain point [0.5, 0.5] : True
Does polygon [(1.0, 0.0), (1.0, 1.0), (0.0, 1.0), (0.0, 0.0)]  contain point [1.5, 1.5] : False
Does polygon [(1.0, 0.0), (1.0, 1.0), (0.0, 1.0), (0.0, 0.0)]  contain point [3.0, 0.5] : False
Does polygon [(4.0, 0.0), (4.0, 1.0), (0.0, 1.0), (0.0, 0.0)]  contain point [0.5, 0.5] : True
Does polygon [(4.0, 0.0), (4.0, 1.0), (0.0, 1.0), (0.0, 0.0)]  contain point [1.5, 1.5] : False
Does polygon [(4.0, 0.0), (4.0, 1.0), (0.0, 1.0), (0.0, 0.0)]  contain point [3.0, 0.5] : True

The last True for the last  case - point [3.0, 0.5]. It seems like it should be true... but the vendor says this should
be FALSE. I'm out of ideas.
