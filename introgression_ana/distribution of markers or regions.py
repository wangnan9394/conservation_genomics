L=[32266151,33368013,41283659,32876879,48982865,27141800,31662302,30741539,30315542]##chromosome length
file_name="top1.txt"
#####format: chr1 \t 29350000 \t 29400000
out_file_name=file_name[:4]+".forR.txt"
out=open(out_file_name,"w")

for ind in range(1,10):
    pred_chr='chr'+str(ind)
    list_pos=[]
    list_pos.append(0)
    with open(file_name,"r")as fd:
        for line in fd:
            line=line.replace("\n","").split("\t")
            #print(line)
            chr=line[0]
            if chr==pred_chr:
                start=int(line[1])
                end=int(line[2])
                list_pos.append(start)
                list_pos.append(end)
        list_pos.append(L[ind-1])
    #print(list_pos)
    for s in range(len(list_pos)):##rho and noraml
        l1=list_pos[s:s+2]
        a=(l1[0]+sum(L[:ind-1])+3000000*(ind-1))*0.0001
        b=(l1[-1]-1+sum(L[:ind-1])+3000000*(ind-1))*0.0001
        if (s % 2) == 0:
            l1='chr'+str(ind)+'\t'+str(a)+'\t'+str(b)+'\t'+'noraml'+'\n'
        else:
            l1='chr'+str(ind)+'\t'+str(a)+'\t'+str(b)+'\t'+'rho'+'\n'
        out.write(l1)

