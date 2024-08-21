WITH tmp AS (
    SELECT fn.name, sn.status
    FROM full_names fn
    JOIN short_names sn ON split_part(fn.name, '.', 1) = sn.name
)
UPDATE full_names fn
SET status = tmp.status
FROM tmp
WHERE fn.name = tmp.name;