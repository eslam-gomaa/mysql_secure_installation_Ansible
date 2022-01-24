#!/bin/bash

apt install ansible -y
git clone https://github.com/eslam-gomaa/mysql_secure_installation_Ansible.git
cd mysql_secure_installation_Ansible

echo "This will Install & Secure MySQL"
ansible-playbook sample-playbook.yml

echo "Check that the user password changed"
cat output.txt | grep 'Password for user' | grep  'changed to the desired state'


echo "Check that the user password will NOT change the next time"
ansible-playbook sample-playbook.yml
cat output.txt | grep 'Password for user' | grep  'Already meets the desired state'