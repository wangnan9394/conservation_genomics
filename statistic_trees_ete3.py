from ete3 import Tree#####统计topo统计

import argparse

parser = argparse.ArgumentParser(description = 'None', add_help = False, usage = '\npython3 -i .nwk -o new.nwk')
required = parser.add_argument_group()
optional = parser.add_argument_group()
required.add_argument('-i', '--input', metavar = '[input.nwk]', help = 'input', required = True)
required.add_argument('-o', '--output', metavar = '[output.nwk]', help = 'output', required = True)
optional.add_argument('-h', '--help', action = 'help', help = 'help')

args = parser.parse_args()
out_top=open(args.output,"w")
def collapsed_leaf(node):
    if len(node2labels[node]) == 1:
       return True
    else:
       return False
t = Tree(args.input,format=9)
# We create a cache with every node content
node2labels = t.get_cached_content(store_attr="name")
out_topo=t.write(is_leaf_fn=collapsed_leaf)
t2 = Tree(t.write(format=100,is_leaf_fn=collapsed_leaf),format=100)
out_top.write(out_topo)
