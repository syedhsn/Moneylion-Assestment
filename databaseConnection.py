import pyodbc

def connection() :
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-1I95FP9;'
                      'Database=FeatureSwitch;'
                      'Trusted_Connection=yes;')
    return conn