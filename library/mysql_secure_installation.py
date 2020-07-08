#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, eslam.gomaa <linkedin.com/in/eslam-sa3dany>

DOCUMENTATION = '''
---
module: mysql_secure_installation

short_description: An idempotent module to perform "mysql_secure_installation" script steps

version_added: "1.0"

description:
    - An idempotent module to perform "mysql_secure_installation" script steps
        - Change MySQL Root Password - for a list of hosts i.e [localhost, 127.0.0.1, ::1,] .etc.
        - Remove Anonymous User
        - Disallow Root Login Remotely
        - Remove Test Database

options:
    login_password:
        description:
            - Root's password to login to MySQL	
        required: true
        type: str
        
    new_password:
        description:
            - New desired Root password
        required: true
        type: str
    user:
        description:
            - MySQL user to login
        default: "root"
        type: str
                
    login_host:
        description:
            - host to connect to
        default: "localhost"
        type: str
    hosts:
        description:
            - List of hosts for the provided user i.e ['localhost', '127.0.0.1', '::1'], Note - all will have the same new password
        default: ["localhost"]
        type: list
    change_root_password:
        description:
            - whether or not to change root password 
        default: True
        type: bool
        
    remove_anonymous_user:
        description:
            - whether or not to remove anonymous user 
        default: True
        type: bool
        
    disallow_root_login_remotely:
        description:
            - whether or not to disallow root login remotely
        default: False
        type: bool
        
    remove_test_db:
        description:
            - whether or not to remove test db
        default: True
        type: bool

 
author:
    - eslam.gomaa (linkedin.com/in/eslam-sa3dany)
'''

EXAMPLES = '''
# with a fresh MySQL Installation
- name: test mysql_secure_installation
  mysql_secure_installation:
    login_password: ''
    new_password: password22
    user: root
    login_host: localhost
    hosts: ['localhost', '127.0.0.1', '::1']
    change_root_password: true
    remove_anonymous_user: true
    disallow_root_login_remotely: true
    remove_test_db: true
  register: mysql_secure

- debug:
    var: mysql_secure

# Change an existing password
- name: test mysql_secure_installation
  mysql_secure_installation:
    login_password: password22
    new_password: password23
    user: root
    login_host: localhost
    hosts: ['localhost', '127.0.0.1', '::1']
    change_root_password: true
    remove_anonymous_user: true
    disallow_root_login_remotely: true
    remove_test_db: true
'''

RETURN = '''
change_root_pwd:
    description: 0 == Success, 1 == Fail
    type: Int
    returned: always
disallow_root_remotely:
    description: 0 == Success, 1 == Fail
    type: Int
    returned: always
hosts_success:
    description: provides a list of the hosts succeeded to change password to i.e ['root@localhost', 'root@mysql.example.com']
    type: List
    returned: always
hosts_failed:
    description: provides a list of the hosts failed to change password to i.e ['root@localhost', 'root@mysql.example.com']
    type: List
    returned: always
remove_anonymous_user:
    description: 0 == Success, 1 == Fail
    type: Int
    returned: always
remove_test_db:
    description: 0 == Success, 1 == Fail
    type: Int
    returned: always
stdout:
    description: Prints the result of the code as compared to the desired state
    type: Str
    returned: always
stderr:
    description: Prints an error message in case of code error
    type: Str
    returned: In case of code error
'''

##############################################
#######################
############
import MySQLdb as mysql
from itertools import chain

def check_mysql_connection(host, user, password=''):
    """
    A function used to check the ability to login to MySQL/Mariadb
    :param host: ie. 'localhost'  - :type String
    :param user: mysql user ie. 'root' - :type String
    :param password: mysql user's password - :type String
    :return: True||False
    """
    try:
        mysql.connect(host=host, user=user, passwd=password)
        return True
    except  mysql.Error:
        return False

