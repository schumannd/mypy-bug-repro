from mb2.steps.jmeter.step import JCfg
from mb2.steps.init.impl import get_resource_costs

class TestCollectMetrics:
    def test_get_resource_costs(self):
        cfg = JCfg()
        get_resource_costs(cfg)  # <- Wrong type should be detected

