from azure.keyvault.secrets import SecretClient
from azure.identity import AzureCliCredential
import datetime


KVUri = "https://carloshuang-keyvault.vault.azure.net/"
credential = AzureCliCredential()
client = SecretClient(vault_url=KVUri, credential=credential)


print(f"Retrieving your secret from carloshuang-keyvault.")

startTime = datetime.datetime.now()
retrieved_secret = client.get_secret("firstSecret")
endTime = datetime.datetime.now()

print(f"The time taken was {(endTime-startTime).microseconds / 1000} milliseconds")

print(f"Your secret is '{retrieved_secret.value}'.")


print(" done.")