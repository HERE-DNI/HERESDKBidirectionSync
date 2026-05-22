---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mapmarker-isoverlapallowed"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isOverlapAllowed.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapmarker-class</li>
<li class="self-crumb">isOverlapAllowed property</li>
</ol>
<div class="self-name">isOverlapAllowed</div>
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
<h1>isOverlapAllowed property</h1></div>
<section id="getter">
<section class="multi-line-signature">
bool
isOverlapAllowed
</section>
<section class="desc markdown">
<p>Determines whether or not the marker can overlap other markers.
Returns <code>true</code> if the marker allows overlap with other markers, <code>false</code> otherwise.
Defaults to <code>true</code>.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool get isOverlapAllowed;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
isOverlapAllowed=(<wbr/>bool value)
</section>
<section class="desc markdown">
<p>Determines whether or not the marker can overlap other markers.
Sets whether the marker is allowed to overlap with other markers.</p>
<p>If <code>false</code>, it will disappear the moment it overlaps another marker that has
a higher visibility priority. A marker that allows overlap will always be drawn.
Among markers that don't allow overlap, the one with the highest draw order has
priority. Marker that is hidden due to overlapping with other markers is not pickable.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set isOverlapAllowed(bool value);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapview-mapmarker-class</li>
<li class="self-crumb">isOverlapAllowed property</li>
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
