

BUILD_TABLES_STRING="""


IF NOT EXISTS (
SELECT *
FROM sys.schemas
WHERE name = 'API')
BEGIN
EXEC('CREATE SCHEMA API')
END


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
CREATE TABLE [API].[FunctionsList](
	[function_id] [int] IDENTITY(1,1) NOT NULL,
	[function_name] [varchar](500) NOT NULL,
	[date_created] [datetime] NULL,
	[created_by] [varchar](100) NULL,
	[last_date_modified] [datetime] NULL,
	[last_modified_by] [varchar](100) NULL,
	[validated] [bit] NULL,
	[sys_interface] [varchar](100) NULL,
	[custom_function_name] [varchar](300) NULL,
	[database_name] [varchar](200) NULL,
	[database_schema] [varchar](200) NULL,
	[removed] [bit] NOT NULL,
 CONSTRAINT [PK_FunctionsList] PRIMARY KEY CLUSTERED 
(
	[function_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]

ALTER TABLE [API].[FunctionsList] ADD  DEFAULT ((0)) FOR [validated]

ALTER TABLE [API].[FunctionsList] ADD  CONSTRAINT [DF_FunctionsList_removed]  DEFAULT ((0)) FOR [removed]

END


-- ================================
-- Table: [API].[Equipment]
-- ================================
IF NOT EXISTS (
    SELECT 1 FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_SCHEMA = 'API' AND TABLE_NAME = 'Equipment'
)
BEGIN
CREATE TABLE [API].[Equipment](
	[equipment_id] [int] IDENTITY(1,1) NOT NULL,
	[equipment_name] [varchar](350) NOT NULL,
	[description] [varchar](500) NULL,
	[date_created] [datetime] NOT NULL,
	[created_by] [varchar](250) NULL,
	[last_date_modified] [datetime] NULL,
	[active] [bit] NOT NULL,
	[removed] [bit] NOT NULL,
	[assigned] [bit] NOT NULL,
 CONSTRAINT [PK_Equipment] PRIMARY KEY CLUSTERED 
(
	[equipment_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]

ALTER TABLE [API].[Equipment] ADD  CONSTRAINT [DF_Equipment_active]  DEFAULT ((0)) FOR [active]

ALTER TABLE [API].[Equipment] ADD  CONSTRAINT [DF_Equipment_removed]  DEFAULT ((0)) FOR [removed]

ALTER TABLE [API].[Equipment] ADD  CONSTRAINT [DF_Equipment_assigned]  DEFAULT ((0)) FOR [assigned]


END





-- ================================
-- Table: [API].[EquipmentGroups]
-- ================================
IF NOT EXISTS (
    SELECT 1 FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_SCHEMA = 'API' AND TABLE_NAME = 'EquipmentGroups'
)
BEGIN
CREATE TABLE [API].[EquipmentGroups](
	[equipment_group_id] [int] IDENTITY(1,1) NOT NULL,
	[equipment_group_name] [varchar](350) NOT NULL,
	[date_created] [datetime] NOT NULL,
	[created_by] [varchar](250) NULL,
	[last_date_modified] [datetime] NULL,
	[active] [bit] NOT NULL,
	[assigned] [bit] NOT NULL,
 CONSTRAINT [PK_EquipmentGroups] PRIMARY KEY CLUSTERED 
(
	[equipment_group_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]


ALTER TABLE [API].[EquipmentGroups] ADD  CONSTRAINT [DF_EquipmentGroups_assigned]  DEFAULT ((0)) FOR [assigned]

END

-- ================================
-- Table: [API].[EquipmentGroupList]
-- ================================
IF NOT EXISTS (
    SELECT 1 FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_SCHEMA = 'API' AND TABLE_NAME = 'EquipmentGroupList'
)
BEGIN

CREATE TABLE [API].[EquipmentGroupList](
	[equipment_group_id] [int] NOT NULL,
	[equipment_id] [int] NOT NULL
) ON [PRIMARY]

ALTER TABLE [API].[EquipmentGroupList]  WITH CHECK ADD  CONSTRAINT [equipmentgroupid] FOREIGN KEY([equipment_group_id])
REFERENCES [API].[EquipmentGroups] ([equipment_group_id])

ALTER TABLE [API].[EquipmentGroupList] CHECK CONSTRAINT [equipmentgroupid]

ALTER TABLE [API].[EquipmentGroupList]  WITH CHECK ADD  CONSTRAINT [equipmentid] FOREIGN KEY([equipment_id])
REFERENCES [API].[Equipment] ([equipment_id])

ALTER TABLE [API].[EquipmentGroupList] CHECK CONSTRAINT [equipmentid]


END


-- ================================
-- Table: [API].[FunctionGroups]
-- ================================
IF NOT EXISTS (
    SELECT 1 FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_SCHEMA = 'API' AND TABLE_NAME = 'FunctionGroups'
)
BEGIN
CREATE TABLE [API].[FunctionGroups](
	[function_group_id] [int] IDENTITY(1,1) NOT NULL,
	[function_group_name] [varchar](350) NOT NULL,
	[date_created] [datetime] NOT NULL,
	[created_by] [varchar](250) NULL,
	[last_date_modified] [datetime] NULL,
	[active] [bit] NOT NULL,
	[assigned] [bit] NOT NULL,
 CONSTRAINT [PK_FunctionGroups] PRIMARY KEY CLUSTERED 
(
	[function_group_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]

ALTER TABLE [API].[FunctionGroups] ADD  CONSTRAINT [DF_FunctionGroups_assigned]  DEFAULT ((0)) FOR [assigned]


END


-- ================================
-- Table: [API].[FunctionGroupList]
-- ================================
IF NOT EXISTS (
    SELECT 1 FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_SCHEMA = 'API' AND TABLE_NAME = 'FunctionGroupList'
)
BEGIN

CREATE TABLE [API].[FunctionGroupList](
	[function_group_id] [int] NOT NULL,
	[function_id] [int] NOT NULL
) ON [PRIMARY]


ALTER TABLE [API].[FunctionGroupList]  WITH CHECK ADD  CONSTRAINT [functiongroup] FOREIGN KEY([function_group_id])
REFERENCES [API].[FunctionGroups] ([function_group_id])

ALTER TABLE [API].[FunctionGroupList] CHECK CONSTRAINT [functiongroup]

ALTER TABLE [API].[FunctionGroupList]  WITH CHECK ADD  CONSTRAINT [functionid] FOREIGN KEY([function_id])
REFERENCES [API].[FunctionsList] ([function_id])

ALTER TABLE [API].[FunctionGroupList] CHECK CONSTRAINT [functionid]



END


-- ================================
-- Table: [API].[EquipmentFunctionAssignments]
-- ================================
IF NOT EXISTS (
    SELECT 1 FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_SCHEMA = 'API' AND TABLE_NAME = 'EquipmentFunctionAssignments'
)
BEGIN

CREATE TABLE [API].[EquipmentFunctionAssignments](
	[assignment_id] [int] IDENTITY(1,1) NOT NULL,
	[assignment_name] [varchar](350) NOT NULL,
	[equipment_group_id] [int] NOT NULL,
	[function_group_id] [int] NOT NULL,
	[date_created] [datetime] NOT NULL,
	[created_by] [varchar](250) NULL,
	[last_date_modified] [datetime] NULL,
	[active] [bit] NOT NULL,
 CONSTRAINT [PK_EquipmentFunctionAssignments] PRIMARY KEY CLUSTERED 
(
	[assignment_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]

ALTER TABLE [API].[EquipmentFunctionAssignments]  WITH CHECK ADD  CONSTRAINT [equip_group_id] FOREIGN KEY([equipment_group_id])
REFERENCES [API].[EquipmentGroups] ([equipment_group_id])

ALTER TABLE [API].[EquipmentFunctionAssignments] CHECK CONSTRAINT [equip_group_id]

ALTER TABLE [API].[EquipmentFunctionAssignments]  WITH CHECK ADD  CONSTRAINT [funct_group_id] FOREIGN KEY([function_group_id])
REFERENCES [API].[FunctionGroups] ([function_group_id])

ALTER TABLE [API].[EquipmentFunctionAssignments] CHECK CONSTRAINT [funct_group_id]



END



-- ================================
-- Table: [API].[EventLogs]
-- ================================
IF NOT EXISTS (
    SELECT 1 FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_SCHEMA = 'API' AND TABLE_NAME = 'EventLogs'
)
BEGIN

CREATE TABLE [API].[EventLogs](
	[log_id] [int] IDENTITY(1,1) NOT NULL,
	[timestamp] [datetime] NOT NULL,
	[username] [varchar](150) NULL,
	[event_type] [varchar](150) NULL,
	[before_change] [varchar](max) NULL,
	[after_change] [varchar](max) NULL,
	[description] [varchar](500) NULL,
 CONSTRAINT [PK_EventLogs] PRIMARY KEY CLUSTERED 
(
	[log_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] 


END



"""