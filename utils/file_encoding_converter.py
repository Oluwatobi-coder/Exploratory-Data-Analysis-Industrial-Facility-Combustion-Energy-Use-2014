import chardet # for detecting character encoding of text files


# helper function for converting files from one encoding to another
def convertFileEncoding(prev_encode,new_encode,old_filepath,target_file):
    f_old=open(old_filepath, 'rb')
    file_content=[]
    while True:
        line=f_old.readline()
        file_content.append(line.decode(prev_encode).encode(new_encode))
        if len(line) ==0:
            break

    f_old.close()
    f_new=open(target_file,'wb')
    f_new.writelines(file_content)
    f_new.close()

# reading the original dataset file
convertFile = open("data_source/IndustrialCombEnergy_2014.csv",'rb')
data = convertFile.read()
convertFile.close()

# executing the function to convert the original dataset in Windows-1252 to utf-8 which is an efficient encoding systems and widely used 
convertFileEncoding(chardet.detect(data)['encoding'], "utf-8", "data_source/IndustrialCombEnergy_2014.csv", "data_source/IndustrialCombEnergy_2014_utf-8_version.csv")