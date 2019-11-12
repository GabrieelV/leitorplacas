# leitorplacas
Projeto para UNIVEL

Como instalar o container:
Após baixar e instalar o DOCKER e os arquivos do repositório, dentro da pasta onde está o arquivo Dockerfile, executar o comando do docker:

  docker build -t trabalho/openalpr . 

Após instalado o container, executar o comando abaixo para executa-lo, sendo que no parâmetro --device= deverá ser o caminho da webcam, no exemplo abaixo está no camimnho /dev/video0

  docker run --device=/dev/video0:/dev/video0 --network=host -it trabalho/openalpr bin/sh
  
Após executado o container, executar o comando abaixo para executar o leitor de placas:

  python3 executar.py
  
  
