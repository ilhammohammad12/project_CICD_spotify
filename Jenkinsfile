pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "oilham/jenkins_spotify:latest"
        DOCKER_CREDENTIALS_ID = "dockerhub-credentials"  // Add your Jenkins credentials ID here
    }
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Build the Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS_ID, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker push $DOCKER_IMAGE
                    """
                }
            }
        }
    }
}
