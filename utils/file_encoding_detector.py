import chardet # for detecting character encoding of text files


# extract encoding from the downloaded csv file
with open("data_source/IndustrialCombEnergy_2014_utf8_version1.csv", 'rb') as rawdata:
    result = chardet.detect(rawdata.read())['encoding']

# display encoding
print(result)
