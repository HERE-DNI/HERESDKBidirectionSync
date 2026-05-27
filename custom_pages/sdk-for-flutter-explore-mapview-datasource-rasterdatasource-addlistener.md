---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-datasource-rasterdatasource-addlistener"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- addListener.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview.datasource/mapview.datasource-library.html">/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</a></li>
<li><a href="../../mapview.datasource/RasterDataSource-class.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasource-class</a></li>
<li class="self-crumb">addListener abstract method</li>
</ol>
<div class="self-name">addListener</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/RasterDataSource-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>addListener abstract method</h1></div>
<section class="multi-line-signature">
void
addListener(<wbr/><ol class="parameter-list single-line"> <li><a href="../../mapview.datasource/RasterDataSourceListener-class.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourcelistener-class</a> listener</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Add listener for receiving state notifications.</p>
<p>The new listener is
appended to the set of data source listeners as a strong reference and will receive only
the notifications occurring after the registration. Caller is responsible for releasing
the strong reference by calling <a href="../../mapview.datasource/RasterDataSource/removeListener.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasource-removelistener</a>.
The state notifications can occur on an arbitrary thread.</p>
<ul>
<li><code>listener</code> Listener to be added for receiving state notifications.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void addListener(RasterDataSourceListener listener);</code></pre>
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
<li><a href="../../mapview.datasource/mapview.datasource-library.html">/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</a></li>
<li><a href="../../mapview.datasource/RasterDataSource-class.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasource-class</a></li>
<li class="self-crumb">addListener abstract method</li>
</ol>
<h5>RasterDataSource class</h5>
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
