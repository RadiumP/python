import xml.etree.ElementTree as ET
from pathlib import Path
tree = ET.parse('test.ppx')
for rule in tree.iter('Rule'):
    for child in rule:
        if(child.tag == 'Name'):
            if(child.text == 'Block'):
                print(rule.attrib['enabled'])
                rule.attrib['enabled'] = 'false'
                print(rule.attrib['enabled'])

with open('test.ppx', 'wb') as f:
    f.write(b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
    tree.write(f)

# p = Path('test.xml')
# p.rename(p.with_suffix('.ppx'))