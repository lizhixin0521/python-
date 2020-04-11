#!/usr/bin/env python3
import difflib

text1 = '''/dev/mapper/rhel-root   /                       xfs     defaults        1 1
UUID=6dd39f47-c929-4564-89a0-213994b789db /boot                   xfs     defaults        1 2
/dev/mapper/rhel-swap   swap                    swap    defaults        0 0
/dev/cdrom              /mnt              iso9660 defaults        0 0
'''

text2 = '''/dev/mapper/rhel-root   /                       xfs     defaults        1 1
UUID=6dd39f47-c929-4564-89a0-213994b789db /boot                   xfs     defaults        1 2
/dev/mapper/rhel-swap   swap                    swap    defaults        0 0
/dev/cdrom              /mnt/cdrom              iso9660 defaults        0 0
'''


text1_line=text1.splitlines()
text2_line=text2.splitlines()
#print(text1_line)
#print(text2_line)

d=difflib.Differ()
diff=d.compare(text1_line,text2_line)
print(type(diff))
print('\n'.join(diff))
