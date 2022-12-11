import vcf
import os
import random
import argparse

parser = argparse.ArgumentParser(description = 'caculate heterozygous windows', add_help = False, usage = '\npython3 -i [input.vcf] -s [step and windows] -o [output.txt]')
required = parser.add_argument_group()
optional = parser.add_argument_group()
required.add_argument('-i', '--input', metavar = '[input_vcf]', help = 'input.vcf', required = True)
required.add_argument('-o', '--output', metavar = '[output]', help = 'output.txt', required = True)
required.add_argument('-s', '--step', metavar = '[step]', help = 'step',default=10000)
optional.add_argument('-h', '--help', action = 'help', help = 'help')
args = parser.parse_args()

samples_name=args.input[:-4]
#filter heterozygous
seed=random.randint(1,1000000)
vcf_reader0 = vcf.Reader(open(args.input, 'r'))
vcf_writer0 = vcf.Writer(open(args.input+str(seed)+'tmp.vcf', 'w'), vcf_reader0)
for record in vcf_reader0:
    gt=record.genotype(samples_name)['GT']
    if gt=='0|1' or gt=='1|0':
        vcf_writer0.write_record(record)
vcf_writer0.close()
#split chromosome

for i in range(1,10):
    vcf_reader1 = vcf.Reader(open(args.input+str(seed)+'tmp.vcf', 'r'))
    vcf_writer1 = vcf.Writer(open(args.input+str(seed)+'chr'+str(i)+'tmp.vcf', 'w'), vcf_reader1)
    for record in vcf_reader1:
        chr=record.CHROM
        gt=record.genotype(samples_name)['GT']
        #print(gt)
        if chr=='chr'+str(i) and gt=='0|1':
            vcf_writer1.write_record(record)
        if chr=='chr'+str(i) and gt=='1|0':
            vcf_writer1.write_record(record)
    vcf_writer1.close()

#caculate het
out=open(args.output,'w')   
win=int(args.step)
step=int(args.step)
L=[32266151,33368013,41283659,32876879,48982865,27141800,31662302,30741539,30315542]
for i in range(1,10):
    for each in range(int((L[i-1])/step+1)):
        chr_test='chr'+str(i)
        start=each*step
        end=start+win
        #print(chr_test,start,end)
        count=0
        vcf_reader2 = vcf.Reader(open(args.input+str(seed)+'chr'+str(i)+'tmp.vcf', 'r'))
        for record in vcf_reader2:
            #print(record)
            chr=record.CHROM
            pos=int(record.POS)
            gt=record.genotype(samples_name)['GT']
            #print(pos)
            if not chr==chr_test:
                pass
            elif chr==chr_test and pos<start:
                pass
            elif chr==chr_test and pos>start and pos<end:
                if gt=='0|1' or gt=='1|0':
                    #print(record)
                    count+=1
            elif chr==chr_test and pos>end:
                break
        ll=chr_test+'\t'+str(start)+'\t'+str(end)+'\t'+str(count/step)+'\n'
        out.write(ll)
        #print(chr_test,start,end,count/10000)
out.close()

#delete tmp files
for i in range(1,10):
    pass
    cmd0='rm -f {}'.format(args.input+str(seed)+'tmp.vcf')
    cmd1='rm -f {}'.format(args.input+str(seed)+'chr'+str(i)+'tmp.vcf')
    os.system(cmd0)
    os.system(cmd1)
    