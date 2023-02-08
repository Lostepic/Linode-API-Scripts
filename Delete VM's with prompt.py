import linode_api4
import os

# Initialize the API client
api_key = os.getenv("LINODE_API_KEY")
client = linode_api4.Client(auth_token=api_key)

# List all Linodes associated with your account
linodes = client.linode.list()

# Print a numbered list of the Linodes
for i, linode in enumerate(linodes):
    print(f"{i+1}. {linode.label} (ID: {linode.id})")

# Prompt the user to select a Linode for deletion
selected_index = int(input("Enter the number of the Linode you wish to delete: ")) - 1
selected_linode = linodes[selected_index]

# Confirm the deletion with the user
confirmation = input(f"Are you sure you want to delete the Linode '{selected_linode.label}' (ID: {selected_linode.id})? [y/N] ")
if confirmation.lower() == "y":
    # Delete the selected Linode
    client.linode.delete(selected_linode.id)
    print(f"Linode '{selected_linode.label}' (ID: {selected_linode.id}) has been deleted.")
else:
    print("Deletion cancelled.")
