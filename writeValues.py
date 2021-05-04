from azure.keyvault.secrets import SecretClient
from azure.identity import AzureCliCredential
import datetime


KVUri = "https://carloshuang-keyvault.vault.azure.net/"
#Change to the appropriate one for the key-vault, use environ variables too if needed.

credential = AzureCliCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

secretName = "firstSecret"
secretValue = "SomeValue"



print(f"Creating a secret in carloshuang-keyvault called '{secretName}' with the value '{secretValue}' ...")

startTime = datetime.datetime.now()
client.set_secret(secretName, secretValue)
endTime = datetime.datetime.now()

print(f"The time taken was {(endTime-startTime).microseconds / 1000} milliseconds")


print(" done.")
