---
title: "isAccuracyVisualized property"
slug: "sdk-for-flutter-explore-mapview-locationindicator-isaccuracyvisualized"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isAccuracyVisualized.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-locationindicator-class</li>
<li class="self-crumb">isAccuracyVisualized property</li>
</ol>
<div class="self-name">isAccuracyVisualized</div>
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
<div class="main-content" data-above-sidebar="mapview/LocationIndicator-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>isAccuracyVisualized property</h1></div>
<section id="getter">
<section class="multi-line-signature">
bool
isAccuracyVisualized
</section>
<section class="desc markdown">
<p>Whether the horizontal accuracy is visualized by scaling the accuracy indicator halo.
Returns whether /sdk-for-flutter-explore-core-location-horizontalaccuracyinmeters is used to scale the accuracy indicator halo.
Default is <code>false</code>, in which case the halo has a fixed and zoom level independent size.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool get isAccuracyVisualized;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
isAccuracyVisualized=(<wbr/>bool value)
</section>
<section class="desc markdown">
<p>Whether the horizontal accuracy is visualized by scaling the accuracy indicator halo.
Sets whether /sdk-for-flutter-explore-core-location-horizontalaccuracyinmeters is used to scale the accuracy indicator halo.
Default is <code>false</code>, in which case the halo has a fixed and zoom level independent size.</p>
<p>When set to <code>true</code>, the radius of the halo corresponds to the value of
/sdk-for-flutter-explore-core-location-horizontalaccuracyinmeters passed to /sdk-for-flutter-explore-mapview-locationindicator-updatelocation
and scales in world coordinates.</p>
<p>For values smaller than 20 meters the halo is hidden.
The radius of the halo is limited to 500 meters and values higher than that or <code>null</code>
will keep the halo at that size.</p>
<p>If the location indicator is set to inactive (which can be checked via /sdk-for-flutter-explore-mapview-locationindicator-isactive flag),
then the halo is always hidden. The value of this property remains unchanged regardless of the flag's value.
If the location indicator is set to active:</p>
<ul>
<li>Built-in location indicators:
<ul>
<li>The halo is always shown.</li>
<li>If the accuracy visualization is set to <code>true</code>, the size of the halo scales with
/sdk-for-flutter-explore-core-location-horizontalaccuracyinmeters in world coordinates.</li>
<li>If the accuracy visualization is set to <code>false</code>, halo displays at a default size.</li>
</ul>
</li>
<li>Custom location indicator:
<ul>
<li>If the accuracy visualization is set to <code>true</code>, halo is shown and the size of the halo scales with
/sdk-for-flutter-explore-core-location-horizontalaccuracyinmeters in world coordinates.</li>
<li>If the accuracy visualization is set to <code>false</code>, no halo is shown since it might not fit together with the custom 3d model.</li>
</ul>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set isAccuracyVisualized(bool value);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-locationindicator-class</li>
<li class="self-crumb">isAccuracyVisualized property</li>
</ol>
<h5>LocationIndicator class</h5>
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
