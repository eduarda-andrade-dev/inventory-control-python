# 📦 Sistema de Controle de Estoque

Aplicação via terminal (CLI) desenvolvida em Python para gestão de almoxarifado, focada na rastreabilidade de produtos e prevenção de falhas operacionais através de validação rigorosa de dados.

Projeto acadêmico desenvolvido no curso de Análise e Desenvolvimento de Sistemas (UNINTER), com nota máxima (100/100) baseada no rigor lógico e critérios de aceitação.

---

## O problema

Falhas humanas no registro de entradas e saídas geram saldos negativos, perda de rastreabilidade e furos de inventário em almoxarifados. Sistemas que não validam a quantidade disponível antes de uma retirada comprometem toda a cadeia de suprimentos.

## A solução

Um sistema focado na integridade dos dados que processa movimentações em tempo real. Suas principais travas incluem:
- **Prevenção de saldos negativos:** O sistema bloqueia movimentações caso o saldo seja insuficiente.
- **Rastreabilidade total:** Registro obrigatório da data da movimentação e do nome do responsável ao confirmar uma saída.
- **Tratamento de Exceções:** Sistema blindado contra entradas inválidas (como letras no lugar de números ou formatos de data incorretos), garantindo que a aplicação não trave durante o uso.

## Como foi feito

O desenvolvimento simulou um ambiente corporativo real, seguindo metodologias ágeis:
1. **Scrum e Kanban:** Organização do fluxo de trabalho (Backlog, To Do, In Progress, Testing, Done).
2. **Engenharia de Requisitos:** Levantamento de necessidades estruturado através de Histórias de Usuário e Critérios de Aceitação.
3. **Desenvolvimento:** Codificação em Python focada em estruturas de dados e blocos de decisão lógicos.

## Tecnologias

- Python
- Engenharia de Requisitos (User Stories)
- Metodologias Ágeis (Scrum / Kanban)
- Lógica de Programação

## Aprendizados

A principal lição deste projeto foi a aplicação prática de tratamentos de erros (try/except) para garantir a estabilidade do software. Traduzir as regras de negócio de um almoxarifado físico para a lógica de código reforçou a importância de prever o comportamento (e os possíveis erros) do usuário final.