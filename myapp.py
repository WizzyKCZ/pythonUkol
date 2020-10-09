import random
end = 0
skore = 0
n = 50
x = 0
print("HRA - VYSSI, NIZSI\n")
while end != 1:
    inp = input("Bude cislo vyssi(1) nebo nizsi(0), nyni je cislo %d: " %n)
    x = random.randint(0, 100)
    if (int(inp) == 1):
        if (x < n):
            print("Prohral jsi ty nulo, cislo bylo: %d\n" %x)
            end = 1
        else:
            print("Dobreeeeeee, cislo bylo: %d" %x)
            skore += 1
            n = x
    elif (int(inp) == 0):
        if (x > n):
            print("Prohral jsi ty nulo, cislo bylo: %d\n" %x)
            end = 1
        else:
            print("Dobreeeeeee, cislo bylo: %d" %x)
            skore += 1
            n = x
    else:
        print("Ty si hnup.\n")
print("Tvoje skore je: %d" %skore)