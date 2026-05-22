---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-locationindicator-materialreflectivity"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- materialReflectivity.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-locationindicator-class</li>
<li class="self-crumb">materialReflectivity property</li>
</ol>
<div class="self-name">materialReflectivity</div>
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
<h1>materialReflectivity property</h1></div>
<section id="getter">
<section class="multi-line-signature">
/sdk-for-flutter-explore-mapview-materialreflectivity-class?
materialReflectivity
</section>
<section class="desc markdown">
<p>The material reflectivity properties of the location indicator.
Enables per‑pixel lighting for all internal markers (navigation, pedestrian,
inactive variants) and the halo when assigned. While <code>materialReflectivity</code> is non‑null the
markers are shaded by scene lights using the provided ambient / diffuse factors. When set
back to <code>null</code>, lighting is disabled and markers revert to unlit (emissive) rendering.</p>
<p>Default value is <code>null</code>.
Retrieves the material reflectivity applied to all markers of location indicator.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MaterialReflectivity? get materialReflectivity;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
materialReflectivity=(<wbr/>/sdk-for-flutter-explore-mapview-materialreflectivity-class? value)
</section>
<section class="desc markdown">
<p>The material reflectivity properties of the location indicator.
Enables per‑pixel lighting for all internal markers (navigation, pedestrian,
inactive variants) and the halo when assigned. While <code>materialReflectivity</code> is non‑null the
markers are shaded by scene lights using the provided ambient / diffuse factors. When set
back to <code>null</code>, lighting is disabled and markers revert to unlit (emissive) rendering.</p>
<p>Default value is <code>null</code>.
Sets the material reflectivity properties for all markers of location indicator including its halo.
This value affects also any custom markers set with <code>setMarker3dModel</code>.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set materialReflectivity(MaterialReflectivity? value);</code></pre>
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
<li class="self-crumb">materialReflectivity property</li>
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



</div>
`
}</HTMLBlock>
