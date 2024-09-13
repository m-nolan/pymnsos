"""
pymnsos

Python code for reading, analyzing MN SOS elections data
"""

__version__ = "0.1.0"
__author__ = "Michael Nolan"
__credits__ = "MinnPost"

def read_mn_table(file,columns):
    return pd.read_csv(file,sep=';',header=None,names=columns)

def read_precinct_table(file):
    columns = ['County ID','Precinct ID','Precinct Name','Congressional District','Legislative District','County Commissioner District',
               'Judicial District','Conservation District','MCD FIPS','School District']
    prec_df = read_mn_table(file,columns)
    prec_df['Precinct Name'] = [re.sub('(.*W)([0-9]+.*)','\g<1>-\g<2>',re.sub('(.*P)([0-9]+.*)','\g<1>-\g<2>',s)).replace('TWP.','TWP') for s in prec_df['Precinct Name']]
    return prec_df

def read_county_table(file):
    columns = ['County ID','County Name','No Precincts']
    return read_mn_table(file,columns)

def read_precinct_results(file,table_file):
    columns = ['State','County ID','Precinct ID','Office ID','Office Name','District','Candidate Order Code','Candidate Name','Suffix',
	           'Incumbent Code','Party Abbreviation','No Precincts Reporting','Total Precinct No','Votes','Vote Percentage','Total Votes']
    prec_table_df = read_precinct_table(table_file)
    prec_result_df = read_mn_table(file,columns)
    prec_result_df = prec_result_df.merge(prec_table_df[['County ID','Precinct ID','Precinct Name']],how='left',on=['County ID','Precinct ID'])
    return prec_result_df.pivot_table(
        index='Precinct Name',
        columns='Party Abbreviation',
        values='Vote Percentage'
    )

def read_county_results(file,table_file):
    columns = ['State','County ID','Precinct ID','Office ID','Office Name','District','Candidate Order Code','Candidate Name','Suffix',
	           'Incumbent Code','Party Abbreviation','No Precincts Reporting','Total Precinct No','Votes','Vote Percentage','Total Votes']
    cty_table_df = read_county_table(table_file)
    cty_result_df = read_mn_table(file,columns)
    cty_result_df = cty_result_df.merge(cty_table_df[['County ID','County Name']],how='left',on='County ID')
    return cty_result_df.pivot_table(
        index='County Name',
        columns='Party Abbreviation',
        values='Vote Percentage'
    )

if __name__ == "__main__":
    print("pymnsos - MN SOS Elections Data code.")