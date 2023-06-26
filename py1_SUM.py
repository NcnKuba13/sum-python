import math

def resuelto(n, S, d):
    try:
        file = open(f"{d}OUT.txt", "w")
    except IOError:
        print("Bład zapisu pliku!")
        exit()

    if n not in range(1, 10000) or S not in range(-50000000, 50000000):
        print("Podane parametry nie należą do zadanych przedziałów!")
        file.write("Parametry spoza przedziałów!")
        return

    if abs(S) % 2 != (n * (n - 1) / 2) % 2 or S > (n * (n - 1) / 2) or S < (-n * (n - 1) / 2):
        print("Nie istnieje!")
        file.write("Nie istnieje!")
        return

    print("0")
    a = 0

    file.write("0\n")

    for i in range(n - 1, 0, -1):
        if (S + i) <= (i * (i - 1) / 2):
            a -= 1
            S += i
        else:
            a += 1
            S -= i

        print("%d" % a)
        file.write("%d\n" % a)

    file.close()


def main():
    r = 1

    for d in range(1, 17):
        try:
            file = open(f"{d}IN.txt")
        except IOError:
            print("Bład zapisu pliku!")
            exit()

        try:
            n = int(file.readline())
            S = int(file.readline())
        except ValueError:
            print("Błędne dane!")
            file = open(f"{d}OUT.txt", "w")
            file.write("Błędne dane!")
            file.close()
            continue
        resuelto(n, S, d)


main()