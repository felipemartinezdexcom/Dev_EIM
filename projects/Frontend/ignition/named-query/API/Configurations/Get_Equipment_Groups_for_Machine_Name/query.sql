SELECT EquipmentGroupList.equipment_group_id,
  EquipmentGroupList.equipment_id,
  EquipmentGroups.equipment_group_name,
  EquipmentGroups.active
FROM [API].EquipmentGroupList
  LEFT OUTER JOIN [API].EquipmentGroups ON EquipmentGroupList.equipment_group_id =
    EquipmentGroups.equipment_group_id
where EquipmentGroupList.equipment_id=:equipment_id
