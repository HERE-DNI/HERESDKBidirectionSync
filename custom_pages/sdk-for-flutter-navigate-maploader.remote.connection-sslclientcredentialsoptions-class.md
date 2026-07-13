---
title: "SslClientCredentialsOptions class - maploader.remote.connection library - Dart API"
slug: "sdk-for-flutter-navigate-maploader.remote.connection-sslclientcredentialsoptions-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader.remote.connection/maploader.remote.connection-library-sidebar.html" data-below-sidebar="maploader.remote.connection/SslClientCredentialsOptions-class-sidebar.html">

<div>

# <span class="kind-class">SslClientCredentialsOptions</span> class

</div>

<div class="section desc markdown">

The structure below exactly match the corresponding gRPC SslCredentialsOptions structure.

Options used to build SslCredentials.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-sslclientcredentialsoptions">SslClientCredentialsOptions</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-pemRootCerts" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">pemRootCerts</span>, </span><span id="sdk-for-flutter-navigate-param-pemPrivateKey" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">pemPrivateKey</span>, </span><span id="sdk-for-flutter-navigate-param-pemCertChain" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">pemCertChain</span></span>)</span>  
Creates a new instance.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-sslclientcredentialsoptions-withoutmutualtls">SslClientCredentialsOptions.withoutMutualTLS</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withoutMutualTLS-param-pemRootCerts" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">pemRootCerts</span></span>)</span>  
The constructor which creates a new instance and sets both `pem_private_key` and `pem_cert_chain` to empty strings.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-pemcertchain">pemCertChain</a></span> <span class="signature">↔ String</span>  
The client's certificate chain in PEM format. It must be non-empty for mutual TLS. Else must be set to empty string.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-pemprivatekey">pemPrivateKey</a></span> <span class="signature">↔ String</span>  
The client's private key in PEM format. It must be non-empty for mutual TLS. Else must be set to empty string.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-pemrootcerts">pemRootCerts</a></span> <span class="signature">↔ String</span>  
The PEM-encoded root certificates used to verify the server.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

