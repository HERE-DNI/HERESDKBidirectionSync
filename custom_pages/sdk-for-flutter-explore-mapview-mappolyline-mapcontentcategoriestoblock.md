---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mappolyline-mapcontentcategoriestoblock"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- mapContentCategoriesToBlock.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapPolyline-class.html">/sdk-for-flutter-explore-mapview-mappolyline-class</a></li>
<li class="self-crumb">mapContentCategoriesToBlock property</li>
</ol>
<div class="self-name">mapContentCategoriesToBlock</div>
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
<div class="main-content" data-above-sidebar="mapview/MapPolyline-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>mapContentCategoriesToBlock property</h1></div>
<section id="getter">
<section class="multi-line-signature">
List&lt;<wbr/><a href="../../mapview/MapContentCategory.html">/sdk-for-flutter-explore-mapview-mapcontentcategory</a>&gt;
mapContentCategoriesToBlock
</section>
<section class="desc markdown">
<p>List of map content categories this polyline should block.
Gets list of map content categories this polyline should block.</p>
<p>Default value is an empty list meaning none of the map categories will be blocked.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;MapContentCategory&gt; get mapContentCategoriesToBlock;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
mapContentCategoriesToBlock=(<wbr/>List&lt;<wbr/><a href="../../mapview/MapContentCategory.html">/sdk-for-flutter-explore-mapview-mapcontentcategory</a>&gt; value)
</section>
<section class="desc markdown">
<p>List of map content categories this polyline should block.
Sets list of map content categories this polyline should block.</p>
<p>Map content categories overlapping the polyline geometry
(progress and non-progress) will be discarded from being rendered.</p>
<p>Duplicate entries will be ignored and will have no additional effect.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set mapContentCategoriesToBlock(List&lt;MapContentCategory&gt; value);</code></pre>
</section>
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
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapPolyline-class.html">/sdk-for-flutter-explore-mapview-mappolyline-class</a></li>
<li class="self-crumb">mapContentCategoriesToBlock property</li>
</ol>
<h5>MapPolyline class</h5>
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
