import csv
import sys


def flatten(l):
    return list(set([item for subl in l for item in subl]))

def main():
    # read the csv
	raw_data = []
	with open(sys.argv[1], 'r') as so_data:
	    lst = csv.reader(so_data)
	    for row in lst:
	        raw_data.append(row)
	        data = []
	for i in raw_data:
	    data.append([int(i[0].strip()), int(i[1].strip())])
	
#	print("set keys to uniq elements from col1 and col2")
	keys1 = list(set([i[0] for i in data]))
	keys2 = list(set([i[1] for i in data]))
	keys = list(set(keys1 + keys2))
	
#	print(" find the subchains for each key")
	subchains = {}
	for key in keys:
	    found = [k for k in data if key in k]
	    found = flatten(found)
	    subchains[key] = found
	
	# This is the tricky bit
	# we need to follow each element of the subchains looking
	# for new links - we are done for a key when the list doesn't grow
#	print("cuppa tea?")
	chain, links = [], []
	chain_dict = {}
	for key in keys:
	    links.append(subchains[key])
	    links = flatten(links)
	    done = False
	    size = len(links)
	    while not done:
	        for i in links:
	            # find subchain for i
	            for e in subchains[i]:
	                chain.append(e)
	                chain = list(set(chain))
	                chain.sort()
	        if len(chain) > size:
	            done = False
	            size = len(chain)
	        else:
	            done = True
	            chain_dict[key] = chain
	            chain, links = [], []
	
#	print("subsets")
	# shorter chains will now be subsets of longer ones
	# and those can be discarded
	remove_list = []
	for i in keys:
	    for j in keys:
	        if set(chain_dict[j]) < set(chain_dict[i]):
	            remove_list.append(j)
	
	remove_list = list(set(remove_list))
	for i in remove_list:
	    del chain_dict[i]
	
#	print("dups")
	# remove duplicate values from dict
	# it doesn't matter which key we remove
	# since we only output from value
	result = {}
	for key, value in chain_dict.items():
	    if value not in result.values():
	        result[key] = value
	
#	print("********************************************************************************")
	# now output as per OP's request
	for k, v in result.items():
	    v.sort()
	    for i in v[1:]:
	        print(v[0], ",", i)
#	    print()
	

if __name__ == '__main__':
    main()
    
