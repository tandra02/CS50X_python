import re

def is_md5_hash(hash_str):
    # Check if the string is exactly 32 characters long and all are valid hex characters
    return bool(re.fullmatch(r'[0-9a-fA-F]{32}', hash_str))

def count_md5_hashes(file_path):
    md5_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            hash_str = line.strip()
            if is_md5_hash(hash_str):
                md5_count += 1
    return md5_count

file_path = '/root/Desktop/QuestionFiles/HashFunctions/Question2/hashes.txt'
md5_hash_count = count_md5_hashes(file_path)
print(f"Number of MD5 hashes: {md5_hash_count}")
