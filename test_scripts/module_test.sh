#!/bin/bash -e
git clone https://github.com/eslam-gomaa/mysql_secure_installation_Ansible.git
cd mysql_secure_installation_Ansible

echo """
**************************************
      Running a Sample Playbook
      This Will:
        1. Install MySQL
        2. Secure it with 'mysql_secure_installation' module  
**************************************
"""
ansible-playbook sample-playbook.yml


echo """
**************************************
      Test: change_root_password
**************************************
"""

echo "Check that the user password changed"
cat output.txt | grep 'Password for user' | grep  'changed to the desired state'

echo "Run the playbook again"
ansible-playbook sample-playbook.yml
echo "Check that the user password will NOT change the next time"
cat output.txt | grep 'Password of' | grep  'Already meets the desired state'


echo """
**************************************
           End of tests
**************************************
"""
