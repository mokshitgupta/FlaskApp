pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "mokshitgupta29/flaskapp:latest"
        DOCKER_REGISTRY = "https://index.docker.io/v1/"
        DOCKER_CREDENTIALS_ID = "2c498829-1aa7-4c9f-802d-d9ffc999dd7f" // your Docker Hub credential ID
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Verify Docker') {
            steps {
                script {
                    def dockerPath = sh(script: 'which docker', returnStdout: true).trim()
                    if (!dockerPath) {
                        error "Docker CLI not found on this node!"
                    }
                    sh 'docker --version'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Docker Login & Push') {
            steps {
                script {
                    docker.withRegistry(DOCKER_REGISTRY, DOCKER_CREDENTIALS_ID) {
                        sh "docker push ${DOCKER_IMAGE}"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    def dockerPath = sh(script: 'which docker', returnStdout: true).trim()
                    if (!dockerPath) {
                        error "Docker CLI not found on this node at deploy stage!"
                    }
                    sh "docker run -d -p 5000:5000 ${DOCKER_IMAGE}"
                }
            }
        }
    }

    post {
        failure {
            echo "Build failed!"
        }
        success {
            echo "Build succeeded!"
        }
    }
}

