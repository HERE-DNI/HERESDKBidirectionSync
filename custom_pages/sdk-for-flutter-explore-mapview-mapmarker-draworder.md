---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-mapmarker-draworder"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- drawOrder.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapmarker-class</li>
<li class="self-crumb">drawOrder property</li>
</ol>
<div class="self-name">drawOrder</div>
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
<div class="main-content" data-above-sidebar="mapview/MapMarker-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>drawOrder property</h1></div>
<section id="getter">
<section class="multi-line-signature">
int
drawOrder
</section>
<section class="desc markdown">
<p>The draw order of this marker relative to other markers.
Gets draw order of this marker relative to other markers. The default value is 0.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int get drawOrder;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
drawOrder=(<wbr/>int value)
</section>
<section class="desc markdown">
<p>The draw order of this marker relative to other markers.
Sets draw order of this marker relative to other markers.</p>
<p>Markers with higher draw order value are drawn on top of markers with lower draw order.
In case multiple markers have the same draw order value
then the order in which they were added to the scene matters. Last added marker is drawn on top.</p>
<p>Allowed range is [0, 1023]. Values outside this range will be clamped. The default value is 0.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set drawOrder(int value);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-mapmarker-class</li>
<li class="self-crumb">drawOrder property</li>
</ol>
<h5>MapMarker class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>
