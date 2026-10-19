pipeline {
    agent any

    environment {
        STUDENT_NAME    = 'Bakhtjan'
        STUDENT_SURNAME = 'Apsatarov'
        STUDENT_GROUP   = 'IT2-2314'
        STUDENT_ID      = '37510'
        IMAGE_NAME      = 'apsatarov-bakhtjan-devops'
        CONTAINER_NAME  = 'apsatarov-bakhtjan-container'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "Student: ${STUDENT_NAME} ${STUDENT_SURNAME}"
                echo "Group: ${STUDENT_GROUP}"
                echo "Student ID: ${STUDENT_ID}"
                sh 'git log -1 --oneline'
            }
        }

        stage('Build') {
            steps {
                sh 'ls -la'
                sh 'bash scripts/Apsatarov_Bakhtjan_system.sh'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    bash -n scripts/Apsatarov_Bakhtjan_system.sh && echo "Bash script syntax OK"
                    python3 -B -c "import ast; ast.parse(open('app/app.py').read()); print('Python syntax OK')"
                    test -f Dockerfile && echo "Dockerfile found"
                    test -f Apsatarov_Bakhtjan_info.txt && echo "Student info file found"
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t ${IMAGE_NAME} .'
                sh 'docker images ${IMAGE_NAME}'
            }
        }

        stage('Docker Run') {
            steps {
                sh '''
                    docker rm -f ${CONTAINER_NAME} || true
                    docker run -d --name ${CONTAINER_NAME} -p 8002:8000 \
                        -e STUDENT_NAME=${STUDENT_NAME} \
                        -e STUDENT_SURNAME=${STUDENT_SURNAME} \
                        -e STUDENT_GROUP=${STUDENT_GROUP} \
                        -e STUDENT_ID=${STUDENT_ID} \
                        ${IMAGE_NAME}
                    sleep 3
                    docker ps --filter name=${CONTAINER_NAME}
                    docker logs ${CONTAINER_NAME}
                    curl -s http://localhost:8002 || true
                '''
            }
        }
    }

    post {
        success { echo 'Pipeline finished successfully!' }
        failure { echo 'Pipeline FAILED. Check the stage that is marked red.' }
    }
}
