---
title: "MapViewBase class abstract"
slug: "sdk-for-flutter-explore-mapview-mapviewbase-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapViewBase-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapViewBase-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapViewBase/MapViewBase.html">MapViewBase</a></li>
<li class="section-title">
<a href="mapview/MapViewBase-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapview/MapViewBase/camera.html">camera</a></li>
<li><a href="mapview/MapViewBase/frameRate.html">frameRate</a></li>
<li><a href="mapview/MapViewBase/gestures.html">gestures</a></li>
<li class="inherited"><a href="mapview/MapViewBase/hashCode.html">hashCode</a></li>
<li><a href="mapview/MapViewBase/hereMapControllerCore.html">hereMapControllerCore</a></li>
<li><a href="mapview/MapViewBase/isValid.html">isValid</a></li>
<li><a href="mapview/MapViewBase/mapContext.html">mapContext</a></li>
<li><a href="mapview/MapViewBase/mapScene.html">mapScene</a></li>
<li><a href="mapview/MapViewBase/pixelScale.html">pixelScale</a></li>
<li class="inherited"><a href="mapview/MapViewBase/runtimeType.html">runtimeType</a></li>
<li><a href="mapview/MapViewBase/viewportSize.html">viewportSize</a></li>
<li><a href="mapview/MapViewBase/watermarkSize.html">watermarkSize</a></li>
<li class="section-title"><a href="mapview/MapViewBase-class.html#instance-methods">Methods</a></li>
<li><a href="mapview/MapViewBase/addLifecycleListener.html">addLifecycleListener</a></li>
<li><a href="mapview/MapViewBase/geoToViewCoordinates.html">geoToViewCoordinates</a></li>
<li class="inherited"><a href="mapview/MapViewBase/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="mapview/MapViewBase/pick.html">pick</a></li>
<li><a href="mapview/MapViewBase/removeLifecycleListener.html">removeLifecycleListener</a></li>
<li><a href="mapview/MapViewBase/setWatermarkLocation.html">setWatermarkLocation</a></li>
<li class="inherited"><a href="mapview/MapViewBase/toString.html">toString</a></li>
<li><a href="mapview/MapViewBase/viewToGeoCoordinates.html">viewToGeoCoordinates</a></li>
<li class="section-title inherited"><a href="mapview/MapViewBase-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapViewBase/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">MapViewBase class</li>
</ol>
<div class="self-name">MapViewBase</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapViewBase-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapViewBase class abstract</h1></div>
<section class="desc markdown">
<p>Represents the available public API from  <code>MapView</code>.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implementers</dt>
<dd><ul class="comma-separated clazz-relationships">
<li>/sdk-for-flutter-explore-mapview-heremapcontroller-class</li>
</ul></dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapViewBase">
/sdk-for-flutter-explore-mapview-mapviewbase-mapviewbase(/sdk-for-flutter-explore-core-geocoordinates-class? viewToGeoCoordinatesLambda(/sdk-for-flutter-explore-core-point2d-class), /sdk-for-flutter-explore-core-point2d-class? geoToViewCoordinatesLambda(/sdk-for-flutter-explore-core-geocoordinates-class), void setWatermarkLocationLambda(/sdk-for-flutter-explore-core-anchor2d-class, /sdk-for-flutter-explore-core-point2d-class), void addLifecycleListenerLambda(/sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class), void removeLifecycleListenerLambda(/sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class), void pickLambda(/sdk-for-flutter-explore-mapview-mapscenemappickfilter-class?, /sdk-for-flutter-explore-core-rectangle2d-class, /sdk-for-flutter-explore-mapview-mapviewbasemappickcallback ), bool isValidGetLambda(), /sdk-for-flutter-explore-mapview-mapcamera-class cameraGetLambda(), /sdk-for-flutter-explore-gestures-gestures-class gesturesGetLambda(), /sdk-for-flutter-explore-mapview-mapscene-class mapSceneGetLambda(), /sdk-for-flutter-explore-mapview-mapcontext-class mapContextGetLambda(), /sdk-for-flutter-explore-mapview-heremapcontrollercore-class hereMapControllerCoreGetLambda(), /sdk-for-flutter-explore-core-size2d-class viewportSizeGetLambda(), int frameRateGetLambda(), void frameRateSetLambda(int), double pixelScaleGetLambda(), /sdk-for-flutter-explore-core-size2d-class watermarkSizeGetLambda())
</dt>
<dd>
          Represents the available public API from  <code>MapView</code>.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="camera">
/sdk-for-flutter-explore-mapview-mapviewbase-camera
→ /sdk-for-flutter-explore-mapview-mapcamera-class
</dt>
<dd>
  The camera to control the view for the map.
Gets the camera to control the view for the map.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="frameRate">
/sdk-for-flutter-explore-mapview-mapviewbase-framerate
↔ int
</dt>
<dd>
  Maximum render frame rate in frames per second.
