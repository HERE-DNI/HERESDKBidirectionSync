---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-heremapcontroller-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- HereMapController-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">HereMapController class</li>
</ol>
<div class="self-name">HereMapController</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/HereMapController-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>HereMapController class abstract</h1></div>
<section class="desc markdown">
<p>Allows interacting with the map displayed by /sdk-for-flutter-explore-mapview-heremap-class widget.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Inheritance</dt>
<dd>
<ul class="gt-separated dark clazz-relationships">
<li>Object</li>
<li>/sdk-for-flutter-explore-mapview-mapviewbase-class</li>
<li>HereMapController</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="HereMapController">
/sdk-for-flutter-explore-mapview-heremapcontroller-heremapcontroller(int id)
</dt>
<dd>
<div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="camera">
/sdk-for-flutter-explore-mapview-mapviewbase-camera
→ /sdk-for-flutter-explore-mapview-mapcamera-class
</dt>
<dd class="inherited">
  The camera to control the view for the map.
Gets the camera to control the view for the map.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="frameRate">
/sdk-for-flutter-explore-mapview-mapviewbase-framerate
↔ int
</dt>
<dd class="inherited">
  Maximum render frame rate in frames per second.
Gets maximum render frame rate in frames per second.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="gestures">
/sdk-for-flutter-explore-mapview-mapviewbase-gestures
→ /sdk-for-flutter-explore-gestures-gestures-class
</dt>
<dd class="inherited">
  The gestures control object for setting up the capture of gestures.
Gets the gestures control object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-mapview-mapviewbase-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="hereMapControllerCore">
/sdk-for-flutter-explore-mapview-mapviewbase-heremapcontrollercore
→ /sdk-for-flutter-explore-mapview-heremapcontrollercore-class
</dt>
<dd class="inherited">
  Here Map associated with this map view.
Gets the /sdk-for-flutter-explore-mapview-heremapcontrollercore-class associated with this map view.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="isValid">
/sdk-for-flutter-explore-mapview-mapviewbase-isvalid
→ bool
</dt>
<dd class="inherited">
  Indicates whether this instance is valid.
It will be made invalid when the corresponding <code>SDKNativeEngine</code> is destroyed.
Returns <code>true</code> if this instance is valid, <code>false</code> otherwise. It will be made
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="mapContext">
/sdk-for-flutter-explore-mapview-mapviewbase-mapcontext
→ /sdk-for-flutter-explore-mapview-mapcontext-class
</dt>
<dd class="inherited">
  Map context associated with this map view.
Gets the map context associated with this map view.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="mapScene">
/sdk-for-flutter-explore-mapview-mapviewbase-mapscene
→ /sdk-for-flutter-explore-mapview-mapscene-class
</dt>
<dd class="inherited">
  Map scene associated with this map view.
Gets the map scene associated with this map view.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="pixelScale">
/sdk-for-flutter-explore-mapview-mapviewbase-pixelscale
→ double
</dt>
<dd class="inherited">
  The pixel scale factor used by this <code>MapView</code>.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-mapview-mapviewbase-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="viewportSize">
/sdk-for-flutter-explore-mapview-mapviewbase-viewportsize
→ /sdk-for-flutter-explore-core-size2d-class
</dt>
<dd class="inherited">
  The size of this map view in physical pixels.
If internally the map view's render surface is not attached yet
(see: /sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class), or after the map view has been destroyed
then a <code>Size2D</code> with zero width and height is returned.
Gets the size of this map view in physical pixels.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="watermarkSize">
/sdk-for-flutter-explore-mapview-mapviewbase-watermarksize
→ /sdk-for-flutter-explore-core-size2d-class
</dt>
<dd class="inherited">
  Provides the size of the watermark in physical pixels.
Returns the watermark size in physical pixels.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="widgetPins">
/sdk-for-flutter-explore-mapview-heremapcontroller-widgetpins
→ List&lt;<wbr/>/sdk-for-flutter-explore-mapview-widgetpin-class&gt;
</dt>
<dd>
  Gets a list of currently added widget pins.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="addLifecycleListener">
/sdk-for-flutter-explore-mapview-mapviewbase-addlifecyclelistener(<wbr/>/sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class lifecycleListener)
    → void

</dt>
<dd class="inherited">
  Adds a /sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class to this map view.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="geoToViewCoordinates">
/sdk-for-flutter-explore-mapview-mapviewbase-geotoviewcoordinates(<wbr/>/sdk-for-flutter-explore-core-geocoordinates-class geoCoordinates)
    → /sdk-for-flutter-explore-core-point2d-class?

