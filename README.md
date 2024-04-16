The POC is implemented in clean architecture.
The structure is like the figure below but in different names.
![Clean Architecture](https://i.stack.imgur.com/1qT9h.png)
Picture 1: copy from https://softwareengineering.stackexchange.com/questions/388578/clean-architecture-is-the-input-boundary-necessary

The module structure of this POC is that:
* `entities`: classes represent business domain object. It corresponds to the "ENTITY" in Picture 1.
* `port.gateways`: gateway interfaces. It corresponds to the "\<I> ENTITY GATEWAY" in Picture 1.
* `adapter`: the implementations of port.gateways. It corresponds to the "ENTITY GATEWAY IMPLEMENTATION" in Picture 1.
* `port.in_bound`: interfaces for defining the input of the use case. It corresponds to the UPPER "\<I> BOUNDARY" and "REQUEST MODEL" in Picture 1.
* `use_cases`: the implementations of port.in_bound. It corresponds to the "INTERACTOR" in Picture 1.
* `port.out_bound`: interfaces for defining the output of the use case. It corresponds to the LOWER "\<I> BOUNDARY" and "RESPONSE MODEL" in Picture 1.
* `presenters`: the implementations of port.out_bound, which able to produce side effects to the world. It corresponds to the "PRESENTER" in Picture 1.
* `factories`: factories for creating adapters, presenters, and use_cases

Refactor TODOs for this POC:
- [ ] Move `port.in_bound.PayloadInterpreter` to `port.gateways` because it actually is a "gateway" that returning entities.
- [ ] The interfaces in `port.in_bound` should not contains gateway interfaces. They should be passed into use_cases from the constructors.
  ```python
  # from 
  def import_mbl(self, tenant: str, import_mbl_payload: str, payload_interpreter: PayloadInterpreter,
                   mbl_gateway: MblGateway, trade_partner_gateway: TradePartnerGateway, presenter: ImportMblResult)
  # to
  def import_mbl(self, tenant: str, import_mbl_payload: str)
  ```
  and the constructor of use_case (implementation) should be:
  ```python
  # from 
  class UseCases(ImportMbl):
    def __init__(self, payload_interpreter: PayloadInterpreter, mbl_gateway: MblGateway, 
      trade_partner_gateway: TradePartnerGateway, presenter: ImportMblResult)
  ```