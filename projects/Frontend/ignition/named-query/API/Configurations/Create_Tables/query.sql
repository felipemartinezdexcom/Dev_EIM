IF NOT EXISTS (
SELECT *
FROM sys.schemas
WHERE name = 'API')
BEGIN
EXEC('CREATE SCHEMA API')
end
-- ================================
-- Table: [API].[FunctionParameters]
-- ================================
IF NOT EXISTS (
    SELECT 1 FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_SCHEMA = 'API' AND TABLE_NAME = 'FunctionParameters'
)
BEGIN
    CREATE TABLE [API].[FunctionParameters] (
    [param_id] INT IDENTITY(1,1) NOT NULL,
    [param_name] VARCHAR(300) NOT NULL,
    [data_type] VARCHAR(100) NOT NULL,
    [function_id] INT NULL,
    [date_created] DATETIME NULL,
    [created_by] VARCHAR(150) NULL,
    [last_date_modified] DATETIME NULL,
    [last_modified_by] VARCHAR(150) NULL,
    [required_param] BIT NULL,
    CONSTRAINT [PK_FunctionParameters] PRIMARY KEY ([param_id])
    );
END


-- ================================
-- Table: [API].[FunctionsList]
-- ================================
IF NOT EXISTS (
    SELECT 1 FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_SCHEMA = 'API' AND TABLE_NAME = 'FunctionsList'
)
BEGIN
    CREATE TABLE [API].[FunctionsList] (
    [function_id] INT IDENTITY(1,1) NOT NULL,
    [function_name] VARCHAR(500) NOT NULL,
    [date_created] DATETIME NULL,
    [created_by] VARCHAR(100) NULL,
    [last_date_modified] DATETIME NULL,
    [last_modified_by] VARCHAR(100) NULL,
    [validated] BIT DEFAULT ((0)) NULL,
    [sys_interface] VARCHAR(100) NULL,
    [database_name] VARCHAR(200) NULL,
    [database_schema] VARCHAR(200) NULL,
    CONSTRAINT [PK_FunctionsList] PRIMARY KEY ([function_id])
    );
END

-- ================================
-- Table: [API].[TransactionsLog]
-- ================================
IF NOT EXISTS (
    SELECT 1 FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_SCHEMA = 'API' AND TABLE_NAME = 'TransactionsLog'
)
BEGIN
    CREATE TABLE [API].[TransactionsLog] (
    [id] INT NOT NULL,
    [timestamp] NVARCHAR(MAX) NULL,
    [sp_name] NVARCHAR(MAX) NOT NULL,
    [result] NVARCHAR(MAX) NULL,
    [data] NVARCHAR(MAX) NULL,
    [message] NVARCHAR(MAX) NULL,
    [sql_timing] NVARCHAR(MAX) NULL,
    [exec_timing] NVARCHAR(MAX) NULL,
    [simulator_call] NVARCHAR(MAX) NULL,
    [simulator_user] NVARCHAR(MAX) NULL,
    [sys_interface] NVARCHAR(MAX) NULL,
    [input_params] NVARCHAR(MAX) NULL,
    [valid_for_prod] NVARCHAR(MAX) NULL,
    CONSTRAINT [PK_TransactionsLog] PRIMARY KEY ([id])
    );
END
