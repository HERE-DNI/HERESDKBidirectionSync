---
title: "SslServerCredentialsOptions constructor - SslServerCredentialsOptions - maploader.remote.connection library - Dart API"
slug: "sdk-for-flutter-navigate-maploader.remote.connection-sslservercredentialsoptions-sslservercredentialsoptions"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader.remote.connection/SslServerCredentialsOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">SslServerCredentialsOptions</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">SslServerCredentialsOptions</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-pemRootCerts" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">pemRootCerts</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-pemKeyCertPairs" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-maploader-remote-connection-pemkeycertpair-class">PemKeyCertPair</a></span>\></span></span> <span class="parameter-name">pemKeyCertPairs</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-clientCertificateRequest" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-remote-connection-clientcertificaterequesttype">ClientCertificateRequestType</a></span> <span class="parameter-name">clientCertificateRequest</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `pemRootCerts` Root certificates (in PEM format) used to verify the client certificate. Required only for mutual TLS.
- `pemKeyCertPairs` List of server key/certificate pairs. At least one pair must be provided.
- `clientCertificateRequest` Indicates whether the server should request and verify the client's certificate.

</div>

## Implementation

``` dart
SslServerCredentialsOptions(this.pemRootCerts, this.pemKeyCertPairs, this.clientCertificateRequest);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

