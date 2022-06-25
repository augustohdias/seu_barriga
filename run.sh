#!/bin/bash

# Como executar a aplicação:
#   Copie o arquivo 'env' do diretorio config e renomeio para 'env.dev'
#   Preencha com as variáveis de teste e execute este script

source ./config/env.dev
python3 ./src/main.py