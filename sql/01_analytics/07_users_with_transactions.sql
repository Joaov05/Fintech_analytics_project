/*
Objetivo:
Identificar quantos usuários realizaram transações financeiras.

Por que essa query é importante:
- Conecta uso do produto com valor gerado
- Base para monetização e LTV

Pergunta que responde:
"Quantos usuários realmente movimentam dinheiro?"
*/

SELECT
  COUNT(DISTINCT u.id) AS users_with_transactions
FROM users u
JOIN accounts a ON a.user_id = u.id
JOIN transactions t ON t.account_id = a.id
WHERE t.status = 'completed';