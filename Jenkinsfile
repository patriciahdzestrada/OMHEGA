pipeline {
    agent any

    stages {

        stage('Verificar Docker') {
            steps {
                sh '''
                    set -e
                    echo "Verificando Docker..."
                    docker --version
                    docker info
                '''
            }
        }

        stage('Construir imagen Docker') {
            steps {
                sh '''
                    set -e
                    docker build -t omhega:${BUILD_NUMBER} .
                '''
            }
        }

        stage('Ejecutar Tests') {
            steps {
                sh '''
                    mkdir -p reports

                    docker run --rm \
                    -v "${WORKSPACE}/reports:/app/reports" \
                    omhega:${BUILD_NUMBER} \
                    python -m pytest -v \
                    --junitxml=/app/reports/junit.xml
                '''
            }
        }
    }

    post {
        always {

            junit(
                testResults: 'reports/junit.xml',
                allowEmptyResults: true
            )

            archiveArtifacts(
                artifacts: 'reports/*',
                allowEmptyArchive: true,
                fingerprint: true
            )
        }
    }
}