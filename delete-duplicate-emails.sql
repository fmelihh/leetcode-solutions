-- https://leetcode.com/problems/delete-duplicate-emails/submissions/1623339796

WITH duplicates AS (
    SELECT
        id,
        ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS row_num
    FROM Person
)
DELETE FROM Person
WHERE id IN (
    SELECT id FROM duplicates WHERE row_num > 1
);
