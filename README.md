# cloud-migration-bumblebees
Accelerating public cloud migration from traditional hosting services to azure


Requirement--------------------------

pip install 
            python-hcl2 
            pyyaml
            azure-identity 
            azure-mgmt-resource
            watchdog
            streamlit

install azure cli in mac ---------- 

git clone https://github.com/Homebrew/brew homebrew
eval "$(homebrew/bin/brew shellenv)"\nbrew update --force --quiet\nchmod -R go-w "$(brew --prefix)/share/zsh"
brew update && brew install azure-cli


Folder structure -------------------------------------------

cloud-migration-bumblebees/
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
