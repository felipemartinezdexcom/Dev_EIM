SELECT EquipmentGroupList.equipment_group_id,
  EquipmentGroupList.equipment_id,
  EquipmentGroups.equipment_group_name
FROM [API].EquipmentGroups
  RIGHT OUTER JOIN [API].EquipmentGroupList ON EquipmentGroupList.equipment_group_id =
    EquipmentGroups.equipment_group_id
    where EquipmentGroupList.equipment_id=:equipment_id