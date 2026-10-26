
pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-southeast-1'
        ECR_REGISTRY = '709860105788.dkr.ecr.ap-southeast-1.amazonaws.com'
        ECR_REPOSITORY = 'college-management-system'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                sh '''
                    set -e
                    docker build -t ${ECR_REPOSITORY}:${IMAGE_TAG} .
                '''
            }
        }

        stage('Django Checks and Tests') {
            steps {
                sh '''
                    set -e
                    docker run --rm ${ECR_REPOSITORY}:${IMAGE_TAG} \
                        python manage.py check
                    docker run --rm ${ECR_REPOSITORY}:${IMAGE_TAG} \
                        python manage.py test main_app
                '''
            }
        }

        stage('Push Image to Amazon ECR') {
            steps {
                sh '''
                    set -e
                    aws ecr get-login-password --region ${AWS_REGION} |
                        docker login --username AWS --password-stdin ${ECR_REGISTRY}

                    docker tag ${ECR_REPOSITORY}:${IMAGE_TAG} \
                        ${ECR_REGISTRY}/${ECR_REPOSITORY}:${IMAGE_TAG}

                    docker push ${ECR_REGISTRY}/${ECR_REPOSITORY}:${IMAGE_TAG}
                '''
            }
        }

        // Deployment stage will be added after verifying the EC2 target.
    }
}
