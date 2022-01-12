import vcf
import os
import argparse

parser = argparse.ArgumentParser(description = 'For citrus', add_help = False, usage = '\npython3 -i [input file from step1] -l [sample list] -o [output.file]')
required = parser.add_argument_group()
optional = parser.add_argument_group()
required.add_argument('-i', '--input', metavar = '[input.beagle.vcf]', help = 'input.beagle.vcf', required = True)
required.add_argument('-l', '--fam', metavar = '[fam name]', help = 'fam_name', required = True)
required.add_argument('-f', '--fai', metavar = '[refence.fai]', help = 'refence.fai', required = True)
required.add_argument('-m', '--mu', metavar = '[mutation ratio]', help = 'mutation ratio', default='2.2e-8',type=str)
optional.add_argument('-h', '--help', action = 'help', help = 'help')

args = parser.parse_args()

#os.system()
family=args.fam
sample_list=[]
mu=args.mu
vcf_reader = vcf.Reader(open(args.input, 'r'))
for record in vcf_reader:
    for sample in record.samples:
        #print(sample.sample)
        sample_list.append(sample.sample)
    break

dict={}
with open(args.fai,'r') as fai_file:
    for i in fai_file:
        i=i.replace("\n","").split('\t')
        chr=i[0]
        changdu=int(i[1])
        dict[chr]=changdu

cmd3='mkdir $PWD/{}_out'.format(family)
cmd2='docker pull terhorst/smcpp'
#print(cmd2)
os.system(cmd2)
#print(cmd3)
os.system(cmd3)
for chr in dict.keys():
    out_tmp1=args.input+chr+'.vcf'
    out_file1=open(out_tmp1,'w')
    header_chr="##contig=<ID="+chr+",length="+str(dict[chr])+">"+'\n'
    header0="##fileformat=VCFv4.2"+'\n'
    out_file1.write(header0)
    out_file1.write(header_chr)
    with open(args.input,'r') as vcf:
        for line in vcf:
            if "#CHROM" in line or line.split('\t')[0]==chr:
                out_file1.write(line)
    cmd0='bgzip -c {} > {}.gz'.format(out_tmp1,out_tmp1)
    #print(cmd0)
    os.system(cmd0)
    cmd1='tabix -p vcf {}.gz'.format(out_tmp1)
    #print(cmd1)
    os.system(cmd1)
    
    s=''
    for one in sample_list:
        s+=one+','
    s=s[:-1]
    cmd4='docker run -v $PWD:/work -w /work terhorst/smcpp:latest vcf2smc /work/{}.gz {}_out/{}.smc.gz {} {}:{}'.format(out_tmp1,family,out_tmp1,chr,family,s)
    #print(cmd4)
    os.system(cmd4)
    
cmd5='mkdir $PWD/{}_analysis'.format(family)
#print(cmd5)
os.system(cmd5)
##for single chr
s1=''
s2=''
for chr in dict.keys():
    s1+='/work/'+family+'_out/'+args.input+chr+'.vcf'+'.smc.gz'+' '
    s2+='/work/{}_analysis/{}/model.final.json'.format(family,chr)+' '
    out_tmp1=args.input+chr+'.vcf'
    cmd6='docker run -v $PWD:/work -w /work terhorst/smcpp:latest estimate -o /work/{}_analysis/{} {} /work/{}_out/{}.smc.gz'.format(family,chr,mu,family,out_tmp1)
    #print(cmd6)
    os.system(cmd6)
##for combine
cmd7='mkdir $PWD/{}_combine'.format(family)
#print(cmd7)
os.system(cmd7)
s1=s1[:-1]
s2=s2[:-1]
cmd8='docker run -v $PWD:/work -w /work terhorst/smcpp:latest estimate -o /work/{}_combine/ {} {}'.format(family,mu,s1)
#print(cmd8)
os.system(cmd8)
cmd9='docker run -v $PWD:/work -w /work terhorst/smcpp:latest plot /work/{}.pdf /work/{}_combine/model.final.json {}'.format(family,family,s2)
#print(cmd9)
os.system(cmd9)
cmd10='rm {}*.vcf*'.format(family)
#os.system(cmd10)



