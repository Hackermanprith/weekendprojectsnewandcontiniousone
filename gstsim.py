from tabulate import tabulate

base = [20]
profitoftheseller = []
totalafterprofit = []
tax = []
totaltobepaid = []

class GstSim:
    def calcprofit(percentforprofit):
        
        profitamount = (percentforprofit / 100) * base[-1] # base[-1] is the last element in the list and then calculating 10% of the last value
        
        y = round(profitamount, 2) #rounding the no to two decimal places
        
        profitoftheseller.append(y) #appending the profit to the list
        
        uploadingtotalafterprofit = base[-1] + y
        z = round(uploadingtotalafterprofit, 2)
        
        totalafterprofit.append(z)
        return profitamount
    
    def calctax():
        taxamount = (20 / 100) * totalafterprofit[-1]
        x = round(taxamount, 2)
        numofele = len(tax)
        if numofele == 0:
            tax.append(x)
        else:
            taxtobegiven = x - tax[-1]
            tax.append(taxtobegiven)
        #doing the stupdation of the tax
        totalrev = totalafterprofit[-1] + tax[-1]
        a = round(totalrev, 2)
        totaltobepaid.append(a)
        base.append(a)
        return taxamount
    
if __name__ == "__main__":
    #basic_ammount = float(input("Enter the basic ammount: "))
    #base.append(basic_ammount)
    #taxpercent = int(input("Enter the tax percent: "))
    #percentofprofit = int(input("Enter the percent of profit: "))
    #num = int(input("After how many hands are you getting the product: "))
    #print("Calculating")
    for i in range(4):
        GstSim.calcprofit(10)
        GstSim.calctax()
        print(f"After {i} hands the total is {totaltobepaid[-1]} and goverment gets {tax[-1]}")