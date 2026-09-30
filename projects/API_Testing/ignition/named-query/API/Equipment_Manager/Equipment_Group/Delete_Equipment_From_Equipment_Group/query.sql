delete from [API].EquipmentGroupList where equipment_group_id=:equipment_group_id and equipment_id=:equipment_id


update [API].Equipment set assigned=0 where equipment_id=:equipment_id