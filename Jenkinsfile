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

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                export PYTHONPATH=$PWD
                pytest -v
                '''
            }
        }
    }
}