/*
Objetivo:
Calcular o Monthly Active Users (MAU).

Definição:
Usuários únicos que realizaram ao menos uma ação relevante no mês.

Por que essa query é importante:
- Mede engajamento do produto
- Métrica base de saúde do produto

Pergunta que responde:
"Quantos usuários usam o produto todo mês?"
*/

SELECT
  date_trunc('month', created_at) AS month,
  COUNT(DISTINCT user_id) AS mau
FROM events
WHERE event_name IN ('app_open', 'pix_completed', 'viewed_home')
GROUP BY 1
ORDER BY 1;