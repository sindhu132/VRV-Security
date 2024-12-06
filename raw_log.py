# Define the content of the raw log file
log_content = """192.168.1.1 - - [03/Dec/2024:10:12:34 +0000] "GET /home HTTP/1.1" 200 512
203.0.113.5 - - [03/Dec/2024:10:12:35 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:36 +0000] "GET /about HTTP/1.1" 200 256
198.51.100.23 - - [03/Dec/2024:10:12:37 +0000] "POST /register HTTP/1.1" 200 128
192.168.1.100 - - [03/Dec/2024:10:12:38 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
172.16.0.3 - - [03/Dec/2024:10:12:39 +0000] "GET /dashboard HTTP/1.1" 200 1024
203.0.113.45 - - [03/Dec/2024:10:12:40 +0000] "POST /feedback HTTP/1.1" 200 128
10.0.0.4 - - [03/Dec/2024:10:12:41 +0000] "GET /profile HTTP/1.1" 200 768
192.168.1.1 - - [03/Dec/2024:10:12:42 +0000] "GET /contact HTTP/1.1" 200 312
198.51.100.23 - - [03/Dec/2024:10:12:43 +0000] "GET /about HTTP/1.1" 200 256
203.0.113.5 - - [03/Dec/2024:10:12:44 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.5 - - [03/Dec/2024:10:12:45 +0000] "GET /services HTTP/1.1" 200 512
192.168.1.100 - - [03/Dec/2024:10:12:46 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
172.16.0.2 - - [03/Dec/2024:10:12:47 +0000] "GET /dashboard HTTP/1.1" 200 1024
192.168.1.1 - - [03/Dec/2024:10:12:48 +0000] "GET /home HTTP/1.1" 200 512
198.51.100.25 - - [03/Dec/2024:10:12:49 +0000] "POST /register HTTP/1.1" 200 128
203.0.113.75 - - [03/Dec/2024:10:12:50 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
192.168.1.10 - - [03/Dec/2024:10:12:51 +0000] "GET /settings HTTP/1.1" 200 256
10.0.0.7 - - [03/Dec/2024:10:12:52 +0000] "GET /support HTTP/1.1" 200 768
198.51.100.29 - - [03/Dec/2024:10:12:53 +0000] "GET /faq HTTP/1.1" 200 128
203.0.113.25 - - [03/Dec/2024:10:12:54 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
"""

# File path to save the raw log file
file_path = "C:/Users/HP/Documents/raw_log_file.txt"

# Write the log content to the file
with open(file_path, 'w') as file:
    file.write(log_content)

print(f"Raw log file created at: {file_path}")
