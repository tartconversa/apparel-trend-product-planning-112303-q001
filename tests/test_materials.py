import csv
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {'search_signals.csv': (['signal_id', 'period', 'region', 'audience', 'theme', 'search_index', 'campaign_flag', 'coverage'], 60), 'sales_context.csv': (['period', 'region', 'sku', 'series', 'units', 'stockout_days', 'price_band'], 48), 'brand_series.csv': (['series', 'season', 'audience', 'price_band', 'position_status', 'updated_at'], 24), 'proposals.csv': (['proposal_id', 'series', 'theme', 'audience', 'price_band', 'review_state', 'sample_slot', 'accepted_at'], 30)}

class MaterialTests(unittest.TestCase):
    def test_declared_csv_contracts(self):
        for filename, (columns, count) in EXPECTED.items():
            with self.subTest(filename=filename):
                with (ROOT / "data" / filename).open(encoding="utf-8-sig", newline="") as stream:
                    reader = csv.DictReader(stream)
                    rows = list(reader)
                self.assertEqual(reader.fieldnames, columns)
                self.assertEqual(len(rows), count)
                self.assertTrue(all(None not in row for row in rows))

if __name__ == "__main__":
    unittest.main()
