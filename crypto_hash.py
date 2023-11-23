import hashlib
import json

# def stringify(data):
#     return json.dumps(data)

def crypto_hash(*args):
    """
    Retrun a sha-256 hash of the given argiments
    """
    stringified_data =sorted(map(lambda data:json.dumps(data),args)) 

    joined_data = ''.join(stringified_data)
  
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()


def main():
    print(f"crypto_hash('1,2'):{crypto_hash('1','2')}")
    print(f"crypto_hash('2,1'):{crypto_hash('2','1')}")
    
if __name__=='__main__':
    main()