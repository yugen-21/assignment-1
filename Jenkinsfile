pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "shamaanjum/flask-app"
        DOCKER_CREDENTIALS_ID = "docker-hub-credentials"
        GIT_CREDENTIALS_ID = "34b9e838-e088-49f3-9cd6-0e4bfcfa0433"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', credentialsId: GIT_CREDENTIALS_ID, url: 'https://github.com/yugen-21/assignment-1.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat "pip install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                bat "pytest tests/"
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %DOCKER_IMAGE% ."
            }
        }

        stage('Push Image to Docker Hub') {
            when {
                expression { return currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                withDockerRegistry([credentialsId: DOCKER_CREDENTIALS_ID, url: '']) {
                    bat "docker login -u your-dockerhub-username -p your-password"
                    bat "docker push %DOCKER_IMAGE%"
                }
            }
        }

        stage('Deploy Application’) {
            steps {
                bat "docker-compose up -d --force-recreate"
            }
        }
    }
}
