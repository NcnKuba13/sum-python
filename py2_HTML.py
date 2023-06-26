import datetime

def main():
    # Czas potrzebny do odpowiedniego formatowania pliku .html z raportem
    today = datetime.date.today()
    today = today.strftime("%d_%m_%Y")
    time = datetime.datetime.now()
    time = time.strftime("%H_%M")

    try:
        file = open(f".\\raporty\\{today}_{time}_raport.html", "w")
    except IOError:
        print("Błąd otwarcia pliku! - raport")
        return -1

    def rows():
        for d in range(1, 17):
            try:
                file1 = open(f"{d}IN.txt", "r")
                n = file1.readline()
                S = file1.readline()
            except IOError:
                print("Błąd otwarcia pliku! - IN")
                return -1
            file1.close()
            try:
                file2 = open(f"{d}OUT.txt", "r")
                C = file2.read()
            except IOError:
                print("Błąd otwarcia pliku! - OUT")
                return -1
            file2.close()

            file.write(f'''<tr>
            <td style="text-align: center; ">{n}</td>
            <td style="text-align: center; ">{S}</td>
            <td style="text-align: center; ">{C}</td>
            </tr>
            ''')

    htmlPage1 = f'''<html>
    <head>
    <title>{today}_{time}_raport</title>
    <meta charset="windows-1250">
    <body style="background-color:powderblue;">
    <style>
    table {{
        font-family: amasis mt pro medium;
        border-collapse: collapse;
        width: 60%;
    }}

    td, th {{
        border: 1px solid #000000;
        text-align: left;
        padding: 8px;
    }}

    tr:nth-child(even) {{
        background-color:#FFDEAD;
    }}
    </style>
    </head>
    <body>

    <center><h2>SUMA CIĄGU JEDYNKOWEGO</h2></center>

    <table align="center">
        <tr>
            <th style="text-align: center; background-color:#32CD32">Długość ciągu (n)</th>
            <th style="text-align: center; background-color:#32CD32">Suma ciągu (S)</th>
            <th style="text-align: center; background-color:#32CD32">Przykład ciągu</th>
        </tr>
    '''

    htmlPage2 = '''
    </table>

    </body>
    </html>
    '''

    file.write(htmlPage1)
    rows()
    file.write(htmlPage2)


if __name__ == '__main__':
    main()
