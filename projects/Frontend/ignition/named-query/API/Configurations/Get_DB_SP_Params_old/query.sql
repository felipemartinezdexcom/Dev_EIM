DECLARE @ProcName SYSNAME =:function_name;

WITH ProcSource AS
(
    SELECT
        p.object_id,
        sm.definition
    FROM sys.procedures p
    INNER JOIN sys.sql_modules sm
        ON p.object_id = sm.object_id
    WHERE p.name = @ProcName
),

ParamBlock AS
(
    SELECT
        object_id,

        -- Get everything between first @ and AS
        SUBSTRING(
            definition,
            CHARINDEX('@', definition),
            CHARINDEX(CHAR(10) + 'AS', definition)
                - CHARINDEX('@', definition)
        ) + ',' AS params_text

    FROM ProcSource
),

ParsedParams AS
(
    SELECT
        p.parameter_id,
        p.name AS param_name,
        TYPE_NAME(p.user_type_id) AS data_type,

        LTRIM(RTRIM(
            SUBSTRING(
                pb.params_text,
                CHARINDEX(p.name, pb.params_text),

                CHARINDEX(
                    ',',
                    pb.params_text,
                    CHARINDEX(p.name, pb.params_text)
                )
                - CHARINDEX(p.name, pb.params_text)
            )
        )) AS parameter_definition

    FROM sys.parameters p
    INNER JOIN ParamBlock pb
        ON p.object_id = pb.object_id

    WHERE p.object_id = OBJECT_ID(@ProcName)
)

SELECT
    parameter_id,
    param_name,
    data_type,

    CASE
        WHEN parameter_definition LIKE '%=%'
            THEN 'NO'
        ELSE 'YES'
    END AS required_param,

    CASE
        WHEN parameter_definition LIKE '%=%'
            THEN LTRIM(RTRIM(
                SUBSTRING(
                    parameter_definition,
                    CHARINDEX('=', parameter_definition) + 1,
                    LEN(parameter_definition)
                )
            ))
        ELSE NULL
    END AS default_value,

    parameter_definition

FROM ParsedParams

ORDER BY parameter_id;