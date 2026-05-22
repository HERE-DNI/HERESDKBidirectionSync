---
title: "Untitled"
slug: "sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SslClientCredentialsOptions-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-remote-connection-maploader-remote-connection-library</li>
<li class="self-crumb">SslClientCredentialsOptions class</li>
</ol>
<div class="self-name">SslClientCredentialsOptions</div>
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
<div class="main-content" data-above-sidebar="maploader.remote.connection/maploader.remote.connection-library-sidebar.html" data-below-sidebar="maploader.remote.connection/SslClientCredentialsOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>SslClientCredentialsOptions class</h1></div>
<section class="desc markdown">
<p>The structure below exactly match the corresponding gRPC SslCredentialsOptions structure.</p>
<p>Options used to build SslCredentials.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="SslClientCredentialsOptions">
/sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-sslclientcredentialsoptions(String pemRootCerts, String pemPrivateKey, String pemCertChain)
</dt>
<dd>
          Creates a new instance.
        </dd>
<dt class="callable" id="SslClientCredentialsOptions.withoutMutualTLS">
/sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-sslclientcredentialsoptions-withoutmutualtls(String pemRootCerts)
</dt>
<dd>
          The constructor which creates a new instance and sets both <code>pem_private_key</code> and
<code>pem_cert_chain</code> to empty strings.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="pemCertChain">
/sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-pemcertchain
↔ String
</dt>
<dd>
  The client's certificate chain in PEM format.
It must be non-empty for mutual TLS. Else must be set to empty string.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="pemPrivateKey">
/sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-pemprivatekey
↔ String
</dt>
<dd>
  The client's private key in PEM format.
It must be non-empty for mutual TLS. Else must be set to empty string.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="pemRootCerts">
/sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-pemrootcerts
↔ String
</dt>
<dd>
  The PEM-encoded root certificates used to verify the server.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-runtimetype
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
/sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-remote-connection-maploader-remote-connection-library</li>
<li class="self-crumb">SslClientCredentialsOptions class</li>
</ol>
<h5>maploader.remote.connection library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>
