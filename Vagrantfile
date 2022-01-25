# -*- mode: ruby -*-
# vi: set ft=ruby :

## Variables ##
memory        = 1024

##################  ##################  ##################

Vagrant.configure("2") do |config|
  # config.ssh.insert_key = false
    config.ssh.username = "vagrant"
    config.ssh.password = "vagrant"

    config.vm.define "ubuntu_16_04" do |ubuntu_16_04|
      ubuntu_16_04.vm.provider :libvirt do |libvirt|
      libvirt.cpus = 2
      libvirt.memory = "#{memory}"
      libvirt.title  = "ubuntu_16_04"
        end
        ubuntu_16_04.vm.hostname = "ubuntu-16-04"
        ubuntu_16_04.vm.box = "generic/ubuntu1604"
        ubuntu_16_04.vm.provision "Test mysql_secure_installation ansible module", type: "shell", path: "test_scripts/ubuntu_16_04.sh", privileged: true
        ubuntu_16_04.vm.provision "Test mysql_secure_installation ansible module", type: "shell", path: "test_scripts/module_test.sh", privileged: true
        # ubuntu_16_04.vm.network :public_network, :dev => "virbr0", :mode => "bridge", :type => "bridge", :ip => "192.168.122.40"
      end

    config.vm.define "ubuntu_18_04" do |ubuntu_18_04|
      ubuntu_18_04.vm.provider :libvirt do |libvirt|
      libvirt.cpus = 2
      libvirt.memory = "#{memory}"
      libvirt.title  = "ubuntu_18_04"
        end
        ubuntu_18_04.vm.hostname = "ubuntu-18-04"
        ubuntu_18_04.vm.box = "generic/ubuntu1804"
        ubuntu_18_04.vm.provision "Test mysql_secure_installation ansible module", type: "shell", path: "test_scripts/Install_ansible_ubuntu_18_04.sh", privileged: true
        ubuntu_18_04.vm.provision "Test mysql_secure_installation ansible module", type: "shell", path: "test_scripts/module_test.sh", privileged: true
      end

    config.vm.define "ubuntu_20_04" do |ubuntu_20_04|
      ubuntu_20_04.vm.provider :libvirt do |libvirt|
      libvirt.cpus = 2
      libvirt.memory = "#{memory}"
      libvirt.title  = "ubuntu_20_04"
        end
        ubuntu_20_04.vm.hostname = "ubuntu-20-04"
        ubuntu_20_04.vm.box = "generic/ubuntu2004"
        ubuntu_20_04.vm.provision "Test mysql_secure_installation ansible module", type: "shell", path: "test_scripts/Install_ansible_ubuntu_20_04.sh", privileged: true
        ubuntu_20_04.vm.provision "Test mysql_secure_installation ansible module", type: "shell", path: "test_scripts/module_test.sh", privileged: true
      end

    config.vm.define "centos_8" do |centos_8|
      centos_8.vm.provider :libvirt do |libvirt|
      libvirt.cpus = 2
      libvirt.memory = "#{memory}"
      libvirt.title  = "centos_8"
        end
        centos_8.vm.hostname = "centos-8"
        centos_8.vm.box = "generic/centos8"
        centos_8.vm.provision "Test mysql_secure_installation ansible module", type: "shell", path: "test_scripts/Install_ansible_centos_8.sh", privileged: true
        centos_8.vm.provision "Test mysql_secure_installation ansible module", type: "shell", path: "test_scripts/module_test.sh", privileged: true
      end

    config.vm.define "centos_7" do |centos_7|
      centos_7.vm.provider :libvirt do |libvirt|
      libvirt.cpus = 2
      libvirt.memory = "#{memory}"
      libvirt.title  = "centos_7"
        end
        centos_7.vm.hostname = "centos-7"
        centos_7.vm.box = "generic/centos7"
        centos_7.vm.provision "Test mysql_secure_installation ansible module", type: "shell", path: "test_scripts/Install_ansible_centos_7.sh", privileged: true
        centos_7.vm.provision "Test mysql_secure_installation ansible module", type: "shell", path: "test_scripts/module_test.sh", privileged: true
      end
  

    
end
