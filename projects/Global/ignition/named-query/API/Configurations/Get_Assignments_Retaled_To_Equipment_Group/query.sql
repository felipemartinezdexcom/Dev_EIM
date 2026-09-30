SELECT EquipmentFunctionAssignments.equipment_group_id,
  EquipmentFunctionAssignments.function_group_id,
  EquipmentFunctionAssignments.assignment_name,
  EquipmentFunctionAssignments.active,
  EquipmentGroups.equipment_group_name,
  FunctionGroups.function_group_name
FROM [API].EquipmentFunctionAssignments
  LEFT OUTER JOIN [API].EquipmentGroups
    ON EquipmentFunctionAssignments.equipment_group_id =
    EquipmentGroups.equipment_group_id
  LEFT OUTER JOIN [API].FunctionGroups
    ON EquipmentFunctionAssignments.function_group_id =
    FunctionGroups.function_group_id
    where EquipmentFunctionAssignments.equipment_group_id=:equipment_group_id