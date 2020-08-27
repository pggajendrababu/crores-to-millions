"""
1 million = 1000 x thousands = 6 zeros = 10_00_000 = 10 lakhs
1 billion = 1000 x millions = 9 zeros = 1_00_00_00_000  = 100 crores
1 trillion = 1000 x billions = 12 zeros
1 quadrillion = 1000 x trillions = 15 zeros
1 quintillion = 1000 x quadrillions = 18 zeros
------------------------------------------------------------------------------------
1 lakh = 100 x thousands = 5 zeros
10 lakhs = 1000 x thousands = 6 zeros
1 crore = 100 lakhs = 7 zeros
100 crores = 1 billion = 9 zeros
"""

us_dollars_current_value = 1
indian_rupees_current_value = 70

"""
convertion from dollars to rupees
----------------------------------------------------------
if case
------------- 
us_doller_current_value = 1
indian_rupees_current_value = 70

70 indian rupees
----------------------------        x   500 dollars = ?
1 us dollar
-----------------------------------------------------------------------------------------------
else case
----------------
us_dollar_current_value = 50
indian_rupees_current_value = 1

1 indian rupees
--------------------------    x      500 dollars = ?
50 us dollars

"""

def millions_to_crores(millions) :
    dollars = millions * 10_00_000
    if  us_dollars_current_value <= indian_rupees_current_value :
        rupees = indian_rupees_current_value * dollars
        #print('rupees = ', rupees)
    else :
        rupees = dollars/us_dollars_current_value
    crores = rupees/1_00_00_000
    return crores

"""
convertion from dollars to rupees
----------------------------------------------------------
if case
------------- 
us_doller_current_value = 1
indian_rupees_current_value = 70

70 indian rupees
----------------------------        x   500 dollars = ?
1 us dollar
-----------------------------------------------------------------------------------------------
else case
----------------
us_dollar_current_value = 50
indian_rupees_current_value = 1

1 indian rupees
--------------------------    x      500 dollars = ?
50 us dollars

"""        
    
def billions_to_crores(billions) :
    millions = billions * 1000
    dollars = millions *  10_00_000
    if  us_dollars_current_value <= indian_rupees_current_value :
        rupees = indian_rupees_current_value * dollars
    else :
        rupees = dollars/us_dollars_current_value 
    crores = rupees/1_00_00_000 
    return crores      

"""
convertion from rupees to dollars
----------------------------------------------------------
if case
------------- 
us_doller_current_value = 1
indian_rupees_current_value = 70

1 us dollar
----------------------------        x   600 indian rupees = ?
70 indian rupees
-----------------------------------------------------------------------------------------------
else case
----------------
us_dollar_current_value = 50
indian_rupees_current_value = 1

50 us dollars
--------------------------    x      600 indian rupees = ?
1 indian rupees

"""    

def crores_to_millions(crores) :
    rupees = crores * 1_00_00_000
    if us_dollars_current_value <= indian_rupees_current_value :
        dollars =  rupees/indian_rupees_current_value 
    else :
        dollars = us_dollars_current_value * rupees
    millions = dollars/10_00_000
    return millions

"""
convertion from rupees to dollars
----------------------------------------------------------
if case
------------- 
us_doller_current_value = 1
indian_rupees_current_value = 70

1 us dollar
----------------------------        x   600 indian rupees = ?
70 indian rupees
-----------------------------------------------------------------------------------------------
else case
----------------
us_dollar_current_value = 50
indian_rupees_current_value = 1

50 us dollars
--------------------------    x      600 indian rupees = ?
1 indian rupees

"""    
        

def crores_to_billions(crores) :
    rupees = crores * 1_00_00_000
    if us_dollars_current_value <= indian_rupees_current_value :
        dollars =  rupees/indian_rupees_current_value 
    else :
        dollars = us_dollars_current_value  * rupees
    millions = dollars/10_00_000
    billions = millions/1_000
    return billions
    
"""
def start( ) :
    x1 = 6.89
    y1 = millions_to_crores(x1)    

    x2 = 5.63
    y2 = billions_to_crores(x2)

    m1 = 48.23
    n1 = crores_to_millions(m1)

    m2 = 39410
    n2 = crores_to_billions(m2)

    print(x1, 'millions US dollars = ', y1, "crores Indian rupees") 
    print(x2, 'billions US dollars = ', y2, "crores Indian rupees")  
    print('-' * 50)
    print(m1, "crores Indian rupees = ", n1, "millions US dollars")
    print(m2, "crores Indian rupees = ", n2, "billions US dollars")

#start( )
"""


"""
note1 block will not be executed when this module 
(converters.py) is imported.
notr1 block will be executed only when we run this module
directlly. Instead of using start( ), we can write like note1.
"""

if __name__ ==  "__main__" : # note1
    
    x1 = 6.89
    y1 = millions_to_crores(x1)    

    x2 = 5.63
    y2 = billions_to_crores(x2)

    m1 = 48.23
    n1 = crores_to_millions(m1)

    m2 = 39410
    n2 = crores_to_billions(m2)

    print(x1, 'millions US dollars = ', y1, "crores Indian rupees") 
    print(x2, 'billions US dollars = ', y2, "crores Indian rupees")  
    print('-' * 50)
    print(m1, "crores Indian rupees = ", n1, "millions US dollars")
    print(m2, "crores Indian rupees = ", n2, "billions US dollars")

