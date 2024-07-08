## Masses of Airframe Estimates
## Jaynie Tercovich 7/3/2024
## These are very ROUGH estimates since epoxy weight is not always guaranteed to be the same. Cuts also won't always be perfect, and sanding can vary..
## Have Kate weigh the body tube in grams and change initial weight (Weight_CF_OG) to that value. Do this for every body tube, average them, and change needed values
## All structural values taken from FibreGlast

############################################################################################################

## Imports
import numpy as np
import math as mth

############################################################################################################

## Constants
# Carbon Fiber (3k plain weave)
Weight_CF = 0.00027  #lb/sqin
C_CF = 19.5  #in
r_CF = 3  #in
R_CF = 3.1  #in
L_CF = 50  #in
Weight_CF_OG = 3.39  #lbs

# Fiberglass (6781 S2-Glass)
Weight_FG = 0.000409915  #lb/sqin
C_FG = 19.5  #in
r_FG = 3  #in
R_FG = 3.1  #in
L_FG = 23  #in
Weight_FG_OG = 1.7  #lbs

# Coupler (Fiber Glass)
Weight_Coup = 0.000409915  #lb/sqin
#C_Coup = 

############################################################################################################

Structure = input('What structure is being made? (CF Tube, FG Tube, Coupler)')

if Structure == 'CF Tube':

    n = int(input('How many layers are being layed up?'))
    Fabric_tot = Weight_CF * C_CF * L_CF * n  #lbs, total weight of fabric without epoxy (no cuts)
    Epoxy_estimate = Weight_CF_OG - Fabric_tot  #lbs, assuming 3.39 pounds (~1537 grams) as average weight of body tube before any cuts.. This is what I remember weighing, could be wrong.

    h = int(float(input('How many total inches are being cut off of the body tube?')))
    A_c = 2*mth.pi*h*(R_CF+r_CF) + 2*mth.pi*(R_CF**2-r_CF**2)  #sqin, area of the body tube that was cut off 

    Fabric_c = Weight_CF * n * A_c  #lbs, weight of fabric cut off 
    Sanding = 0.077 #lbs, total amount of CF sanded off
    Weight_BT = Weight_CF_OG - Fabric_c - Sanding  #lbs, total weight of body tube after cuts and sanding

    print(Weight_BT)

elif Structure == 'FG Tube':

    n = int(input('How many layers are being layed up?'))
    Fabric_tot = Weight_FG * C_FG * L_FG * n  #lbs, total weight of fabric without epoxy (no cuts)
    Epoxy_estimate = Weight_FG_OG - Fabric_tot  #lbs, assuming 3.39 pounds (~1537 grams) as average weight of body tube before any cuts.. This is what I remember weighing, could be wrong.

    h = int(float(input('How many total inches are being cut off of the body tube?')))
    A_c = 2*mth.pi*h*(R_FG+r_FG) + 2*mth.pi*(R_FG**2-r_FG**2)  #sqin, area of the body tube that was cut off  

    Fabric_c = Weight_FG * n * A_c  #lbs, weight of fabric cut off 
    Sanding = 0.035  #lbs, more than CF because an entire layer is being sanded
    Weight_BT = Weight_FG_OG - Fabric_c - Sanding  #lbs, total weight of body tube after cuts and sanding

    print(Weight_BT)



