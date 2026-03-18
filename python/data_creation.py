from faker import Faker
import psycopg2
import random
from datetime import timedelta
from datetime import datetime

# =========================
# CONFIG
# =========================
fake = Faker("pt_BR")
random.seed(42)

conn = psycopg2.connect(
    host="localhost",
    database="fintech_analytics",
    user="postgres",
    password="0000"
)
cur = conn.cursor()

NUM_USERS = 5000

LOGIN_RATE = 0.85
SIGNUP_RATE = 0.67
TRANSACTION_RATE = 0.70

# =========================
# LIMPAR BASE
# =========================
cur.execute("TRUNCATE TABLE transactions RESTART IDENTITY CASCADE;")
cur.execute("TRUNCATE TABLE cards RESTART IDENTITY CASCADE;")
cur.execute("TRUNCATE TABLE accounts RESTART IDENTITY CASCADE;")
cur.execute("TRUNCATE TABLE events RESTART IDENTITY CASCADE;")
cur.execute("TRUNCATE TABLE users RESTART IDENTITY CASCADE;")
conn.commit()

# =========================
# USERS
# =========================
users = []
for user_id in range(1, NUM_USERS + 1):
    created_at = fake.date_time_between(
    start_date=datetime(2024, 1, 1),
    end_date=datetime(2025, 12, 31)
)
    users.append((
        user_id,
        fake.name(),
        fake.unique.email(),
        fake.sha256(),
        created_at
    ))

cur.executemany("""
    INSERT INTO users (id, name, email, password, created_at)
    VALUES (%s, %s, %s, %s, %s)
""", users)

conn.commit()

# =========================
# DEFINIÇÃO CONTROLADA DO FUNIL
# =========================
user_ids = [u[0] for u in users]

login_users = random.sample(user_ids, int(NUM_USERS * LOGIN_RATE))
signup_users = random.sample(login_users, int(len(login_users) * SIGNUP_RATE))
transaction_users = random.sample(signup_users, int(len(signup_users) * TRANSACTION_RATE))

# =========================
# EVENTS
# =========================
events = []
event_id = 1

for user in users:
    user_id = user[0]
    created_at = user[4]

    # 1️⃣ App Open (100%)
    events.append((event_id, user_id, "app_open", "{}", created_at))
    event_id += 1

    # 2️⃣ Signup Started (85%)
    if user_id in login_users:
        started_at = created_at + timedelta(minutes=5)
        events.append((event_id, user_id, "signup_started", "{}", started_at))
        event_id += 1

    # 3️⃣ Signup Completed (67% dos que iniciaram)
    if user_id in signup_users:
        completed_at = created_at + timedelta(minutes=10)
        events.append((event_id, user_id, "signup_completed", "{}", completed_at))
        event_id += 1

cur.executemany("""
    INSERT INTO events (id, user_id, event_name, event_properties, created_at)
    VALUES (%s, %s, %s, %s, %s)
""", events)

conn.commit()

# =========================
# ACCOUNTS (100% DOS QUE COMPLETARAM)
# =========================
accounts = []
account_id = 1

for user_id in signup_users:
    base_date = next(u[4] for u in users if u[0] == user_id)
    accounts.append((
        account_id,
        user_id,
        fake.iban(),
        round(random.uniform(0, 5000), 2),
        "active",
        base_date + timedelta(minutes=20)
    ))
    account_id += 1

cur.executemany("""
    INSERT INTO accounts (id, user_id, account_number, balance, status, created_at)
    VALUES (%s, %s, %s, %s, %s, %s)
""", accounts)

conn.commit()

# =========================
# CARDS (60% DOS QUE TÊM CONTA)
# =========================
cards = []
card_id = 1

for acc in accounts:
    if random.random() < 0.60:
        created = acc[5] + timedelta(days=2)
        activated = created + timedelta(days=1)

        cards.append((
            card_id,
            acc[0],
            random.choice(["virtual", "physical"]),
            created,
            activated,
            fake.date_between(start_date="+2y", end_date="+5y")
        ))
        card_id += 1

cur.executemany("""
    INSERT INTO cards (id, account_id, card_type, created_at, activated_at, expiration_date)
    VALUES (%s, %s, %s, %s, %s, %s)
""", cards)

conn.commit()

# =========================
# TRANSACTIONS (70% DOS QUE TÊM CONTA)
# =========================
transactions = []
transaction_id = 1

for acc in accounts:
    if acc[1] in transaction_users:
        for _ in range(random.randint(1, 5)):
            transactions.append((
                transaction_id,
                acc[0],
                round(random.uniform(20, 800), 2),
                random.choices(["pix", "card", "transfer"], weights=[0.6, 0.3, 0.1])[0],
                "completed",
                random.choice(["app", "web"]),
                acc[5] + timedelta(days=random.randint(1, 60))
            ))
            transaction_id += 1

cur.executemany("""
    INSERT INTO transactions (id, account_id, amount, transaction_type, status, channel, created_at)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""", transactions)

conn.commit()

cur.close()
conn.close()

print("✅ Base recriada com funil matematicamente controlado e coerente!")
