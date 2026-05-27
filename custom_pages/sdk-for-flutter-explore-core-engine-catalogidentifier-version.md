---
title: "Implementation"
slug: "sdk-for-flutter-explore-core-engine-catalogidentifier-version"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- version.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li><a href="../../core.engine/CatalogIdentifier-class.html">/sdk-for-flutter-explore-core-engine-catalogidentifier-class</a></li>
<li class="self-crumb">version property</li>
</ol>
<div class="self-name">version</div>
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
<div class="main-content" data-above-sidebar="core.engine/CatalogIdentifier-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>version property</h1></div>
<section class="multi-line-signature">
        
        int?
        version
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>A version number for a catalog. When accessing a catalog, this version must be specified.
Set <code>null</code> to automatically get the latest version for a catalog.
The field defaults to <code>null</code>.
Since the data inside a catalog can be updated, each published modification needs to correlate
to a specific version number.
Note: when <code>CatalogIdentifier</code> created with <a href="../../core.engine/DesiredCatalog-class.html">/sdk-for-flutter-explore-core-engine-desiredcatalog-class</a> then:</p>
<ul>
<li>numerical <code>-1</code> corresponds to <a href="../../core.engine/CatalogVersionHint/latestWithIgnoringCachedData.html">/sdk-for-flutter-explore-core-engine-catalogversionhint-latestwithignoringcacheddata</a> with <code>ignoreCachedData</code> set to <code>true</code>;</li>
<li><code>null</code> corresponds to <a href="../../core.engine/CatalogVersionHint/latestWithIgnoringCachedData.html">/sdk-for-flutter-explore-core-engine-catalogversionhint-latestwithignoringcacheddata</a> with <code>ignoreCachedData</code> set to <code>false</code>;</li>
<li>other numerical values correspond to <code>version</code> passed to <a href="../../core.engine/CatalogVersionHint/specific.html">/sdk-for-flutter-explore-core-engine-catalogversionhint-specific</a>.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int? version;</code></pre>
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
<li><a href="../../core.engine/CatalogIdentifier-class.html">/sdk-for-flutter-explore-core-engine-catalogidentifier-class</a></li>
<li class="self-crumb">version property</li>
</ol>
<h5>CatalogIdentifier class</h5>
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
