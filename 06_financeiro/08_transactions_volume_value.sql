/*
Objetivo:
Analisar volume e valor de transações ao longo do tempo.

Por que essa query é importante:
- Mede crescimento financeiro
- Permite análises de tendência

Pergunta que responde:
"Quanto dinheiro e quantas transações o produto processa por mês?"
*/

SELECT
  date_trunc('month', t.created_at) AS month,
  COUNT(*) AS total_transactions,
  SUM(t.amount) AS total_amount
FROM transactions t
WHERE t.status = 'completed'
GROUP BY 1
ORDER BY 1;