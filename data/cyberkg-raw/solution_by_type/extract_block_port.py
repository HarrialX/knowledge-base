import glob
import regex as re

mitigation_dir = "data/cyberkg-raw/solution_by_type/workaround/*/*"
max_block_port_distance = 4

result_list = []
for filename in glob.iglob(mitigation_dir):
    with open(filename) as f:
        lines = f.readlines()
        ports = []
        block_mentioned = 0
        for i,line in enumerate(lines):
            if re.search("\\bblock\\b", line, flags=re.IGNORECASE):
                block_mentioned = i
            if i - block_mentioned <= max_block_port_distance:
                matches = re.finditer("ports?\\s(.+\\s){0,3}?(?P<port>[0-9]+)((,\\s|,?\\sand\\s|\\s)(?P<port>[0-9]+))+", line)
                if matches:
                    found = False
                    port_list = []
                    for m in matches:
                        found = True
                        port_list.extend(m.captures("port"))
                    if found:
                        print("Filename:", filename)
                        print("Ports:", ",".join(port_list))
                        print("Text:", "\n".join(lines[block_mentioned: i+1]))
                        result_list.append((filename, ",".join(port_list), "\n".join(lines[block_mentioned: i+1])))

import pickle as pkl
pkl.dump(result_list, open("workaround_block_ports.p", "wb"))

