import vcf
import argparse

parser = argparse.ArgumentParser(description = 'modified vcf file', add_help = False, usage = '\npython3 -i [input.vcf]  -o [output.vcf]')
required = parser.add_argument_group()
optional = parser.add_argument_group()
required.add_argument('-i', '--input', metavar = '[input_vcf]', help = 'input_vcf', required = True)
required.add_argument('-o', '--output', metavar = '[output]', help = 'output', required = True)
optional.add_argument('-h', '--help', action = 'help', help = 'help')
args = parser.parse_args()

#keep header
out_vcf=open(args.output,'w')
with open(args.input,'r') as f:#set3.234.deepvariants.vcf
    for line in f:
        if line.startswith('##'):
            out_vcf.write(line)
        else:
            break

vcf_reader = vcf.Reader(open(args.input, 'r'))
group=vcf_reader.samples

#add sampel names
hh1="#CHROM"+'\t'+"POS"+'\t'+"ID"+'\t'+"REF"+'\t'+"ALT"+'\t'+"QUAL"+'\t'+"FILTER"+'\t'+"INFO"+'\t'+"FORMAT"+'\t'
hh2=''
for one in group:
    hh2+=one+'-h1'+'\t'+one+'-h2'+'\t'
hh=hh1+hh2[:-1]+'\n'
out_vcf.write(hh)

##genotyped
for record in vcf_reader:
    chr=record.CHROM
    pos=record.POS
    id=record.ID
    ref=record.REF
    alt=record.ALT[0]
    qual=record.QUAL
    filter='.'
    info='.'
    format=record.FORMAT
    ll=chr+'\t'+str(pos)+'\t'+id+'\t'+ref+'\t'+str(alt)+'\t'+str(qual)+'\t'+filter+'\t'+info+'\t'+format+'\t'
    l2=''
    for num,sample in enumerate(record.samples):
        b=sample['GT'].split('/')
        #print(b,group[num])
        new_b=b[0]+'/'+b[0]+'\t'+b[1]+'/'+b[1]+'\t'
        l2+=new_b
    all=ll+l2[:-1]+'\n'
    out_vcf.write(all)
