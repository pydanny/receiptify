import envoy
import sys


if __name__ == "__main__":
    filename = sys.argv[-1]
    if filename.endswith("receiptify.py"):
        print("ERROR! Please enter a ReStructuredText filename!")
        sys.exit()
    envoy.run("simplicity receipts.rst > input/receipts.json")
