import numpy as np
import matplotlib.pyplot as plt

def plot(fosEmsRate, defEmsRate):

    iniFossil = 6.88
    iniDef = 1.3
    goalConc = 938
    upperConc = 953
    lowerConc = 923

    iniFromFossil = 5.9168
    iniToFossil = 8.3936

    iniFromDefor = 0.637
    iniToDef = 2.015

    iniConc = 769
    totConc = 769

    fromFossil = 5.9168
    toFossil = 8.3936

    fromDef = 0.637
    toDef = 2.01

    ind = 2000
    iniAbsRate = 0.012 * ((769 - 677))
    absRate = iniAbsRate

    yTotEms = []
    xYears = []

    yTotConc = []
    yAbsRate = []


    while ind <= 2100:

        fosEmsRate = fromFossil - 1;
        while(fosEmsRate < fromFossil or fosEmsRate > toFossil):
            print("Please enter fossil fuel emission rate in GTc/year in the range(", fromFossil, ", ", toFossil, ") for year", ind, ": ")
            fosEmsRate = float(input())

        defEmsRate = fromDef - 1;
        while(defEmsRate < fromDef or defEmsRate > toDef):
            print("Please enter deforestation emission rate in GTc/year in the range(", fromDef, ", ", toDef, ") for year", ind, ": ")
            defEmsRate = float(input())

        totEmsRate = fosEmsRate + defEmsRate

        for year in range(ind, ind + 10):
            absRate = 0.012 * ((totConc - 677))
            totConc = totConc + totEmsRate - absRate
            yTotConc.append(totConc)
            yAbsRate.append(absRate)
            yTotEms.append(totEmsRate)
            xYears.append(year)


        X = np.arange(totConc)

        plt.fill_betweenx(X,1,color='orange')
        plt.hlines(y=938,xmin=0,xmax=1,color='green')
        plt.hlines(y=923,xmin=0,xmax=1,color='red')
        plt.hlines(y=953,xmin=0,xmax=1,color='red')
        plt.ylim(600,1200)
        plt.xticks([])
        plt.savefig("output0.jpg")
        plt.show()


        plt.plot(xYears, yTotConc)
        plt.xlim(2000,2100)
        plt.ylim(0,1400)
        plt.ylabel("Total Concentration of CO2")
        plt.xlabel("Years")
        plt.title("Total Concentration over the Years")
        plt.savefig("output1.jpg")
        plt.show()

        plt.plot(xYears, yTotEms);
        plt.xlim(2000,2100)
        plt.ylim(0,15)
        plt.ylabel("Total Emission Rate of CO2")
        plt.xlabel("Years")
        plt.title("Total Emission Rate over the Years")
        plt.savefig("output2.jpg")
        plt.show()

        plt.plot(xYears, yAbsRate)
        plt.xlim(2000,2100)
        plt.ylim(0,15)
        plt.ylabel("Total Absorption Rate of CO2")
        plt.xlabel("Years")
        plt.title("Total Absorption Rate over the Years")
        plt.savefig("output3.jpg")
        plt.show()

        fromFossil = .86 * fosEmsRate
        toFossil = 1.22 * fosEmsRate

        fromDef = .49 * defEmsRate
        toDef = 1.55 * defEmsRate

        ind = ind + 10
