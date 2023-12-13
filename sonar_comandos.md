
## token pro sonar local

squ_d5fd3904ae90be1dad621088611e8c1fc3c75bc4

## token pro sonarr do Labens

squ_3201664bd8ef53633b174e1f169f1423c56d574a


## comando do sonar scanner local

sonar-scanner.bat -D"sonar.projectKey=squ_d5fd3904ae90be1dad621088611e8c1fc3c75bc4" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9000" -D"sonar.token=squ_d5fd3904ae90be1dad621088611e8c1fc3c75bc4"


## comando do site do sonar scanner

docker run \
    --rm \
    -e SONAR_HOST_URL="http://${SONARQUBE_URL}" \
    -e SONAR_SCANNER_OPTS="-Dsonar.projectKey=${YOUR_PROJECT_KEY}" \
    -e SONAR_TOKEN="myAuthenticationToken" \
    -v "${YOUR_REPO}:/usr/src" \
    sonarsource/sonar-scanner-cli

## comando pro sonar do Labens

docker run --rm -e SONAR_HOST_URL="http://labens.dct.ufrn.br/sonarqube" -e SONAR_LOGIN="squ_3201664bd8ef53633b174e1f169f1423c56d574a" -v "C:\Users\flavi\Documents\z_BACKUP\Arquivos\UFRN\12º Periodo 2023.2\testes\projeto\ace_api_2a_unidade\crud_django_para_teste:/usr/src" sonarsource/sonar-scanner-cli

