
# import mysql.connector
from web3 import Web3

# def get_db():
#     db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="Pandusai@2003",
#         database="cpd"
#     )
#     return db


# def createuser(email, password, rol):
#     db = get_db()
#     cursor = db.cursor()
#     cursor.execute("INSERT INTO users (email, pass, roleofuser) VALUES (%s, %s, %s)", (email, password, rol))
#     db.commit()
#     db.close()
#     if cursor.rowcount > 0:
#         return True
#     else:
#         return False


# def checkuser(email, password, rol):
#     db = get_db()
#     cursor = db.cursor()
#     cursor.execute("SELECT * FROM users WHERE email = %s AND pass = %s AND roleofuser = %s", (email, password, rol))
#     result = cursor.fetchone()
#     db.close()
#     print(result)
#     if result!=None:
#         return True
#     else:
#         return False
    
    
def addProductToBlock(product_name, product_id, status, source, destination, remarks, role):
    w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
    contract_address='0x51b4Cf710bB8Fb4361e09869725B160fAA3EA7b8'
    contract_abi=[
           {
        "constant": False,
        "inputs": [
            {
                "name": "productId",
                "type": "uint256"
            },
            {
                "name": "status",
                "type": "string"
            },
            {
                "name": "source",
                "type": "string"
            },
            {
                "name": "destination",
                "type": "string"
            },
            {
                "name": "remarks",
                "type": "string"
            }
        ],
        "name": "StatusAddtoProduct",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
        
    ]
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)
    tx_hash = contract.functions.StatusAddtoProduct(product_id, status, source, destination, remarks).transact()
    return tx_hash
    
addProductToBlock('rice', 1, 'good', 'hyd', 'bang', 'good', 'farmer')
    
    
    