import pandas as pd
from django.db import connection


class DbQueryExecutionClass():
    def execute_query(self, query, return_type='df'):
        with connection.cursor() as cursor:
            cursor.execute(query)
            if return_type== 'df':
                df= pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                return df
            else:
                return cursor.fetchall()