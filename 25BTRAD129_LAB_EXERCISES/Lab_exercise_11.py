def read_log_file(filename):
    counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            if not content.strip():
                print("The log file is empty.")
                return
            for line in content.splitlines():
                upper_line = line.upper()
                for keyword in counts:
                    counts[keyword] += upper_line.count(keyword)
                    
        print("\nLog File Summary")
        print("----------------")
        for keyword, count in counts.items():
            print(f"{keyword}: {count}")
            
    except FileNotFoundError:
        print("Error: The specified log file was not found.")
    except OSError as error:
        print(f"Unable to read the file: {error}")

read_log_file("sample.log")
