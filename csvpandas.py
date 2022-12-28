import csv
data = open("D:\IT\salesdata.csv",encoding="utf-8-sig")
csv_data=csv.reader(data)
data_lines=list(csv_data)
print(data_lines[0])
print(len(data_lines))

#print(list(csv.reader(open("D:\IT\salesdata.csv",encoding='utf-8-sig'))))

for line in data_lines[:5]:
    print(line)

print('\n')
print(data_lines[10])
print('\n')
print(data_lines[10][5])

all_country=[]
for line in data_lines[1:5]:
    all_country.append(line[1])
    
print(all_country)


region_country=[]
for line in data_lines[1:5]:
    region_country.append(line[0]+' - '+line[1])

print(region_country)

#output_file = open("outputfile.csv",mode='w',newline='')
#csv_writer= csv.writer(output_file,delimiter=',')
#csv_writer.writerow(['a','b','c'])

#csv_writer.writerows([['1','2','3'],['4','5','6']])
#output_file.close()
