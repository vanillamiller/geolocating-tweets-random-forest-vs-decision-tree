import re

class CSV:
    @staticmethod
    def to_csv(filename):

        # sanitized list of lines from train_tweets.txt
        san=[]

        # open read and write files
        filein=open(filename+'.txt','r', encoding="ISO-8859-1")
        fileout=open(filename+'.csv','w', encoding="ISO-8859-1")

        # iterate through infile
        for line in filein:
            quote=re.search(r'"(.*?).*"', line).group(0)
            temp=quote.replace(',','')
            temp=temp[1:len(temp)-1].replace("\"", '')
            temp="'"+temp+"'"
            line=line.replace(quote, temp)
            san.append(line)

        fileout.writelines(san)
        fileout.close()
        filein.close()
        print("tweets read")