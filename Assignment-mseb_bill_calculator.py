#!/usr/bin/env python
# coding: utf-8

# In[7]:


#MSEB electricity bill calculator
fixed_Charges=90
def calcElectricityBill(units):
    units_range=[100,300,500,1000]
    energy_charge_multiplier=[3.05,6.95,9.90,11.50,12.50]
    energy_charge_formula=[3.05*100,6.95*200,9.90*200,11.50*500]
    FAC_multiplier=[0.160,0.270,0.340,0.380,0.400]
    FAC_formula=[0.160*100,0.270*200,0.340*200,0.400*500]
    electricity_duty_Percentage=16
    print("No. of units:",units)
    print("Fixed charges:",fixed_Charges)
    #Calculate energy_charge
    if (units<=units_range[0]):
        energy_charge=energy_charge_multiplier[0]*units
        print("Energy charges:",energy_charge)
    elif (units>units_range[0] and units<=units_range[1]):
        energy_charge=energy_charge_formula[0]+(energy_charge_multiplier[1]*(units-units_range[0]))
        print("Energy charges:",energy_charge)
    elif (units>units_range[1] and units<=units_range[2]):
        energy_charge=energy_charge_formula[0]+energy_charge_formula[1]+(energy_charge_multiplier[2]*(units-units_range[1]))
        print("Energy charges:",energy_charge)
    elif (units>units_range[2] and units<=units_range[3]):
        energy_charge=energy_charge_formula[0]+energy_charge_formula[1]+energy_charge_formula[2]+(energy_charge_multiplier[3]*(units-units_range[2]))
        print("Energy charges:",energy_charge)
    elif (units>units_range[3]):
        energy_charge=energy_charge_formula[0]+energy_charge_formula[1]+energy_charge_formula[2]+energy_charge_formula[3]+(energy_charge_multiplier[4]*(units-units_range[3]))
        print("Energy charges:",energy_charge)
    Wheeling_charges=1.28*units
    print("Wheeling charges:",Wheeling_charges)
   # calulate fuel_adj_charge
    if (units<=units_range[0]):
        fuel_adj_charge=FAC_multiplier[0]*units
        print("FAC:",fuel_adj_charge)
    elif (units>units_range[0] and units<=units_range[1]):
        fuel_adj_charge=FAC_formula[0]+(FAC_multiplier[1]*(units-units_range[0]))
        print("FAC:",fuel_adj_charge)
    elif (units>units_range[1] and units<=units_range[2]):
        fuel_adj_charge=FAC_formula[0]+FAC_formula[1]+(FAC_multiplier[2]*(units-units_range[1]))
        print("FAC:",fuel_adj_charge)
    elif (units>units_range[2] and units<=units_range[3]):
        fuel_adj_charge=FAC_formula[0]+FAC_formula[1]+FAC_formula[2]+(FAC_multiplier[3]*(units-units_range[2]))
        print("FAC:",fuel_adj_charge)
    elif (units>units_range[3]):
        fuel_adj_charge=FAC_formula[0]+FAC_formula[1]+FAC_formula[2]+FAC_formula[3]+FAC_multiplier[4]*(units-units_range[3])
        print("FAC:",fuel_adj_charge)
    electricity_duty=electricity_duty_Percentage*(fixed_Charges+energy_charge+Wheeling_charges+fuel_adj_charge)/100
    print("Electricity duty:",electricity_duty)
    total_bill=fixed_Charges+energy_charge+Wheeling_charges+fuel_adj_charge+electricity_duty
    print("Total current bill:"+str(total_bill))

units=135
calcElectricityBill(units)


# In[ ]:





# In[ ]:





# In[ ]:




