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

📁 Desafio-DIO-Bradesco-Assistente-virtual/
├── 📁 data/                          # SEUS DADOS (ignorados no git)
│   ├── perfil_financeiro.json        # Sua renda e metas
│   ├── transacoes.csv                # Seu histórico de gastos
│   ├── historico_atendimento.csv     # Suas conversas
│   └── dicas_orcamento.json          # Suas dicas personalizadas
│
├── 📁 docs/                           # Documentação
│   ├── 01-documentacao-agente.md     
│   ├── 02-base-conhecimento.md       
│   ├── 03-prompts.md                  
│   └── 04-metricas.md                 
│
├── 📁 src/                             # Código fonte
│   └── assistente.py                   
│
├── 📁 examples/                         # Dados de exemplo
│   ├── exemplo_transacoes.csv
│   └── exemplo_perfil.json
│
├── .gitignore                           # Protege seus dados
├── README.md                            # Documentação principal
└── requirements.txt                      # Dependências
