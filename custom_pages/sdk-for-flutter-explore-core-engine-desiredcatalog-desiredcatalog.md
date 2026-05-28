---
title: "DesiredCatalog constructor"
slug: "sdk-for-flutter-explore-core-engine-desiredcatalog-desiredcatalog"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- DesiredCatalog.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-explore-core-engine-desiredcatalog-class</li>
<li class="self-crumb">DesiredCatalog factory constructor</li>
</ol>
<div class="self-name">DesiredCatalog</div>
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
<div class="main-content" data-above-sidebar="core.engine/DesiredCatalog-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>DesiredCatalog constructor</h1></div>
<section class="multi-line-signature">
DesiredCatalog(<wbr/><ol class="parameter-list single-line"> <li>String hrn, </li>
<li>/sdk-for-flutter-explore-core-engine-catalogversionhint-class version</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li>
<p><code>hrn</code> A HERE Resource Name (HRN) for this catalog. This is a unique string returned by the HERE platform when you add a new
catalog to your project. For more information, see /sdk-for-flutter-explore-core-engine-catalogidentifier-hrn</p>
</li>
<li>
<p><code>version</code> The version to use for this Catalog's data.
You should use either /sdk-for-flutter-explore-core-engine-catalogversionhint-specific to specify a specific version of the catalog or
/sdk-for-flutter-explore-core-engine-catalogversionhint-latestwithignoringcacheddata to access the latest version of the catalog available on the HERE platform.
Based on the value in this field, the HERE platform will determine the best version to use for this catalog
or result in error logs if the desired version is not available.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory DesiredCatalog(String hrn, CatalogVersionHint version) =&gt; $prototype.make(hrn, version);</code></pre>
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
<li>/sdk-for-flutter-explore-core-engine-desiredcatalog-class</li>
<li class="self-crumb">DesiredCatalog factory constructor</li>
</ol>
<h5>DesiredCatalog class</h5>
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
