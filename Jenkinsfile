pipeline {
    agent any

    environment {
        REGISTRY_USERNAME = "mmahmadi0101"
        REGISTRY_PASSWORD = credentials('dockerhub_password')   
        REGISTRY = "${REGISTRY_USERNAME}/ideablog"
        GIT_REPO_URL = "https://gitlab.com/mm.ahmadi0101/ideablog.git"
        containerID = ''
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM', 
                    branches: [[name: '*/dev']], 
                    doGenerateSubmoduleConfigurations: false, 
                    extensions: [], 
                    submoduleCfg: [], 
                    userRemoteConfigs: [[url: "${GIT_REPO_URL}"]]
                ])
            }
        }
        
        stage('Build and Run Container') {
            steps {
                script {
                    sh 'echo ${REGISTRY_USERNAME}'
                    sh 'docker-compose up -d --build'
                    containerID = sh(script: 'docker-compose ps -q back', returnStdout: true).trim()
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    def testExitCode = sh(script: "docker exec ${containerID} python manage.py test", returnStatus: true)
                    if (testExitCode != 0) {
                        error('Tests failed!')
                    }
                }
            }
        }

        stage('Deploy to Docker Hub') {
            steps {
                script {
                    sh """
                        echo ${REGISTRY_PASSWORD} | docker login -u ${REGISTRY_USERNAME} --password-stdin
                        docker push ${REGISTRY}:${BUILD_NUMBER}
                        docker tag ${REGISTRY}:${BUILD_NUMBER} ${REGISTRY}:latest
                        docker push ${REGISTRY}:latest
                    """
                }
            }
        }
    }
    
    post {
        always {
            sh '''
                docker-compose down
                docker rmi ${REGISTRY}:${BUILD_NUMBER}
                docker rmi ${REGISTRY}:latest
                docker logout
            '''
            cleanWs()
        }
    }
}
