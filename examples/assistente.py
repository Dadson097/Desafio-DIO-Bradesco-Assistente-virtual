import streamlit as st
import pandas as pd
import json
from datetime import datetime
import os
import plotly.express as px
from pathlib import Path

# Configuração da página
st.set_page_config(
    page_title="Assistente de Gastos",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Assistente de Gastos Leve")
st.markdown("---")

# === FUNÇÕES DE DADOS ===
def inicializar_dados():
    """Cria dados iniciais se não existirem"""
    
    Path("data").mkdir(exist_ok=True)
    
    if not os.path.exists('data/transacoes.csv'):
        dados_exemplo = {
            'data': [
                '2026-02-01', '2026-02-03', '2026-02-05', '2026-02-07', '2026-02-10',
                '2026-02-12', '2026-02-15', '2026-02-18', '2026-02-20', '2026-02-22'
            ],
            'categoria': [
                'alimentação', 'transporte', 'moradia', 'lazer', 'alimentação',
                'saúde', 'transporte', 'alimentação', 'moradia', 'lazer'
            ],
            'descricao': [
                'Supermercado', 'Uber', 'Aluguel', 'Cinema', 'Restaurante',
                'Farmácia', 'Ônibus', 'Mercado', 'Conta luz', 'Ifood'
            ],
            'valor': [
                350.00, 45.00, 1200.00, 60.00, 120.00,
                80.00, 15.00, 280.00, 150.00, 95.00
            ]
        }
        pd.DataFrame(dados_exemplo).to_csv('data/transacoes.csv', index=False)
    
    if not os.path.exists('data/perfil.json'):
        perfil_exemplo = {
            "renda_mensal": 3500.00,
            "meta_economia": 700.00,
            "orcamento": {
                "alimentação": 800,
                "transporte": 300,
                "moradia": 1300,
                "lazer": 400,
                "saúde": 200,
                "outros": 500
            }
        }
        with open('data/perfil.json', 'w') as f:
            json.dump(perfil_exemplo, f, indent=2)

def carregar_dados():
    """Carrega dados dos arquivos"""
    transacoes = pd.read_csv('data/transacoes.csv')
    transacoes['data'] = pd.to_datetime(transacoes['data'])
    
    with open('data/perfil.json', 'r') as f:
        perfil = json.load(f)
    
    return transacoes, perfil

# === INTERFACE DE COLETA DE DADOS ===
def interface_coleta_dados():
    """Interface para coleta manual de dados"""
    
    st.sidebar.markdown("---")
    st.sidebar.header("📝 Adicionar Dados")
    
    tabs = st.sidebar.tabs(["➕ Transação", "⚙️ Perfil"])
    
    with tabs[0]:
        with st.form("transacao_rapida"):
            data = st.date_input("Data", datetime.now())
            categoria = st.selectbox(
                "Categoria",
                ["alimentação", "transporte", "moradia", "lazer", "saúde", "outros"]
            )
            descricao = st.text_input("Descrição", placeholder="Ex: Supermercado")
            valor = st.number_input("Valor (R$)", min_value=0.01, step=10.0)
            
            if st.form_submit_button("💾 Salvar transação", use_container_width=True):
                try:
                    df = pd.read_csv('data/transacoes.csv')
                    nova = pd.DataFrame({
                        'data': [data.strftime('%Y-%m-%d')],
                        'categoria': [categoria],
                        'descricao': [descricao],
                        'valor': [valor]
                    })
                    df = pd.concat([df, nova], ignore_index=True)
                    df.to_csv('data/transacoes.csv', index=False)
                    st.success("✅ Transação salva!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro: {e}")
    
    with tabs[1]:
        with st.form("perfil_rapido"):
            renda = st.number_input("Renda mensal", min_value=0.0, value=3500.0, step=100.0)
            meta = st.number_input("Meta de economia", min_value=0.0, value=700.0, step=50.0)
            
            st.caption("Orçamento por categoria:")
            col1, col2 = st.columns(2)
            with col1:
                ali = st.number_input("Alim.", value=800, key="ali")
                trans = st.number_input("Transp.", value=300, key="trans")
                mora = st.number_input("Morad.", value=1300, key="mora")
            with col2:
                lazer = st.number_input("Lazer", value=400, key="laz")
                saude = st.number_input("Saúde", value=200, key="sau")
                outros = st.number_input("Outros", value=500, key="out")
            
            if st.form_submit_button("💾 Salvar perfil", use_container_width=True):
                perfil = {
                    "renda_mensal": renda,
                    "meta_economia": meta,
                    "orcamento": {
                        "alimentação": ali,
                        "transporte": trans,
                        "moradia": mora,
                        "lazer": lazer,
                        "saúde": saude,
                        "outros": outros
                    }
                }
                with open('data/perfil.json', 'w') as f:
                    json.dump(perfil, f, indent=2)
                st.success("✅ Perfil salvo!")
                st.rerun()
    
    st.sidebar.divider()
    if st.sidebar.checkbox("👁️ Ver dados atuais"):
        try:
            st.sidebar.dataframe(pd.read_csv('data/transacoes.csv').tail(5), height=200)
            st.sidebar.caption("Últimas 5 transações")
        except:
            st.sidebar.info("Sem transações")

# === ASSISTENTE INTELIGENTE ===
class AssistenteFinanceiro:
    def __init__(self, transacoes, perfil):
        self.transacoes = transacoes
        self.perfil = perfil
        self.hoje = datetime.now()
        
        self.transacoes_mes = self.transacoes[
            (self.transacoes['data'].dt.month == self.hoje.month) &
            (self.transacoes['data'].dt.year == self.hoje.year)
        ]
        
        self.total_gastos = self.transacoes_mes['valor'].sum()
        self.gastos_categoria = self.transacoes_mes.groupby('categoria')['valor'].sum().to_dict()
        self.num_transacoes = len(self.transacoes_mes)
    
    def responder(self, pergunta):
        """Responde à pergunta do usuário"""
        pergunta = pergunta.lower().strip()
        
        # 1. SAUDAÇÕES
        if any(p in pergunta for p in ['oi', 'olá', 'hello', 'boa tarde', 'bom dia']):
            return "Olá! 👋 Como posso ajudar com suas finanças hoje? Digite 'ajuda' para ver os comandos disponíveis."
        
        # 2. QUANTO GASTEI
        elif any(p in pergunta for p in [
            'quanto gastei', 'total gasto', 'soma', 'gastei no mês',
            'qual foi meu gasto', 'meus gastos', 'quanto eu gastei',
            'total do mês', 'resumo do mês', 'gastos do mês'
        ]):
            return f"💰 **Total gasto em {self.hoje.strftime('%B/%Y')}:** R$ {self.total_gastos:.2f}"
        
        # 3. ONDE GASTO MAIS
        elif any(p in pergunta for p in [
            'onde gasto mais', 'maior gasto', 'categoria que mais',
            'o que mais gasto', 'principal gasto', 'maior despesa'
        ]):
            if not self.gastos_categoria:
                return "📭 Nenhum gasto registrado neste mês."
            maior_cat = max(self.gastos_categoria, key=self.gastos_categoria.get)
            maior_valor = self.gastos_categoria[maior_cat]
            percentual = (maior_valor / self.total_gastos) * 100 if self.total_gastos > 0 else 0
            return f"📊 **Sua maior despesa é com {maior_cat}**\nValor: R$ {maior_valor:.2f} ({percentual:.1f}% do total)"
        
        # 4. GASTOS POR CATEGORIA
        elif any(p in pergunta for p in [
            'gastos por categoria', 'como gastei', 'detalhar', 'por categoria',
            'cada categoria', 'divisão de gastos'
        ]):
            if not self.gastos_categoria:
                return "📭 Nenhum gasto registrado neste mês."
            resposta = "📋 **Gastos por categoria:**\n\n"
            for cat, valor in sorted(self.gastos_categoria.items(), key=lambda x: x[1], reverse=True):
                percentual = (valor / self.total_gastos) * 100
                resposta += f"• {cat.capitalize()}: R$ {valor:.2f} ({percentual:.1f}%)\n"
            return resposta
        
        # 5. ORÇAMENTO
        elif any(p in pergunta for p in [
            'orçamento', 'dentro do', 'estouro', 'limite', 'comparar orçamento'
        ]):
            alertas = []
            for cat, orcado in self.perfil['orcamento'].items():
                gasto = self.gastos_categoria.get(cat, 0)
                if gasto > orcado:
                    alertas.append(f"🔴 {cat}: R$ {gasto:.2f} (limite: R$ {orcado:.2f})")
            if alertas:
                return "⚠️ **Categorias acima do orçamento:**\n" + "\n".join(alertas)
            else:
                return "✅ **Tudo dentro do orçamento!**"
        
        # 6. SALDO
        elif any(p in pergunta for p in [
            'saldo', 'economia', 'sobra', 'quanto sobra', 'dinheiro restante'
        ]):
            saldo = self.perfil['renda_mensal'] - self.total_gastos
            percentual = (saldo / self.perfil['renda_mensal']) * 100
            return f"💵 **Resumo financeiro:**\n• Renda: R$ {self.perfil['renda_mensal']:.2f}\n• Gastos: R$ {self.total_gastos:.2f}\n• Saldo: R$ {saldo:.2f} ({percentual:.1f}% da renda)"
        
        # 7. DICAS
        elif any(p in pergunta for p in [
            'dica', 'economizar', 'poupar', 'como economizar', 'sugestão'
        ]):
            return self._dar_dicas()
        
        # 8. ÚLTIMAS TRANSAÇÕES
        elif any(p in pergunta for p in [
            'últimas', 'recentes', 'últimos gastos', 'últimas compras'
        ]):
            return self._ultimas_transacoes()
        
        # 9. AJUDA
        elif any(p in pergunta for p in ['ajuda', 'comandos', 'o que você faz', 'como usar', 'help']):
            return self._menu_ajuda()
        
        # 10. NÃO ENTENDI
        else:
            return "❓ **Não entendi.** Digite **'ajuda'** para ver os comandos disponíveis."
    
    def _dar_dicas(self):
        """Dicas de economia"""
        dicas = [
            "🍽️ **Cozinhe em casa:** Comer fora 1x por semana já faz diferença",
            "🚌 **Transporte público:** Pode custar 1/3 do Uber",
            "📱 **Revise assinaturas:** Cancele o que não usa",
            "🛒 **Compras com lista:** Evita impulso no mercado",
            "⚡ **Economia de energia:** Desligue aparelhos da tomada",
            "💰 **Regra 50-30-20:** 50% necessidades, 30% desejos, 20% economia"
        ]
        return "💡 **Dicas para economizar:**\n\n" + "\n".join(dicas[:4])
    
    def _ultimas_transacoes(self):
        """Mostra últimas 5 transações"""
        ultimas = self.transacoes_mes.sort_values('data', ascending=False).head(5)
        
        if ultimas.empty:
            return "📭 Nenhuma transação recente."
        
        resposta = "📝 **Últimas transações:**\n\n"
        for _, row in ultimas.iterrows():
            data = row['data'].strftime('%d/%m')
            resposta += f"• {data} - {row['descricao']}: R$ {row['valor']:.2f}\n"
        
        return resposta
    
    def _menu_ajuda(self):
        """Menu de ajuda completo"""
        return """❓ **MENU DE AJUDA - Comandos Disponíveis**

💰 **GASTOS:**
• "Quanto gastei?" - Total do mês
• "Onde gasto mais?" - Maior categoria
• "Gastos por categoria" - Detalhamento

📊 **ANÁLISE:**
• "Meu orçamento" - Compara com limites
• "Saldo" - Renda - Gastos
• "Últimas transações" - Gastos recentes

💡 **DICAS:**
• "Dicas" - Sugestões de economia
• "Ajuda" - Mostra este menu

⚙️ **BARRA LATERAL:**
• Adicione transações
• Configure seu perfil
• Veja o resumo do mês

Digite sua pergunta! 👆"""

# === INTERFACE PRINCIPAL ===
def main():
    inicializar_dados()
    transacoes, perfil = carregar_dados()
    assistente = AssistenteFinanceiro(transacoes, perfil)
    
    # Sidebar
    with st.sidebar:
        st.header("📊 Resumo do Mês")
        st.metric("Total Gastos", f"R$ {assistente.total_gastos:.2f}")
        st.metric("Renda", f"R$ {perfil['renda_mensal']:.2f}")
        
        saldo = perfil['renda_mensal'] - assistente.total_gastos
        st.metric("Saldo", f"R$ {saldo:.2f}")
        
        # Botão de ajuda na sidebar (NOVO!)
        with st.expander("❓ Comandos disponíveis"):
            st.markdown("""
            **💰 Gastos:**
            • "Quanto gastei?" - Total do mês
            • "Onde gasto mais?" - Maior categoria
            • "Gastos por categoria" - Detalhamento
            
            **📊 Análise:**
            • "Meu orçamento" - Comparar com limites
            • "Saldo" - Renda vs Gastos
            • "Últimas transações" - Gastos recentes
            
            **💡 Dicas:**
            • "Dicas" - Sugestões de economia
            • "Ajuda" - Mostrar esta lista
            """)
        
        interface_coleta_dados()
        
        st.divider()
        st.caption(f"📍 {assistente.hoje.strftime('%B/%Y')}")
        st.caption(f"📝 {assistente.num_transacoes} transações")
        
        if assistente.gastos_categoria:
            df_gastos = pd.DataFrame([
                {"Categoria": cat, "Valor": val}
                for cat, val in assistente.gastos_categoria.items()
            ])
            fig = px.pie(df_gastos, values='Valor', names='Categoria', title="Gastos por Categoria")
            st.plotly_chart(fig, use_container_width=True)
    
    # Chat
    st.subheader("💬 Converse com seu Assistente")
    
    if "mensagens" not in st.session_state:
        mensagem_inicial = """👋 **Olá! Sou seu assistente financeiro!**

📌 **Comandos disponíveis:**
• "Quanto gastei?" - Total do mês
• "Onde gasto mais?" - Maior categoria
• "Gastos por categoria" - Detalhamento
• "Meu orçamento" - Comparar com limites
• "Saldo" - Renda vs Gastos
• "Dicas" - Sugestões de economia
• "Últimas transações" - Gastos recentes

💡 **Digite sua pergunta ou use a barra lateral para adicionar transações!**
"""
        st.session_state.mensagens = [
            {"role": "assistant", "content": mensagem_inicial}
        ]
    
    for msg in st.session_state.mensagens[-10:]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    
    if prompt := st.chat_input("Digite sua pergunta..."):
        st.session_state.mensagens.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            resposta = assistente.responder(prompt)
            st.markdown(resposta)
            st.session_state.mensagens.append({"role": "assistant", "content": resposta})
    
    if st.button("🗑️ Limpar conversa"):
        st.session_state.mensagens = [
            {"role": "assistant", "content": "Conversa reiniciada! Digite 'ajuda' para ver os comandos."}
        ]
        st.rerun()

if __name__ == "__main__":
    main()