# Aplicação web com Flask e Gcloud DataStore


## 🏁 Tópicos

<!--ts-->
   * [Rodando o projeto localmente](#rodando-o-projeto-localmente)
   * [Como executar o emulador do Datastore](#como-executar-o-emulador-do-datastore)
   * [Como usar o servidor de desenvolvimento local](#como-usar-o-servidor-de-desenvolvimento-local)
   * [Implantação do aplicativo para o gcloud appengine](#implantação-do-aplicativo-para-o-gcloud-appengine)
   * [Pré-requisitos](#pré-requisitos)
   * [Instalando o componente Gcloud App Engine Python](#instalando-o-componente-gcloud-app-engine-python)
   * [Criando um novo projeto](#criando-um-novo-projeto)
   * [Vinculando-se a um projeto existente](#vinculando-se-a-um-projeto-existente)
   * [Empurrando seu aplicativo para a Nuvem do Google](#empurrando-seu-aplicativo-para-a-nuvem-do-google)
<!--te-->


## Rodando o projeto localmente:
<br>


#### Como executar o emulador do Datastore:
<br>
Para usar o emulador do Datastore, serão necessários:

* um JRE Java, versão 8 ou superior;
* A Google Cloud CLI
* um aplicativo criado com Bibliotecas de cliente do Google Cloud.
<br><br>

#### Instalação do emulador Datastore:
O emulador do Datastore é um componente da CLI gcloud da CLI do Google Cloud. Use o comando gcloud components install para instalar o emulador do Datastore:

    gcloud components install cloud-datastore-emulator

<br>

#### Iniciar o emulador:
Para iniciar o emulador, execute datastore start em um prompt de comando:

    gcloud beta emulators datastore start
<br>
Por padrão o servidor irá rodar na porta 8081
<br><br>

### Como usar o servidor de desenvolvimento local:
<br>
A Google Cloud CLI inclui um servidor de desenvolvimento local (dev_appserver.py), que você pode usar para simular a execução do aplicativo no App Engine de produção ou acessar serviços incluídos do App Engine.
<br>
<br>

#### Inclua as seguintes variáveis de ambiente no seu arquivo app.yaml: 

    env_variables:
        DATASTORE_DATASET:
        DATASTORE_EMULATOR_HOST: localhost:8081
        DATASTORE_EMULATOR_HOST_PATH: localhost:8081/datastore
        DATASTORE_HOST:
        DATASTORE_PROJECT_ID:
<br>

#### Para iniciar o servidor de desenvolvimento local:

Execute o comando dev_appserver.py da seguinte maneira no diretório que contém o arquivo de configuração app.yaml do aplicativo:

    dev_appserver.py .

Ou especificando o arquivo a ser executado:

    dev_appserver.py app.yaml
<br>

## Implantação do aplicativo para o gcloud appengine
<br>

#### Pré-requisitos:

* SDK gcloud atualizado instalado no seu sistema: https://cloud.google.com/sdk/install

* Componente Gcloud App Engine Python

* Projeto gcloud criado e vinculado

* Instancia Gcloud Datastore criada: https://cloud.google.com/datastore/docs/store-query-data?hl=pt-br

#### Instalando o componente Gcloud App Engine Python:

A partir do Google Cloud SDK Shell (iniciado com permissões administrativas)

     gcloud components install app-engine-python

#### Criando um novo projeto:

Se você ainda não criou um projeto gcloud, você pode fazer isso a partir de https://console.cloud.google.com ou da linha de comando de seus computadores usando o SDK. Se você já criou o projeto via https://console.cloud.google.com você precisará realizar a vinculação a um projeto existente. Se, em vez disso, você usar a linha de comando SDK em seu computador, isso será feito para você.

     gcloud create project PROJECT-NAME

substituindo o PROJECT-NAME pelo nome do seu próprio projeto.

##### Vinculando-se a um projeto existente:

De qualquer ferramenta de linha de comando\terminal:

     gcloud config set project PROJECT-NAME

substituindo o PROJECT-NAME pelo nome do seu próprio projeto.

Ativar a Cloud Build Api no projeto com o comando:

     gcloud services enable cloudbuild.googleapis.com

### Empurrando seu aplicativo para a Nuvem do Google:

Agora que seu ambiente local do Google foi configurado para apontar para o projeto app-engine correto, mude para sua pasta de projeto e digite o seguinte código em seu terminal local/shell/cli para empurrar seu projeto para o projeto em sua Conta Google Cloud.

     gcloud app deploy

Para ver seu aplicativo publicado, você pode usar o seguinte código em seu terminal/shell/cli

     gcloud app browse

Ou você pode visitar https://YOUR-PROJECT.appspot.com, substituindo seus projetos pelo seu próprio nome de projetos.