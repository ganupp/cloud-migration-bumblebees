# cloud-migration-bumblebees
Accelerating public cloud migration from traditional hosting services to Azure.

## Execution
````
$ python3 -m venv .venv
$ source .vev/Scripts/activate
$ pip install -r requirements.txt
$ ./run.sh
````

## Starting point
migration.py > Azure services
main.py      > UI


cloud-migration-bumblebees/
├──azureManager/
   └──azure_manager.py
   └──constants.py
├── main.py 
├── /k8s                
│   ├── deployment.yaml  
│   ├── service.yaml     
├── /src                 
│   ├── index.js         
│   └── ...
├── Dockerfile           
├── .dockerignore      
└── package.json                     
├── terraform/
│   └── infra/                 
│       ├── backend.ENV.hcl.dist
│       ├── compute.tf
│       ├── data.tf
│       ├── monitoring.tf
│       ├── provider.tf
│       ├── secrets.ENV.tfvars.dist
│       ├── slb.tf
│       ├── terraform.tf
│       └── variables.tf
└── README.md                 
