import models as md


class DatabaseConnection:

    def __init__(self) -> None:
        # durectory should be C:\Users\<username>\AppData\Roaming\<directory_name>
        md.db.connect()


        self.create_passwords_table()


    def create_passwords_table(self):

        try:
            md.db.create_tables([md.Password])

        except:

            print("Such table already exists")


    def add_password(self, new_p_address, new_p_name, new_p, new_p_description):

        new_password = md.Password.create(
                        password_address=new_p_address,
                        password_name=new_p_name,
                        password=new_p,
                        password_description=new_p_description
                    )
        
        new_password.save()


    def fetch_data(self):
            
        db_data = md.Password.select(md.Password.password_name, md.Password.password_address)

        return db_data


    def fetch_password_data(self, sql_data):

        password_data = sql_data.split()

        result = md.Password.select().where((md.Password.password_name == password_data[0]) & (md.Password.password_address == password_data[1]))

        return result
    

    def update_password_data(self, password_data, password_value):
        
        splitted_data = password_data.split()

        row = md.Password.get((md.Password.password_name == splitted_data[0]) & (md.Password.password_address == splitted_data[1]))
            
        row.password = password_value

        row.save()


    def delete_password(self, p_name, p_address):

        password_info = md.Password.get(md.Password.password_name == p_name & md.Password.password_address == p_address)

        password_info.delete_instance()


    def __del__(self) -> None:

        md.db.close()