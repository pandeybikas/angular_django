from db_utils.helpers import DbQueryExecutionClass
from db_utils import constant
class BaseAccessLayerClass(DbQueryExecutionClass):
    def fetch_country_name(self):
        table_name=constant.WATER_DEPLETION_TBL

        query= f''' select distinct "Country" from {table_name} '''
        df= self.execute_query(query)
        return df


    def fetch_avg_depletion_rate(self, **Kwargs):
        table_name=constant.WATER_DEPLETION_TBL
        country= Kwargs.get('country', 'India')
        query= f''' 
                SELECT 
                    "Year", 
                    CAST(AVG("Groundwater Depletion Rate (%)") AS DECIMAL(10,2)) AS avg_depletion_rate
                FROM {table_name}
                WHERE "Country" = '{country}' 
                GROUP BY "Year"
                ORDER BY "Year"
                   '''
      
        df= self.execute_query(query)
        return df