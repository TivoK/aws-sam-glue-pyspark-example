### Create Build
- SYNTAX: ```sam build```

### Deploy SAM App
- SYNTAX:```sam deploy --profile {your profile name} --capabilities CAPABILITY_NAMED_IAM --guided```
> sam deploy --profile my-profile --capabilities CAPABILITY_NAMED_IAM --guided

### Copy Multiple Files to S3 Bucket
- SYNTAX:```aws --profile {your profile name} cp {folder with files} {destination s3 bucket} --recursive```
> aws --profile my-profile  s3 cp ./data s3://example-source-glue-pyspark-demo --recursive

### Run The Glue Job
- SYNTAX:```aws glue --profile {your profile name} start-job-run --job-name  {glue job name}``
> aws glue --profile my-profile start-job-run --job-name  ExampleDemoGlueJobETL

### Delete Stack
- SYNTAX: ```aws cloudformation --profile {your profile name} delete-stack --stack-name {your stack name} --region {aws region}```
> aws cloudformation --profile my-profile delete-stack --stack-name example-glue-pyspark --region us-east-1