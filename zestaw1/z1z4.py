# Napisać program, który dynamicznie wyświetla „pasek postępu” o zadanej długości. Powinno to wyglądać tak
# (kolejne etapy):
# |--------------------------------------------------| 0%
# |============================----------------------| 56%
# |==================================================| 100%

import sys

n = int(sys.argv[1])
if n < 0 or n > 100:
    print("Give the number between 0 and 100")
    exit(1)

print("|", "-"*100, "| 0%", sep="")
print("|", "="*n, "-"*(100-n), "| ", n, "%", sep="")
print("|", "="*100, "| 100%", sep="")

