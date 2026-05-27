---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-maplayer-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- MapLayer-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapLayer-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapLayer/MapLayer.html">MapLayer</a></li>
<li class="section-title inherited">
<a href="mapview/MapLayer-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview/MapLayer/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview/MapLayer/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview/MapLayer-class.html#instance-methods">Methods</a></li>
<li><a href="mapview/MapLayer/destroy.html">destroy</a></li>
<li class="inherited"><a href="mapview/MapLayer/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="mapview/MapLayer/setEnabled.html">setEnabled</a></li>
<li><a href="mapview/MapLayer/setPriority.html">setPriority</a></li>
<li><a href="mapview/MapLayer/setStyle.html">setStyle</a></li>
<li class="inherited"><a href="mapview/MapLayer/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/MapLayer-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapLayer/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapLayer class</li>
</ol>
<div class="self-name">MapLayer</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapLayer-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapLayer class abstract</h1></div>
<section class="desc markdown">
<p>Interface for managing a map layer.</p>
<p>A map layer can be created by using the <a href="../mapview/MapLayerBuilder-class.html">/sdk-for-flutter-explore-mapview-maplayerbuilder-class</a>. At creation, the layer
gets added to a map. The layer gets removed from the map upon instance destruction.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapLayer">
<a href="../mapview/MapLayer/MapLayer.html">/sdk-for-flutter-explore-mapview-maplayer-maplayer</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../mapview/MapLayer/hashCode.html">/sdk-for-flutter-explore-mapview-maplayer-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview/MapLayer/runtimeType.html">/sdk-for-flutter-explore-mapview-maplayer-runtimetype</a>
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
<dt class="callable" id="destroy">
<a href="../mapview/MapLayer/destroy.html">/sdk-for-flutter-explore-mapview-maplayer-destroy</a>(<wbr/>)
    → void

</dt>
<dd>
  Frees all internally used resources.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview/MapLayer/noSuchMethod.html">/sdk-for-flutter-explore-mapview-maplayer-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="setEnabled">
<a href="../mapview/MapLayer/setEnabled.html">/sdk-for-flutter-explore-mapview-maplayer-setenabled</a>(<wbr/>bool enable)
    → void

</dt>
<dd>
  Sets whether or not the layer is enabled to be drawn.
  

</dd>
<dt class="callable" id="setPriority">
<a href="../mapview/MapLayer/setPriority.html">/sdk-for-flutter-explore-mapview-maplayer-setpriority</a>(<wbr/><a href="../mapview/MapLayerPriority-class.html">/sdk-for-flutter-explore-mapview-maplayerpriority-class</a> priority)
    → void

</dt>
<dd>
  Sets the render priority for the layer which replaces any previously defined priorities.
  

</dd>
<dt class="callable" id="setStyle">
<a href="../mapview/MapLayer/setStyle.html">/sdk-for-flutter-explore-mapview-maplayer-setstyle</a>(<wbr/><a href="../mapview/Style-class.html">/sdk-for-flutter-explore-mapview-style-class</a> style)
    → void

</dt>
<dd>
  Sets the style to be used by the layer.
  

</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview/MapLayer/toString.html">/sdk-for-flutter-explore-mapview-maplayer-tostring</a>(<wbr/>)
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
<a href="../mapview/MapLayer/operator_equals.html">/sdk-for-flutter-explore-mapview-maplayer-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapLayer class</li>
</ol>
<h5>mapview library</h5>
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
</HTMLBlock>
