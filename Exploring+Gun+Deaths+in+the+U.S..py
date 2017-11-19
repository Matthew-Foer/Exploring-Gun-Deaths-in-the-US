
# coding: utf-8

# In[1]:


import csv
f = open("/Users/matthewfoer/Desktop/guns.csv",'r')
data = list(csv.reader(f))


places = []
for row in data:
    places.append(row[9])
       
print(set(places))


# In[2]:


headers = data[0]
data = data[1:]
print(headers)
print(data[:5])


# In[3]:


years = [row[1] for row in data]

year_counts = {}
for year in years:
    if year not in year_counts:
        year_counts[year] = 0
    year_counts[year] += 1

year_counts


# In[4]:


import datetime

dates = [datetime.datetime(year = int(row[1]), month = int(row[2]), day = 1) for row in data]
print(dates[:5])


# In[5]:


date_counts = {}

for date in dates:
    if date not in date_counts:
        date_counts[date] = 0
    date_counts[date] += 1
    
print(date_counts)


# In[6]:


def qual_count(quality):
    qualities = [row[quality] for row in data]
    qual_counts = {}
    for qual in qualities:
        if qual not in qual_counts:
            qual_counts[qual] = 0
        qual_counts[qual] += 1
    return qual_counts

race_counts = qual_count(7)
sex_counts = qual_count(5)
print(race_counts)
print(sex_counts)


# In[7]:


f = open("census.csv", 'r')
census = list(csv.reader(f))
print(census)


# In[ ]:


mapping = {
    "Asian/Pacific Islander": 15159516 + 674625,
    "Native American/Native Alaskan": 3739506,
    "Black": 40250635,
    "Hispanic": 44618105,
    "White": 197318956
}

race_per_hundredk = {}
for k,v in race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

race_per_hundredk


# In[ ]:



mapping = {
    "Asian/Pacific Islander": 15159516 + 674625,
    "Native American/Native Alaskan": 3739506,
    "Black": 40250635,
    "Hispanic": 44618105,
    "White": 197318956
}



race_per_hundredk = {}
for k,v in race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

race_per_hundredk


# In[8]:


intents = [row[3] for row in data]
races = [row[7] for row in data]

homicide_race_counts = {}

for i, race in enumerate(races):
    if intents[i] == "Homicide":
        if race not in homicide_race_counts:
            homicide_race_counts[race] = 0
        homicide_race_counts[race] += 1

print(homicide_race_counts)

race_per_hundredk_hom = {}
for k,v in homicide_race_counts.items():
    race_per_hundredk_hom[k] = (v/mapping[k]) * 100000

race_per_hundredk_hom

