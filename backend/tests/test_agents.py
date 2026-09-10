def test_agent_orchestrator():
    prompt = "Test execution query for agentic-smart-contract-auditor"
    assert len(prompt) > 0
    assert "Test" in prompt
