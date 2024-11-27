import sys
def int_to_hex(input):
    return hex(input).split("0x")[1].zfill(2)
if len(sys.argv) < 2:
    raise FileNotFoundError("Please provide two files to compare!")
file1 = sys.argv[1]
file2 = sys.argv[2]
file1_obj = open(file1,"rb")
file1_cntnt = file1_obj.read()
file1_cntnt = [file1_cntnt[i] for i in file1_cntnt]
file1_obj.close()
file2_obj = open(file2,"rb")
file2_cntnt = file2_obj.read()
file2_cntnt = [file2_cntnt[i] for i in file2_cntnt]
file2_obj.close()
x,y = 0,0
left_content = [file1_cntnt[i:i+16] for i in range(0,len(file1_cntnt),16)]
right_content = [file2_cntnt[i:i+16] for i in range(0,len(file2_cntnt),16)]
if len(left_content) >= len(right_content):
    print("--| 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F | --| 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F")
    for y_, line in enumerate(left_content):
        print(f"{int_to_hex(y_)}| ",end="")
        for x_, byte in enumerate(line):
            print(f"{int_to_hex(byte)} ",end="")
        print("| ",end="")
        if not len(right_content) <= y_:
            print(f"{int_to_hex(y_)}| ",end="")
            for x_, byte_ in enumerate(right_content[y_]):
                print(f"{int_to_hex(byte_)} ",end="")
        print()