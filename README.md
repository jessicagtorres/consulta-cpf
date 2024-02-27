# consulta-cpf

**Visão Geral**

Este programa permite aos usuários consultarem um CPF Lover (programa de fidelidade da Cacau Show) e visualizar informações associadas, como nome, nível, descrição do nível e promoções disponíveis interagindo com uma API web.

**Instalação e Configuração**

Baixe o código-fonte do programa.  
Instale as dependências necessárias listadas no arquivo requirements.txt.  
Execute o programa a partir da linha de comando utilizando o seguinte comando:  
```python consulta-cpf.py```

**Guia do Usuário**

Abra o programa "Consulta de CPF".  
Insira o CPF que deseja consultar.  
Clique no botão "Consultar CPF".  
Os detalhes associados ao CPF consultado serão exibidos na área de resultados.  
Caso o CPF tenha alguma promoção vinculada, o código referente a promoção será apresentado junto com a quantidade de resgates efetuados e o ID para consulta no banco de dados a fim de verificar se a promoção já foi resgatada anteriormente.  

**Referência de API**  
O programa interage com a seguinte API web:

URL: https://cacaudigital.azure-api.net/Loyalty.gateway.api/Cadastro/  
Chave de autenticação: ECX3ykaPZvlkneCxPwZV74EmZXY6sFSDXXWsEf8LTFve-47PGhkwkX9Fw3nWwOtEjzvaphPBWalZgVNMEHvbLA
