pipeline {
	agent any

	stages {
		stage('Preparation') {
			steps {
				sh 'which docker-compose || curl -L "https://github.com/docker/compose/releases/download/v2.23.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose'
                sh 'chmod +x /usr/local/bin/docker-compose'
			}
		}
		stage('UnitTest') {
			agent {
				dockerfile {
					filename 'Dockerfile'
				}
			}
			steps {
				sh 'python3 -m unittest unitstest.py'
			}
		}
		stage('UITest') {
			steps {
				sh 'docker-compose up --build -d'
				sh 'docker-compose exec -T app sh -c "python3 -m unittest -v seleniumtest.py"'
			}
		}
		stage('OWASP-DC') {
			steps {
				dependencyCheck additionalArguments: '''
						--disableYarnAudit
							-o './'
							-s './'
							-f 'ALL'
							--prettyPrint''', odcInstallation: 'OWASP-DC'

				dependencyCheckPublisher pattern: 'dependency-check-report.xml'
			}
		}
		stage('Code Quality Check via SonarQube') {
			steps {
				script {
					def scannerHome = tool 'SonarQube';
					withSonarQubeEnv('SonarQube') {
						sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=OWASP -Dsonar.sources=."
					}
				}
			}
		}
	}
	post {
		always {
			step([$class: 'DependencyCheckPublisher', pattern: '**/dependency-check-report.xml'])
			recordIssues enabledForFailure: true, tool: sonarQube()
		}
	}
}
