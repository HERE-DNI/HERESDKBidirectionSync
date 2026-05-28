---
title: "MapMatcher class abstract"
slug: "sdk-for-flutter-navigate-mapmatcher-mapmatcher-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMatcher-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapmatcher/MapMatcher-class.html#constructors">Constructors</a></li>
<li><a href="mapmatcher/MapMatcher/MapMatcher.html">MapMatcher</a></li>
<li><a href="mapmatcher/MapMatcher/MapMatcher.withEngine.html">withEngine</a></li>
<li><a href="mapmatcher/MapMatcher/MapMatcher.withLayers.html">withLayers</a></li>
<li class="section-title inherited">
<a href="mapmatcher/MapMatcher-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapmatcher/MapMatcher/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapmatcher/MapMatcher/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapmatcher/MapMatcher-class.html#instance-methods">Methods</a></li>
<li><a href="mapmatcher/MapMatcher/match.html">match</a></li>
<li class="inherited"><a href="mapmatcher/MapMatcher/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapmatcher/MapMatcher/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapmatcher/MapMatcher-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapmatcher/MapMatcher/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapmatcher-mapmatcher-library</li>
<li class="self-crumb">MapMatcher class</li>
</ol>
<div class="self-name">MapMatcher</div>
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
<div class="main-content" data-above-sidebar="mapmatcher/mapmatcher-library-sidebar.html" data-below-sidebar="mapmatcher/MapMatcher-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapMatcher class abstract</h1></div>
<section class="desc markdown">
<p>This class provides map-matching functionality.</p>
<p>It determines whether a location can be
matched to a nearby road network and provides additional OCM map data for that location.</p>
<p><strong>Note:</strong> This is a <strong>beta</strong> release of this feature. There may be bugs and unexpected
behaviors. Related APIs may change in future releases without a deprecation process.</p>
<p>A <code>MapMatcher</code> maintains an internal state across location updates.
This helps to check if the match is consistent with previous matches or if an unrealistic jump occurred due to low accuracy
of the provided location.</p>
<p>A <code>MapMatcher</code> requires OCM tile data, either through caching, prefetching, or installed <code>Region</code> data.
If the necessary tiles are not found, an online request is initiated. Note that in such cases,
the download is triggered silently in the background, and <code>null</code> is returned
immediately.</p>
<p>The <code>MapMatcher</code> supports two layer configurations for retrieving segment geometry data:</p>
<ul>
<li>
<p><strong>Rendering layer (<code>LayerConfiguration.Feature.RENDERING</code>)</strong>: Enabled by default.
If your application uses map rendering or <code>MapView</code> components, using this layer is recommended.</p>
</li>
<li>
<p><strong>eHorizon layer (<code>LayerConfiguration.Feature.EHORIZON</code>)</strong>: Not enabled by default.
It encodes segment geometries outside the rendering layer groups to reduce the amount of downloaded data.
Use the eHorizon layer when:</p>
<ul>
<li>No <code>MapView</code> is used in your application.</li>
<li>Only the eHorizon layer is used in your application.
In these cases, using the eHorizon layer will reduce the required data to download. If the rendering layer is enabled, it will increase the required data to download.</li>
</ul>
</li>
</ul>
<p><strong>Important</strong>: If <code>useRenderingLayers</code> is set to <code>false</code> without properly enabling the eHorizon layer,
it may produce incorrect results. Layer configuration is especially important when prefetching or installing
region data. Missing data will be downloaded online automatically as needed.</p>
<p>If your hardware supports pitch and high precision altitude information and you want to use them in the <code>MapMatcher</code>
to improve map-matching, then enable the <code>LayerConfiguration.Feature.ADAS</code> layer:</p>
<ol>
<li>Turn on the <code>ADAS</code> layer via <code>LayerConfiguration.enabledFeatures</code> (it will increase data consumption).</li>
<li>If available, set <code>location.pitchInDegrees</code>, <code>location.coordinates.altitude</code> and <code>location.verticalAccuracyInMeters</code>.</li>
<li>In case of issues, please contact your HERE representative.</li>
</ol>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapMatcher">
/sdk-for-flutter-navigate-mapmatcher-mapmatcher-mapmatcher()
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="MapMatcher.withEngine">
/sdk-for-flutter-navigate-mapmatcher-mapmatcher-mapmatcher-withengine(/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine)
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="MapMatcher.withLayers">
/sdk-for-flutter-navigate-mapmatcher-mapmatcher-mapmatcher-withlayers(/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine, bool useRenderingLayers)
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-mapmatcher-mapmatcher-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapmatcher-mapmatcher-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="match">
/sdk-for-flutter-navigate-mapmatcher-mapmatcher-match(<wbr/>/sdk-for-flutter-navigate-core-location-class location)
    → /sdk-for-flutter-navigate-navigation-mapmatchedlocation-class?

</dt>
<dd>
  This method computes the map-matched location for the provided input location.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapmatcher-mapmatcher-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapmatcher-mapmatcher-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-mapmatcher-mapmatcher-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
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
<li>/sdk-for-flutter-navigate-mapmatcher-mapmatcher-library</li>
<li class="self-crumb">MapMatcher class</li>
</ol>
<h5>mapmatcher library</h5>
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
