import peewee

from datetime import datetime
from database_manage import DatabaseManager
from local_settings import DATABASE

database_manager = DatabaseManager(
    DATABASE['name'],
    user=DATABASE['user'],
    password=DATABASE['password'],
    host=DATABASE['host'],
    port=DATABASE['port'],
)


class MyBaseModel(peewee.Model):
    created_date = peewee.DateField(default=datetime.now)
    updated_date = peewee.DateTimeField(default=datetime.now)

    class Meta:
        abstract = True
        database = database_manager.db


class URL(peewee.Model):
    url = peewee.CharField(unique=True)


class Article(MyBaseModel):
    title = peewee.CharField(max_length=256, verbose_name='Title')
    description = peewee.TextField(verbose_name='Description')
    Links = peewee.ForeignKeyField(
        URL,
        on_delete='CASCADE',
        verbose_name='Links',
    )


if __name__ == '__main__':
    try:
        for model in [Article, URL]:
            if not model.table_exists():
                database_manager.create_table(models=[model])
    except peewee.DatabaseError as error:
        print(f'Database Error : {error}')
    finally:
        database_manager.db.close()
