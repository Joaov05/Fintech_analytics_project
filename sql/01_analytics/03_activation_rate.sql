/*
Objetivo:
Calcular a taxa de ativação do produto.

Definição de ativação:
Usuário que completou o signup e realizou ao menos uma ação de valor
(ex: pix_completed ou card_activated).

Por que essa query é importante:
- Mede se o produto entrega valor inicial
- Métrica importante para Product Analytics

Pergunta que responde:
"Quantos usuários realmente ativam após se cadastrar?"
*/

WITH signed_users AS (
  SELECT DISTINCT user_id
  FROM events
  WHERE event_name = 'signup_completed'
),
activated_users AS (
  SELECT DISTINCT user_id
  FROM events
  WHERE event_name IN ('pix_completed', 'card_activated')
)
SELECT
  COUNT(DISTINCT a.user_id) * 1.0
  / COUNT(DISTINCT s.user_id) AS activation_rate
FROM signed_users s
LEFT JOIN activated_users a
  ON a.user_id = s.user_id;