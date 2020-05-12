from pyhive import presto
connection = presto.connect(
    'presto-tableau.prod.dataf.eb',
    8443,
    user_okta,
    password=password_okta,
    protocol='https',
)
cursor = connection.cursor()
cursor.execute('select id, created, name from hive.eb.events order by created desc limit 1')
print(cursor.fetchall())
