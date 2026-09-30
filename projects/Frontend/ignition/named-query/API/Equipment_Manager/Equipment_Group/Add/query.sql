IF NOT EXISTS
(
    SELECT 1
    FROM [API].[EquipmentGroups]
    WHERE equipment_group_name = :equipment_group_name
)
BEGIN
    INSERT INTO [API].[EquipmentGroups]
    (
        equipment_group_name,
        date_created,
        created_by,
        last_date_modified,
        active
    )
    VALUES
    (
        :equipment_group_name,
        GETDATE(),
        :created_by,
        GETDATE(),
        1
    );

    SELECT equipment_group_id AS result
    FROM [API].[EquipmentGroups]
    WHERE equipment_group_name = :equipment_group_name;
END
ELSE
BEGIN
    SELECT 0 AS result;
END