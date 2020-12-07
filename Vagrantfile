# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
 # The most common configuration options are documented and commented below.
 # For a complete reference, please see the online documentation at
 # https://docs.vagrantup.com.

 # Every Vagrant development environment requires a box. You can search for
 # boxes at https://vagrantcloud.com/search.
 config.vm.box = "ubuntu/bionic64"
 config.vm.box_version = "~> 20200304.0.0"  #Just a version (changable)

 config.vm.network "forwarded_port", guest: 8000, host: 8000 #laptop
 #guest: 800 is the development server

 config.vm.provision "shell", inline: <<-SHELL  #This is how we can run scripts when we first create server
   systemctl disable apt-daily.service    #this two following lines to stop auto update, otherwise it will conflict with the follow 'sudo apt-get upate'
   systemctl disable apt-daily.timer

   sudo apt-get update  #This is update the local repository with all the available packages so that, we can instlal python 3 zip
   sudo apt-get install -y python3-venv zip
   touch /home/vagrant/.bash_aliases  #this and following lines for setting python3 instead of default python 2
   if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
     echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
     echo "alias python='python3'" >> /home/vagrant/.bash_aliases #every time we don't need to write python 3 when will we work on it
   fi
 SHELL
end
