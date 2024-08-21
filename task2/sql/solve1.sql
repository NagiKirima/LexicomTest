INSERT INTO full_names (name, status)
    SELECT fn.name, sn.status
    FROM full_names fn
    JOIN short_names sn ON split_part(fn.name, '.', 1) = sn.name
ON CONFLICT (name) DO UPDATE 
SET status = EXCLUDED.status;