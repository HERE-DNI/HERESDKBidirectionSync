---
title: "Implementation"
slug: "sdk-for-flutter-explore-search-placefilter-fueltypes"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- fuelTypes.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li><a href="../../search/PlaceFilter-class.html">/sdk-for-flutter-explore-search-placefilter-class</a></li>
<li class="self-crumb">fuelTypes property</li>
</ol>
<div class="self-name">fuelTypes</div>
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
<div class="main-content" data-above-sidebar="search/PlaceFilter-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>fuelTypes property</h1></div>
<section class="multi-line-signature">
        
        List&lt;<wbr/><a href="../../transport/FuelType.html">/sdk-for-flutter-explore-transport-fueltype</a>&gt;
fuelTypes
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>The list of <a href="../../transport/FuelType.html">/sdk-for-flutter-explore-transport-fueltype</a> elements that should be used to find only
the <a href="../../search/FuelStation-class.html">/sdk-for-flutter-explore-search-fuelstation-class</a> search results that support all of them.
This filter is available to use with the <code>SearchEngine</code> and
<code>OfflineSearchEngine</code> (only available for the Navigate license), however <code>OfflineSearchEngine</code>
supports it only for <code>searchByText</code> and <code>searchByCategory</code> with allowed fuel types <code>DIESEL</code>, <code>LPG</code>,
<code>BIO_DIESEL</code>, <code>CNG</code>, <code>DIESEL_WITH_ADDITIVES</code>, <code>E10</code>, <code>E85</code>, <code>ETHANOL</code>, <code>ETHANOL_WITH_ADDITIVES</code>,
<code>GASOLINE</code>, <code>HYDROGEN</code>, <code>LNG</code>, <code>MIDGRADE</code>, <code>PREMIUM</code> and <code>REGULAR</code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;FuelType&gt; fuelTypes;</code></pre>
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
<li><a href="../../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li><a href="../../search/PlaceFilter-class.html">/sdk-for-flutter-explore-search-placefilter-class</a></li>
<li class="self-crumb">fuelTypes property</li>
</ol>
<h5>PlaceFilter class</h5>
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
