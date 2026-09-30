SELECT EquipmentFunctionAssignments.assignment_id,
  EquipmentFunctionAssignments.assignment_name,
  EquipmentGroups.equipment_group_name,
  FunctionGroups.function_group_name,
  EquipmentFunctionAssignments.date_created,
  EquipmentFunctionAssignments.created_by,
  EquipmentFunctionAssignments.last_date_modified,
  EquipmentFunctionAssignments.active,
  EquipmentFunctionAssignments.equipment_group_id
FROM [API].EquipmentFunctionAssignments
  LEFT OUTER JOIN [API].EquipmentGroups
    ON EquipmentFunctionAssignments.equipment_group_id =
    EquipmentGroups.equipment_group_id
  LEFT OUTER JOIN [API].FunctionGroups
    ON EquipmentFunctionAssignments.function_group_id =
    FunctionGroups.function_group_id