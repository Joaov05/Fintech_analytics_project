/*
Objetivo:
Calcular o Daily Active Users (DAU).

Por que essa query é importante:
- Mede uso diário do produto
- Ajuda a analisar recorrência

Pergunta que responde:
"Quantos usuários usam o produto por dia?"
*/

SELECT
  date_trunc('day', created_at) AS day,
  COUNT(DISTINCT user_id) AS dau
FROM events
WHERE event_name IN ('app_open', 'pix_completed', 'viewed_home')
GROUP BY 1
ORDER BY 1;