#!/usr/bin/env python
# coding: utf-8

# In[11]:


# -*- coding: utf-8 -*-
import sys
import unicodedata

def print_unicode_table(words):
    print("decimal hex chr {0:^40}".format("name"))
    print("------- ----- --- {0:-<40}".format(""))
    print(words)
    code = ord(" ")
    end = sys.maxunicode
    if not words:
        while code < end:
            c = chr(code)
            name = unicodedata.name(c, "*** unknown ***")
            print("{0:7} {0:5X} {0:^3c} {1}".format(code, name.title()))
            code += 1
    else:
        while code < end:
            c = chr(code)
            name = unicodedata.name(c, "*** unknown ***")
            flag = True
            for word in words:
                   if word.lower() not in name.lower():
                        flag = False
            if flag:
                print("{0:7} {0:5X} {0:^3c} {1}".format(code, name.title()))
            code += 1
# End print_unicode_table

# Start main script
words = None

if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [string]".format(sys.argv[0]))
        words = 0
    else:
        words = sys.argv[1:]

if words != 0:
    print_unicode_table(words)

#End main script


# In[ ]:




