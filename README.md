# stock_investment

streamlit


# Deploy EC2 docker manually
https://github.com/entbappy/Streamlit-app-Docker-Image/blob/main/README.md

## Update apt-get
sudo apt-get update -y
sudo apt-get upgrade

## Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
docker --version

## Deploy using Docker
git clone https://github.com/ksriyudthsak/stock_investment.git
docker build -t ksriyudthsak/st-stock-docker:latest . 
docker images -a  
docker run -d -p 8501:8501 ksriyudthsak/st-stock-docker 
docker ps  
docker stop container_id
docker rm $(docker ps -a -q)
docker login 
docker push ksriyudthsak/st-stock-docker:latest 
docker rmi ksriyudthsak/st-stock-docker:latest
docker pull ksriyudthsak/st-stock-docker

# Deploy automatically
https://www.youtube.com/watch?v=Ea8a9JozlGA&list=PLqoUmUbJ_zDHPwK-ZWATXiYrUXwWkLY65&index=6

## Launch EC2 instance and install Docker
- In EC2, add port 8501 for streamlit
- In terminal, chmod 400 [key].pem
- Check the access, ssh -i [key].pem [username: ubuntu, ec2_user]@[IP]

## Build Docker Image
- same as manual deploement
- install aws: sudo snap install aws-cli --classic

## Create a repository using Elastic Container Registry
- just create repository app
- add ecr role in IAM to user (Policy: AdministratorAccess)

## Create Access Key in AWS IAM and Configure
- get access key and save it in csv file
- set up configuration, aws configure
- to check, aws configure list

## Login to Elastic Container Registry
- view push command
- clone git repo and follow the command

## Create an Application Load Balancer
- create load balancers in EC2
- 

## Create Task Definition Cluster and Service
- In ECS, create Task definitions
- In IAM role, add ecs role -> AmazonECSTaskExecutionRolePolicy
- In ECS, create Cluster

# Terraform + Streamlit
https://qiita.com/Maki-HamarukiLab/items/6c2d9b1d1a42c1969b7f

## create key pair
aws ec2 create-key-pair --key-name streamlit-terraform-keypair-tokyo --query 'KeyMaterial' --output text > streamlit-terraform-keypair-tokyo.pem
chmod 400 streamlit-terraform-keypair-tokyo.pem