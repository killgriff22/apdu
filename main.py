from smartcard.System import *
from smartcard.util import *
from smartcard.Exceptions import *
while True:
    if readers():
        for reader in readers():
                try:
                    connection = reader.createConnection()
                    connection.connect()
                    string = toHexString(connection.getATR())
                    string = string.split(" ")
                    for i,i_ in enumerate(string[:]):
                        string[i] = int(i_,16)
                    print(reader,": ATR:")
                    print("Base-10: ",string)
                    print("Hex: ",toHexString(connection.getATR()))
                    print("string: ",[chr(i) for i in string])
                except NoCardException:
                    print(reader, "no card inserted")
                except CardConnectionException as e:
                    print(reader, "bad connection")
                    print(e)
                input("press Enter to continue")
    else:
        print("No Readers availible")