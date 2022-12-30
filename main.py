from blockchain import Blockchain

blockchain = Blockchain()

blockchain.add_block("Python")
blockchain.add_block("JAVA")
blockchain.add_block("JavaScript")
blockchain.add_block("C++")


for block in blockchain.get_blocks():
    print()
    print('\t' + block.to_string())

print()


