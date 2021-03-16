
'''
    DS2001
    Angela Fee 
    Problem 7 - COVID Vaccinations 
    March 2021    
'''
import csv 
import matplotlib.pyplot as plt 

def read_csv(filename):
    # useful function taken from DS 2000 Lecture 
    ''' Function: read_csv
        Parameters: filename, a string
        Returns: 2d list of strings, the contents of the file
    '''
    data = []
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter = ",")
        next(csv_reader)
        for row in csv_reader:
            data.append(row)
    return data

def get_col(table, col, cast = str):
    # useful function taken from DS 2000 Lecture
    ''' Function: get_col
        Parameters: table, a 2d list of anything, and col an int
        Returns: all the data for that column, as a list
    '''
    col_data = []
    for row in table:
        col_data.append(cast(row[col]))
    return col_data


def population():
    '''
    Parameters: Does not take in anything 
    -------
    Function: create a dictionary with the country code as keys 
    and the population as values 
    ------- 
    Returns: Dictionary created 
    -------
    '''
    FILE = "worldpop.csv"
    data = read_csv(FILE)  # sends file to be processed into data in read csv
    codes = get_col(data, 1) # isolates the column of country codes into list
    pop = get_col(data, 2) # isolates the column of population into list
    
    pop_dict = {}
    for i in range(len(codes)):
        if codes[i] in pop_dict: # if key is already in dict: update value 
            pop_dict[codes[i]].append(pop[i]) # appends new value to key 
        else:
            pop_dict[codes[i]] = [pop[i]] # otherwise add key, current value 
    return pop_dict # returns dictionary 

def country():
    '''
    Parameters: Does not take in anything 
    -------
    Function: create a dictionary with the country as keys 
    and the country code as values 
    ------- 
    Returns: Dictionary created 
    -------
    '''
    FILE = "worldpop.csv"
    data = read_csv(FILE)  # sends file to be processed into data in read csv
    codes = get_col(data, 1) # isolates the column of country codes into list
    country = get_col(data, 0) # isolates the column of population into list
    
    code_dict = {}
    for i in range(len(country)):
        if country[i] in code_dict: # if key is already in dict: update value 
            code_dict[country[i]].append(codes[i]) # appends new value to key 
        else:
            code_dict[country[i]] = [codes[i]] # otherwise add key, current value 
    return code_dict # returns dictionary 

def vac_by_country(code_str):
    '''
    Parameters: Takes in the country code as string  
    -------
    Function: create a dictionary with the country code as keys 
    and the [date, total vaccinations] as value 
    ------- 
    Returns: List of lists in which list 1 = dates list 2 = vaccines by day 
    -------
    '''
    FILE = "covid-vaccinations.csv"
    code_dates = [] # initialize list for dates corresponding to code  
    code_vacc = []  # initialize list for vaccines corresponding to code 
    data = read_csv(FILE)  # sends file to be processed into data in read csv
    codes = get_col(data, 1) # isolates the column of country codes into list
    dates = get_col(data, 2) # isolates the column of dates into list
    vaccine = get_col(data, 3) # isolates the column of total vaccines into list
    
    for i in range(len(codes)):
        if code_str == codes[i]: # if code equals code in col cell 
              code_dates.append(dates[i]) # append date at that position
              code_vacc.append(vaccine[i]) # append vacc # at that position 
        lst = [code_dates, code_vacc] # massive list of lists
    return lst # returns list of lists 

def cumulative(lst1): 
     '''
    Parameters: List of Strings 
    --------
    Function: Converts list elements to integers; builds up cumulative count 
    by summing list elements
    -------
    Returns: Returns list of integers with cumulative counts  
    '''
     # initialie total variable for summation of list elements in iterations
     total = 0 
     # initialize list to keep track of cumulative change in value 
     final_lst = []
    
     # for loop to build cumulative count of lst, convert to int 
     for i in range(len(lst1)):
        current = int(lst1[i]) # isolates current vacc as int
        total = total + current; # cumulative amt 
        final_lst.append(total) # add to growing cumulative count of vaccines 
     return final_lst

def vac_rate(cntry_str):
    '''
    Parameters: String Input: Country Name or Country Code 
    --------
    Function: Find vaccinations per 1000 people for specific country; 
    Produce a graph of the cumulative total vaccinations 
    over time
    -------
    Returns: the number of vaccinations per 1000 people as a number 
    rounded to the nearest decimal. 
    '''
    code_str = "" # initialized code string
    # Determine if valid country code 
    world_dict = population() # the dictionary 
    cntry_dict = country() # the dictionary 
    cn_codes = world_dict.keys() # extracts list of keys from dictionary
    
    # Run through dictionaries and identify corresponding population 
    for i in range(len(cn_codes)):
        if cntry_str in world_dict:  
            code_str = cntry_str # code as str 
            pop = (world_dict[code_str]) # extracts population at specific cde 
            pop = int(pop[0]) # list -> str -> int 
        elif cntry_str in cntry_dict: 
            code_str = (cntry_dict[cntry_str])[0] # code as str
            pop = (world_dict[code_str]) # extracts population at specific cde 
            pop = int(pop[0]) # list -> str -> int
        else: 
            "invalid code entered"
            break
    
    code_lst = vac_by_country(code_str) # giant list of lists for code
    vacc_day = code_lst[1] # isolate list of vaccines by day
    dates = code_lst[0] # isolate dates
    
    # initialize lists for graphing 
    lst_y = cumulative(vacc_day) 
    
    # plotting 
    plt.plot(dates, lst_y)
    plt.gcf().autofmt_xdate()
    
    # plotting labels 
    # determine country as specified code 
    plt.title('Cumulative Count of Vaccine Dose for {}'.format(code_str))
    plt.xlabel('Date')
    plt.ylabel('Number of COVID Doses Given')
    plt.show()    
    
    total_vacc = lst_y[-1] # final list element 
    avg_vacc = (total_vacc / pop) * 1000  # vaccinations per 1000 ppl
    print(round(avg_vacc), "vaccinations per 1000 people")
        

if __name__ == "__main__":
    print("Test Run for Lebanon: ")
    vac_rate('LBN')
    print("\nTest Run for Poland: ")
    vac_rate("Poland")


