#Elastic Application - Face Recognition & Retrieve data from DynamoDB using AWS Lambda

##About the Project

####Code Strucutre
├── Readme.md
├── handler.py
├── DockerFile
├── encoding
├── entry.sh
├── requirements.txt
└── workload_generator


## Getting Started


1. We run the workload.py script to test our test cases. This script inputs the s3 input bucket from
there it triggers the lambda function and from the lambda function the outputs are stored in the
output bucket.
2. We check the input buckets whether the videos are getting updated in the bucket or not. After a
while we check the output bucket for results. Logs are created for debugging.

<!-- LICENSE -->

#### Team Members

1. Ramchandra Sai- Worked on creating trigger and docker image , uploading it to ECR.
2. Disha Agarwal - Worked on lambda function parts face recognition, video splitting and retrieving info from dynamodb.
3. Sanket Duhoon - Worked on creating dynamodb database, querying database, and fixing bugs in handler.py.

##### AWS Resources

- AWS Credentials are provided in the Excel file.

- The PEM key file is added to the submission.
  IMAGE_BUCKET = 'cc-p2-input-bucket'
  OUTPUT_BUCKET = 'cc-p2-output-bucket'

