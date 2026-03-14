# 📊 Product Analytics — Insights & Hipóteses de Produto  
**Projeto:** Banco Digital (Base Sintética)  
**Foco:** Onboarding, Ativação, Engajamento e Retenção  

---

## 🔎 Visão Geral

Este documento consolida os principais insights gerados a partir da análise
dos dados de eventos, contas e transações de um banco digital fictício.
O objetivo é identificar oportunidades de melhoria no produto e propor
hipóteses orientadas por dados.

As análises foram realizadas com SQL sobre uma base PostgreSQL, utilizando
métricas clássicas de Product Analytics.

---

## 📈 INSIGHTS DE PRODUTO

### Insight 1 — Conversão forte no cadastro, mas ainda com espaço de melhoria

Dos **5.000 usuários** que abriram o app e iniciaram o processo de sign-up,  
**80,6% (4.030 usuários)** concluíram o cadastro.

Apesar de ser uma taxa de conversão relativamente alta, aproximadamente  
**1 em cada 5 usuários abandona o processo**, indicando fricção no fluxo
de onboarding.

**Impacto:**  
Mesmo pequenas melhorias nesse funil podem gerar ganhos relevantes
no número total de usuários cadastrados.

---

### Insight 2 — Ativação concentrada em ações de alto valor

Usuários que realizam eventos como `pix_completed` ou `card_activated`
apresentam maior engajamento inicial quando comparados a usuários que
apenas navegam pelo aplicativo.

**Impacto:**  
Nem todas as interações geram valor real. O produto precisa direcionar
o usuário rapidamente para ações-chave.

---

### Insight 3 — Criar conta não garante geração de valor

Uma parcela significativa dos usuários cria conta bancária, mas não
realiza transações financeiras concluídas.

**Impacto:**  
Existe um gap claro entre onboarding e monetização do produto.

---

### Insight 4 — Engajamento é mais esporádico do que recorrente

A relação entre DAU e MAU indica que os usuários não utilizam o produto
diariamente, caracterizando um comportamento mais pontual e transacional.

**Impacto:**  
Estratégias de engajamento devem considerar que o banco não é,
naturalmente, um produto de uso diário.

---

### Insight 5 — Primeiros dias definem retenção

Usuários que não realizam nenhuma ação relevante nos primeiros dias após
o cadastro apresentam baixa retenção nos meses seguintes.

**Impacto:**  
O período logo após o signup é crítico para criação de hábito e percepção
de valor.

---

## 🧪 HIPÓTESES DE PRODUTO

### Hipótese 1 — Redução de fricção no cadastro

**Se** simplificarmos o fluxo de cadastro (menos campos ou etapas),  
**então** a taxa de conclusão do sign-up aumentará,  
**porque** aproximadamente 19,4% dos usuários abandonam o processo antes
de finalizá-lo.

**Métrica de sucesso:**  
Signup Conversion Rate

---

### Hipótese 2 — Direcionamento para Pix no onboarding

**Se** destacarmos o Pix como principal ação logo após o cadastro,  
**então** a taxa de ativação aumentará,  
**porque** usuários que realizam Pix demonstram maior engajamento inicial.

**Métrica de sucesso:**  
Activation Rate  
Tempo até a primeira transação Pix

---

### Hipótese 3 — Incentivo à primeira transação

**Se** oferecermos um incentivo simbólico para a primeira transação
(ex: cashback ou benefício inicial),  
**então** mais usuários realizarão transações financeiras,  
**porque** muitos usuários criam conta, mas não movimentam saldo.

**Métrica de sucesso:**  
% de usuários com transação concluída

---

### Hipótese 4 — Comunicação focada nos primeiros dias

**Se** implementarmos comunicações educativas e orientadas nos primeiros
dias após o cadastro,  
**então** a retenção mensal aumentará,  
**porque** usuários inativos no início tendem a churnar rapidamente.

**Métrica de sucesso:**  
Retenção M1 e M2

---

### Hipótese 5 — Estímulo ao uso recorrente

**Se** criarmos funcionalidades que incentivem o uso recorrente
(ex: atalhos, histórico inteligente ou notificações contextuais),  
**então** o DAU aumentará,  
**porque** o produto apresenta uso esporádico ao longo do mês.

**Métrica de sucesso:**  
DAU / MAU (Stickiness)

---