from django.db import migrations


def rename_file_column(apps, schema_editor):
    with schema_editor.connection.cursor() as cursor:
        cursor.execute("SHOW COLUMNS FROM documents_document LIKE 'file'")
        if cursor.fetchone():
            cursor.execute(
                "ALTER TABLE documents_document CHANGE `file` `file_url` varchar(100) NOT NULL"
            )


def reverse_rename_file_column(apps, schema_editor):
    with schema_editor.connection.cursor() as cursor:
        cursor.execute("SHOW COLUMNS FROM documents_document LIKE 'file_url'")
        if cursor.fetchone():
            cursor.execute(
                "ALTER TABLE documents_document CHANGE `file_url` `file` varchar(100) NOT NULL"
            )


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(rename_file_column, reverse_code=reverse_rename_file_column),
    ]
