
# Basic Setting for AWS Provision
* Create a user with API access on AWS
* Setting up Ansible for AWS
* AWS manual setup
* AWS Auto setup by Ansible - Check it's an appropriate!

## Create a user with API access on AWS
* Create a user on AWS
* Using user's information with API access

---
### Using user's information with API access
* Create source file [Any Name ex.aws_access_keys]
```
    export AWS_ACCESS_KEY_ID="[Key ID info]"
    export AWS_SECRET_ACCESS_KEY="[Access Key info]"
    export AWS_REGION="[ex.us-west-2]"
```
* Run Source File
```
    source [Source File Name ex.aws_access_keys]
```

---
## Setting up Ansible for AWS Provisioning
* ansible.cfg
* my_inventory Folder
* Run ansible-inventory

---
### ansible.cfg
```
    [defaults]
    inventory = my_inventory
    
    [inventory]
    enabled_plugins = ini
```

---
### my_inventory Folder
* host
```
    [local]
    localhost       ansible_connection=local  
```

---
### Run ansible-inventory
```
    ansible-inventory
    ansible-inventory --list
    ansible-inventory --graph
    ansible -m ping localhost
```

---
## CLI AWS Setting
* Create Ansible Role for AWS
* Create tasks - create.yml, clean.yml, info.yml, main.yml

---
### Create Ansible Role for AWS
```
    ansible-galexy init [NAME ex.aws]
```

---
### Create tasks
* playbook.yml - Add all tasks into main playbook file
```
    tasks:
      - name: Create the AWS infrastructure
        import_role:
                name: aws
                tasks_from: create.yml
        tags:
                - create
      - name: Provisioning AWS infrastructure
        import_role:
                name: aws
                tasks_from: info.yml
        tags:
                - info
                - never
      - name: Clean AWS infrastructure
        import_role:
                name: aws
                tasks_from: clean.yml
        tags:
                - clean
                - never
```

* Then, create all tasks file named create.yml, clean.yml, info.yml, main.yml into your AWS role tasks folder
* Lastly, check all tasks are properly worked.
```
    
```

---
## Manual AWS Setting
* This is manual configuration of AWS to verify the proper functionality of all setting. 
* Create VPC
* Create Subnet
* Create an Internet Gateway
* Create a Route Table
* Create a Security Group
* Launch an EC2 Instance and SSH key pair

---

### Create VPC
``` 
    VPC settings
    Name tag                [NAME]
    IPv4 CIDR block         Default setting
    IPv4 CIDR               Ex.[10.42.0.0/16]
    IPv6 CIDR block         Default setting 
```

---
### Create Subnet
```
    VPC ID                  Default
    Subnet name             Default
    Availability Zone       Based on your location
    IPv4 CIDR block         Ex.[10.42.10.0/24]
    
```

---
### Create an Internet Gateway
```
    Name tage               [NAME]    
```
* Click Attach to VPC that you created

---
### Create a Route Table
```
    Name                    [NAME]
    VPC                     [Select your VPC]
```
* Go to the *Explicit subnet associations* and Click *Edit subnet associations*
* Click your subnet and Save
* Go to the *Edit routes*
* Add route your Internet Gateway - 0.0.0.0/0 with the Internet Gateway you created (ex.igw-0cdafe...) 

---
### Create a Security Group
```
    Security group name     [NAME]
    Description             [Description]
    
    Add Inbound rules
```

```Inbound rules
    SSH                     [Any location - IPv4]
    HTTP                    [Any location - IPv4]
```

---
### Launch EC2 Instance
* Use the AMI marketplace to select the `Ubuntu Server 20.04 LTS (HVM)`
* Instance type: `t2.micro` (free tier eligible)
  * 1 vCPU
  * 1GB RAM
* Name: [Name]
* Create a storage unit of 10GB (EBS is included in the free tier up to 30GB)
* Choose the VPC, subnet, security groups create earlier
* Make sure the instance has a tag attached to it. Choose any tag that makes sense for you. This tage will allow you to "find" your machine in AWS later on.
* Create a new keypair when requested, download and store the file in secure location. Name the file `[NAME]`

---
### Connect EC2 Instance with SSH key pair

* Change Permission your key file
```
    chmod 600 [key name].pem
```

* Try to connect to the EC2 Instance 
```
    ssh -i [key name].pem ubuntu(UserName)@[ip address]
```
