#Bash Commands

- ssh {username}@{ip-address} - loggs onto the server
- scp -r {file} {user}@{address}:{filelocation to be saved at} -  this is how to copy the files onto the server
- read about the fhs, linux file hierarchy system 
- katabasis - github for bash commands 
- man cmd
- Chromanslack
- ssh {user}@{ip-adress} - logs into server
- apt - its bascially the brew but for the server
- history | grep "searchterm" -
- htop - shows a high level overview of what processes are happineing 
- iotop -o - what is being read in and out of the disk that is not a kernal process
- sudo - is used access root user privelages 
- iftop - shows all the process running on the wifi 
- slurm -s -i eth0 - the shape of your traffic, the flatter the red and green line, the faltter the traffic
- curl http://icanhazip.com - tells you your ip address
- glances - another one that shows process
##Systemctl 
- apt-get -y install firewalld - the -y forces the yes
- systemctl status firewalld - system controll status then name of module
- daemon - means background process
- firewall-cmd --list-all - shows you the zone 
- firewall-cmd --add-port=5000/tcp --permanent - lets the port pass the firewall
- - systemctl start firewalld  
- systemctl reload firewalld  
- systemctl status firewalld  
- systemctl enable firewalld  - entire firewalld well start next time the whole computer starts 
- system status 
- scp -r web_trader root@{ip-address}:/opt - copies file to the server
  
- ssh-keygen -t rsa -b 4096 - creates a key
- curl - X GET -H 
- lshw - lists hardware
- apt-get -y update - updates the package manager
- apt-get -y install fail2ban firewalld nginx ntp python3-pip - 
- systemctl status fail2ban firewalld nginx ntp python3-pip - scan - for green dots to make sure things are working
- cat /etc/ssh/sshd_config - outputs the configurtaion file for the ssh daemon 
- journalctl -xe - journal of the operating system 
- hostname -I - gives you the server ip
- cp -r - copies all the directories and files within a file
- ~/ - runs the given commmand from home 
- sudo -H pip install --ignore-installed -U ipython
- su - switch user
- vi /etc/ssh/sshd_config - opens the ssdh_config file to make adjustments
- apt -get -y update
- adduser --disabled-password --gecos "" {username} -creates a user without the need of a password 
-  usermod -aG sudo {username} - gives the user sudo privaledges 



#Definitions 

fail2ban - intrustion detection system
firewalld - command line interface for ip tables or firewall daemon for the background process
nginx - reverse proxy, also an http webserver
ntp - network time protocol
skel - things we wanna copy over to every new user
sudo - (super user do) gives admin provalgies 
whoami - user
hostname - server
address - arbitrary paths of reference to a patricular palce on your operating system and that maybe be acces to a particular service
protocalls - rules for exchanging information

#VI

:q! - exit without saving 
:x - save and exit


#Homework
- linux fhs 
- netblocks
- symbolic links
- protocalls - https,ssh,htp
- /// local computer
- // somebody elses computer
- node.js
- exress
- python3 metaclasses 
  

#VI
:q! - exit without saving 
:x - save and exit

#Books 

- Start up nation
- zero to one mk
- the right kind of crazy 
- the medicci effect 
- design patterns gang of four
- the art of computer programming
- the catheedral and the bizare 
- surfaces and analysis
- metaclasses python3 
- The Pro Git book


