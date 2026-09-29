-- =========================================================
-- E-COMMERCE SALES ANALYSIS
-- Database: Oracle 21c XE
-- Dataset: Sample Superstore
-- =========================================================


-- =========================================================
-- 1. OVERALL KPIs
-- =========================================================

SELECT
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    SUM(quantity) AS total_quantity,
    COUNT(DISTINCT order_id) AS total_orders,
    COUNT(DISTINCT customer_id) AS total_customers,
    ROUND(SUM(sales) / COUNT(DISTINCT order_id), 2) AS average_order_value,
    ROUND((SUM(profit) / SUM(sales)) * 100, 2) AS profit_margin
FROM ecommerce_sales;


-- =========================================================
-- 2. SALES AND PROFIT BY CATEGORY
-- =========================================================

SELECT
    category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    SUM(quantity) AS total_quantity
FROM ecommerce_sales
GROUP BY category
ORDER BY total_sales DESC;


-- =========================================================
-- 3. SALES AND PROFIT BY SUB-CATEGORY
-- =========================================================

SELECT
    sub_category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    SUM(quantity) AS total_quantity
FROM ecommerce_sales
GROUP BY sub_category
ORDER BY total_sales DESC;


-- =========================================================
-- 4. TOP 10 PRODUCTS BY SALES
-- =========================================================

SELECT
    product_name,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM ecommerce_sales
GROUP BY product_name
ORDER BY total_sales DESC
FETCH FIRST 10 ROWS ONLY;


-- =========================================================
-- 5. TOP 10 CUSTOMERS BY SALES
-- =========================================================

SELECT
    customer_name,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    SUM(quantity) AS total_quantity
FROM ecommerce_sales
GROUP BY customer_name
ORDER BY total_sales DESC
FETCH FIRST 10 ROWS ONLY;


-- =========================================================
-- 6. MONTHLY SALES AND PROFIT
-- =========================================================

SELECT
    TO_CHAR(order_date, 'YYYY-MM') AS sales_month,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM ecommerce_sales
GROUP BY TO_CHAR(order_date, 'YYYY-MM')
ORDER BY sales_month;


-- =========================================================
-- 7. SALES AND PROFIT BY REGION
-- =========================================================

SELECT
    region,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    SUM(quantity) AS total_quantity
FROM ecommerce_sales
GROUP BY region
ORDER BY total_sales DESC;


-- =========================================================
-- 8. DISCOUNT VS PROFIT ANALYSIS
-- =========================================================

SELECT
    sub_category,
    ROUND(AVG(discount) * 100, 2) AS avg_discount_percent,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM ecommerce_sales
GROUP BY sub_category
ORDER BY avg_discount_percent DESC;


-- =========================================================
-- 9. LOSS-MAKING SUB-CATEGORIES
-- =========================================================

SELECT
    sub_category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM ecommerce_sales
GROUP BY sub_category
HAVING SUM(profit) < 0
ORDER BY total_profit;


-- =========================================================
-- 10. TOP 10 PRODUCTS BY PROFIT
-- =========================================================

SELECT
    product_name,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(SUM(sales), 2) AS total_sales
FROM ecommerce_sales
GROUP BY product_name
ORDER BY total_profit DESC
FETCH FIRST 10 ROWS ONLY;


-- =========================================================
-- 11. SALES AND PROFIT BY CUSTOMER SEGMENT
-- =========================================================

SELECT
    segment,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    SUM(quantity) AS total_quantity,
    COUNT(DISTINCT order_id) AS total_orders
FROM ecommerce_sales
GROUP BY segment
ORDER BY total_sales DESC;


-- =========================================================
-- 12. PROFITABLE VS LOSS-MAKING PRODUCTS
-- =========================================================

SELECT
    product_name,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM ecommerce_sales
GROUP BY product_name
ORDER BY total_profit ASC;