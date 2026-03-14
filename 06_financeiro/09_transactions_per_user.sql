/*
Objetivo:
Calcular a frequência de uso financeiro por usuário.

Por que essa query é importante:
- Identifica heavy users e low users
- Base para segmentação e estratégias de produto

Pergunta que responde:
"Quantas transações cada usuário realiza?"
*/

SELECT
  u.id AS user_id,
  COUNT(t.id) AS total_transactions
FROM users u
JOIN accounts a ON a.user_id = u.id
JOIN transactions t ON t.account_id = a.id
WHERE t.status = 'completed'
GROUP BY u.id;