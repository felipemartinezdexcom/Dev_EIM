update storeProcsList set sp_name=:new_sp_name,update_insert=:update_insert,
last_date_modified=datetime('new'),
last_modified_by=:username
where sp_id=:sp_id