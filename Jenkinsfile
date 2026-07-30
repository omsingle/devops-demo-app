pipeline {
    agent any

    environment {
        IMAGE_NAME = "yuki982/devops-demo-app"
        IMAGE_TAG = "v1"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test Application') {
            agent {
                docker {
                    image 'python:3.12'
                }
            }

            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                export PYTHONPATH=$PWD
                pytest -v
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                '''
            }
        }
    }
}