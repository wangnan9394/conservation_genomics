import vcf
out=open("out.txt","w")

###input vcf: Jg1 Jg2 Jg3 Jg4 Jg5 sjg1 sjg2 sjg3 sjg4 sjg5
##Jg indicated cultivated sjg indicated wild
vcf_reader = vcf.Reader(open('keep.vcf', 'r'))
for record in vcf_reader:
    list=[]
    for i in record.samples:
        gt=record.genotype(i.sample)['GT']
        list.append(gt)
    list_Jg=list[:5]

    list_sjg=list[5:11]
    print(list_Jg,list_sjg)
    #list_out=list[11:]
    Jg_sort=sorted(set(list_Jg),key=list_Jg.index)
    sjg_sort=sorted(set(list_sjg),key=list_sjg.index)
    print(Jg_sort,'*****',sjg_sort)
    if len(Jg_sort)==1 and len(sjg_sort)==1 and Jg_sort[0]=='1/1' and sjg_sort[0]=='0/0':
        ll=record.CHROM+'\t'+str(record.POS)+'\t'+record.REF+'\t'+str(record.ALT[0])+'\n'
        out.write(ll)
    if len(Jg_sort)==1 and len(sjg_sort)==1 and Jg_sort[0]=='0/0' and sjg_sort[0]=='1/1':
        print(record.ALT)
        ll=record.CHROM+'\t'+str(record.POS)+'\t'+str(record.ALT[0])+'\t'+record.REF+'\n'
        out.write(ll)

