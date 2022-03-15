"""
literals, sets, ranges, alternatives, and escapes
all tests here print 2: offset where pattern found
"""

import re                                  # the one to use today

# pattern, string = "A.C.", "xxABCDxx"       # nonspecial chars match themselves
# matchobj = re.search(pattern, string)      # '.' means any one char
# if matchobj:                               # search returns match object or None
#     print(matchobj.groups())                # groups is index where matched

# pattobj  = re.compile("A.*C.*")            # 'R*' means zero or more Rs
# matchobj = pattobj.search("xxABCDxx")      # compile returns pattern obj
# if matchobj:                               # patt.search returns match obj
#     print(matchobj.groups())
#     print(matchobj.groups())

# selection sets
print(re.search(" *A.C[DE][D-F][^G-ZE]G\t+ ?", "..ABCDEFG\t..").groups())

# alternatives: R1|R2 means R1 or R2
print(re.search("(A|X)(B|Y)(C|Z)D", "..AYCD..").groups())       # test each char
print(re.search("(?:A|X)(?:B|Y)(?:C|Z)D", "..AYCD..").groups()) # same, not saved
print(re.search("A|XB|YC|ZD", "..AYCD..").groups())             # matches just A!
print(re.search("(A|XB|YC|ZD)YCD", "..AYCD..").groups())        # just first char

# word boundaries
print(re.search(r"\bABCD", "..ABCD ").groups())     # \b means word boundary
print(re.search(r"ABCD\b", "..ABCD ").groups())     # use r'...' to escape '\'
