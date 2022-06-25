#!/bin/bash

# Como executar a aplicação localmente:
#
#   - Copie o arquivo 'config/env';
#   - Renomeie a cópia para 'env.dev';
#   - Preencha as variáveis de ambiente;
#   - Execute este 'run.sh'

source ./config/env.dev
python3 ./src/main.py