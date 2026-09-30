SELECT EquipmentGroupList.equipment_group_id,
  Equipment.equipment_name,
  Equipment.equipment_id
FROM [API].EquipmentGroupList
  RIGHT OUTER JOIN [API].Equipment ON EquipmentGroupList.equipment_id =
    Equipment.equipment_id
    where EquipmentGroupList.equipment_group_id=:equipment_group_id