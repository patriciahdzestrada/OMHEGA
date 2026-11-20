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
                    set -e
                    mkdir -p reports

                    docker run --rm \
                      -e PYTHONPATH=/app/src \
                      -v "${WORKSPACE}/reports:/app/reports" \
                      omhega:${BUILD_NUMBER} \
                      bash -c '
                        set +e
                        python -m pytest -v --junitxml=/app/reports/junit.xml
                        EXIT_CODE=$?
                        set -e

                        python - << "PYEOF"
import csv, xml.etree.ElementTree as ET
from pathlib import Path

xml_path = Path("/app/reports/junit.xml")
csv_path = Path("/app/reports/test_results.csv")
rows = []

if xml_path.exists():
    root = ET.parse(xml_path).getroot()
    suites = [root] if root.tag == "testsuite" else root.findall("testsuite")
    for suite in suites:
        for case in suite.findall("testcase"):
            status = "passed"
            detail = ""
            if case.find("failure") is not None:
                status = "failed"
                detail = case.find("failure").attrib.get("message", "")
            elif case.find("error") is not None:
                status = "error"
                detail = case.find("error").attrib.get("message", "")
            elif case.find("skipped") is not None:
                status = "skipped"
                detail = case.find("skipped").attrib.get("message", "")
            rows.append({
                "classname": case.attrib.get("classname", ""),
                "name": case.attrib.get("name", ""),
                "time_s": case.attrib.get("time", ""),
                "status": status,
                "detail": detail
            })

with csv_path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["classname", "name", "time_s", "status", "detail"])
    writer.writeheader()
    writer.writerows(rows)
PYEOF

                        exit $EXIT_CODE
                      '
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