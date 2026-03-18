/*
Objetivo:
Criar uma base única por usuário conectando usuários, eventos e contas.

Por que essa query é importante:
- Garante que todas as análises partam do user_id
- Base para funil, ativação e retenção
- Evita duplicidade de usuários em análises

Pergunta que responde:
"Quais são os principais eventos e datas associadas a cada usuário?"
*/

SELECT
  u.id AS user_id,
  MIN(e.created_at) FILTER (WHERE e.event_name = 'app_open') AS app_open_at,
  MIN(e.created_at) FILTER (WHERE e.event_name = 'signup_started') AS signup_started_at,
  MIN(e.created_at) FILTER (WHERE e.event_name = 'signup_completed') AS signup_completed_at,
  MIN(a.created_at) AS account_created_at
FROM users u
LEFT JOIN events e ON e.user_id = u.id
LEFT JOIN accounts a ON a.user_id = u.id
GROUP BY u.id;