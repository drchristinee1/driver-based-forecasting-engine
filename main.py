import json
from forecasting_engine.forecast import run_forecast

def load_input(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def main():
    print("=== Driver-Based Forecasting Engine ===")

    input_file = "data/sample_input.json"

    try:
        data = load_input(input_file)
    except FileNotFoundError:
        print(f"Input file not found: {input_file}")
        return

    result = run_forecast(data)

    print("\n=== Forecast Result ===\n")
    print(json.dumps(result, indent=4))

    # Save output
    output_file = "outputs/sample_output.json"
    with open(output_file, 'w') as f:
        json.dump(result, f, indent=4)

    print(f"\nOutput saved to {output_file}")

if __name__ == "__main__":
    main()
