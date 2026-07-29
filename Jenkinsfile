pipeline {
    agent {
    docker {
        image 'python:3.12'
    }
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

        echo "===== CURRENT DIRECTORY ====="
        pwd

        echo "===== FILES ====="
        ls -la
        ls -la app

        echo "===== PYTHON VERSION ====="
        python --version

        echo "===== PYTHON PATH ====="
        python -c 'import sys; print(sys.path)'

        echo "===== IMPORT TEST ====="
        python -c 'from app.main import app; print("Import OK")'

        echo "===== RUN PYTEST ====="
        pytest -v
        '''
    }
}
    }
}