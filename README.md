Burocracia de implementação:
 - Definição do MVP 
   - Fazer uma panela de macarrao cozido.

 - Escolha de linguagem
   - python

 - Regra de negocio
    - Blocos
      - preparo do material
      - cozimento do macarrao
    - Componentes (processos que definem funcionalidades do projeto)
      [preparo]
      - pegar panela
      - encher panela de agua
      - pegar macarrao
      [execuçao]
      - criar fogo
      - ferver agua
      - colocar macarrao na panela
      - cozinhar o macarrao
    - Funcionalidades (subfuncionalidades tecnicas de cada um dos componentes)
      - definir panela a partir do tamanho
      - definir tipo e quantidade(espaço) de macarrão, tempo de cozimento 
      - verificar se cabe na panela

 - Definição da arquitetura do projeto
   - arquitetura hexagonal
    - familiaridade
    - modularização
    - queremos aprender
    - escalabilidade
    
 - Projeto
    - Project manger
     -poetry
        -simplicidade
    - Modularização  
      {  
        domain:{  
          models,  
          services:{  
            preparo,  
            execução  
          },  
          infrastructure,  
          usecases  
        }  
      }  

  - Automatização de comandos

 - Desing de codigo
    - models:  
      -panela (
          tamanho, 
          tem agua(bool), 
          agua fervendo(bool), 
          tem macarrao(bool)
        )
      - macarrao (
          tipo, 
          porção, 
          tempo de cozimento, 
          #cabe(bool)#, 
          cozido(bool)
        )

    - services preparo:
      - pegar panela -> Panela 
      - pegar macarrao -> macarrao (verificar se cabe)
      - encher a panela com agua -> panela1 

    - services de execucao
      - criar fogo -> #Fogo# 
      - esquentar agua -> Panela - verificar se tem agua
      - colocar o macarrao -> Panela
      - cozinhar o macarrao -> esperar tempo de cozimento -> macarrao

      