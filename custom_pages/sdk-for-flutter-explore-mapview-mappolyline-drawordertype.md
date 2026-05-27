---
title: "drawOrderType property"
slug: "sdk-for-flutter-explore-mapview-mappolyline-drawordertype"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- drawOrderType.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mappolyline-class</li>
<li class="self-crumb">drawOrderType property</li>
</ol>
<div class="self-name">drawOrderType</div>
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
<h1>drawOrderType property</h1></div>
<section id="getter">
<section class="multi-line-signature">
/sdk-for-flutter-explore-mapview-drawordertype
drawOrderType
</section>
<section class="desc markdown">
<p>The draw order type of the polyline.
Gets the draw order type of the polyline.</p>
<p>The default value is /sdk-for-flutter-explore-mapview-drawordertype.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">DrawOrderType get drawOrderType;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
drawOrderType=(<wbr/>/sdk-for-flutter-explore-mapview-drawordertype value)
</section>
<section class="desc markdown">
<p>The draw order type of the polyline.
Sets the draw order type of the polyline.</p>
<p>For /sdk-for-flutter-explore-mapview-drawordertype, map polylines with outlines having
the same draw order are drawn as a whole in the order of addition to a map scene. There
is no possibility that parts of another polyline, regardless of its draw order value,
are drawn between outline and mainline of another polyline.</p>
<p>With /sdk-for-flutter-explore-mapview-drawordertype, polylines are rendered one by one.</p>
<p>For /sdk-for-flutter-explore-mapview-drawordertype, for multiple polylines with
outlines having the same draw order, all outlines are rendered first in an arbitrary order
and then all mainlines are drawn on top of those polylines in an arbitrary order.</p>
<p>/sdk-for-flutter-explore-mapview-drawordertype allows speeding up the rendering
process and keeping high frame rates when many similar polylines (with same styling
attributes and /sdk-for-flutter-explore-mapview-mappolylinerepresentation-class) are present in a map scene.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set drawOrderType(DrawOrderType value);</code></pre>
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mappolyline-class</li>
<li class="self-crumb">drawOrderType property</li>
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
`
}</HTMLBlock>
