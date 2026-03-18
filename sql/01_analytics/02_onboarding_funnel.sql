/*
Objetivo:
Construir o funil de onboarding completo do produto.

Etapas do funil:
1. App Open
2. Signup Started
3. Signup Completed
4. Account Created

Por que essa query é importante:
- Identifica gargalos no onboarding
- Mede conversão entre etapas
- Base para análises de crescimento

Pergunta que responde:
"Em qual etapa do onboarding os usuários mais desistem?"
*/

WITH funnel AS (
  SELECT
    u.id AS user_id,
    MIN(e.created_at) FILTER (WHERE e.event_name = 'app_open') AS app_open_at,
    MIN(e.created_at) FILTER (WHERE e.event_name = 'signup_started') AS signup_started_at,
    MIN(e.created_at) FILTER (WHERE e.event_name = 'signup_completed') AS signup_completed_at,
    MIN(a.created_at) AS account_created_at
  FROM users u
  LEFT JOIN events e ON e.user_id = u.id
  LEFT JOIN accounts a ON a.user_id = u.id
  GROUP BY u.id
)
SELECT
  COUNT(*) FILTER (WHERE app_open_at IS NOT NULL) AS app_open,
  COUNT(*) FILTER (WHERE signup_started_at IS NOT NULL) AS signup_started,
  COUNT(*) FILTER (WHERE signup_completed_at IS NOT NULL) AS signup_completed,
  COUNT(*) FILTER (WHERE account_created_at IS NOT NULL) AS account_created
FROM funnel;