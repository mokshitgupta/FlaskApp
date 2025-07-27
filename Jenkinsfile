pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:${env.PATH}" // so Jenkins finds docker
        IMAGE_NAME = 'flaskapp:latest'
    }

    stages {
        // No explicit checkout stage here, Declarative pipeline checks out automatically

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

        stage('Deploy') {
            steps {
                sh "docker-compose up -d"
            }
        }
    }
}
