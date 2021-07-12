# Knowledge Bases
This repository contains some domain-specific knowledge bases (raw data and knowledge facts). So far, we're going to construct a cybersecurity knowledge graph and a medication knowledge graph.


### Cybersecurity KG
We collect information from https://www.cvedetails.com/vulnerabilities-by-types.php, where we crawl reported vulnerabilities of for each year (see **./data/cyberkg-raw/<year>/**). For each CVE vulnerability, we collect its following information and save in csv files, each line refers to:
- **(1st col) line index**
- **(2nd col) cve-id** : Unique ID for a CVE code
- **(3rd col) cve-url** : Corresponding webpage 
- **(4th col) cve-desc** : Descriptions for one CVE code  (maybe 'None')
- **(5th col) pub-time** : Publication time               
- **(6th col) score** : CVSS socre reported on webpage
- **(7th col) vulner-type** : Vulnerability type (also results caused by this CVE, maybe 'None')
- **(8th col) cwe-id** : Corresponding CWE ID             (maybe 'None')
- **(9th col) cwe-url** : URL for corresponding CWE       (maybe 'None')
- **(10th col) cwe-def** : Definition for CWE    (maybe 'None')
- **(11th col) cwe-rel** : Related CWEs, includes *relation*, *cwe-id*, *cwe-def*  (maybe 'None')
- **(12th col) pd-info** : includes *product type*, *vendor*, *product name*, *version*

In saved csv files, above items are split by a single '|'. In **pd-info**, information for same product version is splitted by a single comma ',', for different products/versions are split by a single semicolon ';' In **vulner-type**, one CVE may have more than one vulnerability types, we split them by ','.
