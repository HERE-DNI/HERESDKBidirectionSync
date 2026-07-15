---
title: "CertificateSettings class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core-engine-certificatesettings-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/CertificateSettings-class-sidebar.html">

<div>

# <span class="kind-class">CertificateSettings</span> class

</div>

<div class="section desc markdown">

Certificate settings to be used by Curl+OpenSSL for authority only on Android

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-core-engine-certificatesettings-certificatesettings">CertificateSettings</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-clientCertFileBlob" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">clientCertFileBlob</span>, </span><span id="sdk-for-flutter-explore-param-clientKeyFileBlob" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">clientKeyFileBlob</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-core-engine-certificatesettings-certfileblob">certFileBlob</a></span> <span class="signature">↔ String?</span>  
The CA file as blob (<https://curl.se/libcurl/c/CURLOPT_CAINFO_BLOB.html>) Binary data of PEM encoded content holding one or more certificates to verify the HTTPS server with. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-certificatesettings-clientcertfileblob">clientCertFileBlob</a></span> <span class="signature">↔ String</span>  
The client certificate file as blob (<https://curl.se/libcurl/c/CURLOPT_SSLCERT_BLOB.html>) The format must be "P12" or "PEM" on OpenSSL. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-certificatesettings-clientkeyfileblob">clientKeyFileBlob</a></span> <span class="signature">↔ String</span>  
The client key certificate file as blob (<https://curl.se/libcurl/c/CURLOPT_SSLKEY_BLOB.html>) Compatible with OpenSSL. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-certificatesettings-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-certificatesettings-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-core-engine-certificatesettings-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-certificatesettings-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-core-engine-certificatesettings-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

