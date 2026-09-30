SELECT ---EquipmentGroupList.equipment_id,
 --- EquipmentGroupList.equipment_group_id,
  Equipment.equipment_name,
  Equipment.description,
  EquipmentGroups.equipment_group_name
FROM [API].EquipmentGroupList
  LEFT OUTER JOIN [API].Equipment ON EquipmentGroupList.equipment_id =
    Equipment.equipment_id
  LEFT OUTER JOIN [API].EquipmentGroups ON EquipmentGroupList.equipment_group_id =
    EquipmentGroups.equipment_group_id
      where EquipmentGroupList.equipment_group_id=:equipment_group_id