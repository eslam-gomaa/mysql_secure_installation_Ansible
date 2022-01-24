pipeline {
  agent { label 'kvm_lab' }
  stages {
    stage('Clone') {
      steps {
        git(url: 'https://github.com/eslam-gomaa/mysql_secure_installation_Ansible.git', branch: 'master', credentialsId: 'github_id')
      }
    }
    stage('Test Ubuntu 18.04') {
      steps {
        echo 'Begin Testing'
        sh 'vagrant up ubuntu_18_04'
        
        script {
          try {
            echo 'Removing the testing vm'
            sh 'vagrant destroy -f ubuntu_18_04'
          } catch (err) {
            echo err.getMessage()
          }
        }
        
        // catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') { // Ignore the error returned by destroying th VM.
        //   sh 'vagrant destroy -f ubuntu_18_04'
        // }

      }
    }
  }
}