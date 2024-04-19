class TradePartnerMapper:
    def __init__(self, tp_repo, tenant):
        self.tp_repo = tp_repo
        self.tenant = tenant

    def map(self, trade_partner: str):
        return self.tp_repo.find_most_similar(self.tenant, trade_partner)
