---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-mappolylinedashimagerepresentation-mappolylinedashimagerepresentation-uniform"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolylineDashImageRepresentation.uniform.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mappolylinedashimagerepresentation-class</li>
<li class="self-crumb">MapPolylineDashImageRepresentation.uniform factory constructor</li>
</ol>
<div class="self-name">MapPolylineDashImageRepresentation.uniform</div>
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
<div class="main-content" data-above-sidebar="mapview/MapPolylineDashImageRepresentation-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MapPolylineDashImageRepresentation.uniform constructor</h1></div>
<section class="multi-line-signature">
MapPolylineDashImageRepresentation.uniform(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class dashLength, </li>
<li>/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class dashWidth, </li>
<li>/sdk-for-flutter-explore-mapview-mapimage-class image</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a uniform dash pattern in which the length of a gap is the same as the length of
a dash.</p>
<p>Dashes are rendered as image.</p>
<p>This allows for patterns like <code>' — — — —'</code> or <code>'  ——  ——  ——'</code>.</p>
<p>For /sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class supplied for <code>dashLength</code> and <code>dashWidth</code>,
only /sdk-for-flutter-explore-mapview-mapmeasurekind is supported for /sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-measurekind
and only /sdk-for-flutter-explore-mapview-rendersizeunit is supported for /sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-sizeunit.</p>
<p>Only map measure values in range [3-19] are supported.</p>
<p>The value of the keys in /sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-sizes is truncated to integer values,
hence only a single value can be provided per zoom level.</p>
<p>The values are interpolated linearly between zoom levels.</p>
<ul>
<li>
<p><code>dashLength</code> The map measure dependent length of a dash, to which image width is stretched.</p>
</li>
<li>
<p><code>dashWidth</code> The map measure dependent width of a dash, to which image height is stretched.</p>
</li>
<li>
<p><code>image</code> Image to be rendered in place of dash space. It is stretched to match <code>dashWidth</code> and <code>dashLength</code>.</p>
</li>
</ul>
<p>Throws /sdk-for-flutter-explore-mapview-mappolylinerepresentationinstantiationexception-class. In case of invalid input parameters.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapPolylineDashImageRepresentation.uniform(MapMeasureDependentRenderSize dashLength, MapMeasureDependentRenderSize dashWidth, MapImage image) =&gt; $prototype.uniform(dashLength, dashWidth, image);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-mappolylinedashimagerepresentation-class</li>
<li class="self-crumb">MapPolylineDashImageRepresentation.uniform factory constructor</li>
</ol>
<h5>MapPolylineDashImageRepresentation class</h5>
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
