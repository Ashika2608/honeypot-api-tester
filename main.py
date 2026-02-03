from tester import test_honeypot_endpoint

def main():
    print("=== Agentic Honeypot API Endpoint Tester ===")

    url = input("Enter Honeypot API Endpoint URL: ")
    result = test_honeypot_endpoint(url)

    print("\nTest Result:")
    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
