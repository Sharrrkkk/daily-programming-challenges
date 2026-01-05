SELECT
    P1.product_id AS product_id,
    'store1' AS "store",
    P1.store1 AS price
FROM
    Products AS P1
WHERE
    P1.store1 IS NOT NULL

UNION ALL
SELECT
    P2.product_id AS product_id,
    'store2' AS "store",
    P2.store2 AS price
FROM
    Products AS P2
WHERE
    P2.store2 IS NOT NULL

UNION ALL
SELECT
    P3.product_id AS product_id,
    'store3' AS "store",
    P3.store3 AS price
FROM
    Products AS P3
WHERE
    P3.store3 IS NOT NULL
ORDER BY
    product_id
;