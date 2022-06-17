import os
import boto3
import pandas as pd 
from io import StringIO
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType
from pyspark.sql.functions import year, dayofmonth,hour, minute,second

#if you see this message--the upload worked!

#get access to S3 Buckets
s3 = boto3.resource('s3')


def transform_runtime(df):
    '''performs a small tranformation; adds timestamp year and day of month
    :params: 
        df - dataframe
    :returns: dataframe 
    '''
    return df.withColumn('transform_year',year('RunTime')). \
            withColumn('transform_day', dayofmonth('RunTime')). \
            withColumn('transfrom_hour',hour('RunTime')). \
            withColumn('transform_minute', minute('RunTime')). \
            withColumn('transform_secs',second('RunTime'))

def read_csv(data):
    '''reads csv files into spark dataframe
    :params: 
        data - csv data passed in by StringIO
    :returns:
        df - dataframe object
    '''
    
    pd_df = pd.read_csv(data,header=None)
    spark_schema = StructType([StructField('RunTime', StringType(), True), \
                        StructField('Type', StringType(), True) ])
    spark= SparkSession.builder.master('local'). \
                    appName('test-date').getOrCreate()
    df = spark.createDataFrame(pd_df,schema=spark_schema)
    return df

def output_csv(df,name):
    '''save the transformed df into csv in target bucket
    :params:
        df - dataframe
    :returns:
        None '''
    buffer = StringIO()
    df.toPandas().to_csv(buffer)
    target.put_object(Body=buffer.getvalue(), Key=name)
    return True 



#define source and targets 
source = s3.Bucket('example-source-glue-pyspark-demo')
target = s3.Bucket('example-target-glue-pyspark-demo')
#list all objects
objects_all =source.objects.all()
#get the appropriate named files..
files = [obj.key for obj in objects_all.filter(Prefix='times')]

#for each file bucket transform, rename and place in target bucket...
for key in files:
    csv_obj = source.Object(key=key).get().get('Body').read().decode('utf-8')
    data = StringIO(csv_obj)
    df = read_csv(data)
    tr_df =transform_runtime(df)
    new_key =key.replace('times','times_transform')
    res= output_csv(tr_df,new_key)