Gets maximum render frame rate in frames per second.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="gestures">
/sdk-for-flutter-explore-mapview-mapviewbase-gestures
→ /sdk-for-flutter-explore-gestures-gestures-class
</dt>
<dd>
  The gestures control object for setting up the capture of gestures.
Gets the gestures control object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-mapview-mapviewbase-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="hereMapControllerCore">
/sdk-for-flutter-explore-mapview-mapviewbase-heremapcontrollercore
→ /sdk-for-flutter-explore-mapview-heremapcontrollercore-class
</dt>
<dd>
  Here Map associated with this map view.
Gets the /sdk-for-flutter-explore-mapview-heremapcontrollercore-class associated with this map view.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="isValid">
/sdk-for-flutter-explore-mapview-mapviewbase-isvalid
→ bool
</dt>
<dd>
  Indicates whether this instance is valid.
It will be made invalid when the corresponding <code>SDKNativeEngine</code> is destroyed.
Returns <code>true</code> if this instance is valid, <code>false</code> otherwise. It will be made
  <div class="features">no setter</div>
</dd>
<dt class="property" id="mapContext">
/sdk-for-flutter-explore-mapview-mapviewbase-mapcontext
→ /sdk-for-flutter-explore-mapview-mapcontext-class
</dt>
<dd>
  Map context associated with this map view.
Gets the map context associated with this map view.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="mapScene">
/sdk-for-flutter-explore-mapview-mapviewbase-mapscene
→ /sdk-for-flutter-explore-mapview-mapscene-class
</dt>
<dd>
  Map scene associated with this map view.
Gets the map scene associated with this map view.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="pixelScale">
/sdk-for-flutter-explore-mapview-mapviewbase-pixelscale
→ double
</dt>
<dd>
  The pixel scale factor used by this <code>MapView</code>.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-mapview-mapviewbase-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="viewportSize">
/sdk-for-flutter-explore-mapview-mapviewbase-viewportsize
→ /sdk-for-flutter-explore-core-size2d-class
</dt>
<dd>
  The size of this map view in physical pixels.
If internally the map view's render surface is not attached yet
(see: /sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class), or after the map view has been destroyed
then a <code>Size2D</code> with zero width and height is returned.
Gets the size of this map view in physical pixels.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="watermarkSize">
/sdk-for-flutter-explore-mapview-mapviewbase-watermarksize
→ /sdk-for-flutter-explore-core-size2d-class
</dt>
<dd>
  Provides the size of the watermark in physical pixels.
Returns the watermark size in physical pixels.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="addLifecycleListener">
/sdk-for-flutter-explore-mapview-mapviewbase-addlifecyclelistener(<wbr/>/sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class lifecycleListener)
    → void

</dt>
<dd>
  Adds a /sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class to this map view.
  

</dd>
<dt class="callable" id="geoToViewCoordinates">
/sdk-for-flutter-explore-mapview-mapviewbase-geotoviewcoordinates(<wbr/>/sdk-for-flutter-explore-core-geocoordinates-class geoCoordinates)
    → /sdk-for-flutter-explore-core-point2d-class?

</dt>
<dd>
  Converts geographical coordinates to view coordinates (in pixels).
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-mapview-mapviewbase-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="pick">
/sdk-for-flutter-explore-mapview-mapviewbase-pick(<wbr/>/sdk-for-flutter-explore-mapview-mapscenemappickfilter-class? filter, /sdk-for-flutter-explore-core-rectangle2d-class viewArea, /sdk-for-flutter-explore-mapview-mapviewbasemappickcallback callback)
    → void

</dt>
<dd>
  Returns all map content located inside the specified pick area.
  

</dd>
<dt class="callable" id="removeLifecycleListener">
/sdk-for-flutter-explore-mapview-mapviewbase-removelifecyclelistener(<wbr/>/sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class lifecycleListener)
    → void

</dt>
<dd>
  Removes a /sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class from this map view.
  

</dd>
<dt class="callable" id="setWatermarkLocation">
/sdk-for-flutter-explore-mapview-mapviewbase-setwatermarklocation(<wbr/>/sdk-for-flutter-explore-core-anchor2d-class anchor, /sdk-for-flutter-explore-core-point2d-class offset)
    → void

</dt>
<dd>
  Sets the position of the HERE logo watermark within the map view.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-mapview-mapviewbase-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="viewToGeoCoordinates">
/sdk-for-flutter-explore-mapview-mapviewbase-viewtogeocoordinates(<wbr/>/sdk-for-flutter-explore-core-point2d-class viewCoordinates)
    → /sdk-for-flutter-explore-core-geocoordinates-class?

</dt>
<dd>
  Converts view coordinates (in pixels) to geographical coordinates.
  

</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-explore-mapview-mapviewbase-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">MapViewBase class</li>
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
