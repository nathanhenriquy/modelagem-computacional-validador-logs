# Checklist — Validador Formal em Três Níveis (Modelagem Computacional)

> **Tema escolhido:** Tema 2 (Logs e protocolos)
---

## 0. Logística e envio
- [x] Trabalho feito em **trio**
- [x] **Repositório GitHub público** criado
- [] **Link do repositório** postado no Blackboard
- [ ] **Vídeo no YouTube como _unlisted_** (10 a 12 min)
- [ ] **Link do vídeo** postado no Blackboard 
- [ ] **Relatório técnico em PDF**

---

## 1. Os três reconhecedores — exigências comuns
Para **cada um dos três níveis** (LR, LLC, R), conferir os 9 itens abaixo:

### 1.1 Nível LR — Sequência de eventos (DFA)
> Começa com `LOGIN`, seguido de `AUTH`, seguido de **zero ou mais** `REQUEST`, terminando com `LOGOUT`.
> Aceito: `LOGIN AUTH REQUEST REQUEST LOGOUT` · Rejeitado: `LOGIN LOGOUT AUTH`

- [ ] 1. Descrição em português da linguagem
- [ ] 2. Definição formal em notação matemática (`{w ∈ Σ* | …}` ou equivalente)
- [ ] 3. Alfabeto utilizado (tokens: `LOGIN`, `AUTH`, `REQUEST`, `LOGOUT`)
- [ ] 4. Exemplos de cadeias aceitas e rejeitadas
- [ ] 5. Modelo (**DFA**) com **tabela de transição completa** + **diagrama**
- [ ] 6. Implementação em Python
- [ ] 7. Testes automatizados
- [ ] 8. Execução passo a passo de **uma aceita** e **uma rejeitada**
- [ ] 9. Número de passos consumidos pelo programa em cada teste

### 1.2 Nível LLC — Blocos aninhados de transação (Pilha/PDA/GLC)
> Cada `BEGIN` precisa de um `END` correspondente, podendo aninhar.
> Aceito: `BEGIN BEGIN END END` · Rejeitado: `BEGIN END END`

- [ ] 1. Descrição em português da linguagem
- [ ] 2. Definição formal em notação matemática
- [ ] 3. Alfabeto utilizado (`BEGIN`, `END`)
- [ ] 4. Exemplos de cadeias aceitas e rejeitadas
- [ ] 5. Modelo (**PDA/GLC**) com **transições principais + evolução da pilha** + **diagrama**
- [ ] 6. Implementação em Python
- [ ] 7. Testes automatizados
- [ ] 8. Execução passo a passo de **uma aceita** e **uma rejeitada**
- [ ] 9. Número de passos consumidos pelo programa em cada teste

### 1.3 Nível R — Trio balanceado (Máquina de Turing)
> `L = { OPEN^n COMMIT^n CLOSE^n | n ≥ 1 }`
> Aceito: `OPEN OPEN COMMIT COMMIT CLOSE CLOSE` · Rejeitado: `OPEN COMMIT CLOSE CLOSE`

- [ ] 1. Descrição em português da linguagem
- [ ] 2. Definição formal em notação matemática
- [ ] 3. Alfabeto utilizado (`OPEN`, `COMMIT`, `CLOSE` + símbolos de fita/branco)
- [ ] 4. Exemplos de cadeias aceitas e rejeitadas
- [ ] 5. Modelo (**MT**) com **tabela de transição completa** + **diagrama**
- [ ] 6. Implementação em Python
- [ ] 7. Testes automatizados
- [ ] 8. Execução passo a passo de **uma aceita** e **uma rejeitada**
- [ ] 9. Número de passos consumidos pelo programa em cada teste

---

## 2. Regras de implementação (atenção — fácil perder pontos aqui)
- [ ] **Implementação manual obrigatória**: cada reconhecedor é um **simulador do autômato** (DFA, PDA ou MT)
- [ ] Estados, alfabeto(s), estado inicial, estados finais e tabela de transição **declarados explicitamente como dados** (dicionários/conjuntos) — **não** como sequência de `if/else`
- [ ] O programa **aplica a função de transição símbolo a símbolo** (ou movimento a movimento, na MT)
- [ ] **`re` NÃO** pode ser o reconhecedor principal em nenhum dos três níveis
- [ ] No LR, `re` só pode aparecer como **comparação opcional (bônus)** — nunca como engine de aceitação/rejeição
- [ ] Bibliotecas auxiliares (Graphviz, pytest, matplotlib) são bem-vindas, mas **não substituem** o reconhecedor

### 2.1 Definição operacional de "passo" (contador exclusivo)
- [ ] **DFA/NFA**: incrementa a cada leitura de símbolo **com mudança de estado**
- [ ] **PDA**: incrementa a cada transição, **contando empilhamento e desempilhamento**
- [ ] **MT**: incrementa a cada **movimento da cabeça** (leitura, escrita, deslocamento)
- [ ] O contador **NÃO** conta iterações do laço Python nem linhas executadas

---

