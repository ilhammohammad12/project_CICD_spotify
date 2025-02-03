pipeline {
    agent any
    environment {
        SSH_CREDENTIALS_ID = 'my-ssh-key'
        REMOTE_SERVER = 'root@192.168.1.200'
        DOCKER_IMAGE = "oilham/jenkins_spotify:latest"
        DOCKER_CREDENTIALS_ID = "dockerhub-credentials"  // Add your Jenkins credentials ID here
    }
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        stage('Copy Required Files to Remote Server') {
            steps {
                sshagent([SSH_CREDENTIALS_ID]) {
                    sh """
                        scp -o StrictHostKeyChecking=no Dockerfile ${REMOTE_SERVER}:/tmp/app
                        scp -o StrictHostKeyChecking=no -r * ${REMOTE_SERVER}:/tmp/app
                    """
                }
            }
        }
        stage('Build the Docker Image') {
            steps {
                sshagent([SSH_CREDENTIALS_ID]) {
                    sh """
                        ssh -o StrictHostKeyChecking=no ${REMOTE_SERVER} 'cd /tmp/app && docker build -t $DOCKER_IMAGE .'
                    """
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                sshagent([SSH_CREDENTIALS_ID]) {
                    withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS_ID, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh """
                            ssh -o StrictHostKeyChecking=no ${REMOTE_SERVER} '
                                cd /tmp/app &&
                                echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin &&
                                docker push $DOCKER_IMAGE
                            '
                        """
                    }
                }
            }
        }
    }
}
