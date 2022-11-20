pipeline {
    agent any
    environment {
    DOCKER_TAG = getDockerTag()
    }
    stages{
        stage ("Build stage"){
            steps{
                sh "docker-compose build"
        sh "docker tag avl_backend:latest ezmamig/avl_backend:${DOCKER_TAG}"
        sh "docker tag avl_client:latest ezmamig/avl_client:${DOCKER_TAG}"
            }
        }
        stage ("Unit tests stage"){
            steps{
                sh 'echo "Mock unit tests"'
            }
        }
        stage ("Integration tests stage"){
            steps{
                sh 'echo "Mock integration tests"'
            }
        }
        stage ("Publish docker images"){
            steps{
                withCredentials([string(credentialsId: 'docker-hub', variable: 'dockerHubPassword')]) {
                    sh "docker login -u ezmamig -p ${dockerHubPassword}"
                    sh "docker push ezmamig/avl_backend:${DOCKER_TAG}"
                    sh "docker push ezmamig/avl_client:${DOCKER_TAG}"
                }
            }
        }
        stage ("Cleanup"){
            steps{
                sh "docker rmi -f avl_backend:latest"
                sh "docker rmi -f avl_client:latest"
                sh "docker rmi -f ezmamig/avl_backend:${DOCKER_TAG}"
                sh "docker rmi -f ezmamig/avl_client:${DOCKER_TAG}"
            }
        }
    }
}

def getDockerTag() {
    def tag = sh script: 'git rev-parse HEAD', returnStdout: true
    return tag
}
