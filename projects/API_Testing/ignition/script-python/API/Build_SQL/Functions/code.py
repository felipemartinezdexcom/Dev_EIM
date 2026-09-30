import os



def get_mssql_data_export(db_connection_name, schema, table_names=None):
    """
    Export MSSQL data as INSERT statements.

    Args:
        db_connection_name (str): Ignition datasource name
        schema (str): MSSQL schema name
        table_names (list): Optional list of tables to export.
                            If None or empty, exports all tables.

    Returns:
        str
    """

    export_statements = []

    try:


        # ----------------------------------------------------------
        # Determine tables to export
        # ----------------------------------------------------------
        if table_names is None:
            table_names = []

        if len(table_names) == 0:

            tables_query = """
                SELECT TABLE_NAME
                FROM INFORMATION_SCHEMA.TABLES
                WHERE TABLE_TYPE = 'BASE TABLE'
                  AND TABLE_SCHEMA = ?
                ORDER BY TABLE_NAME
            """

            results = system.db.runPrepQuery(
                tables_query,
                [schema],
                db_connection_name
            )

            table_names = []

            for row in range(results.getRowCount()):
                table_names.append(
                    results.getValueAt(row, "TABLE_NAME")
                )

        if len(table_names) == 0:
            return "-- No tables found in schema [{}]".format(schema)

  
        # ----------------------------------------------------------
        # Export each table
        # ----------------------------------------------------------
        for table_name in table_names:

            full_name = "[{}].[{}]".format(
                schema,
                table_name
            )

            export_statements.append("")
            export_statements.append("-- ====================================")
            export_statements.append("-- Data for {}".format(full_name))
            export_statements.append("-- ====================================")

            # ------------------------------------------------------
            # Verify table exists
            # ------------------------------------------------------
            table_exists_query = """
                SELECT COUNT(*) AS cnt
                FROM INFORMATION_SCHEMA.TABLES
                WHERE TABLE_SCHEMA = ?
                  AND TABLE_NAME = ?
            """

            exists_result = system.db.runPrepQuery(
                table_exists_query,
                [schema, table_name],
                db_connection_name
            )

            if exists_result.getValueAt(0, "cnt") == 0:

                export_statements.append(
                    "-- Table not found: {}".format(full_name)
                )

                continue

            # ------------------------------------------------------
            # Detect identity column
            # ------------------------------------------------------
            identity_query = """
                SELECT COLUMN_NAME
                FROM INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_SCHEMA = ?
                  AND TABLE_NAME = ?
                  AND COLUMNPROPERTY(
                        OBJECT_ID(TABLE_SCHEMA + '.' + TABLE_NAME),
                        COLUMN_NAME,
                        'IsIdentity'
                      ) = 1
            """

            identity_result = system.db.runPrepQuery(
                identity_query,
                [schema, table_name],
                db_connection_name
            )

            has_identity = identity_result.getRowCount() > 0
            identity_column = None

            if has_identity:
                identity_column = identity_result.getValueAt(
                    0,
                    "COLUMN_NAME"
                )

            # ------------------------------------------------------
            # Get data
            # ------------------------------------------------------
            data_query = "SELECT * FROM {}".format(full_name)

            data_result = system.db.runQuery(
                data_query,
                db_connection_name
            )

            row_count = data_result.getRowCount()

            if row_count == 0:

                export_statements.append("-- No data found")

                continue

            col_count = data_result.getColumnCount()

            col_names = []

            for col in range(col_count):

                col_names.append(
                    "[{}]".format(
                        data_result.getColumnName(col)
                    )
                )

            cols_joined = ", ".join(col_names)

            # ------------------------------------------------------
            # Enable identity insert if needed
            # ------------------------------------------------------
            if has_identity:

                export_statements.append("")
                export_statements.append(
                    "SET IDENTITY_INSERT {} ON;".format(
                        full_name
                    )
                )
                export_statements.append("")

            # ------------------------------------------------------
            # Generate INSERT statements
            # ------------------------------------------------------
            for data_row in range(row_count):

                values = []

                for col in range(col_count):

                    val = data_result.getValueAt(
                        data_row,
                        col
                    )

                    if val is None:

                        values.append("NULL")

                    elif isinstance(val, bool):

                        values.append(
                            "1" if val else "0"
                        )

                    elif isinstance(val, (int, long, float)):

                        values.append(str(val))

                    else:

                        try:
                            class_name = val.getClass().getName()
                        except:
                            class_name = ""

                        if class_name in (
                            "java.sql.Timestamp",
                            "java.sql.Date",
                            "java.util.Date",
                            "java.sql.Time"
                        ):

                            values.append(
                                "'" +
                                system.date.format(
                                    val,
                                    "yyyy-MM-dd HH:mm:ss.SSS"
                                ) +
                                "'"
                            )

                        else:

                            escaped = str(val).replace(
                                "'",
                                "''"
                            )

                            values.append(
                                "'" + escaped + "'"
                            )

                insert_stmt = (
                    "INSERT INTO {} ({}) VALUES ({});"
                ).format(
                    full_name,
                    cols_joined,
                    ", ".join(values)
                )

                export_statements.append(
                    insert_stmt
                )

            # ------------------------------------------------------
            # Disable identity insert
            # ------------------------------------------------------
            if has_identity:

                export_statements.append("")
                export_statements.append(
                    "SET IDENTITY_INSERT {} OFF;".format(
                        full_name
                    )
                )




        return "\n".join(
            export_statements
        )

    except Exception as e:

        return "-- ERROR: {}".format(
            str(e)
        )
        
        



# ── Configure this ────────────────────────────────────────────────────────────
TARGET_PATH = "/usr/local/bin/ignition/data/projects/API_Testing/ignition/script-python/API/Build_SQL/Software_Versions/code.py"
# ─────────────────────────────────────────────────────────────────────────────




def insert_Software_Version(TARGET_PATH, Software_Version_String):
	

    if not os.path.isfile(TARGET_PATH):
        print("[ERROR] File not found: " + TARGET_PATH)
        return

    with open(TARGET_PATH, "r") as fh:
        source = fh.read()

	updated = source.rstrip("\n") + "\n" +"Software_Version_"+str(system.date.format(system.date.now(), "yyyyMMdd_HHmmss"))+'="""'+ Software_Version_String+'"""'

    with open(TARGET_PATH, "w") as fh:
        fh.write(updated)

    print("[OK] demo_function injected -> " + TARGET_PATH)

def rebuild_from_Software_Version(APIConfigDB, SoftwareVersion):
	
	params={"database":APIConfigDB}
	system.db.execUpdate("API/Configurations/Drop_All_Tables",params)
	params["query_string"]=API.Build_SQL.Steps.BUILD_TABLES_STRING
	system.db.execUpdate("API/Configurations/Query_String_Update", params)
	params["query_string"]=SoftwareVersion
	system.db.execUpdate("API/Configurations/Query_String_Update", params)
	return "Rebuilt Completed"