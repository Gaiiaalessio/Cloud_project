# Cloud_project

This project implements a cloud-based file storage system that allows users to upload, download and delete files while maintaining the privacy of their storage space. The system was developed using containerization with Docker and Docker-Compose.


To start the system on your environment, follow the steps below:
1.	Make sure you have Docker and Docker-Compose installed on your system.
2.	Start the containers by running the command docker-compose up -d.
3.	Access Nextcloud through the following URL: http://localhost:8080.


To run performance tests, follow the steps below:
1.	Create new users through the commands:
   
    a.	chmod +x add_user.sh
  	
    b.	./add_user.sh
  	
3.	Run the locustfile.py file through the command locust -f locustfile.py
4.	Access Locust through the following URL: http://localhost:8089.
