---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-mapmarker-visibilityranges"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- visibilityRanges.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapmarker-class</li>
<li class="self-crumb">visibilityRanges property</li>
</ol>
<div class="self-name">visibilityRanges</div>
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
<h1>visibilityRanges property</h1></div>
<section id="getter">
<section class="multi-line-signature">
List&lt;<wbr/>/sdk-for-flutter-explore-mapview-mapmeasurerange-class&gt;
visibilityRanges
</section>
<section class="desc markdown">
<p>The list of visibility ranges. The map marker is visible only inside these map measure ranges.
Gets the list of visibility ranges. The map marker is visible only inside these map measure
ranges. When empty (the default), the map marker is visible without map measure restrictions.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;MapMeasureRange&gt; get visibilityRanges;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
visibilityRanges=(<wbr/>List&lt;<wbr/>/sdk-for-flutter-explore-mapview-mapmeasurerange-class&gt; value)
</section>
<section class="desc markdown">
<p>The list of visibility ranges. The map marker is visible only inside these map measure ranges.
Sets visibility ranges for this map marker.</p>
<p>A range is half open - [minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.
The map marker is visible only inside these map measure ranges.</p>
<p>When empty (the default), the map marker is visible without map measure restrictions.
Only <code>MapMeasureRange</code>(s) of /sdk-for-flutter-explore-mapview-mapmeasurekind type are supported.
<code>MapMeasureRange</code>(s) of other unsupported types will be ignored.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set visibilityRanges(List&lt;MapMeasureRange&gt; value);</code></pre>
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
<li class="self-crumb">visibilityRanges property</li>
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
