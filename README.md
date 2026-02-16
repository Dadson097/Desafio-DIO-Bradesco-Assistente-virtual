# 🎓 Assistente Financeiro Personalizado

> Versão adaptada do Edu - Agora focado em **controle de gastos pessoais** com interface amigável!

## 💡 Sobre este Projeto

Este é meu assistente financeiro pessoal, adaptado do projeto original Edu. 
Ele me ajuda a controlar gastos, analisar orçamento e dar dicas de economia 
usando MEUS dados financeiros reais.

### ✨ Funcionalidades Adaptadas:
- ✅ **Análise de gastos pessoais** com dados reais
- ✅ **Comparação com orçamento** mensal
- ✅ **Dicas personalizadas** baseadas nos meus padrões de gasto
- ✅ **Interface de coleta de dados** integrada
- ✅ **100% local** - meus dados não saem do meu PC

## 🏗️ Estrutura do Projeto

Desafio-DIO-Bradesco-Assistente-virtual/
│
├── 📁 data/ # Seus dados pessoais (NÃO sobem para o GitHub)
│ ├── perfil_financeiro.json # Sua renda mensal e metas de economia
│ ├── transacoes.csv # Todas as suas transações financeiras
│ ├── historico_atendimento.csv # Histórico das conversas com o assistente
│ └── dicas_orcamento.json # Base de conhecimento personalizada
│
├── 📁 docs/ # Documentação completa do projeto
│ ├── 01-documentacao-agente.md # Persona e comportamento do assistente
│ ├── 02-base-conhecimento.md # Estrutura e uso dos dados
│ ├── 03-prompts.md # Comandos e respostas esperadas
│ └── 04-metricas.md # Métricas de avaliação
│
├── 📁 src/ # Código fonte
│ └── assistente.py # Aplicação principal em Streamlit
│
├── 📁 examples/ # Exemplos para referência
│ ├── exemplo_transacoes.csv # Formato esperado das transações
│ └── exemplo_perfil.json # Formato esperado do perfil
│
├── .gitignore # Arquivos ignorados pelo Git
├── README.md # Esta documentação
└── requirements.txt # Dependências do projeto
