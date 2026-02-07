from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_and_filter(data_dir: Path) -> pd.DataFrame:
	csv_files = sorted(data_dir.glob("*.csv"))
	frames: list[pd.DataFrame] = []

	for csv_file in csv_files:
		df = pd.read_csv(csv_file)

    # Filter for "Pink Morsel" product and select relevant columns
		product_mask = df["product"].astype(str).str.strip().str.casefold() == "pink morsel"
		df = df.loc[product_mask, ["price", "quantity", "date", "region"]].copy()

    # Clean price and quantity columns and calculate slales
		df["price"] = (
			df["price"].astype(str).str.replace("$", "", regex=False).astype(float)
		)
		df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
		df["sales"] = df["price"] * df["quantity"]

		df = df[["sales", "date", "region"]]
		frames.append(df)

	if not frames:
		return pd.DataFrame(columns=["sales", "date", "region"])

	return pd.concat(frames, ignore_index=True)


def main() -> None:
	repo_root = Path(__file__).resolve().parent
	data_dir = repo_root / "data"
	output_path = repo_root / "pink_morsel_sales.csv"

	result = load_and_filter(data_dir)
	result.to_csv(output_path, index=False)


if __name__ == "__main__":
	main()
