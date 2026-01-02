---
url: https://nadohq.github.io/nado-python-sdk/_modules/nado_protocol/client/apis/rewards/query.html
---

# Source code for nado_protocol.client.apis.rewards.query

```python

from nado_protocol.client.apis.base import NadoBaseAPI

[docs]class RewardsQueryAPI(NadoBaseAPI):
    # TODO: revise once staking contract is deployed
[docs]    def get_claim_and_stake_estimated_tokens(self, wallet: str) -> int:
        """
        Estimates the amount of USDC -> TOKEN swap when claiming + staking USDC rewards
        """
        assert self.context.contracts.staking is not None
        return self.context.contracts.staking.functions.getEstimatedTokensToStake(
            wallet
        ).call()

```