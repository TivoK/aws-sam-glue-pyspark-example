# What’s AWS SAM?

AWS SAM (ServerLess Application Manager) is an AWS open-source Framework that allows us to  create AWS Resources, package dependencies and deploy them directly to AWS. It leverages AWS CloudFormation Stacks and Templates to get our applications in the cloud. An overview of AWS CloudFormation templates and SAM are down-below:

[AWS SAM - Getting Started]

[AWS CloudFormation Templates]

# Tutorial

In this tutorial we will be leveraging this example AWS Glue PySpark Job. This project assumes
you have an AWS Account w/ valid permissions and AWS Configured locally on your machine.

```
git clone https://github.com/TivoK/aws-sam-glue-pyspark-example.git
```

# CLI Commands
Below are the SAM and AWS CLI commands used in this tutorial for reference.

```
###create sam app
sam build

###deploy sam app
sam deploy --profile {your-proile-here} --capabilities CAPABILITY_NAMED_IAM --guided

###aws command to upload files to s3 Bucket
aws s3 --profile {your-proile-here} cp ./data s3://example-source-glue-pyspark-demo --recursive

###aws command to run AWS Glue Job
aws glue --{your-profile-here} start-job-run --job-name  ExampleDemoGlueJobETL
```

# Video
[AWS SAM - AWS Glue PySpark Demo] 

[AWS SAM - Getting Started]: <https://aws.amazon.com/serverless/sam/>
[AWS CloudFormation Templates]: <https://aws.amazon.com/cloudformation/resources/templates/>
[AWS SAM - AWS Glue PySpark Demo]:<https://www.youtube.com/watch?v=UTmn8MfXWuE>


