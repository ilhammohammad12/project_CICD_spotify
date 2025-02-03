pipeline{
    agent any
    environment {
        DOCKER_IMAGE: docker push oilham/jenkins_spotify:latest
        DOCKER_CREDTENTIALS_ID:
    }
    stages {
        stage('checkout scm'){
            steps{
            checkout scm
        }}

        stage('Build the docker'){
            steps{
            sh 'docker build -t $(DOCKER_IMAGE) .'
            }
        }
        stage( 'push the docker'){
        steps{
             withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS_ID, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker push $DOCKER_IMAGE
                    """
        }
        }
    }
}