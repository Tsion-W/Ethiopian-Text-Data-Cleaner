import argparse
from cleaner.cleaner import EthiopianTextCleaner

def main():
    parser = argparse.ArgumentParser(description="Clean Ethiopian text data")
    parser.add_argument("--input", required=True, help="Input text file")
    parser.add_argument("--output", required=True, help="Output text file")
    parser.add_argument("--normalize-numerals", action="store_true", help="Convert Geez numerals to Arabic numerals")
    args = parser.parse_args()

    cleaner = EthiopianTextCleaner(
        normalize_numerals=args.normalize_numerals,
    )

    with open(args.input, "r", encoding="utf-8") as f:
        lines = f.readlines()

    cleaned = cleaner.clean_corpus(lines)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write("\n".join(cleaned))

    print(f"[INFO] Cleaned text saved to {args.output}")

if __name__ == "__main__":
    main()
