import sys
import json
col = json.loads(sys.stdin.read())
board = col["board"]
copper = col["copper"]
r = copper[1:3]
r = int(r,16)*2
if r > 255:
 r = 255
r = str(hex(r))[2:]
g = copper[3:5]
g = int(g,16)*2
if g > 255:
 g = 255
g = str(hex(g))[2:]
b = copper[5:7]
b = int(b,16)*2
if b > 255:
 b = 255
b = str(hex(b))[2:]
copperactive = "#" + r + g + b
pads = col["pads"]
clad = col["clad"]
vcut = col["vcut"]
silk = col["silk"]
r = pads[1:3]
r = int(r,16)/2
r = str(hex(r))[2:]
g = pads[3:5]
g = int(g,16)/2
g = str(hex(g))[2:]
b = pads[5:7]
b = int(b,16)/2
b = str(hex(b))[2:]
labelbg = "#" + r + g + b
sys.stdout.write("background:%s\n" %(board))
sys.stdout.write("on:%s\n" %(copperactive))
sys.stdout.write("off:%s\n" %(copper))
sys.stdout.write("gate_on:%s\n" %(clad))
sys.stdout.write("gate_off:%s\n" %(clad))
sys.stdout.write("gate_bg:%s\n" %(pads))
sys.stdout.write("text_fg:%s\n" %(silk))
sys.stdout.write("text_bg:%s\n" %(labelbg))
sys.stdout.write("bus:%s,%s,%s,%s,%s,%s,%s,%s\n" %(copper,copper,copper,copper,copper,copper,copper,copper))
sys.stdout.write("led_off_fg:#f00,#f80,#dd0,#0d0,#88f,#a0d,#f99,#eee,white,#000\n")
sys.stdout.write("led_off_bg:%s,%s,%s,%s,%s,%s,%s,%s,#f00,%s\n" %(board,board,board,board,board,board,board,board,board))
sys.stdout.write("led_off_border:%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %(silk,silk,silk,silk,silk,silk,silk,silk,silk,silk))
sys.stdout.write("led_on_fg:%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\nled_on_bg:#f00,#f80,#dd0,#0d0,#88f,#a0d,#f99,#eee,#0f0,#fff\nled_on_border:%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %(silk,silk,silk,silk,silk,silk,silk,silk,silk,silk,silk,silk,silk,silk,silk,silk,silk,silk,silk,silk))
sys.stdout.write("chiplabel_fg:%s\n" %(pads))
sys.stdout.write("chiplabel_bg:%s\n" %(vcut))
sys.stdout.write("switch_off_fg:%s\n" %(silk))
sys.stdout.write("switch_off_bg:%s\n" %(board))
sys.stdout.write("switch_off_border:%s\n" %(silk))
sys.stdout.write("switch_on_fg:%s\n" %(silk))
sys.stdout.write("switch_on_bg:#0f0\n")
sys.stdout.write("switch_on_border:%s\n" %(silk))
sys.stdout.write("error_bg:#ff0\nerror_fg_off:#f00\nerror_fg_on:#f88\n")
sys.stdout.write("link:#00f\ntitle:black\n")
sys.stdout.write("terminal_fg:%s\n" %(silk))
sys.stdout.write("terminal_mid:gray\n")
sys.stdout.write("terminal_bg:black\n")
sys.stdout.write("terminal_outside_fg:%s\n" %(silk))
sys.stdout.write("terminal_outside_bg:%s\n" %(pads))