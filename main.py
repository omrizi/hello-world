from dotenv import load_dotenv

load_dotenv()
def main():
    try:
        env = os.environ.get("ENV")
        tier = os.environ.get("TIER")
        print(f"{env}-{tier}")
    except Exception as e:
        print(f"error {e} occured")

if __name__ == "__main__":
    main()