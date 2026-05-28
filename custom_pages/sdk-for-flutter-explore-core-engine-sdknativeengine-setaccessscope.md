---
title: "setAccessScope abstract method"
slug: "sdk-for-flutter-explore-core-engine-sdknativeengine-setaccessscope"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setAccessScope.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-explore-core-engine-sdknativeengine-class</li>
<li class="self-crumb">setAccessScope abstract method</li>
</ol>
<div class="self-name">setAccessScope</div>
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
<h1>setAccessScope abstract method</h1></div>
<section class="multi-line-signature">
void
setAccessScope(<wbr/><ol class="parameter-list single-line"> <li>String scope</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Overrides the token scope of the HERE SDK with new value.</p>
<p>A new token will be fetched with the set scope and used for future requests.
Setting an empty string will fetch a token for the global scope.</p>
<p>This method can be called from any thread.</p>
<ul>
<li><code>scope</code> New scope for token</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setAccessScope(String scope);</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-explore-core-engine-sdknativeengine-class</li>
<li class="self-crumb">setAccessScope abstract method</li>
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
`
}</HTMLBlock>
