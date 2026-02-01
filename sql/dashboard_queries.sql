

----Daily KPIs Overview for Food Delivery Orders----
SELECT *
FROM food_delivery.gold_daily_kpis
ORDER BY order_date;

----Daily Food Delivery SLA Report----
SELECT *
FROM food_delivery.gold_daily_sla_health
ORDER BY order_date;

----Top Ten Delayed Orders from Gold Store----
SELECT *
FROM food_delivery.gold_store_sla_ranking
ORDER BY delay_rate DESC
LIMIT 10;


----High Risk Customer Insights Analysis----
SELECT *
FROM food_delivery.gold_customer_churn_risk
WHERE churn_risk_segment LIKE 'High%';

----Churn Risk and Value Insights by Customer Segment----
SELECT * FROM food_delivery.gold_customer_risk_profile

----Hygiene Incident Analysis by Location----
SELECT * FROM food_delivery.gold_geo_safety_map

----Traffic Trends in Food Delivery Markets----
SELECT *
FROM food_delivery.gold_market_congestion
WHERE market_id IS NOT NULL
ORDER BY congestion_ratio DESC;

----Top Risky Stores----
SELECT
store_id,
count(order_id) As order_count
FROM food_delivery.gold_geo_safety_map
WHERE ai_topic = 'Hygiene'
GROUP BY store_id
ORDER BY order_count DESC
LIMIT 10

----Congestion Ratio by Market----
SELECT 
market_id,
ROUND(congestion_ratio,2) AS congestion_ratio
FROM food_delivery.gold_market_congestion
WHERE market_id IS NOT NULL
ORDER BY congestion_ratio DESC
LIMIT 10;
