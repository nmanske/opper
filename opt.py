import sys
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('command', help='parse options of specified command')
parser.add_argument('options', help='learn more about these')
parser.add_argument('-a', '--all', help='display all available options',
                    action='store_true')
args = parser.parse_args()

cmd_in = args.command
opts_in = list(args.options.replace('-',''))

cmd_defs = os.listdir('definitions')
if cmd_in not in cmd_defs:
    print(cmd_in + ' does not have a definition')
    sys.exit(0)

#cmd_in = sys.argv[1]
#opts_in = sys.argv[2]

opts_dict = {}
syn_dict = {}
defs_dict = {}

# CONSTRUCT DICTIONARIES OF TARGET CMD
with open('definitions/' + cmd_in, 'r') as f:
    entries = f.read().split('\n\n')
    for index, entry in enumerate(entries, start=1):
        opts = entry.replace(',','').replace('-','').split('\n')[0].split(' ')
        for opt in opts:
            opts_dict.update({opt:index})
        syn_dict.update({index:entry.split('\n')[0]})
        defs = ' '.join(entry.split('\n')[1:])
        defs_dict.update({index:defs})

# FETCH OPTIONS IN USER GIVEN ORDER
for opt in opts_in:
    if opt in opts_dict:
        dict_index = opts_dict.get(opt)
        syn_entry = syn_dict.get(dict_index)
        dict_entry = defs_dict.get(dict_index)
        if not dict_entry:
            dict_entry = 'no description found'
        print(syn_entry + '\n' + dict_entry + '\n')
    else:
        print('-' + opt + '\ninvalid option\n')
