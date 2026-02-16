# 🎓 Assistente Financeiro Personalizado

> Agente de IA Generativa adaptado para **controle de gastos pessoais**

## 💡 O Que é Este Projeto?

Este é meu assistente financeiro pessoal, adaptado do projeto original **Edu**. Diferente do original que ensina conceitos gerais, minha versão é focada em **análise de gastos e orçamento pessoal**, usando meus dados reais para respostas personalizadas.

### ✨ O Que Meu Assistente Faz:

| Funcionalidade | Descrição |
|----------------|-----------|
| ✅ **Análise de Gastos** | Calcula totais e detalha gastos por categoria |
| ✅ **Comparação com Orçamento** | Verifica se estou dentro dos limites planejados |
| ✅ **Dicas Personalizadas** | Sugere economias baseadas nos meus padrões |
| ✅ **Interface Amigável** | Chat intuitivo com comandos em linguagem natural |
| ✅ **100% Local** | Meus dados nunca saem do meu computador |

### ❌ O Que Meu Assistente NÃO Faz:

* ❌ Não recomenda investimentos
* ❌ Não acessa dados bancários online
* ❌ Não compartilha informações com terceiros
* ❌ Não substitui um consultor financeiro

## 🏗️ Estrutura do Projeto

```
├── data/                          # MEUS DADOS PESSOAIS (ignorados no git)
│   ├── perfil_financeiro.json     # Minha renda e metas (adaptado)
│   ├── transacoes.csv             # Meu histórico de gastos
│   ├── historico_atendimento.csv  # Minhas conversas com o assistente
│   └── dicas_orcamento.json       # Minhas dicas personalizadas (adaptado)
│
├── docs/                          # Documentação completa
│   ├── 01-documentacao-agente.md  # Persona e comportamento adaptados
│   ├── 02-base-conhecimento.md    # Estratégia de dados personalizada
│   ├── 03-prompts.md              # Prompts adaptados para gastos
│   ├── 04-metricas.md             # Métricas de avaliação
│   └── 05-pitch.md                # Apresentação do projeto
│
├── examples/                       # Dados de exemplo (NOVO)
│   ├── exemplo_transacoes.csv      # Formato das transações
│   └── exemplo_perfil.json         # Formato do perfil
│
└── src/
    └── assistente.py               # Aplicação Streamlit (renomeado)
```

## 🎯 Como Usar

### Primeiros Passos:
1. **Configure seu perfil** na aba "Perfil" da barra lateral
2. **Adicione suas transações** na aba "Transação"
3. **Comece a conversar** com o assistente

### Comandos Disponíveis:

| Comando | Exemplo | Resposta |
|---------|---------|----------|
| **Quanto gastei?** | "Quanto gastei esse mês?" | Total do mês atual |
| **Onde gasto mais?** | "Qual minha maior despesa?" | Categoria com maior gasto |
| **Gastos por categoria** | "Como gastei meu dinheiro?" | Detalhamento completo |
| **Meu orçamento** | "Estou dentro do orçamento?" | Comparação com limites |
| **Saldo** | "Quanto sobra esse mês?" | Renda - Gastos |
| **Dicas** | "Como posso economizar?" | Sugestões personalizadas |
| **Ajuda** | "O que você sabe fazer?" | Lista todos os comandos |

## 📊 Exemplo de Uso

**Usuário:** "Quanto gastei esse mês?"  
**Assistente:** "💰 **Total gasto em Fevereiro/2026:** R$ 2.495,01"

**Usuário:** "Onde gasto mais?"  
**Assistente:** "📊 **Sua maior despesa é com moradia**  
Valor: R$ 1.350,00 (54.1% do total)"

**Usuário:** "Dicas"  
**Assistente:** "💡 **Dicas para economizar:**  
• Cozinhar em casa 3x por semana pode economizar R$ 200/mês  
• Transporte público custa 1/3 do valor do Uber"

## 🔒 Privacidade e Segurança

```
✅ SEUS DADOS ESTÃO SEGUROS PORQUE:
├── 🔒 Ficam APENAS no seu computador
├── 🚫 NUNCA são enviados para internet
├── 📁 Formato aberto (CSV/JSON)
├── 🏠 Você controla tudo
└── 💰 100% gratuito
```

## 🛠️ Tecnologias Utilizadas

- **Frontend/Interface:** [Streamlit](https://streamlit.io/)
- **Manipulação de Dados:** [Pandas](https://pandas.pydata.org/)
- **Gráficos:** [Plotly](https://plotly.com/)
- **IA (opcional):** [Hugging Face](https://huggingface.co/) / Transformers
```

⭐ **Dica:** Mantenha seus dados sempre atualizados na aba "Transação" para melhores análises!
