---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-maparrow-measuredependenttailwidth"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- measureDependentTailWidth.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-maparrow-class</li>
<li class="self-crumb">measureDependentTailWidth property</li>
</ol>
<div class="self-name">measureDependentTailWidth</div>
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
<div class="main-content" data-above-sidebar="mapview/MapArrow-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>measureDependentTailWidth property</h1></div>
<section id="getter">
<section class="multi-line-signature">
Map&lt;<wbr/>/sdk-for-flutter-navigate-mapview-mapmeasure-class, double&gt;
measureDependentTailWidth
</section>
<section class="desc markdown">
<p>The width of the arrow tail in pixels, where the key is a /sdk-for-flutter-navigate-mapview-mapmeasure-class and the value is
a tail width in pixels at this /sdk-for-flutter-navigate-mapview-mapmeasure-class.
Gets the /sdk-for-flutter-navigate-mapview-mapmeasure-class dependent arrow tail width in pixels.</p>
<p>If tail width was configured without /sdk-for-flutter-navigate-mapview-mapmeasure-class dependency, then <code>measureDependentTailWidth</code>
contains single entry with measure 0 of type /sdk-for-flutter-navigate-mapview-mapmeasurekind and width value
equal to <code>widthInPixels</code>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Map&lt;MapMeasure, double&gt; get measureDependentTailWidth;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
measureDependentTailWidth=(<wbr/>Map&lt;<wbr/>/sdk-for-flutter-navigate-mapview-mapmeasure-class, double&gt; value)
</section>
<section class="desc markdown">
<p>The width of the arrow tail in pixels, where the key is a /sdk-for-flutter-navigate-mapview-mapmeasure-class and the value is
a tail width in pixels at this /sdk-for-flutter-navigate-mapview-mapmeasure-class.
Sets the /sdk-for-flutter-navigate-mapview-mapmeasure-class dependent arrow tail width in pixels.</p>
<p>The width values are linearly interpolated between nearest map entries.
Width values for /sdk-for-flutter-navigate-mapview-mapmeasure-class outside the map entries are kept constant, using the
value of the largest/smallest key.</p>
<p>Only /sdk-for-flutter-navigate-mapview-mapmeasure-class of /sdk-for-flutter-navigate-mapview-mapmeasurekind type is supported.
Other /sdk-for-flutter-navigate-mapview-mapmeasure-class types are unsupported and hence, will be ignored.</p>
<p>Map with a single entry is equivalent to use of the <code>widthInPixels</code> value
in the constructor, so a constant width setting, independent of camera.</p>
<p>Empty input is ignored and existing width is maintained.</p>
<p>The width values should be positive. Map entries with width values less than or equal to 0 are ignored.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set measureDependentTailWidth(Map&lt;MapMeasure, double&gt; value);</code></pre>
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-maparrow-class</li>
<li class="self-crumb">measureDependentTailWidth property</li>
</ol>
<h5>MapArrow class</h5>
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
