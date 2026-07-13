---
title: "SslClientCredentialsOptions.withoutMutualTLS constructor - SslClientCredentialsOptions - maploader.remote.connection library - Dart API"
slug: "sdk-for-flutter-navigate-maploader.remote.connection-sslclientcredentialsoptions-sslclientcredentialsoptions-withoutmutualtls"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader.remote.connection/SslClientCredentialsOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">SslClientCredentialsOptions.withoutMutualTLS</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">SslClientCredentialsOptions.withoutMutualTLS</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withoutMutualTLS-param-pemRootCerts" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">pemRootCerts</span></span>

)

</div>

<div class="section desc markdown">

The constructor which creates a new instance and sets both `pem_private_key` and `pem_cert_chain` to empty strings.

- `pemRootCerts` The PEM-encoded root certificates used to verify the server.

</div>

## Implementation

``` dart
SslClientCredentialsOptions.withoutMutualTLS(this.pemRootCerts)
    : pemPrivateKey = "", pemCertChain = "";
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

