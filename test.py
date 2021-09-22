import xml.etree.ElementTree as ET
from pathlib import Path
root = ET.parse('test.ppx')
for rule in root.iter('Rule'):
    for child in rule:
        if(child.tag == 'Name'):
            if(child.text == 'Block'):
                print(rule.attrib['enabled'])
                rule.attrib['enabled'] = 'false'
                print(rule.attrib['enabled'])
root.write('test.xml')

p = Path('test.xml')
p.rename(p.with_suffix('.ppx'))