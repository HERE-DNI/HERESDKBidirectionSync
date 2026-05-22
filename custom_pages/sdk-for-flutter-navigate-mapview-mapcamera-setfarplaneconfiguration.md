---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mapcamera-setfarplaneconfiguration"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setFarPlaneConfiguration.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapcamera-class</li>
<li class="self-crumb">setFarPlaneConfiguration abstract method</li>
</ol>
<div class="self-name">setFarPlaneConfiguration</div>
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
<div class="main-content" data-above-sidebar="mapview/MapCamera-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>setFarPlaneConfiguration abstract method</h1></div>
<section class="multi-line-signature">
void
setFarPlaneConfiguration(<wbr/><ol class="parameter-list single-line"> <li>Map&lt;<wbr/>double, /sdk-for-flutter-navigate-mapview-mapcamerafarplaneconfiguration-class&gt; configs</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Sets far plane distance configs per zoom level.</p>
<p>Values are linearly interpolated between provided zoom levels.
For z between z0 and z1:
t = (z - z0) / (z1 - z0)
distanceFactor(z) = lerp(distanceFactor0, distanceFactor1, t)
minDistance(z) = lerp(minDistance0, minDistance1, t)</p>
<p>Effective far plane for the current frame is:
farPlaneInMeters = max(
minDistance(z),
distanceToTargetInMeters * distanceFactor(z)
)</p>
<p>Sample Configuration (balanced quality/performance, tune per zoom level):
14.4  -&gt; FarPlaneConfiguration(1.3)
18.34 -&gt; FarPlaneConfiguration(2.0)
19.60 -&gt; FarPlaneConfiguration(1.3)
minDistanceInMeters remains default in this case.
Passing an empty map clears the per-zoom override and restores the default behavior.
Non-finite zoom levels or values are ignored. Distance factors are clamped to 0.1 to 10.0.
The minimum distance is clamped to a range of [100, 3000] meters.</p>
<ul>
<li><code>configs</code> Per-zoom override mapping from zoom level to distance configuration.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setFarPlaneConfiguration(Map&lt;double, MapCameraFarPlaneConfiguration&gt; configs);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapview-mapcamera-class</li>
<li class="self-crumb">setFarPlaneConfiguration abstract method</li>
</ol>
<h5>MapCamera class</h5>
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
