import sys
mode = sys.argv[1]
if not "farbfeld" == sys.stdin.read(8):
 exit(1)
size = sys.stdin.read(8)
x = (pow(256,3)*ord(size[0]))+(pow(256,2)*ord(size[1]))+(pow(256,1)*ord(size[2]))+(pow(256,0)*ord(size[3]))
y = (pow(256,3)*ord(size[4]))+(pow(256,2)*ord(size[5]))+(pow(256,1)*ord(size[6]))+(pow(256,0)*ord(size[7]))
n = x*y
sys.stdout.write("farbfeld")
sys.stdout.write(size)
rr=0
gg=0
bb=0
aa=0
while bool(n):
 o = sys.stdin.read(8)
 r = (ord(o[0])*256)+ord(o[1])
 g = (ord(o[2])*256)+ord(o[3])
 b = (ord(o[4])*256)+ord(o[5])
 a = (ord(o[6])*256)+ord(o[7])
 dr=r-rr
 dg=g-gg
 db=b-bb
 da=a-aa
 d=(dr+dg+db+da)/4
 if mode == "rc":
  if d < 0:
   g = max(g - abs(d),0)
   b = max(b - abs(d),0)
  if d >= 0:
   r = max(r - abs(d),0)
 if mode == "gm":
  if d < 0:
   r = max(r - abs(d),0)
   b = max(b - abs(d),0)
  if d >= 0:
   g = max(g - abs(d),0)
 if mode == "by":
  if d < 0:
   r = max(r - abs(d),0)
   g = max(g - abs(d),0)
  if d >= 0:
   b = max(b - abs(d),0)
 sys.stdout.write("%s%s%s%s%s%s%s%s" %(chr(r/256),chr(r%256),chr(g/256),chr(g%256),chr(b/256),chr(b%256),o[6],o[7]))
 rr=r
 gg=g
 bb=b
 aa=a
 n=n-1