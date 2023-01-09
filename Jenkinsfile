pipeline {
    agent any
     environment {
    DOCKER_REPO_URL='ghcr.io/7shivam/galaxy-bigfilms-backend'
  }
     
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/7shivam/galaxy-bigfilms-backend.git']]])
            }
        }
   
            stage('Snyk Code') {
            steps {
               withCredentials([string(credentialsId: 'snyk_token_latest', variable: 'snyk_token_latest')]) {

                    sh "snyk --version"
                sh "snyk auth $snyk_token_latest"
               
                  sh "snyk test --json | snyk-to-html -o devresults.html"
                 sh "snyk code test --json | snyk-to-html -o coderesults.html"
               }
              }
            }
        stage('docker image Build') {
            steps {
                sh 'docker build -t $DOCKER_REPO_URL:$BUILD_NUMBER .'
            }
        }
        stage('Login to github') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'github-token', passwordVariable: 'pass', usernameVariable: 'user')]) {
                    sh 'docker login ghcr.io -u 7shivam -p $pass'
                }
            }
        }
        stage('push image to github') {
            steps {
                sh 'docker push $DOCKER_REPO_URL:$BUILD_NUMBER'
            }
        }
        stage('container image scan') {         
      steps    {                
	        sh 'trivy image --severity HIGH,CRITICAL $DOCKER_REPO_URL:$BUILD_NUMBER' 
                }           
           }
         
    }
}
