---
title: "SslClientCredentialsOptions constructor - SslClientCredentialsOptions - maploader.remote.connection library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-sslclientcredentialsoptions"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader.remote.connection/SslClientCredentialsOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">SslClientCredentialsOptions</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">SslClientCredentialsOptions</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-pemRootCerts" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">pemRootCerts</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-pemPrivateKey" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">pemPrivateKey</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-pemCertChain" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">pemCertChain</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `pemRootCerts` The PEM-encoded root certificates used to verify the server.
- `pemPrivateKey` The client's private key in PEM format. It must be non-empty for mutual TLS. Else must be set to empty string.
- `pemCertChain` The client's certificate chain in PEM format. It must be non-empty for mutual TLS. Else must be set to empty string.

</div>

## Implementation

``` dart
SslClientCredentialsOptions(this.pemRootCerts, this.pemPrivateKey, this.pemCertChain);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

