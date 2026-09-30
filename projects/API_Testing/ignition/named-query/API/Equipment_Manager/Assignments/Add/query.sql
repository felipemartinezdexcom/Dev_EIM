IF NOT EXISTS
(
    SELECT 1
    FROM [API].[EquipmentFunctionAssignments]
    WHERE [equipment_group_id]=:equipment_group_id and [function_group_id]=:function_group_id 

)
BEGIN
    INSERT INTO [API].[EquipmentFunctionAssignments]
    (
        assignment_name,
        equipment_group_id,
        function_group_id,
        date_created,
        created_by,
        last_date_modified,
        active
    )
    VALUES
    (
        :assignment_name,
        :equipment_group_id,
        :function_group_id,
        GETDATE(),
        :created_by,
        GETDATE(),
        1
    );
	SELECT 1 AS result;
END
ELSE
BEGIN
    SELECT 0 AS result;
END