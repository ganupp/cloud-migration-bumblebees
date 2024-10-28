# cloud-migration-bumblebees
Accelerating public cloud migration from traditional hosting services to Azure.

## Execution
````
$ python3 -m venv .venv
$ source .vev/Scripts/activate
$ pip install -r requirements.txt
$ ./run.sh
````

## Pre-requisites
Azure account \
Base application hosted in traditional infra

## Folder structure

### Starting point
| __File__      | __Functionality__ |
|---------------|------------------------|
|run.sh     |bash script to run the scripts |
|migration.py     |Backend starting point|
|main.py     |UI starting point |


### Modules
| __Folder__      | __Functionality__ |
|---------------|------------------------|
|azureManager     |Service to interact with Azure |
|parsers     |Util module with OCS & K8s parsers |
|scriptGenerators     |Util module to generate yamls from template |

### Base Application
| __Folder__      | __Functionality__ |
|---------------|------------------------|
|base-appl     |Whiteapp with .tf and .yaml configs to test |
|cloud-migration-bumblebees/war-files | repo/ .war files downloaded from UI input |

### Plan B
| __Folder__      | __Functionality__ |
|---------------|------------------------|
|planb     |Other tested approaches - azure SDK, terraform scripts |

## Tech stack
Python 3.12 \
Streamlit (python) \ 
requirements.txt


