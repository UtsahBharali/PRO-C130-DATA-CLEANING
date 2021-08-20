import csv 
data = []
with open("data_final.csv","r")as f :
    csvreader  = csv.reader(f)
    for row in csvreader:
        data.append(row)

headers = data[0]
#print(headers)
planet_data = data[1:]
#print(planet_data)
#converting the planet name to lower case
for data_point in planet_data:
    data_point[2] = data_point[2].lower()

planet_data.sort(key = lambda
planet_data:planet_data[2]
)
with open("data_2_final_sort.csv","a+")as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)