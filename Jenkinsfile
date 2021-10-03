pipeline {
  agent any
     environment {
        AWS_REGION  = 'us-east-1'
        GITCOMMIT="${env.GIT_COMMIT.take(7)}"
        IMAGE="232452606882.dkr.ecr.us-east-1.amazonaws.com/nginx-example"
        APPNAME=example-enginx

    }

stages {

    stage('CI - docker build and push to ecr') {
      
      steps {

       sh(label: 'ECR login and docker push', script:
         '''
         #!/bin/bash
         
           echo "Authenticate with ECR"
            set +x # Don't echo credentials from the login command!
            echo "Building New ECR Image"
            eval $(aws ecr get-login --region "$AWS_REGION" --no-include-email)
            # Enable Debug and Exit immediately 
            set -xe
            echo $GITCOMMIT
            docker build  -t ${IMAGE}:${GITCOMMIT} .
            #two push one for master tag other is git commit ID
            docker push ${IMAGE}:${GITCOMMIT}
            docker tag ${IMAGE}:${GITCOMMIT} ${IMAGE}:latest
            docker push ${IMAGE}:latest
         '''.stripIndent())
 

      }
    }
    stage('CD -  into k8s') {
      
      steps {

       sh(label: 'push the container to k8s', script:
         '''
         #!/bin/bash
              
            helm status example-enginx && 
            helm upgrade --set applicationManifest.image=${IMAGE}:${GITCOMMIT} ${APPNAME} ./helm || 
            helm install --set applicationManifest.image=${IMAGE}:${GITCOMMIT} ${APPNAME} ./helm
         '''.stripIndent())
      }
    }
}
}