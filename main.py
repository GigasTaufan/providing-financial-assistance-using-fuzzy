import csv

#fungsi untuk menentukan apakah gaji termasuk golongan rendah
def gaji_rendah(x):
    start = 0.219
    max = 0.507
    if x <= start :
        rendah = 1
    elif x > start and x <= max :
        rendah = (x-max)/(start-max)
    else:
        rendah = 0
    return rendah

#fungsi untuk menentukan apakah gaji termasuk golongan menengah
def gaji_menengah(x):
    min = 0.423
    max = 0.78
    start = 0.6
    end = 0.747
    if x >= start and x <= end :
        menengah = 1
    elif x < start and x >= min :
        menengah = (x-min)/(start-min)
    elif x > end and x < max :
        menengah = (x-end)/(max-end)
    else:
        menengah = 0
    return menengah

#fungsi untuk menentukan apakah gaji termasuk golongan tinggi
def gaji_tinggi(x):
    min = 0.765
    start = 0.793
    if x >= start :
        tinggi = 1
    elif x < start and x >= min :
        tinggi =  tinggi = (x-min)/(start-min)
    else:
        tinggi = 0
    return tinggi

#fungsi untuk menentukan apakah hutang termasuk golongan rendah
def hutang_rendah(x):
    start = 10
    max = 27.166
    if x <= start :
        rendah = 1
    elif x > start and x <= max :
        rendah = (x-max)/(start-max)
    else:
        rendah = 0
    return rendah

#fungsi untuk menentukan apakah hutang termasuk golongan menengah
def hutang_menengah(x):
    min = 23.644
    max = 63.226
    start = 29.854
    end = 49.628
    if x >= start and x <= end :
        menengah = 1
    elif x < start and x >= min :
        menengah = (x-min)/(start-min)
    elif x > end and x < max :
        menengah = (x-end)/(max-end)
    else:
        menengah = 0
    return menengah

#fungsi untuk menentukan apakah hutang termasuk golongan tinggi
def hutang_tinggi(x):
    min = 55.54
    start = 68.12
    if x >= start :
        tinggi = 1
    elif x < start and x >= min :
        tinggi =  tinggi = (x-min)/(start-min)
    else:
        tinggi = 0
    return tinggi

short = []

def getSugeno(elem):
    return elem['sugeno']

def hasilFile(result):
    with open('output.csv', 'w', newline='') as csvFile:
        for i in result:
            csvFile.write(i)
            csvFile.write('\n')
    csvFile.close()

if __name__ == '__main__':
    data = []
    with open('DataTugas2.csv') as csvfile:
        spamreader = csv.reader(csvfile)
        next(spamreader, None)
        for row in spamreader:
            data.append([int(row[0]), float(row[1]), float(row[2])])
			
            #inference terima
            terima1 = min(gaji_tinggi(float(row[1])), hutang_tinggi(float(row[2])))
            terima2 = min(gaji_menengah(float(row[1])), hutang_tinggi(float(row[2])))
            terima3 = min(gaji_rendah(float(row[1])), hutang_tinggi(float(row[2])))
            terima4 = min(gaji_rendah(float(row[1])), hutang_menengah(float(row[2])))

            #inference pertimbangkan
            pertimbangkan1 = min(gaji_tinggi(float(row[1])), hutang_menengah(float(row[2])))
            pertimbangkan2 = min(gaji_menengah(float(row[1])), hutang_menengah(float(row[2])))
            pertimbangkan3 = min(gaji_rendah(float(row[1])), hutang_rendah(float(row[2])))

            #inference tolak
            tolak1 = min(gaji_tinggi(float(row[1])), hutang_rendah(float(row[2])))
            tolak2 = min(gaji_menengah(float(row[1])), hutang_rendah(float(row[2])))

            #defuzzification menentukan nilai max
            max_terima = max(terima1, terima2, terima3, terima4)
            max_pertimbangkan = max(pertimbangkan1, pertimbangkan2, pertimbangkan3)
            max_tolak = max(tolak1, tolak2)

            #rumus sugeno
            sugeno = ((max_tolak*20) + (max_pertimbangkan*30) + (max_terima*50))/(max_terima + max_pertimbangkan + max_tolak)
            urutan = {
                'no': row[0],
                'pendapatan':row[1],
                'hutang':row[2],
                'sugeno':sugeno,
            }
            short.append(urutan)

        # print(shortingan)
        sorted = sorted(short, key=getSugeno, reverse=True)

        for i in range(20):
            print(sorted[i])

        result = []
        i = 0
        for i in range(0,20):
            result.append(sorted[i]['no'])
        print(result)

    hasilFile(result)
	