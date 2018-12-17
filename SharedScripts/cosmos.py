import azure.cosmos.cosmos_client as cosmos_client

def CountDocuments(database,container):
    config = {
        'ENDPOINT': 'YOUR_COSMOSDB_ENDPOINT',
        'PRIMARYKEY': 'YOUR_COSMOSDB_KEY',
        'DATABASE': database,
        'CONTAINER': container
    }

    # Initialize the Cosmos client
    client = cosmos_client.CosmosClient(url_connection=config['ENDPOINT'], auth={
                                        'masterKey': config['PRIMARYKEY']})

    # Connect to a database
    database_link = 'dbs/' + config['DATABASE']
    db = client.ReadDatabase(database_link)

    # Connect to a container
    container_definition = {
        'id': config['CONTAINER']
    }
    container_link = database_link + '/colls/{0}'.format(config['CONTAINER'])
    container = client.ReadContainer(container_link)

    # Query these items in SQL
    query = {'query': 'SELECT * FROM server s'}

    options = {}
    options['enableCrossPartitionQuery'] = True
    options['maxItemCount'] = 2

    result_iterable = client.QueryItems(container['_self'], query, options)
    count = 0
    for item in iter(result_iterable):
        count = count +1

    #return count
    msg = str(count) + ' document(s) found in DB'
    return msg
