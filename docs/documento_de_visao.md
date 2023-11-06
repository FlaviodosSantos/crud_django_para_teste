# Documento de Visão

Documento construído a partido do **Modelo BSI - Doc 001 - Documento de Visão** que pode ser encontrado no
link: https://docs.google.com/document/d/1DPBcyGHgflmz5RDsZQ2X8KVBPoEF5PdAz9BBNFyLa6A/edit?usp=sharing

## Equipe e Definição de Papéis

Membro     |     Papel   |   E-mail   |
---------  | ----------- | ---------- |
Taciano    | Cliente Professor  | taciano@bsi.ufrn.br
Flavio     | Analista, Testador | flavio.santos.009@ufrn.gov.br


### Matriz de Competências

Membro     |     Competências   |
---------  | ----------- |
Flavio     | Gestão, Desenvolvedor Django |

## Perfis dos Usuários

O sistema poderá ser utilizado por diversos usuários. Temos os seguintes perfis/atores:

Perfil                                 | Descrição   |
---------                              | ----------- |
Administrador | Este usuário realiza os cadastros base e pode realizar qualquer função.
Chefe | Este usuário utiliza o sistema para cadastrar as zonas, os agentes e o índice.
Agente | Este usuário utiliza utiliza o sistema para cadastrar os quarteirões e bairros.

## Lista de Requisitos Funcionais

Requisito                                 | Descrição   | Ator |
---------                                 | ----------- | ---------- |
RF001 - Manter um cadastro de chefes     | Manter um cadastro de chefe com os atributos matricula, nome e zonas. | Administrador |
RF001 - Manter um cadastro de agentes     | Manter um cadastro de agente com os atributos matricula, nome e zona. | Chefe |
RF002 - Manter um cadastro de Zonas | Manter cadastro das zonas com os atributos numero e quarteirões. | Chefe |
RF003 - Manter o cadastro de Quarteirões | Manter cadastro da quarteirão com os atributos numero, bairro e numero de imoveis . | Agente |
RF004 - Manter cadastro de Bairros | manter cadastro de bairro com atributos codigo, nome e numero de imoveis. | Chefe |
RF005 - Manter o cadastro de Índice | manter cadastro do indice por bairro. | Chefe |

### Modelo Logico

Abaixo apresentamos o modelo logico.

 ![Modelo Conceitual](images/logico_2.png)


#### Descrição das Entidades

## Lista de Requisitos Não-Funcionais

Requisito                                 | Descrição   |
---------                                 | ----------- |
RNF001 - Deve ser acessível via navegador | Deve abrir perfeitamento no Firefox e no Chrome. |
RNF002 - Consultas deve ser eficiente | O sistema deve executar as consultas em milessegundos |
RNF003 - Log e histórico de acesso e funções | Deve manter um log de todos os acessos e das funções executadas pelo usuário |

## Riscos

Tabela com o mapeamento dos riscos do projeto, as possíveis soluções e os responsáveis.

Data | Risco | Prioridade | Responsável | Status | Providência/Solução |
------ | ------ | ------ | ------ | ------ | ------ |
10/11/2023 | Não aprendizado das ferramentas utilizadas pelos componentes do grupo | Alta | Todos | Vigente | Reforçar estudos sobre as ferramentas e aulas com a integrante que conhece a ferramenta |
10/11/2023 | Ausência por qualquer motivo do cliente | Média | Gerente | Vigente | Planejar o cronograma tendo em base a agenda do cliente |
10/11/2023 | Divisão de tarefas mal sucedida | Baixa | Gerente | Vigente | Acompanhar de perto o desenvolvimento de cada membro da equipe |
10/11/2023 | Implementação de protótipo com as tecnologias | Alto | Todos | Resolvido | Encontrar tutorial com a maioria da tecnologia e implementar um caso base do sistema |

### Referências