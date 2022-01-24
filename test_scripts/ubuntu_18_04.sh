#!/bin/bash

apt install ansible
git clone https://github.com/eslam-gomaa/mysql_secure_installation_Ansible.git
cd mysql_secure_installation_Ansible

echo "This will Install & Secure MySQL"
ansible-playbook sample-playbook.yml