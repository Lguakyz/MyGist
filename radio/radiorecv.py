import sys
min = int(sys.argv[1])
max = int(sys.argv[2])
for o in sys.stdin:
 if int(o) >= min and int(o) < max:
  if sys.argv[3] == "16":
   a = int((65536.0*(int(o)-min)/(float(max)-float(min))))
   p = int(a % 256)
   q = int(a / 256)
   sys.stdout.write("%s%s" %(chr(p),chr(q)))
  if sys.argv[3] == "8":
   int((256.0*(int(o)-min)/(float(max)-float(min))))