-- 1. Total Revenue and Profit
SELECT 
    ROUND(SUM(sales), 2) AS total_revenue,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND((SUM(profit) / SUM(sales)) * 100, 2) AS profit_margin_pct
FROM orders;

-- 2. Sales by Category
SELECT 
    category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM orders
GROUP BY category
ORDER BY total_sales DESC;

-- 3. Top 5 States by Revenue
SELECT 
    state,
    ROUND(SUM(sales), 2) AS total_sales
FROM orders
GROUP BY state
ORDER BY total_sales DESC
LIMIT 5;

-- 4. Loss-Making Sub-Categories
SELECT 
    sub_category,
    ROUND(SUM(profit), 2) AS total_profit
FROM orders
GROUP BY sub_category
HAVING total_profit < 0
ORDER BY total_profit ASC;

-- 5. Monthly Revenue Trend
SELECT 
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    ROUND(SUM(sales), 2) AS monthly_sales
FROM orders
GROUP BY month
ORDER BY month;
