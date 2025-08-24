import pathlib
from log_integrity_chain import build_chain

def test_build_chain_basic(tmp_path):
    csv_path = tmp_path / 'evidence_log.csv'
    csv_path.write_text('artifact_id,utc_timestamp\nA1,2025-01-01T00:00:00Z\nA2,2025-01-01T01:00:00Z\n')
    chain = build_chain(csv_path)
    assert len(chain) == 3  # header + 2 lines
    # Ensure each chain hash links (except first which uses empty prev)
    for i in range(1, len(chain)):
        assert chain[i]['chain_hash'] != chain[i-1]['chain_hash']
