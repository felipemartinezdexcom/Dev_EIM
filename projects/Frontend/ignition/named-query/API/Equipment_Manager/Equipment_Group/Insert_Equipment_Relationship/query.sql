

IF NOT EXISTS (
    SELECT 1
    FROM [API].[EquipmentGroupList]
    WHERE equipment_group_id = :equipment_group_id
      AND equipment_id = :equipment_id
)
BEGIN
    INSERT INTO [API].[EquipmentGroupList]
        (equipment_group_id, equipment_id)
    VALUES
        (:equipment_group_id, :equipment_id);
        
    update [API].Equipment set assigned=1 where equipment_id=:equipment_id
END