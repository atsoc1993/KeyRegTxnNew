from algosdk.v2client.algod import AlgodClient
from algosdk.transaction import KeyregTxn
from algosdk.mnemonic import to_private_key
from algosdk.account import address_from_private_key

algod_token = '' #Insert token, leave empty if using nodely
algod_server = '' #Insert server, eg; nodely @ 'https://mainnet-api.4160.nodely.dev'
algod_client = AlgodClient(algod_token, algod_server)

status = algod_client.status()

mnemonic = '' #Insert mnemonic
pk = to_private_key(mnemonic)
address = address_from_private_key(pk)


#Use 'goal account partkeyinfo -d yourDataDirectory' or 'goal account partkeyinfo' from the ~/node directory if you exported to get the information below
selection_key = ''
vote_key = ''
state_proof_key = ''
votefst = 0 # use 'First' and 'Last', not 'Effective First Round' and 'Effective Last Round'
votelst = 0
key_dilution=0 


#Get params, params.flat_fee to True and params.fee to 2_000_000 (2 Algo)
params = algod_client.suggested_params()
params.flat_fee = True
params.fee = 2_000_000

set_node_online = KeyregTxn(
    sender=address,
    selkey=selection_key,
    votekey=vote_key,
    sprfkey=state_proof_key,
    votefst=votefst,
    votelst=votelst,
    votekd=key_dilution,
    sp=params,
)


signed_tx = set_node_online.sign(pk)
tx_id = algod_client.send_transaction(signed_tx)
print(tx_id)


