# EU eHealthNetwork Digital COVID Certificate: Valueset updates

This is a protoype client-server to demonstrate how clients can update to the latest Digital COVID Certificate (DCC) valuesets. 
These valuesets are made available via an endpoint on the DCC Gateway (DCCG). 

This prototype is concerned with demonstrating a robust mechanism for clients to update to latest valuesets within a period of time acceptable to such clients.

The process of updating the valuesets in themselves at the well-known endpoint on the DCCG will not be considered here. A simple "mock" server is supplied to host the required server endpoints and to simulate an actual update of the valuesets.

## Acronyms

* DCC - Digital COVID Certificate
* eHN - EU eHeathNetwork
* [HTTP](https://datatracker.ietf.org/doc/html/rfc2616) - Hyper Text Transfer Protocol
* [IP](https://datatracker.ietf.org/doc/html/rfc791) - Internet Protocol
* [REST](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm) - Representational State Transfer
* [TCP](https://datatracker.ietf.org/doc/html/rfc793) - Transmission Control Protocol

## Definition of Terms

* client - in this case:a DCC issuer or verifier application
* server - in this case: the DCC Gateway

## Requirements 

* It shall be possible for a client to:
   *  update to the latest DCC valuesets as soon as they are published at the well-known DCCG endpoint
   *  update to the latest DCC valuesets within a time-scale acceptable to the client
   *  maintain control of if, how and when any new valueset shall be updated at the client side
* The server
   *  shall ideally be stateless to allow for ease of re-start if there is a server outage
   *  shall not persist any client identity on the server-side

The term "persist" is used in the same manner as the EU Regulations for the DCC: nothing stored in a durable manner e.g. to a database on a third server or a disk file etc. Thus the server will have to know - at least ephemerally in RAM - the client IP address in order to reply to the client request, but this client IP address must not be persisted.

### Deployment Constraints

* WAN connectivity
* Highly Dynamic - clients can come and go in no pre-determined fashion
* Must be robust to be both client and server outages

## Architecture

### Constraints

Standard distributed notification mechanisms can either be server-push or client-pull.
In considering the requirements (#requirements) and in particular the [deployment constraints](#deployment-constraints) as given above we 
arrive at the following considerations:

#### Server-Push

This is a standard design pattern known as Observer or Publish-And-Subscribe. For the distributed case, the server takes on the role of Publisher and the client is the Subscriber. The Publisher informs Subscribers about updates. Note: this is in essence the mechanism between the European Federated Gateway Service (EFGS) callback mechanism for notifier warn apps (e.g. Corona Warn, Corona Melder etc)

* Pro's
   * already implemented for notifier apps
   * development teams are familiar with the mechanism
* Con's
   * requires subscribers to be available once they have subscribed (not come and go in a highly dynamic manner)
   * persistence of client connection information is required in order to call back to the client
   * error handling becomes somewhat involved (although not impossible) if subscribers disappear without warning
   * subscribers will simply not be notified if there is a server outage
   * after a server outage either the server will have had to persist all subscribers or all clients will have to re-subscribe
   * state maintained server-side

#### Client-Pull

This is the standard client-polling model that is used on the internet and for which HTTP is a suitable protocol.

* Pro's
   * clients can dynamically come and go
   * server-side is stateless
   * no persistence of client connections
   * robust with respect to client outages (handled by standard HTTP / TCP / IP protocols)
   * robust with respect to server outages - client knows immediately if server not available
* Con's
   * more bandwidth required overall than for the server-push model (due to client polling)
   
Given the constraints - in particular no persistence server-side of client connections - then it seems the [Client-Pull](#client-pull) model is the most suitable for our requirements. In this case, we can then use the HTTP protocol for client requests. A stateless server-side also maps well to the REST model, so it would seem most appropriate and fitting to supply server endpoints according to the REST model and accessed via HTTP.

### Client-Server Interaction

Given we are using the Client-Pull stateless server-side model, a client will have to poll in order to determine if there is a more recent valueset available. A date-time timestamp shall be made available indicating the date-time of the most recent valueset. A client can then request this date-time value and if there is a more recent valueset than the valueset the client currently has, the client may choose to download this more recent valueset.

#### Client Maintains Control of Updates

Of importance here is that it is the client who maintains control of whether it wishes to download the new valueset or not.

#### Client-Pull Bandwidth Concerns

Note that simply polling for a timestamp requires very few bytes of traffic so this goes a long way to mitigating the main drawback of increased bandwith usage associated with the client-pull mode. It can be argued that the valuesets with a total size of single-digit kilobytes is by modern standards also minimal, perhaps even negligible. 

However, it is important cases to be keep in mind that we have a scenario of WAN connectivity with many hundreds (if not thousands) of clients. 
Each of these clients will be reasonably regularly polling the server. This linearly increases the amount of data the server has to serve by the number of clients. 
Keeping the amount of returned data to a minimum for the standard poll requests means we can limit the amount of data the server has to serve not just by the different between the size in timestamp and the valueset but that difference multiplied by the number of clients. 
Keeping the amount of data low in a standard polling scenario (obtaining the timestamp) helps maintain a robust and responsive server-side service since there will be a far lower probability of network saturation than if the whole valueset is returned each time.

### Server End-Points

The above considerations lead to providing two server-side endpoints:

| Endpoint | Description | HTTP Verb(s) |
| ---- | ---- | ---- |
| valueset date-time | most recent valueset date-time timestamp | GET |
| valueset | the full, latest valueset | GET (POST?) |
