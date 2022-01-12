out=open("filter.rho","w")
out1=open("other.rho","w")
list0=[]
list=[]
with open("all.region.txt","r") as fd:
    for line1 in fd:
        line2=line1.replace("\n","").split('\t')
        chr_test=line2[0].split('_')[0]
        start_test=line2[0].split('_')[1]
        end_test=line2[0].split('_')[2]
        v=0
        with open("intron.region.txt","r") as f:
            for line in f:
                line=line.replace("\n","").split('\t')
                chr=line[0].split('_')[0]
                start=line[0].split('_')[1]
                end=line[0].split('_')[2]
                if chr==chr_test and start_test<end and end_test>start:
                    v=1
                    #print(line1)
                    out.write(line1)
                    list0.append(line1)
                else:
                    v=0
                
        if v==0:
            list.append(line1)
list=set(sorted(list))
for each in list:
    if not each in list0:
        out1.write(each)
