import databaseConnection
import json

def getMethod(email, feature) :
    conn = databaseConnection.connection()
    cursor = conn.cursor()

    query = '''SELECT COUNT(*) FROM [FeatureSwitch].[dbo].[Feature] WHERE email = ? AND featureName = ?'''
    value = (email, feature)
    cursor.execute(query, value)
    result = cursor.fetchone()[0]

    if result == 1 :
        query1 = '''SELECT enable FROM [FeatureSwitch].[dbo].[Feature] WHERE email = ? AND featureName = ?'''
        value1 = (email, feature)
        cursor.execute(query1, value1)
        result1 = cursor.fetchone()[0]

        if result1 == 0 :
            x = 0
            output = {"can Access": bool(x)}
            json_object = json.dumps(output, indent=4)
            print(json_object)
        else :
            x = 1
            output = {"can Access": bool(x)}
            json_object = json.dumps(output, indent=4)
            print(json_object)
    else :
        output = {"Error": "Data not available"}
        json_object = json.dumps(output, indent=4)
        print(json_object)