def mysql_secure_installation(login_password, new_password, user='root',login_host='localhost', hosts=['hostname'], change_root_password= True, remove_anonymous_user= True, disallow_root_login_remotely= False, remove_test_db= True):
    """
    A function to perform the steps of mysql_secure_installation script
    :param login_password: Root's password to login to MySQL
    :param new_password: New desired Root password :type String
    :param user: MySQL user - default: 'root' :type String
    :param login_host: host to connect to - default: 'localhost' :type String
    :param hosts: List of hosts for the provided user i.e ['localhost', '127.0.0.1', '::1'] :type List
    :param change_root_password:  default: True - :type Boolean
    :param remove_anonymous_user: default: True - :type: Boolean
    :param disallow_root_login_remotely: default: False - :type Boolean
    :param remove_test_db: default: True - :type: Boolean
    :return:
    """
    if isinstance(hosts, str):
        hosts = hosts.split(',')
    info = {'change_root_pwd': None, 'hosts_failed': [], 'hosts_success': [],'remove_anonymous_user': None, 'remove_test_db': None, 'disallow_root_remotely': None }

    def remove_anon_user(cursor):
        if remove_anonymous_user:
            cursor.execute("select user, host from mysql.user where user='';")
            anon_user = cursor.fetchall()
            if len(anon_user) >= 1:
                cursor.execute('use mysql;')
                cursor.execute("DELETE FROM user WHERE user='';")
                cursor.execute("update mysql.user set plugin=null where user='root';")
                cursor.execute("select user, host from mysql.user where user='';")
                check = cursor.fetchall()
                if len(check) >= 1:
                    info['remove_anonymous_user'] = 1
                else:
                    info['remove_anonymous_user'] = 0
            else:
                info['remove_anonymous_user'] = 0

    def remove_testdb(cursor):
        if remove_test_db:
            cursor.execute("show databases;")
            testdb = cursor.fetchall()
            if 'test' in list(chain.from_iterable(testdb)): # if database "test" exists in the "db's list"
                cursor.execute("drop database test;")

                cursor.execute("show databases;") # Test if the "test" db deleted
                check_test_db = cursor.fetchall()
                if 'test' in list(chain.from_iterable(check_test_db)): # return 1 if the db still exists
                    info['remove_test_db'] = 1
                else:
                    info['remove_test_db'] = 0
            else: # means "test" db does not exist
                info['remove_test_db'] = 0


    def disallow_root_remotely(cursor):
        if disallow_root_login_remotely:
            cursor.execute("select user, host from mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');")
            remote = cursor.fetchall()
            if len(remote) >= 1:
                cursor.execute("DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');")
                cursor.execute("flush privileges;")

                cursor.execute("select user, host from mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');")
                check_remote = cursor.fetchall()
                if len(check_remote) >= 1: # test
                    info['disallow_root_remotely'] = 1
                else:
                    info['disallow_root_remotely'] = 0
            else:
                info['disallow_root_remotely'] = 0

    if check_mysql_connection(host=login_host, user=user, password=login_password):
        try:
            connection = mysql.connect(host=login_host, user=user, passwd=login_password, db='mysql')
            cursor = connection.cursor()

            cursor.execute("SELECT host, user, password, plugin FROM mysql.user where User='{}' LIMIT 0,1;".format(user))
            socket_exists = cursor.fetchall()
            if 'unix_socket' in list(chain.from_iterable(socket_exists)):
                cursor.execute("UPDATE mysql.user SET plugin = '' WHERE user = {};".format(user))

            remove_anon_user(cursor)
            remove_testdb(cursor)
            disallow_root_remotely(cursor)
            if change_root_password:
                pwd = {}
                for host in hosts:
                    cursor.execute('use mysql;')
                    cursor.execute(
                        'update user set password=PASSWORD("{}") where User="{}" AND Host="{}";'.format(new_password,
                                                                                                        user, host))
                    cursor.execute('flush privileges;')
                    cursor.execute('select user, host, password from mysql.user where user="{}";'.format(user))
                    data = cursor.fetchall()
                    for d in data:
                        if d[1] == host:
                            pwd['{}'.format(d[1])] = d[2]

                out = set(hosts).symmetric_difference(set(pwd.keys()))
                info['hosts_failed'] = list(out)
                hosts_ = list(set(hosts) - set(list(out)))

                for host in hosts_:
                    if pwd[host] == pwd[login_host]:
                        info['hosts_success'].append(host)
                    else:
                        info['hosts_failed'].append(login_host)

                if len(info['hosts_success']) >= 1:
                    info['stdout'] = 'Password for user: {} @ Hosts: {} changed to the desired state'.format(user, info['hosts_success'])
                if len(info['hosts_failed']) >= 1:
                    info['change_root_pwd'] = 1
                #    info['stderr'] = 'Could NOT change password for User: {} @ Hosts: {}'.format(user,info['hosts_failed'])
                else:
                    info['change_root_pwd'] = 0
            connection.close()
        except mysql.Error as e:
            info['change_root_pwd'] = 1
            info['stderr'] = e

    elif check_mysql_connection(host=login_host, user=user, password=new_password):
        connection = mysql.connect(host=login_host, user=user, passwd=new_password, db='mysql')
        cursor_ = connection.cursor()
        remove_anon_user(cursor_)
        remove_testdb(cursor_)
        disallow_root_remotely(cursor_)
        info['change_root_pwd'] = 0
        info['stdout'] = 'Password of {}@{} Already meets the desired state'.format(user, login_host)

    else:
        info['change_root_pwd'] = 1
        info['stdout'] = 'Neither the provided old passwd nor the new passwd are correct'
    return info
############
#######################
##############################################

from ansible.module_utils.basic import *

def main():
    fields = {
        "login_password": {"required": True, "type": "str", "no_log": True},
        "new_password": {"required": True, "type": "str", "no_log": True},
        "user": {"type": "str", "default": "root"},
        "login_host": {"type": "str", "default": "localhost"},
        "hosts": {"type": "list", "default": ["localhost"]},
        "change_root_password": {"type": "bool", "default": True, "choices": [True, False]},
        "remove_anonymous_user": {"type": "bool", "default": True, "choices": [True, False]},
        "disallow_root_login_remotely": {"type": "bool", "default": False, "choices": [True, False]},
        "remove_test_db": {"type": "bool", "default": True, "choices": [True, False]},
    }

    module = AnsibleModule(argument_spec=fields)

    run = mysql_secure_installation(login_password=module.params['login_password'],
                              new_password=module.params['new_password'],
                              user=module.params['user'],
                              login_host=module.params['login_host'],
                              hosts=module.params['hosts'],
                              change_root_password=module.params['change_root_password'],
                              remove_anonymous_user=module.params['remove_anonymous_user'],
                              disallow_root_login_remotely=module.params['disallow_root_login_remotely'],
                              remove_test_db=module.params['remove_test_db'])

    if run["change_root_pwd"] == 1 and len(run["hosts_failed"]) == 0:
        module.warn('mysql_secure_installation --> Neither the provided old passwd nor the new passwd are correct -- Skipping')

    if len(run["hosts_success"]) >= 1:
        changed_ = True
    else:
        changed_ = False

    module.exit_json(changed=changed_, meta=run)


if __name__ == '__main__':
    main()
