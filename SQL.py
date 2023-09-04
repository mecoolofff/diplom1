# Список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true)
# SELECT c.login, o.inDelivery, COUNT(*) AS total_orders
# FROM "Couriers" c
# JOIN "Orders" o ON c.id = o.id
# WHERE o.inDelivery = true
# GROUP BY c.login;

# Все трекеры заказов и их статусы
# SELECT track,
# CASE
# WHEN finished = true THEN 2
# WHEN cancelled = true THEN -1
# WHEN "inDelivery" = true THEN 1
# ELSE 0
# END AS status
# FROM "Orders";
