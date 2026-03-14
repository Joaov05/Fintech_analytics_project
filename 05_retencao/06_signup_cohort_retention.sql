/*
Objetivo:
Construir uma base de retenção por cohort de signup.

Definição:
Usuários são agrupados pelo mês de signup e acompanhados nos meses seguintes.

Por que essa query é importante:
- Mede retenção ao longo do tempo
- Identifica queda de engajamento

Pergunta que responde:
"Usuários continuam usando o produto após o cadastro?"
*/

WITH signup AS (
  SELECT
    user_id,
    date_trunc('month', created_at) AS signup_month
  FROM events
  WHERE event_name = 'signup_completed'
),
activity AS (
  SELECT
    user_id,
    date_trunc('month', created_at) AS activity_month
  FROM events
  WHERE event_name IN ('app_open', 'pix_completed')
)
SELECT
  s.signup_month,
  a.activity_month,
  COUNT(DISTINCT a.user_id) AS retained_users
FROM signup s
JOIN activity a ON a.user_id = s.user_id
GROUP BY 1,2
ORDER BY 1,2;