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
    return switch.get(i, "Invalid day of week")