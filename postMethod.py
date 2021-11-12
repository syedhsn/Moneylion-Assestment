import databaseConnection
import json
from fastapi import status

def postMethod(jsonData) :
    conn = databaseConnection.connection()
    cursor = conn.cursor()

    data = json.loads(jsonData)

    if data['enable'] == bool(0):
        query = '''UPDATE [FeatureSwitch].[dbo].[Feature] SET enable = 1 WHERE email = ? AND featureName = ?;'''
        value = (data['email'], data['featureName'])
        cursor.execute(query, value)
        conn.commit()

        query1 = '''SELECT enable FROM [FeatureSwitch].[dbo].[Feature] WHERE email = ? AND featureName = ?'''
        value1 = (data['email'], data['featureName'])
        cursor.execute(query1, value1)
        result1 = cursor.fetchone()[0]

        if result1 == 1 :
            print(status.HTTP_200_OK)
        else :
            print(status.HTTP_500_INTERNAL_SERVER_ERROR)
    else :
        print(status.HTTP_304_NOT_MODIFIED)




