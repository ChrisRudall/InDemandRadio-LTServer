import telnetlib
import re
HOST = "localhost"
PORT = 1234

tn = telnetlib.Telnet(HOST,PORT)
tn.write("Frisky_Radio_Beta.metadata".encode('ascii') + b"\n")
tn.expect([r"--- 1 ---"], 5)
tn.expect([r"title=\""], 5)
r = tn.expect([r"\""], 5)

print(r[2].decode('ascii')[:-1])
tn.close()
