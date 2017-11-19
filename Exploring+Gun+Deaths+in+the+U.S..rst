
.. code:: ipython3

    import csv
    f = open("/Users/matthewfoer/Desktop/guns.csv",'r')
    data = list(csv.reader(f))
    
    
    places = []
    for row in data:
        places.append(row[9])
           
    print(set(places))


.. parsed-literal::

    {'Farm', 'Home', 'place', 'School/instiution', 'Residential institution', 'Street', 'Other unspecified', 'Sports', 'Other specified', 'Trade/service area', 'NA', 'Industrial/construction'}


.. code:: ipython3

    headers = data[0]
    data = data[1:]
    print(headers)
    print(data[:5])


.. parsed-literal::

    ['', 'year', 'month', 'intent', 'police', 'sex', 'age', 'race', 'hispanic', 'place', 'education']
    [['1', '2012', '01', 'Suicide', '0', 'M', '34', 'Asian/Pacific Islander', '100', 'Home', 'BA+'], ['2', '2012', '01', 'Suicide', '0', 'F', '21', 'White', '100', 'Street', 'Some college'], ['3', '2012', '01', 'Suicide', '0', 'M', '60', 'White', '100', 'Other specified', 'BA+'], ['4', '2012', '02', 'Suicide', '0', 'M', '64', 'White', '100', 'Home', 'BA+'], ['5', '2012', '02', 'Suicide', '0', 'M', '31', 'White', '100', 'Other specified', 'HS/GED']]


.. code:: ipython3

    years = [row[1] for row in data]
    
    year_counts = {}
    for year in years:
        if year not in year_counts:
            year_counts[year] = 0
        year_counts[year] += 1
    
    year_counts




.. parsed-literal::

    {'2012': 33563, '2013': 33636, '2014': 33599}



.. code:: ipython3

    import datetime
    
    dates = [datetime.datetime(year = int(row[1]), month = int(row[2]), day = 1) for row in data]
    print(dates[:5])


.. parsed-literal::

    [datetime.datetime(2012, 1, 1, 0, 0), datetime.datetime(2012, 1, 1, 0, 0), datetime.datetime(2012, 1, 1, 0, 0), datetime.datetime(2012, 2, 1, 0, 0), datetime.datetime(2012, 2, 1, 0, 0)]


.. code:: ipython3

    date_counts = {}
    
    for date in dates:
        if date not in date_counts:
            date_counts[date] = 0
        date_counts[date] += 1
        
    print(date_counts)


.. parsed-literal::

    {datetime.datetime(2012, 1, 1, 0, 0): 2758, datetime.datetime(2012, 2, 1, 0, 0): 2357, datetime.datetime(2012, 3, 1, 0, 0): 2743, datetime.datetime(2012, 4, 1, 0, 0): 2795, datetime.datetime(2012, 5, 1, 0, 0): 2999, datetime.datetime(2012, 6, 1, 0, 0): 2826, datetime.datetime(2012, 7, 1, 0, 0): 3026, datetime.datetime(2012, 8, 1, 0, 0): 2954, datetime.datetime(2012, 9, 1, 0, 0): 2852, datetime.datetime(2012, 10, 1, 0, 0): 2733, datetime.datetime(2012, 11, 1, 0, 0): 2729, datetime.datetime(2012, 12, 1, 0, 0): 2791, datetime.datetime(2013, 1, 1, 0, 0): 2864, datetime.datetime(2013, 2, 1, 0, 0): 2375, datetime.datetime(2013, 3, 1, 0, 0): 2862, datetime.datetime(2013, 4, 1, 0, 0): 2798, datetime.datetime(2013, 5, 1, 0, 0): 2806, datetime.datetime(2013, 6, 1, 0, 0): 2920, datetime.datetime(2013, 7, 1, 0, 0): 3079, datetime.datetime(2013, 8, 1, 0, 0): 2859, datetime.datetime(2013, 9, 1, 0, 0): 2742, datetime.datetime(2013, 10, 1, 0, 0): 2808, datetime.datetime(2013, 11, 1, 0, 0): 2758, datetime.datetime(2013, 12, 1, 0, 0): 2765, datetime.datetime(2014, 1, 1, 0, 0): 2651, datetime.datetime(2014, 2, 1, 0, 0): 2361, datetime.datetime(2014, 3, 1, 0, 0): 2684, datetime.datetime(2014, 4, 1, 0, 0): 2862, datetime.datetime(2014, 5, 1, 0, 0): 2864, datetime.datetime(2014, 6, 1, 0, 0): 2931, datetime.datetime(2014, 7, 1, 0, 0): 2884, datetime.datetime(2014, 8, 1, 0, 0): 2970, datetime.datetime(2014, 9, 1, 0, 0): 2914, datetime.datetime(2014, 10, 1, 0, 0): 2865, datetime.datetime(2014, 11, 1, 0, 0): 2756, datetime.datetime(2014, 12, 1, 0, 0): 2857}


.. code:: ipython3

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


.. parsed-literal::

    {'Asian/Pacific Islander': 1326, 'White': 66237, 'Native American/Native Alaskan': 917, 'Black': 23296, 'Hispanic': 9022}
    {'M': 86349, 'F': 14449}


.. code:: ipython3

    f = open("census.csv", 'r')
    census = list(csv.reader(f))
    print(census)


::


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-7-9c41e03ae4db> in <module>()
    ----> 1 f = open("census.csv", 'r')
          2 census = list(csv.reader(f))
          3 print(census)


    FileNotFoundError: [Errno 2] No such file or directory: 'census.csv'


.. code:: ipython3

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

.. code:: ipython3

    
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

.. code:: ipython3

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



.. parsed-literal::

    {'White': 9147, 'Asian/Pacific Islander': 559, 'Black': 19510, 'Native American/Native Alaskan': 326, 'Hispanic': 5634}


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-8-93c33586a937> in <module>()
         14 race_per_hundredk_hom = {}
         15 for k,v in homicide_race_counts.items():
    ---> 16     race_per_hundredk_hom[k] = (v/mapping[k]) * 100000
         17 
         18 race_per_hundredk_hom


    NameError: name 'mapping' is not defined

