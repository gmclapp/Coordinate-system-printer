import csv

def interpolate(x1,y1,x2,y2,x):
    '''given data points x1,y1 and x2,y2 this function finds a y given an x
    between x1 and x2 and linearly interpolating.'''
    try:
        y = ((y2-y1)/(x2-x1))*(x-x1) + y1
    except TypeError:
        y = y1
        
    return(y)

def vlookup_interpolate(rfile, index, search_col, result_col):
    ''' The file is where the data is stored.
    index is the item to search rows for.
    search_col is the column in which the index should be searched for.
    result_col should be the column from which the result should be
    extracted.'''

    index = float(index)
    search_col = int(search_col)
    result_col = int(result_col)
    
    RDR = csv.reader(rfile, dialect = 'excel')
    pos_diff = 1000 
    neg_diff = -1000

    x1 = None
    y1 = None
    x2 = None
    y2 = None

    for row in RDR:
        ''' Search for the rows just smaller and just larger than the search
        term. Calculate the difference between the x value in a given row
        and the search term. Keep the rows that result in the smallest
        positive difference and the smallest negative difference.'''
        
        try:
            diff = index - float(row[search_col])
            
        except ValueError:
            if row[search_col] == "Inf":
                diff = math.inf
                
            #print("Header?")
            continue

        if diff < pos_diff and diff > 0:
            x1 = float(row[search_col])
            y1 = float(row[result_col])
            pos_diff = diff

        elif diff > neg_diff and diff < 0:
            x2 = float(row[search_col])
            y2 = float(row[result_col])
            neg_diff = diff
            
        elif diff == 0:
            x1 = float(row[search_col])
            y1 = float(row[result_col])
            x2 = None
            y2 = None

    return (x1, y1, x2, y2)
    # Return the x,y pairs of the search column and result column just
    # above and below the desired x value.

def vlookup(rfile, index, search_col, result_col):
    ''' The file is where the data is stored.
    index is the item to search rows for.
    search_col is the column in which the index should be searched for.
    result_col should be the column from which the result should be
    extracted.'''
    
    RDR = csv.reader(rfile, dialect = 'excel')

    y=None
    
    for row in RDR:
        try:
            if index == int(row[search_col]):
                y = row[result_col]
            else:
                pass
        except ValueError:
            continue
    return(y)

def fetch_row(rfile, index, search_col):
    '''The file is where the data is stored.
    index is the item to search rows for.
    search_col is the column in which the index should be searched for.'''
    RDR = csv.reader(rfile, dialect = 'excel')
    
    y=None
    
    for row in RDR:
        try:
            if index == int(row[search_col]):
                y = row
            else:
                pass
        except ValueError:
            continue
    return(y)
    
def list_headers(rfile, r_c):
    ''' The argument should indicate whether the headers are in the
    first row or in the first column. pass 'r' for row, 'c' for
    column.'''

    headers = []
    RDR = csv.reader(rfile, dialect = 'excel')
    if r_c.lower() == 'r':
        for row in RDR:
            print(row[0])
            headers.append(row[0])
                  
    elif r_c.lower() == 'c':
        for element in RDR[0]:
            print(element)
            headers.append(row[0])

    return(headers)
