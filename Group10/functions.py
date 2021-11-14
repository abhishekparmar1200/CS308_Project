

def solve(emsList, absList):


    #The CO2 concentration values(PPMV) of the period 1970-2100 at an interval of every 10 years taken from IPCC website
    originalConc = [325, 337, 353, 369, 388, 412,437, 463, 488, 509, 525, 537, 545, 549] 
    #Converting the values from PPMV to GtC
    for i in range(0, len(originalConc)):
        originalConc[i] = originalConc[i] * 2.13
    
    years = []
    #year list stores the corresponding year values
    for year in range(1970, 2110, 10):
        years.append(year)
    
    totConc = originalConc[3] #to store the total concentration of CO2 in atmosphere. Initially stores the CO2 conc value for year 2000
    totConcList = [] #List to store the total conc of CO2 value over the years
    yearList = [] #list to store years till the current user input
    emsListGraph = [] #list to store the emission rate values which the user provides
    absListGraph = [] #list to store the absorption rate values which the user provides
    year = 2001
    
    #calculating total concentration values for the emission and apsorption values over the current time period
    for ind in range(0, len(emsList)):
        for year1 in range(year, year + 5):
            totConc = totConc + emsList[ind] - absList[ind]
            totConcList.append(totConc)
            emsListGraph.append(emsList[ind])
            absListGraph.append(absList[ind])
            yearList.append(year1)
            
        year = year + 5
    return [yearList, emsListGraph, yearList, absListGraph, years, originalConc, yearList, totConcList]
    # cur = int((year - 1970)/10);
    # lowerLim = int(originalConc[cur] - 200)
    # upperLim = int(originalConc[cur] + 200)
    # X = np.arange(totConc)
    # plt.fill_betweenx(X,1,color='orange')
    # plt.hlines(originalConc[cur],xmin=0,xmax=1,color='red')
    # plt.ylabel(X)
    # plt.ylim(lowerLim, upperLim)
    # plt.xticks([])
    # plt.show()
    
    # plt.plot(yearList, emsListGraph, color = 'blue')
    # plt.plot(yearList, absListGraph, color = 'green')
    # plt.xlim(2000,2100)
    # plt.ylim(0,17)
    # plt.ylabel("Total Emission Rate of CO2")
    # plt.xlabel("Years")
    # plt.title("Total Emission Rate over the Years")
    # plt.show()
    
    # plt.plot(years, originalConc, color = 'red')
    # plt.plot(yearList, totConcList)
    # plt.xlim(1970,2100)
    # plt.ylim(0,1400)
    # plt.ylabel("Total Concentration of CO2")
    # plt.xlabel("Years")
    # plt.title("Total Concentration over the Years")
    # plt.show()
    


# emsList = []
# absList = []

# for year in range(2000,2100, 5):
#     print("Please enter emission rate for year", year, ": ")
#     ems = float(input())
#     print("Please enter absorption rate for year", year, ": ")
#     abs = float(input())
#     emsList.append(ems)
#     absList.append(abs)
#     solve(emsList, absList)
    
