from google.cloud import pubsub_v1
from google.oauth2.service_account import Credentials

# TODO: replace 'your-project-id' with your GCP project ID
project_id = "my-dev-project-417118"
# TODO: replace 'your-topic-id' with your Pub/Sub topic ID
topic_id = "Order_topic"
credentials = Credentials.from_service_account_file("C:/Users/TS6934/Downloads/my-dev-project-417118-49e4999f52af.json")

publisher = pubsub_v1.PublisherClient(credentials=credentials)
topic_path = publisher.topic_path(project_id, topic_id)

data = "Hello World"
# # Data must be a bytestring
data = data.encode("utf-8")
# # When you publish a message, the client returns a future.
future = publisher.publish(topic_path, data)
print(future.result())
#
print(f"Published messages to {topic_path}.")
