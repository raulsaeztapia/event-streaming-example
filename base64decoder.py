#!/usr/bin/python

import struct
import base64

reader = open("base64-float.binary", "rb")
decDataSet = base64.standard_b64decode(reader.read())
count =len(decDataSet) // 4
result = struct.unpack('>{0}f'.format(count),decDataSet)
print(result)
