---
title: "removeIf abstract method"
slug: "sdk-for-flutter-explore-mapview-datasource-polygondatasource-removeif"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- removeIf.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-explore-mapview-datasource-polygondatasource-class</li>
<li class="self-crumb">removeIf abstract method</li>
</ol>
<div class="self-name">removeIf</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/PolygonDataSource-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>removeIf abstract method</h1></div>
<section class="multi-line-signature">
void
removeIf(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-explore-mapview-datasource-polygondatasourcepolygondataprocessor inspector</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Iterates through all the polygons from the data source and passes them to the
given inspector, one by one.</p>
<p>All polygons for which the inspector returns <code>true</code> get removed from the data source.
The inspector cannot update the polygon data.</p>
<ul>
<li><code>inspector</code> Polygon data processor.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void removeIf(PolygonDataSourcePolygonDataProcessor inspector);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-explore-mapview-datasource-polygondatasource-class</li>
<li class="self-crumb">removeIf abstract method</li>
</ol>
<h5>PolygonDataSource class</h5>
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
