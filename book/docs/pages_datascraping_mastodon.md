# Analysing public Mastodon data

## Why Mastodon can be an interesting data source

As an alternative to Twitter, we also explore Mastodon as a source for public comments on politics, culture and science. Mastodon is a decentralised network in which several local servers connect, and the learning curve for using it is slightly higher than on other social media platforms. This means that the community on Mastodon is rather small and that most users are either very interested in (new) technologies or join for ideological reasons, e.g. because they oppose for-profit networks.

Mastodon will, therefore, not give you a broad insight into a wide range of societal positions, but it can still be interesting to find out about *trending topics* in more specialised communities such as higher education and game development.

## Technical requirements

 The endpoints for collecting public data from Mastodon are explained here in their [Playing with public data](https://docs.joinmastodon.org/client/public/) documentation. You can access data for different purposes:

- Endpoint for fetching public timelines: https://mastodon.example/api/v1/timelines/public
- With user-defined limits: https://mastodon.example/api/v1/timelines/public?limit=2

For a full documentation on querying Mastodon with Python, please read the [Mastodonpy documentation](https://mastodonpy.readthedocs.io/en/stable/).

