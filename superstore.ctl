LOAD DATA
INFILE 'data/cleaned_superstore.csv'
INTO TABLE ecommerce_sales
APPEND
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
TRAILING NULLCOLS
(
    row_id,
    order_id,
    order_date DATE "YYYY-MM-DD",
    ship_date DATE "YYYY-MM-DD",
    ship_mode,
    customer_id,
    customer_name,
    segment,
    country,
    city,
    state,
    postal_code,
    region,
    product_id,
    category,
    sub_category,
    product_name,
    sales,
    quantity,
    discount,
    profit
)