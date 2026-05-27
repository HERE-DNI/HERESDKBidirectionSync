---
title: "Constructors"
slug: "sdk-for-flutter-explore-core-engine-certificatesettings-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- CertificateSettings-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core.engine/CertificateSettings-class.html#constructors">Constructors</a></li>
<li><a href="core.engine/CertificateSettings/CertificateSettings.html">CertificateSettings</a></li>
<li class="section-title">
<a href="core.engine/CertificateSettings-class.html#instance-properties">Properties</a>
</li>
<li><a href="core.engine/CertificateSettings/certFileBlob.html">certFileBlob</a></li>
<li><a href="core.engine/CertificateSettings/clientCertFileBlob.html">clientCertFileBlob</a></li>
<li><a href="core.engine/CertificateSettings/clientKeyFileBlob.html">clientKeyFileBlob</a></li>
<li><a href="core.engine/CertificateSettings/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="core.engine/CertificateSettings/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="core.engine/CertificateSettings-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="core.engine/CertificateSettings/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core.engine/CertificateSettings/toString.html">toString</a></li>
<li class="section-title"><a href="core.engine/CertificateSettings-class.html#operators">Operators</a></li>
<li><a href="core.engine/CertificateSettings/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li class="self-crumb">CertificateSettings class</li>
</ol>
<div class="self-name">CertificateSettings</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/CertificateSettings-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>CertificateSettings class</h1></div>
<section class="desc markdown">
<p>Certificate settings to be used by Curl+OpenSSL for authority only on Android</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="CertificateSettings">
<a href="../core.engine/CertificateSettings/CertificateSettings.html">/sdk-for-flutter-explore-core-engine-certificatesettings-certificatesettings</a>(String clientCertFileBlob, String clientKeyFileBlob)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="certFileBlob">
<a href="../core.engine/CertificateSettings/certFileBlob.html">/sdk-for-flutter-explore-core-engine-certificatesettings-certfileblob</a>
↔ String?
</dt>
<dd>
  The CA file as blob
(<a href="https://curl.se/libcurl/c/CURLOPT_CAINFO_BLOB.html">https://curl.se/libcurl/c/CURLOPT_CAINFO_BLOB.html</a>)
Binary data of PEM encoded content holding one or more certificates to verify the HTTPS server with.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="clientCertFileBlob">
<a href="../core.engine/CertificateSettings/clientCertFileBlob.html">/sdk-for-flutter-explore-core-engine-certificatesettings-clientcertfileblob</a>
↔ String
</dt>
<dd>
  The client certificate file as blob
(<a href="https://curl.se/libcurl/c/CURLOPT_SSLCERT_BLOB.html">https://curl.se/libcurl/c/CURLOPT_SSLCERT_BLOB.html</a>)
The format must be "P12" or "PEM" on OpenSSL.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="clientKeyFileBlob">
<a href="../core.engine/CertificateSettings/clientKeyFileBlob.html">/sdk-for-flutter-explore-core-engine-certificatesettings-clientkeyfileblob</a>
↔ String
</dt>
<dd>
  The client key certificate file as blob
(<a href="https://curl.se/libcurl/c/CURLOPT_SSLKEY_BLOB.html">https://curl.se/libcurl/c/CURLOPT_SSLKEY_BLOB.html</a>)
Compatible with OpenSSL.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../core.engine/CertificateSettings/hashCode.html">/sdk-for-flutter-explore-core-engine-certificatesettings-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../core.engine/CertificateSettings/runtimeType.html">/sdk-for-flutter-explore-core-engine-certificatesettings-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../core.engine/CertificateSettings/noSuchMethod.html">/sdk-for-flutter-explore-core-engine-certificatesettings-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../core.engine/CertificateSettings/toString.html">/sdk-for-flutter-explore-core-engine-certificatesettings-tostring</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
<a href="../core.engine/CertificateSettings/operator_equals.html">/sdk-for-flutter-explore-core-engine-certificatesettings-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li class="self-crumb">CertificateSettings class</li>
</ol>
<h5>core.engine library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
</HTMLBlock>
