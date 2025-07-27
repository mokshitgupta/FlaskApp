pipeline {
    agent any

    environment {
        IMAGE_NAME = 'flaskapp:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/mokshitgupta/FlaskApp.git'
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
