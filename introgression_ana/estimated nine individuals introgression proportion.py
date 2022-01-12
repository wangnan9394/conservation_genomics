L=[32266151,33368013,41283659,32876879,48982865,27141800,31662302,30741539,30315542]
file1="DB.out.R.txt"
file2="sjg_DYT01.out.R.txt"
file3="sjg_HK02.out.R.txt"
file4="sjg_HS03.out.R.txt"
file5="sjg_MJS02.out.R.txt"
file6="sjg_SD01.out.R.txt"
file7="sjg_WH.out.R.txt"
file8="sjg_XHS.out.R.txt"
file9="sjg_ZX11.out.R.txt"

out=open("proportion.chr_all.txt",'w')
header='CHROM'+'\t'+'POS'+'\t'+'DB'+'\t'+'sjg_DYT01'+'\t'+'sjg_HK02'+'\t'+'sjg_HS03'+'\t'+'sjg_MJS02'+'\t'+'sjg_SD01'+'\t'+'sjg_WH'+'\t'+'sjg_XHS'+'\t'+'sjg_ZX11'+'\n'
def test(file,chromosome,num):
    v='0/0'
    with open(file,'r') as f:
        for line in f:
            line=line.replace("\n","").split('\t')
            type=line[3]
            if line[0]==chromosome:
                if type=='mix':
                    if num>int(line[1])-1 and num<int(line[2])+1:
                        v='0/1'
                if type=='out':
                    if num>int(line[1])-1 and num<int(line[2])+1:
                        v='1/1'
    return v
for each in range(1,10):
    chr='chr'+str(each)
    for i in range(1,L[each-1]):
        n1=str(test(file1,chr,i))+'\t'
        n2=str(test(file2,chr,i))+'\t'
        n3=str(test(file3,chr,i))+'\t'
        n4=str(test(file4,chr,i))+'\t'
        n5=str(test(file5,chr,i))+'\t'
        n6=str(test(file6,chr,i))+'\t'
        n7=str(test(file7,chr,i))+'\t'
        n8=str(test(file8,chr,i))+'\t'
        n9=str(test(file9,chr,i))+'\n'
        ll=chr+'\t'+str(i)+'\t'+n1+n2+n3+n4+n5+n6+n7+n8+n9
        out.write(ll)



