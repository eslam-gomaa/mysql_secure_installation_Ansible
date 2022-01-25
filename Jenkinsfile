pipeline {
  agent { label 'kvm_lab' }
  stages {
    stage('Clone') {
      steps {
        git(url: 'https://github.com/eslam-gomaa/mysql_secure_installation_Ansible.git', branch: 'master', credentialsId: 'github_id')
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
                vagrant destroy -f
              done        
          '''
        }
      }
    }
    stage('Download boxs that don\'t exist') {
      steps {
        // Add any new box here to download it before running the tests
        // to prevent a BUG that may prevent downloading the box from within the pipeline.
        script {
          sh '''
          for image_name in "generic/ubuntu1804" "generic/ubuntu1604" "generic/ubuntu2004"
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
        echo 'Begin Testing'
        sh 'vagrant up ubuntu_18_04'

        echo 'Removing the test vm'
        sh 'vagrant destroy -f ubuntu_18_04'
      }
    }
    stage('Test Ubuntu 16.04') {
      steps {
        // script {
        //   echo 'Download the box if needed (Avoiding a bug)'
        //   sh '''
        //     image_name="generic/ubuntu1604"
        //     if ! vagrant box list | grep $image_name >/dev/null
        //     then
        //       echo "Downloading $image_name"
        //       vagrant box add $image_name --provider libvirt  --no-tty
        //     fi
        //   '''
        // }
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