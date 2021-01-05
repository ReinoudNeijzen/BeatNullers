#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
import csv


# In[31]:


dirty_in_file = "vertikotimes.csv"
in_file = "vertikotimes_clean.csv"
out_file = "vertrecords.csv"


# In[32]:


with open(dirty_in_file, "r") as f_in:
    with open(in_file, "w", newline = "") as f_out:
        csv_reader = csv.reader(f_in)
        csv_writer = csv.writer(f_out)
        for row in csv_reader:
            if row and re.match(r'[b?kz|xc].*', row[0]):
                csv_writer.writerow(row)


# In[30]:


with open(in_file, "r") as f_in:
    with open(out_file, "w", newline="") as f_out:
        csv_reader = csv.reader(f_in)
        csv_writer = csv.writer(f_out)
        for row in csv_reader:
            if re.findall(r'\s1\/', row[3]):
                csv_writer.writerow(row)


# In[ ]:




