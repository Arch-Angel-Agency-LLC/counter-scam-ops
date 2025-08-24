from decision_helper import suggest

def test_suggest_minimal_path():
    recs = suggest(docx=0, pdf=0, portals=0, wallets=0, sessions=0, branches=0)
    # Should prioritize docx request and portal send & wallet first ask
    assert any('editable DOCX' in r for r in recs)
    assert any('Send hosted logo' in r for r in recs)
    assert any('first wallet address' in r for r in recs)

def test_suggest_stabilize():
    recs = suggest(docx=3, pdf=2, portals=1, wallets=2, sessions=3, branches=4)
    assert any('Stabilize' in r for r in recs)
