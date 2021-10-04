library("shared-library")
ECRlogin_PUSH()

pipeline {
  agent any
     environment {
        AWS_REGION = "us-east-1"
        GITCOMMIT = "${env.GIT_COMMIT.take(7)}"
        IMAGE = "232452606882.dkr.ecr.us-east-1.amazonaws.com/nginx-example"
        APPNAME = "example-enginx"

    }

stages {

    stage('CI - docker build and push to ecr') {
      
      steps {
        script{
         ECRlogin_PUSH(AWS_REGION:$AWS_REGION,GITCOMMIT:$GITCOMMIT,IMAGE:$IMAGE)
      }
      }
    }
    stage('CD -  into k8s') {
      
      steps {

       sh(label: 'push the container to k8s', script:
         '''
         #!/bin/bash
              
            helm status example-enginx && 
            helm upgrade   !!!!!!     CHANGE TO -i !!!!!!   --set applicationManifest.image=${IMAGE}:${GITCOMMIT} ${APPNAME} ./helm || 
            helm install --set applicationManifest.image=${IMAGE}:${GITCOMMIT} ${APPNAME} ./helm
         '''.stripIndent())
      }
    }
}
}