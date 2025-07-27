pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:${env.PATH}"
        IMAGE_NAME = 'mokshitgupta29/flaskapp:latest'
        DOCKER_CREDENTIALS_ID = '2c498829-1aa7-4c9f-802d-d9ffc999dd7f' // Replace with your actual ID
    }

    stages {
        stage('Verify Docker') {
            steps {
                sh 'which docker'
                sh 'docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Docker Login & Push') {
            steps {
                withDockerRegistry(credentialsId: "${DOCKER_CREDENTIALS_ID}", url: '') {
                    sh "docker push ${IMAGE_NAME}"
                }
            }
        }

        stage('Deploy') {
            steps {
                sh "docker-compose up -d"
            }
        }
    }
}
