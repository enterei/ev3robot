def targetvalue(i):
    switch={
        0: 'No color',
        1: 'Black',
        2:'Blue',
        3: 'Green',
        4: 'Yellow',
        5: 'Red',
        6: 'White',
        7: 'Brown'
    }
    return switch.get(i, i)
def targetMode(i):
    switch={
        1: 'COL-REFLECT', #Reflected light. Red LED on.
        2: 'COL-AMBIENT',#Ambient light. Blue LEDs on.
        3: 'COL-COLOR',#Color. All LEDs rapidly cycling, appears white.
        4: 'REF-RAW',#Raw reflected. Red LED on
        5: 'RGB-RAW',#Raw Color Components. All LEDs rapidly cycling, appears white.


    }
    return switch.get(i,i)