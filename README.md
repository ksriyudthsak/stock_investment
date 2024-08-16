# stock_investment

streamlit


# References for deploy EC2 docker
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

## Docker
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