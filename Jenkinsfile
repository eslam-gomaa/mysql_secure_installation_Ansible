def ubuntu_18_04 = addEmbeddableBadgeConfiguration(id: "ubuntu_18_04", subject: "Test_result")


pipeline {
  agent { label 'kvm_lab' }
  stages {
    stage('Clone') {
      steps {
        git(url: 'https://github.com/eslam-gomaa/mysql_secure_installation_Ansible.git', branch: 'master', credentialsId: 'github_id')
      }
    }
    stage('Post clone step') {
      steps {
        script {
          echo "Changing the owner & permissions of .vagrant directory"
          // Avoid Permission denied when executing 'git clean -fdx' (Removes .vagrant directory)
          sh '''
            if [ ! -d .vagrant ]
            then
                mkdir -p .vagrant
                chown $(whoami):$(whoami) .vagrant -R
                chmod +s .vagrant -R
                setfacl -m d:u:$(whoami):rwx .vagrant/
                setfacl -m u:$(whoami):rwx .vagrant/
            fi     
          '''
        }
      }
    }
    stage('Destroy old test VMs') {
      steps {
        script {
          echo "Double check that old test vm's are cleared"
          sh '''
              for i in $(virsh list --all --name)
              do
                virsh destroy "$i"
                virsh undefine "$i"
                virsh vol-delete --pool default "$i".img
              done
          '''
          sh 'vagrant destroy -f'
        }
      }
    }
    stage('Download boxs that don\'t exist') {
      steps {
        // Add any new box here to download it before running the tests
        // to prevent a BUG that may prevent downloading the box from within the pipeline.
        script {
          sh '''
          for image_name in "generic/ubuntu1804" "generic/ubuntu1604" "generic/ubuntu2004" "generic/centos8" "generic/centos7" "generic/fedora34"  "generic/debian10"
          do
              if ! vagrant box list | grep $image_name >/dev/null
              then
                  echo "Downloading $image_name"
                  vagrant box add $image_name --provider libvirt  --no-tty
              fi
          done          
          '''
        }
      }
    }
    
    stage('Test Ubuntu 18.04') {
      steps {
        ubuntu_18_04.setStatus('running')
        script {
          try {
            echo 'Begin Testing'
            sh 'vagrant up ubuntu_18_04'
            ubuntu_18_04.setStatus('passed')
            ubuntu_18_04.setColor('brightgreen')
          } catch (Exception err) {
            ubuntu_18_04.setStatus('failed')
            ubuntu_18_04.setColor('pink')
            }
          echo 'Removing the test vm'
          sh 'vagrant destroy -f ubuntu_18_04'
        }
        error "Build failed"
      }
    }
    stage('Test Ubuntu 16.04') {
      steps {
        echo 'Begin Testing'
        sh 'vagrant up ubuntu_16_04'

        echo 'Removing the test vm'
        sh 'vagrant destroy -f ubuntu_16_04'
      }
    }
    stage('Test Ubuntu 20.04') {
      steps {
        echo 'Begin Testing'
        sh 'vagrant up ubuntu_20_04'

        echo 'Removing the test vm'
        sh 'vagrant destroy -f ubuntu_20_04'
      }
    }
    stage('Test CentOS 7') {
      steps {
        echo 'Begin Testing'
        sh 'vagrant up centos_7'

        echo 'Removing the test vm'
        sh 'vagrant destroy -f centos_7'
      }
    }
    stage('Test CentOS 8') {
      steps {
        echo 'Begin Testing'
        sh 'vagrant up centos_8'

        echo 'Removing the test vm'
        sh 'vagrant destroy -f centos_8'
      }
    }
    stage('Test fedora 34') {
      steps {
        echo 'Begin Testing'
        sh 'vagrant up fedora34'

        echo 'Removing the test vm'
        sh 'vagrant destroy -f fedora34'
      }
    }
    stage('Test debian 10') {
      steps {
        echo 'Begin Testing'
        sh 'vagrant up debian10'

        echo 'Removing the test vm'
        sh 'vagrant destroy -f debian10'
      }
    }
  }
}

        // script {
        //   try {
        //     echo 'Removing the testing vm'
        //     sh 'vagrant destroy -f ubuntu_18_04'
        //   } catch (err) {
        //     echo err.getMessage()
        //   }
        // }
        // sh 'exit 0'