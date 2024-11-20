import pandas

series = pandas.read_json("2/pupils.json", typ='series', orient='records')

yearList = []
for tup in series.items():
    yearList.append(tup[1].year)

yearSeries = pandas.Series(yearList)
yearSeries.to_json("2/years.json")
