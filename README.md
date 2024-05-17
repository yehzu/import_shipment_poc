The POC is implemented in clean architecture.
The structure is like the figure below but in different names.
![Clean Architecture](https://i.stack.imgur.com/1qT9h.png)
Picture 1: copy from https://softwareengineering.stackexchange.com/questions/388578/clean-architecture-is-the-input-boundary-necessary

The module structure of this POC is that:
* `impl.entities`: classes represent business domain object. It corresponds to the "ENTITY" in Picture 1.
* `port.gateways`: gateway interfaces. It corresponds to the "\<I> ENTITY GATEWAY" in Picture 1.
* `impl.adapters`: the implementations of port.gateways. It corresponds to the "ENTITY GATEWAY IMPLEMENTATION" in Picture 1.
* `port.inbound`: interfaces for defining the input of the use case. It corresponds to the UPPER "\<I> BOUNDARY" and "REQUEST MODEL" in Picture 1.
* `impl.use_cases`: the implementations of port.in_bound. It corresponds to the "INTERACTOR" in Picture 1.
* `port.outbound`: interfaces for defining the output of the use case. It corresponds to the LOWER "\<I> BOUNDARY" and "RESPONSE MODEL" in Picture 1.
* `impl.presenters`: the implementations of port.out_bound, which able to produce side effects to the world. It corresponds to the "PRESENTER" in Picture 1.
* `impl.factories`: factories for creating adapters, presenters, and use_cases
