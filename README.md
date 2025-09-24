Exercise: Secrets Manager
Design an API key storage system to store API keys for services. The
program should present two options to users to store and retrieve
passwords. You can use either an in-memory storage or store your
credentials in a file.
For storing, the program should ask for the inputs and store the password
securely. The inputs are:
String: ServiceName
String: APIKey
For retrieving the program asks for the service name and retrieves the
API key.

Extra Credit (Optional)
1.Experiment with storing your passwords in a database (e.g. SQLite,
MySQL, etc.) and retrieving that at runtime so the credentials persist.