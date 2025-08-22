from typing import Dict

import pymysql


class MySQLManager:
    def __init__(self, credential: dict):
        self.credential = credential

    def _connect(self):
        return pymysql.connect(
            host=self.credential["host"],
            user=self.credential["user"],
            password=self.credential["password"],
            database=self.credential["dbname"],
            port=int(self.credential.get("port", 3306)),
        )

    def check_connection(self) -> Dict[str, str]:
        try:
            with self._connect() as conn:
                return {"success": True, "message": "Connected successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}

    def check_binlog_status(self) -> Dict[str, str]:
        """Checks whether binlog is enabled and configured properly"""
        try:
            with self._connect() as conn:
                with conn.cursor() as cur:
                    cur.execute("SHOW VARIABLES LIKE 'log_bin';")
                    log_bin = cur.fetchone()[1]

                    cur.execute("SHOW VARIABLES LIKE 'binlog_format';")
                    binlog_format = cur.fetchone()[1]

                    cur.execute("SHOW VARIABLES LIKE 'binlog_row_image';")
                    row_image = cur.fetchone()[1]

                    cur.execute("SHOW VARIABLES LIKE 'server_id';")
                    server_id = cur.fetchone()[1]

                    if log_bin.lower() != "on":
                        return {"success": False, "message": "Binary log is OFF"}
                    if binlog_format.upper() != "ROW":
                        return {"success": False, "message": f"Invalid binlog_format={binlog_format}, must be ROW"}
                    if row_image.upper() != "FULL":
                        return {"success": False, "message": f"Invalid binlog_row_image={row_image}, must be FULL"}
                    if server_id == "0":
                        return {"success": False, "message": "server_id must be non-zero for replication"}

                    return {
                        "success": True,
                        "message": f"Binlog enabled with format={binlog_format}, row_image={row_image}, server_id={server_id}"
                    }

        except Exception as e:
            return {"success": False, "message": str(e)}
