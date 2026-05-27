---
title: "Implementation"
slug: "sdk-for-flutter-explore-core-engine-sdknativeengine-setaccesskeysecret"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- setAccessKeySecret.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li><a href="../../core.engine/SDKNativeEngine-class.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-class</a></li>
<li class="self-crumb">setAccessKeySecret abstract method</li>
</ol>
<div class="self-name">setAccessKeySecret</div>
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
<div class="main-content" data-above-sidebar="core.engine/SDKNativeEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>setAccessKeySecret abstract method</h1></div>
<section class="multi-line-signature">
void
setAccessKeySecret(<wbr/><ol class="parameter-list single-line"> <li>String accessKeySecret</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Overrides HERE SDK access key secret with new value.</p>
<p>The new credentials will be used for new requests.</p>
<p><strong>Note:</strong>
This method can be called from any thread.
Access key ID can be set with constructor of SDKNativeEngine.
New instance of SDKNativeEngine should be used if a new access key ID is required.</p>
<ul>
<li><code>accessKeySecret</code> New access key secret.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setAccessKeySecret(String accessKeySecret);</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li><a href="../../core.engine/SDKNativeEngine-class.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-class</a></li>
<li class="self-crumb">setAccessKeySecret abstract method</li>
</ol>
<h5>SDKNativeEngine class</h5>
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
