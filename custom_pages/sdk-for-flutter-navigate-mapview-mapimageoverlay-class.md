---
title: "MapImageOverlay class abstract"
slug: "sdk-for-flutter-navigate-mapview-mapimageoverlay-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapImageOverlay-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapImageOverlay-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapImageOverlay/MapImageOverlay.html">MapImageOverlay</a></li>
<li><a href="mapview/MapImageOverlay/MapImageOverlay.withAnchor.html">withAnchor</a></li>
<li class="section-title">
<a href="mapview/MapImageOverlay-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapview/MapImageOverlay/anchor.html">anchor</a></li>
<li><a href="mapview/MapImageOverlay/drawOrder.html">drawOrder</a></li>
<li class="inherited"><a href="mapview/MapImageOverlay/hashCode.html">hashCode</a></li>
<li><a href="mapview/MapImageOverlay/image.html">image</a></li>
<li class="inherited"><a href="mapview/MapImageOverlay/runtimeType.html">runtimeType</a></li>
<li><a href="mapview/MapImageOverlay/viewCoordinates.html">viewCoordinates</a></li>
<li class="section-title inherited"><a href="mapview/MapImageOverlay-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview/MapImageOverlay/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/MapImageOverlay/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/MapImageOverlay-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapImageOverlay/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">MapImageOverlay class</li>
</ol>
<div class="self-name">MapImageOverlay</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapImageOverlay-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapImageOverlay class abstract</h1></div>
<section class="desc markdown">
<p><code>MapImageOverlay</code> is used to draw images over the map, at a view coordinate inside the map viewport.</p>
<p>The image to be displayed is represented by a /sdk-for-flutter-navigate-mapview-mapimage-class object.
By default, the overlay is centered on the given view coordinate.</p>
<p>The resulting viewport area covered by the overlay is computed out of the overlay's view coordinate,
the anchor point and the image size. The overlay subareas that fall outside of the map viewport get clipped.</p>
<p>To display the map overlay, it needs to be added to the scene using /sdk-for-flutter-navigate-mapview-mapscene-addmapimageoverlay.
To stop displaying it, remove it from the scene using /sdk-for-flutter-navigate-mapview-mapscene-removemapimageoverlay.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapImageOverlay">
/sdk-for-flutter-navigate-mapview-mapimageoverlay-mapimageoverlay(/sdk-for-flutter-navigate-core-point2d-class viewCoordinates, /sdk-for-flutter-navigate-mapview-mapimage-class image)
</dt>
<dd>
          Creates an instance of an overlay at given view coordinates, represented by specified image.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="MapImageOverlay.withAnchor">
/sdk-for-flutter-navigate-mapview-mapimageoverlay-mapimageoverlay-withanchor(/sdk-for-flutter-navigate-core-point2d-class viewCoordinates, /sdk-for-flutter-navigate-mapview-mapimage-class image, /sdk-for-flutter-navigate-core-anchor2d-class anchor)
</dt>
<dd>
          Creates an instance of an overlay at given view coordinates, represented by specified image,
with anchor point specifying how the image is positioned relative to the overlay's view coordinates.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="anchor">
/sdk-for-flutter-navigate-mapview-mapimageoverlay-anchor
↔ /sdk-for-flutter-navigate-core-anchor2d-class
</dt>
<dd>
  The anchor point for the overlay image which specifies the position offset relative
to the overlay's view coordinates.
Gets current anchor point for the overlay image.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="drawOrder">
/sdk-for-flutter-navigate-mapview-mapimageoverlay-draworder
↔ int
</dt>
<dd>
  Draw order of this <code>MapImageOverlay</code>.
Gets draw order of this <code>MapImageOverlay</code>. The default value is 0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-mapview-mapimageoverlay-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="image">
/sdk-for-flutter-navigate-mapview-mapimageoverlay-image
↔ /sdk-for-flutter-navigate-mapview-mapimage-class
</dt>
<dd>
  Image overlayed on the map.
Gets currently used map image.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapview-mapimageoverlay-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="viewCoordinates">
/sdk-for-flutter-navigate-mapview-mapimageoverlay-viewcoordinates
↔ /sdk-for-flutter-navigate-core-point2d-class
</dt>
<dd>
  The view point in pixels on the map viewport where the map overlay is drawn.
Gets the view point in pixels on the map viewport where the overlay is drawn.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapview-mapimageoverlay-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapview-mapimageoverlay-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-mapview-mapimageoverlay-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">MapImageOverlay class</li>
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
`
}</HTMLBlock>
