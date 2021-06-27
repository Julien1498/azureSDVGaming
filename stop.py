from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient

GROUP_NAME = 'MachineTest1_group'
VM_NAME = 'MachineTest1'

def get_credentials():
    subscription_id = "98bbe141-a2b9-4d6d-a410-35d71c6d0108"
    credentials = ServicePrincipalCredentials(
        client_id="8c51d398-463c-41fd-bfbc-8ef8807e7127",
        secret="~0ykwkBO69NeH_lENdg1dgg50N6~-P5HYH",
        tenant="b7b023b8-7c32-4c02-92a6-c8cdaa1d189c"
    )
    return credentials, subscription_id

def stop():
    credentials, subscription_id = get_credentials()
    compute_client = ComputeManagementClient(credentials, subscription_id)
    # Stop the VM
    print('\Stop VM')
    async_vm_start = compute_client.virtual_machines.power_off(
        GROUP_NAME, VM_NAME)
    async_vm_start.wait()
    print('\nFINI')

if __name__ == "__main__":
    stop()