</dt>
<dd class="inherited">
  Converts geographical coordinates to view coordinates (in pixels).
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-mapview-mapviewbase-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="pause">
/sdk-for-flutter-explore-mapview-heremapcontroller-pause(<wbr/>)
    → void

</dt>
<dd>
  Pauses the map widget.
  

</dd>
<dt class="callable inherited" id="pick">
/sdk-for-flutter-explore-mapview-mapviewbase-pick(<wbr/>/sdk-for-flutter-explore-mapview-mapscenemappickfilter-class? filter, /sdk-for-flutter-explore-core-rectangle2d-class viewArea, /sdk-for-flutter-explore-mapview-mapviewbasemappickcallback callback)
    → void

</dt>
<dd class="inherited">
  Returns all map content located inside the specified pick area.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="pinWidget">
/sdk-for-flutter-explore-mapview-heremapcontroller-pinwidget(<wbr/>Widget widget, /sdk-for-flutter-explore-core-geocoordinates-class coordinates, {/sdk-for-flutter-explore-core-anchor2d-class? anchor})
    → /sdk-for-flutter-explore-mapview-widgetpin-class?

</dt>
<dd>
  Pins a <code>Widget</code> to the MapView and returns a proxy object that can be used to
control the pinning.
  

</dd>
<dt class="callable inherited" id="removeLifecycleListener">
/sdk-for-flutter-explore-mapview-mapviewbase-removelifecyclelistener(<wbr/>/sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class lifecycleListener)
    → void

</dt>
<dd class="inherited">
  Removes a /sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class from this map view.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="resume">
/sdk-for-flutter-explore-mapview-heremapcontroller-resume(<wbr/>)
    → void

</dt>
<dd>
  Resumes the map widget.
  

</dd>
<dt class="callable inherited" id="setWatermarkLocation">
/sdk-for-flutter-explore-mapview-mapviewbase-setwatermarklocation(<wbr/>/sdk-for-flutter-explore-core-anchor2d-class anchor, /sdk-for-flutter-explore-core-point2d-class offset)
    → void

</dt>
<dd class="inherited">
  Sets the position of the HERE logo watermark within the map view.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="takeScreenshot">
/sdk-for-flutter-explore-mapview-heremapcontroller-takescreenshot(<wbr/>/sdk-for-flutter-explore-mapview-takescreenshotcallback callback)
    → void

</dt>
<dd>
  Asynchronously retrieves a screenshot of the map view.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-mapview-mapviewbase-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="unpinWidget">
/sdk-for-flutter-explore-mapview-heremapcontroller-unpinwidget(<wbr/>Widget widget)
    → void

</dt>
<dd>
  Removes a /sdk-for-flutter-explore-mapview-widgetpin-class from the MapView by specifying the corresponding <code>Widget</code>.
Trying to unpin a widget that was not pinned or has been unpinned before has no effect.
All pinned widgets equal to <code>widget</code> will be removed.
  

</dd>
<dt class="callable inherited" id="viewToGeoCoordinates">
/sdk-for-flutter-explore-mapview-mapviewbase-viewtogeocoordinates(<wbr/>/sdk-for-flutter-explore-core-point2d-class viewCoordinates)
    → /sdk-for-flutter-explore-core-geocoordinates-class?

</dt>
<dd class="inherited">
  Converts view coordinates (in pixels) to geographical coordinates.
  <div class="features">inherited</div>
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
<section class="summary offset-anchor" id="static-properties">
<h2>Static Properties</h2>
<dl class="properties">
<dt class="property" id="primaryLanguage">
/sdk-for-flutter-explore-mapview-heremapcontroller-primarylanguage
↔ /sdk-for-flutter-explore-core-languagecode?
</dt>
<dd>
  The code of desired primary map display language.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="secondaryLanguage">
/sdk-for-flutter-explore-mapview-heremapcontroller-secondarylanguage
↔ /sdk-for-flutter-explore-core-languagecode?
</dt>
<dd>
  The code of desired secondary map display language.
Note: This feature is in beta state and thus there can be bugs and unexpected behavior.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="shadowQuality">
/sdk-for-flutter-explore-mapview-heremapcontroller-shadowquality
↔ /sdk-for-flutter-explore-mapview-shadowquality
</dt>
<dd>
  The current shadow quality.
Default shadow quality is /sdk-for-flutter-explore-mapview-shadowquality.
Note: This feature is in beta state and thus there can be bugs and unexpected behavior.
  <div class="features">getter/setter pair</div>
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
<li class="self-crumb">HereMapController class</li>
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



</div>
`
}</HTMLBlock>
