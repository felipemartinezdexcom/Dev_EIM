IF NOT EXISTS (
    SELECT 1 FROM [API].Equipment WHERE [equipment_name] = :equipment_name  
)
BEGIN
    INSERT INTO [API].Equipment (
        [equipment_name],
        [date_created],
        [created_by],
        [active]
    )
    VALUES (
        :equipment_name,
        GETDATE(),
        :username,
        0
    );
END
