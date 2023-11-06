#Elastic Application - Image Recognition

##About the Project

####Code Strucutre
├── Readme.md
├── app-tier
│   ├── image_classification.py
│   ├── main.py
│   ├── s3_utils.py
│   └── sqs_utils.py
├── Cloud_Project1
│   ├── web_server.py
│   ├── appScaler.py
│   ├── credentials.py
│   ├── customEC2Manager.py
│   ├── sqs_utils.py
│   └── requirements.txt
└── workload_generator


## Getting Started

There are two folders, Cloud_Project1(web_tier) and app-tier each containing their separate dependencies and code.
To install the required dependencies, run

```
pip3 install -r requirements.txt
```

For running the main flask server:

```
cd /home/ec2-user/Cloud_Project1
nohup python web_server.py &
```

For running the controller script to perform auto-scaling:

```
cd /home/ec2-user/Cloud_Project1
python3 appScaler.py
```

For running the app-tier code, first install the dependancies using pip.
Use amiID ami-0d5865d3d6fffbdb2 to launch the instance

```
cd /home/ubuntu/app-tier
python3 main.py
```


<!-- LICENSE -->

#### Team Members

1. Ramchandra Sai- Worked on the web-tier part of the application.
2. Disha Agarwal - Worked on the apptier part
3. Sanket Duhoon - Worked on the auto scaler part.

##### AWS Resources

- AWS Credentials are provided in the Excel file.

- The PEM key file is added to the submission.
  IMAGE_BUCKET = 'cc-p1-img-store'
  OUTPUT_BUCKET = 'cc-p1-label-store'
  INPUT_QUEUE = "https://sqs.us-east-1.amazonaws.com/770825654535/requestQueue"
  OUTPUT_QUEUE = "https://sqs.us-east-1.amazonaws.com/770825654535/responseQueue"
