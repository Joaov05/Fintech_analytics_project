/*
========================================
PROJETO: Product Analytics – Banco Digital
ARQUIVO: 01_kpis_overview.sql
========================================

CONTEXTO DE NEGÓCIO
Este arquivo consolida as principais métricas do produto
para acompanhamento executivo e análise exploratória.

Essas métricas ajudam a responder:
- O produto está crescendo?
- Os usuários estão ativando?
- Os usuários estão gerando valor?

----------------------------------------

DEFINIÇÃO DAS MÉTRICAS

- total_users:
  Número total de usuários cadastrados na base.

- users_with_account:
  Usuários que criaram ao menos uma conta bancária.

- activated_users:
  Usuários que realizaram ao menos uma ação de valor
  (pix_completed ou card_activated).

- users_with_transactions:
  Usuários que realizaram ao menos uma transação concluída.

----------------------------------------

OBSERVAÇÕES
- Base centrada no user_id
- Transações consideram apenas status = 'completed'
- Query pode ser transformada em VIEW futuramente
========================================
*/

SELECT
  COUNT(DISTINCT u.id) AS total_users,

  COUNT(DISTINCT a.user_id) AS users_with_account,

  COUNT(DISTINCT e.user_id) FILTER (
    WHERE e.event_name IN ('pix_completed', 'card_activated')
  ) AS activated_users,

  COUNT(DISTINCT t.account_id) AS users_with_transactions

FROM users u
LEFT JOIN accounts a
  ON a.user_id = u.id
LEFT JOIN events e
  ON e.user_id = u.id
LEFT JOIN transactions t
  ON t.account_id = a.id
 AND t.status = 'completed';