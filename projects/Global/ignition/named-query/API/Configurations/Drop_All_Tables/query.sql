DECLARE @sql NVARCHAR(MAX) = N'';

-- Drop foreign keys
SELECT @sql = @sql +
    'ALTER TABLE [' + OBJECT_SCHEMA_NAME(parent_object_id) + '].[' +
    OBJECT_NAME(parent_object_id) + '] DROP CONSTRAINT [' + name + '];'
    + CHAR(13) + CHAR(10)
FROM sys.foreign_keys
WHERE OBJECT_SCHEMA_NAME(parent_object_id) = 'API';

EXEC sp_executesql @sql;

-- Drop tables
SET @sql = N'';

SELECT @sql = @sql +
    'DROP TABLE [' + TABLE_SCHEMA + '].[' + TABLE_NAME + '];'
    + CHAR(13) + CHAR(10)
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE'
  AND TABLE_SCHEMA = 'API';

PRINT @sql;  -- Optional review

EXEC sp_executesql @sql;