## 3. Bateria de testes
- [ ] **LR**: 3 cadeias aceitas + 3 rejeitadas
- [ ] **LLC**: 3 cadeias aceitas + 3 rejeitadas
- [ ] **R**: 3 cadeias aceitas + 3 rejeitadas
- [ ] **Total = 18 cadeias**
- [ ] Incluir **casos de borda** quando fizer sentido (cadeia vazia, tamanho 1, no limite da regra)
- [ ] O programa imprime **tabela esperado vs obtido** para cada teste
- [ ] O programa informa o **número de passos** executados em cada cadeia
- [ ] Reconhecedor robusto a **cadeias-surpresa** (mesmo alfabeto e definição formal) — até **0,25 ponto** reservado a isso

---

## 4. Estrutura do repositório
```
projeto/
  README.md
  requirements.txt
  src/
    regular.py
    livre_contexto.py
    recursiva.py
    testes.py
  testes/
    testes_regular.txt
    testes_livre_contexto.txt
    testes_recursiva.txt
  diagramas/
    dfa_regular.(png|svg|pdf|tex)
    pda_livre_contexto.(png|svg|pdf|tex)
    mt_recursiva.(png|svg|pdf|tex)
  relatorio/
    relatorio.pdf
```
- [ ] `README.md` presente
- [ ] `requirements.txt` presente
- [ ] `src/regular.py`, `src/livre_contexto.py`, `src/recursiva.py`, `src/testes.py`
- [ ] `testes/` com os 3 arquivos `.txt`
- [ ] `diagramas/` com os 3 diagramas (DFA, PDA, MT)
- [ ] `relatorio/relatorio.pdf`
- [ ] Cada reconhecedor tem **modo de execução autônomo** (ex.: `python src/regular.py "LOGIN AUTH REQUEST LOGOUT"`)
- [ ] `testes.py` lê `testes/*.txt` e roda contra os 3 reconhecedores
- [ ] README permite rodar a **bateria completa em um único comando**
- [ ] Diagramas em PNG/SVG/PDF ou código TikZ/Graphviz — **fotos de quadro/papel NÃO são aceitas**

---

## 5. Relatório técnico (PDF, 4 a 7 páginas)
- [ ] 1. Introdução e contexto aplicado
- [ ] 2. LR escolhida: descrição, definição formal, modelo, exemplos
- [ ] 3. LLC escolhida: descrição, definição formal, modelo, exemplos
- [ ] 4. R escolhida: descrição, definição formal, modelo, exemplos
- [ ] 5. Modelos formais e transições (tabelas e diagramas dos três)
- [ ] 6. Implementação (visão geral do código, decisões principais)
- [ ] 7. Testes e resultados (tabela esperado vs obtido, número de passos)
- [ ] 8. Comparação entre os três níveis da hierarquia (`LR ⊊ LLC ⊊ R`)
- [ ] 9. Conclusão e limitações
- [ ] Detalha a **execução passo a passo de uma aceita e uma rejeitada por linguagem**
- [ ] Total entre **4 e 7 páginas**

---

## 6. Vídeo de apresentação (10 a 12 min, _unlisted_)
Conteúdo obrigatório:
- [ ] 1. Contexto aplicado
- [ ] 2. Explicação das três linguagens escolhidas
- [ ] 3. Modelos formais usados
- [ ] 4. Demonstração do programa rodando a bateria
- [ ] 5. Resultados dos testes
- [ ] 6. Comparação entre LR, LLC e R

Divisão de fala (obrigatória):
- [ ] Cada integrante apresenta **pelo menos um dos três níveis** (LR, LLC ou R)
- [ ] Cada fala inclui **modelo formal + implementação + ao menos um teste** do nível
- [ ] Abertura (contexto) e fechamento (comparação) distribuídos livremente
- [ ] **Todos os 3 integrantes falam** (ausência → perda da nota individual de apresentação)
- [ ] **Não** é leitura linha por linha do código
- [ ] Duração entre **10 e 12 minutos**

---

## 7. Bônus opcional (até +0,5, teto de 5,0)
- [ ] Interface em Streamlit ou Gradio para testar cadeias nos três reconhecedores
- [ ] Visualização animada do autômato / pilha / fita da MT
- [ ] Minimização do DFA do nível LR
- [ ] Comparação direta DFA manual × módulo `re` na linguagem LR
- [ ] Segunda MT (ex.: `a^n b^n c^n`, palíndromos binários, ou a MT `w#w` do Tema 1)
- [ ] Discussão do crescimento do nº de passos em função do tamanho da entrada
- [ ] Prova de não-regularidade via **Lema do Bombeamento** aplicada à LLC ou R *(estritamente bônus)*
- [ ] Uso de Lark, pyformlang ou JFLAP apenas como comparação

---

### Conferência final rápida
- [ ] 3 reconhecedores × 9 itens = tudo coberto
- [ ] 18 cadeias de teste no total
- [ ] Tabela esperado vs obtido + contagem de passos imprimindo corretamente
- [ ] Repositório bate com a árvore de pastas exigida
- [ ] Relatório dentro de 4–7 páginas com as 9 seções
- [ ] Vídeo 10–12 min com fala dos 3 integrantes
- [ ] Links (repo + vídeo) no Blackboard **antes do dia 10**