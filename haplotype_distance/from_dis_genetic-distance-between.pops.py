import numpy as np
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description = 'dis-to-halotype.average', add_help = False, usage = '\npython3 -i [input.dis]')
required = parser.add_argument_group()
optional = parser.add_argument_group()
required.add_argument('-i', '--input', metavar = '[input_dis]', help = 'input_dis', required = True)
required.add_argument('-o', '--output', metavar = '[output]', help = 'output', required = True)
optional.add_argument('-h', '--help', action = 'help', help = 'help')
args = parser.parse_args()




group=[]
group_WILDAPO=["DB","I1","J1","K1","P3-1","BZ01","DYS002-5","DYT01","FC01","GT01","HK02","HS03","JK09","LH10","LY04","MJS02","MP12","NQ03","RYS","SD01","SK03","SY02","WH","WP"]
group_WILDSEX1=["N1","Y6-1","DR01","FC-7","FC14","LS","LS4","SY01","TZ","YSY02","ZL01"]
group_WILDSEX2=["PN","QLS","DSD-1","DSD-2","LZSZ-1","LZSZ-2","NXG-1","NXG-2","NXG-3","NXG-4","NXG-5","NXG-6","NXG-7","NXG-8","NXG-9","PN01","PN03"]
group_CULAPO=["Glossy","JgA02","JgA03","JgA04","JgA05","JgA06","JgA10","JgA12","JgA13","JgA17","JgA18","Normal"]
group_CULSEX=["JgA01","JgA07","JgA09","JgA11","JgA14","N18FOR","O21JGLYP1"]
#group_WILDSEX1.extend(group_WILDSEX2)

##fam classfication
fam=["WILDAPO","WILDAPO","WILDAPO","WILDAPO","WILDAPO","WILDAPO","WILDAPO","WILDAPO","WILDAPO","WILDAPO","WILDAPO","WILDAPO","WILDAPO","WILDAPO","WILDAPO","WILDAPO","WILDAPO","WILDAPO","WILDAPO","WILDAPO","WILDAPO","WILDAPO","WILDAPO","WILDAPO"]
fam_SEX1=["WILDSEX1","WILDSEX1","WILDSEX1","WILDSEX1","WILDSEX1","WILDSEX1","WILDSEX1","WILDSEX1","WILDSEX1","WILDSEX1","WILDSEX1"]
fam_SEX2=["WILDSEX2","WILDSEX2","WILDSEX2","WILDSEX2","WILDSEX2","WILDSEX2","WILDSEX2","WILDSEX2","WILDSEX2","WILDSEX2","WILDSEX2","WILDSEX2","WILDSEX2","WILDSEX2","WILDSEX2","WILDSEX2","WILDSEX2"]

dict_fam={}
for i in range(len(fam)):
    dict_fam[group_WILDAPO[i]]=fam[i]

##define function
def hapsex1(group_list,setsample,setpfile):
    #read data frame
    group_WILDAPO=["DB","I1","J1","K1","P3-1","BZ01","DYS002-5","DYT01","FC01","GT01","HK02","HS03","JK09","LH10","LY04","MJS02","MP12","NQ03","RYS","SD01","SK03","SY02","WH","WP"]
    g=[]
    group=[]
    with open(setpfile,'r') as fd:
        for line in fd:
            line=line.replace(" ","").replace("\n","").split("\t")
            if len(line)>1:
                group.append(line[0])
                line1=line[1:]
                g.append(line1)
    df=pd.DataFrame(g)

    #constrct dictory
    dict={}
    for i in range(len(df)):
        for r in range(len(df)):
            a=str(group[i])+'and'+str(group[r])
            dict[a]=df.iloc[i,r]

    #cacultae average haplotype distance in the all samples
    aver_dis=[]
    for selected1 in group_WILDAPO:
        for selected2 in group_WILDAPO:
            value1=selected1+'-h1'+'and'+selected2+'-h2'
            #print(value2,dict[value2])
            aver_dis.append(float(dict[value1]))
    fff=np.array(aver_dis)
    fff_mean=np.mean(fff)

    #caculate-DB hap1 and hap2
    one=setsample
    value3=float(dict[one+'-h1'+'and'+one+'-h2'])

    #caculate-DB with group_list
    list_value=[]
    list_value_another_hap=[]
    for two1 in group_list:
        value4=float(dict[one+'-h1'+'and'+two1+'-h1'])
        value5=float(dict[one+'-h1'+'and'+two1+'-h2'])
        value6=float(dict[one+'-h2'+'and'+two1+'-h1'])
        value7=float(dict[one+'-h2'+'and'+two1+'-h2'])
        if (value6+value7) < (value4+value5):
            if value6>0:
                list_value.append(value6)
            if value7>0:
                list_value.append(value7)
            if value4>0:
                list_value_another_hap.append(value4)
            if value5>0:
                list_value_another_hap.append(value5)
        if (value6+value7) > (value4+value5):
            if value4>0:
                list_value.append(value4)
            if value5>0:
                list_value.append(value5)
            if value6>0:
                list_value_another_hap.append(value6)
            if value7>0:
                list_value_another_hap.append(value7)
                #print(one,two1)
    #print(list_value)
    #print(dict['DB-h1andJgA01-h1'])
    list_value=np.array(list_value)
    list_value_another_hap=np.array(list_value_another_hap)
    hap_one_sex1=np.mean(list_value)
    list_value_another_hap_sex1=np.mean(list_value_another_hap)
    return (value3/fff_mean,hap_one_sex1/fff_mean,list_value_another_hap_sex1/fff_mean)

#caculate the distance haplotypes (one individual) and apo-sample+all-SEXsamples

out_results=open(args.output,'w') 
for sample in group_WILDAPO:      
    a,b,c=hapsex1(group_WILDSEX1,sample,args.input)
    lllll=sample+'\t'+str(a)+'\t'+str(b)+'\t'+str(c)+'\n'
    out_results.write(lllll)
    #a,b=hapsex1(group_WILDSEX2,i)
    #print(a,b)

#if value3/fff_mean>0 and hap_one_sex1/fff_mean>0:
#    lll='args.input'+'\t'+one+'\t'+str(value3/fff_mean)+'\t'+str(hap_one_sex1/fff_mean)
#    #out_results.write(lll)
#    print(lll)
#if value3/fff_mean>0:
#    lll='\t'+dict_fam[one]+'\t'+str(value3/fff_mean)+'\n'
#    out_results.write(lll)
    