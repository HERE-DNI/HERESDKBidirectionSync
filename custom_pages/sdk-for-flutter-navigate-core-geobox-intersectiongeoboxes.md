---
title: "Untitled"
slug: "sdk-for-flutter-navigate-core-geobox-intersectiongeoboxes"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- intersectionGeoBoxes.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li>/sdk-for-flutter-navigate-core-geobox-class</li>
<li class="self-crumb">intersectionGeoBoxes static method</li>
</ol>
<div class="self-name">intersectionGeoBoxes</div>
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
<div class="main-content" data-above-sidebar="core/GeoBox-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>intersectionGeoBoxes static method</h1></div>
<section class="multi-line-signature">
List&lt;<wbr/>/sdk-for-flutter-navigate-core-geobox-class&gt;
intersectionGeoBoxes(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/>/sdk-for-flutter-navigate-core-geobox-class&gt; geoBoxes</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Computes intersection of list of /sdk-for-flutter-navigate-core-geobox-class instances.</p>
<p>The altitude values are ignored.
Limitation: Geo boxes are considered as non-intersecting if they overlap only on a single point, horizontal line or vertical line.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li><code>geoBoxes</code> List of /sdk-for-flutter-navigate-core-geobox-class instances.</li>
</ul>
<p>Returns <code>List&lt;GeoBox&gt;</code>. It will be empty if there is no overlap between all the passed /sdk-for-flutter-navigate-core-geobox-class instances.</p>
<p>Otherwise, 1 or more geo boxes covering common area by all the passed /sdk-for-flutter-navigate-core-geobox-class instances.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static List&lt;GeoBox&gt; intersectionGeoBoxes(List&lt;GeoBox&gt; geoBoxes) =&gt; $prototype.intersectionGeoBoxes(geoBoxes);</code></pre>
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
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li>/sdk-for-flutter-navigate-core-geobox-class</li>
<li class="self-crumb">intersectionGeoBoxes static method</li>
</ol>
<h5>GeoBox class</h5>
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
