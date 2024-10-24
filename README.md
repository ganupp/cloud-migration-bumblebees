# cloud-migration-bumblebees
Requirement--------------------------

pip install python-hcl2 azure-identity azure-mgmt-resource

install azure cli in mac ---------- 


git clone https://github.com/Homebrew/brew homebrew
eval "$(homebrew/bin/brew shellenv)"\nbrew update --force --quiet\nchmod -R go-w "$(brew --prefix)/share/zsh"
brew update && brew install azure-cli


Accelerating public cloud migration from traditional hosting services to azure



Folder structure -------------------------------------------

cloud-migration-bumblebees/
├── main.py                    
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
