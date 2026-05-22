---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-mapmarker-fadeduration"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- fadeDuration.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapmarker-class</li>
<li class="self-crumb">fadeDuration property</li>
</ol>
<div class="self-name">fadeDuration</div>
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
<h1>fadeDuration property</h1></div>
<section id="getter">
<section class="multi-line-signature">
Duration
fadeDuration
</section>
<section class="desc markdown">
<p>Duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.
Gets the current duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Duration get fadeDuration;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
fadeDuration=(<wbr/>Duration value)
</section>
<section class="desc markdown">
<p>Duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.
Sets duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.</p>
<p>Provided value is clamped in range [0.0, 10.0] seconds. Default value is 0 seconds which means the effect is disabled
and marker is added/removed immediately without any animation.
Fade-in effect is also applied when marker leaves and then re-enters screen area.</p>
<p>Change to this property is made asynchronously and is not guaranteed
to take effect on the next rendered frame. In particular, changing fade duration and removing
the marker immediately after may result in the new value being ignored for this removal.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set fadeDuration(Duration value);</code></pre>
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
<li class="self-crumb">fadeDuration property</li>
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
