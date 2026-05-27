---
title: "Implementation"
slug: "sdk-for-flutter-explore-core-authenticationcallback"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- AuthenticationCallback.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
<li class="self-crumb">AuthenticationCallback typedef</li>
</ol>
<div class="self-name">AuthenticationCallback</div>
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
<div class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>AuthenticationCallback typedef</h1></div>
<section class="multi-line-signature">
AuthenticationCallback =
     void Function(<a href="../core/AuthenticationError.html">/sdk-for-flutter-explore-core-authenticationerror</a>? authenticationError, <a href="../core/AuthenticationData-class.html">/sdk-for-flutter-explore-core-authenticationdata-class</a>? authenticationData)
</section>
<section class="desc markdown">
<p>Callback passed to <a href="../core/Authentication/authenticateWithSDKNativeEngine.html">/sdk-for-flutter-explore-core-authentication-authenticatewithsdknativeengine</a>.</p>
<p>This callback is called on the main thread asynchronously when an
authenticate call has completed.</p>
<ul>
<li>
<p><code>authenticationError</code> Represents the operation status. It is 'null' for an operation that succeeds.</p>
</li>
<li>
<p><code>authenticationData</code> Represents the authentication data.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef AuthenticationCallback = void Function(AuthenticationError? authenticationError, AuthenticationData? authenticationData);</code></pre>
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
<li><a href="../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
<li class="self-crumb">AuthenticationCallback typedef</li>
</ol>
<h5>core library</h5>
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
