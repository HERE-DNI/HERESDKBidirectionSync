---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-maplayermapmeasuredependentstoragelevels-withstorageleveloffset"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- withStorageLevelOffset.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-maplayermapmeasuredependentstoragelevels-class</li>
<li class="self-crumb">withStorageLevelOffset static method</li>
</ol>
<div class="self-name">withStorageLevelOffset</div>
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
<div class="main-content" data-above-sidebar="mapview/MapLayerMapMeasureDependentStorageLevels-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>withStorageLevelOffset static method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-mapview-maplayermapmeasuredependentstoragelevels-class
withStorageLevelOffset(<wbr/><ol class="parameter-list single-line"> <li>int offset</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Creates an instance of /sdk-for-flutter-navigate-mapview-maplayermapmeasuredependentstoragelevels-class with the specified storage level offset.</p>
<p>This creates a map where the storage level is determined by applying an "offset" to the zoom level.
A negative offset results in a storage level lower than the zoom level, while a positive offset increases it.
For example, with an offset of 0, the storage level matches the zoom level directly.
An offset of -1 makes the storage level one less than the zoom level, and so on.
The offset value is clamped to the range of -3 to 3.
Note: The generated mapping adjusts so that when the map camera is significantly tilted,
the storage level is further reduced for data near the horizon.</p>
<ul>
<li><code>offset</code> Defines an offset of storage level from the zoom level.
The value will be clamped to a range of -3 to 3.</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-mapview-maplayermapmeasuredependentstoragelevels-class. MapLayerMapMeasureDependentStorageLevels instance.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapLayerMapMeasureDependentStorageLevels withStorageLevelOffset(int offset) =&gt; $prototype.withStorageLevelOffset(offset);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapview-maplayermapmeasuredependentstoragelevels-class</li>
<li class="self-crumb">withStorageLevelOffset static method</li>
</ol>
<h5>MapLayerMapMeasureDependentStorageLevels class</h5>
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
