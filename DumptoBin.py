import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
Dumpfile = open("dump.txt","r")
Dump = Dumpfile.read().split("\n")
for i,line in enumerate(Dump):
    OutBin = open(f"out_{i+1}.bin","wb")
    for byte in line.split(" "):
        OutBin.write(int(byte,16).to_bytes())
        print(f"Byte: {byte} {int(byte,16)}")
    OutBin.close()
Dumpfile.close()