import random
import os
import argparse


parser = argparse.ArgumentParser(description = 'For slim output to vcf merge', add_help = False, usage = '\npython3 -g [input.vcf] -g [groups number]')
required = parser.add_argument_group()
optional = parser.add_argument_group()
required.add_argument('-i', '--input', metavar = '[input.txt]', help = 'input', required = True)
required.add_argument('-g', '--group', metavar = '[group]', help = 'groups', required = True)
optional.add_argument('-h', '--help', action = 'help', help = 'help')


args = parser.parse_args()


input_name=args.input
groups=int(args.group)


seed=random.randint(1,100000)
count=0
with open(input_name) as f:
    fd=f.readlines()
    for i in fd:
        count+=1
        if "#OUT:" in i:
            target=count-1
            break
       
with open(input_name) as f:
    fd=f.readlines()[target:]
    count=0
    for line in fd:
        if "#OUT:" in line:
            count+=1
            filename=input_name+'.'+'p'+str(count)+'.vcf'
            file=open(filename,'w')
        elif "#CHROM" in line:
            s=''
            for i in range(100):###Ñù±¾Êý
                i='p'+str(count)+'i'+str(i)
                s+=i+'\t'
            ll="#CHROM"+'\t'+'POS'+'\t'+'ID'+'\t'+'REF'+'\t'+'ALT'+'\t'+'QUAL'+'\t'+'FILTER'+'\t'+'INFO'+'\t'+'FORMAT'+'\t'+s
            file.write(ll[:-1]+'\n')
        else:
            file.write(line)
               
#step2:merge vcfs
for num in range(1,groups+1):
    vcfname=input_name+'.'+'p'+str(num)+'.vcf'
    cmd1='bgzip -c {} > {}.gz'.format(vcfname,vcfname)
    os.system(cmd1)
    cmd2='tabix -p vcf {}.gz'.format(vcfname)
    os.system(cmd2)


cmd3='bcftools merge {}*.vcf.gz >{}.merge.vcf.vaild'.format(input_name,input_name)
os.system(cmd3)
old="\.\/\."
new="0|0"
cmd4="sed -i 's/{}/{}/g' {}.merge.vcf.vaild".format(old,new,input_name)
os.system(cmd4)


##step:clear
cmd5='rm -rf {}*.vcf'.format(input_name)
cmd6='rm -rf {}*.vcf.gz*'.format(input_name)
os.system(cmd5)
os.system(cmd6)