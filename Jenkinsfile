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
    stage('Test Ubuntu 18.04') {
      steps {
        echo 'Begin Testing'
        timeout(time: 30, unit: 'MINUTES') {
          sh 'vagrant up ubuntu_18_04'
          }

        echo 'Removing the test vm'
        sh 'vagrant destroy -f ubuntu_18_04'
      }
    }
    stage('Test Ubuntu 16.04') {
      steps {
        echo 'Begin Testing'
        timeout(time: 30, unit: 'MINUTES') {
          sh 'vagrant up ubuntu_16_04'
          }

        echo 'Removing the test vm'
        sh 'vagrant destroy -f ubuntu_16_04'
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