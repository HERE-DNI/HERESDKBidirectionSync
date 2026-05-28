---
title: "SslClientCredentialsOptions.withoutMutualTLS constructor"
slug: "sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-sslclientcredentialsoptions-withoutmutualtls"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SslClientCredentialsOptions.withoutMutualTLS.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-remote-connection-maploader-remote-connection-library</li>
<li>/sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-class</li>
<li class="self-crumb">SslClientCredentialsOptions.withoutMutualTLS constructor</li>
</ol>
<div class="self-name">SslClientCredentialsOptions.withoutMutualTLS</div>
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
<div class="main-content" data-above-sidebar="maploader.remote.connection/SslClientCredentialsOptions-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>SslClientCredentialsOptions.withoutMutualTLS constructor</h1></div>
<section class="multi-line-signature">
SslClientCredentialsOptions.withoutMutualTLS(<wbr/><ol class="parameter-list single-line"> <li>String pemRootCerts</li>
</ol>)
    </section>
<section class="desc markdown">
<p>The constructor which creates a new instance and sets both <code>pem_private_key</code> and
<code>pem_cert_chain</code> to empty strings.</p>
<ul>
<li><code>pemRootCerts</code> The PEM-encoded root certificates used to verify the server.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">SslClientCredentialsOptions.withoutMutualTLS(this.pemRootCerts)
    : pemPrivateKey = "", pemCertChain = "";</code></pre>
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
<li>/sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-class</li>
<li class="self-crumb">SslClientCredentialsOptions.withoutMutualTLS constructor</li>
</ol>
<h5>SslClientCredentialsOptions class</h5>
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
`
}</HTMLBlock>
