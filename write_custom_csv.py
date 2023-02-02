import csv 

cnt=0
w = open('custom.csv','w', newline='', encoding='utf-8')
wr = csv.writer(w)

with open("price_dataset_large.csv", "r", encoding='utf-8') as f:
    reader = csv.reader(f, delimiter="\t")
    for i, line in enumerate(reader):
        if i==0:
            wr.writerow(line[0].split(','))
        else:
            price = line[0].split(',')[-1]
            if price.isdigit() and int(price)<=30000 and cnt<=200000: 
                wr.writerow(line[0].split(','))
                cnt+=1
            if price.isdigit() and int(price)>30000:
                wr.writerow(line[0].split(','))
            

print(cnt)