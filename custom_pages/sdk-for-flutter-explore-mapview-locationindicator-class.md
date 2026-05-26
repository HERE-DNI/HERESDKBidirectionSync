---
title: "LocationIndicator class abstract"
slug: "sdk-for-flutter-explore-mapview-locationindicator-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationIndicator-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/LocationIndicator-class.html#constructors">Constructors</a></li>
<li><a href="mapview/LocationIndicator/LocationIndicator.html">LocationIndicator</a></li>
<li><a href="mapview/LocationIndicator/LocationIndicator.withMapView.html">withMapView</a></li>
<li class="section-title">
<a href="mapview/LocationIndicator-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview/LocationIndicator/hashCode.html">hashCode</a></li>
<li><a href="mapview/LocationIndicator/isAccuracyVisualized.html">isAccuracyVisualized</a></li>
<li><a href="mapview/LocationIndicator/isActive.html">isActive</a></li>
<li><a href="mapview/LocationIndicator/locationIndicatorStyle.html">locationIndicatorStyle</a></li>
<li><a href="mapview/LocationIndicator/materialReflectivity.html">materialReflectivity</a></li>
<li><a href="mapview/LocationIndicator/opacity.html">opacity</a></li>
<li class="inherited"><a href="mapview/LocationIndicator/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview/LocationIndicator-class.html#instance-methods">Methods</a></li>
<li><a href="mapview/LocationIndicator/disable.html">disable</a></li>
<li><a href="mapview/LocationIndicator/enable.html">enable</a></li>
<li><a href="mapview/LocationIndicator/getHaloColor.html">getHaloColor</a></li>
<li class="inherited"><a href="mapview/LocationIndicator/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="mapview/LocationIndicator/setHaloColor.html">setHaloColor</a></li>
<li><a class="deprecated" href="mapview/LocationIndicator/setMarker3dModel.html">setMarker3dModel</a></li>
<li><a href="mapview/LocationIndicator/setMarker3dModelWithRenderSizeUnit.html">setMarker3dModelWithRenderSizeUnit</a></li>
<li class="inherited"><a href="mapview/LocationIndicator/toString.html">toString</a></li>
<li><a href="mapview/LocationIndicator/updateLocation.html">updateLocation</a></li>
<li><a href="mapview/LocationIndicator/updateLocationAndCamera.html">updateLocationAndCamera</a></li>
<li class="section-title inherited"><a href="mapview/LocationIndicator-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/LocationIndicator/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">LocationIndicator class</li>
</ol>
<div class="self-name">LocationIndicator</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/LocationIndicator-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>LocationIndicator class abstract</h1></div>
<section class="desc markdown">
<p>Graphical object to represent the location of the user on the map.</p>
<p>It is either a green dot for pedestrian style or a triangular arrow for vehicle navigation style.
This style can be changed by /sdk-for-flutter-explore-mapview-locationindicator-locationindicatorstyle</p>
<p>The location is made available to an instance of this class by calling /sdk-for-flutter-explore-mapview-locationindicator-updatelocation or
/sdk-for-flutter-explore-mapview-locationindicator-updatelocationandcamera.</p>
<p>Use /sdk-for-flutter-explore-mapview-locationindicator-enable to add this object to the map and /sdk-for-flutter-explore-mapview-locationindicator-disable to remove it.</p>
<p>Note: The LocationIndicator is always rendered at a fixed altitude near 0. Changing the MapCamera
to look at geographic coordinates with an altitude that is higher can cause the following behavior: If the
MapCamera angle is tilted and altitude is too high, the LocationIndicator can unexpectedly
disappear from the viewport due to the new perspective.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="LocationIndicator">
/sdk-for-flutter-explore-mapview-locationindicator-locationindicator()
</dt>
<dd>
          Creates an instance of LocationIndicator.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="LocationIndicator.withMapView">
/sdk-for-flutter-explore-mapview-locationindicator-locationindicator-withmapview(/sdk-for-flutter-explore-mapview-mapviewbase-class mapView)
</dt>
<dd>
          Creates an instance of LocationIndicator and adds it to provided /sdk-for-flutter-explore-mapview-mapviewbase-class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-mapview-locationindicator-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="isAccuracyVisualized">
/sdk-for-flutter-explore-mapview-locationindicator-isaccuracyvisualized
↔ bool
</dt>
<dd>
  Whether the horizontal accuracy is visualized by scaling the accuracy indicator halo.
Returns whether /sdk-for-flutter-explore-core-location-horizontalaccuracyinmeters is used to scale the accuracy indicator halo.
Default is <code>false</code>, in which case the halo has a fixed and zoom level independent size.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isActive">
/sdk-for-flutter-explore-mapview-locationindicator-isactive
↔ bool
</dt>
<dd>
  A Boolean value that determines whether the active on inactive version of location indicator is shown.
Returns <code>true</code> if active version of the location indicator is shown or <code>false</code>
when inactive version is shown. By default, it is <code>true</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="locationIndicatorStyle">
/sdk-for-flutter-explore-mapview-locationindicator-locationindicatorstyle
↔ /sdk-for-flutter-explore-mapview-locationindicatorindicatorstyle
</dt>
<dd>
  The visual style of location indicator.
By default, it is set to /sdk-for-flutter-explore-mapview-locationindicatorindicatorstyle.
Returns visual style of location indicator.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="materialReflectivity">
/sdk-for-flutter-explore-mapview-locationindicator-materialreflectivity
↔ /sdk-for-flutter-explore-mapview-materialreflectivity-class?
</dt>
<dd>
  The material reflectivity properties of the location indicator.
Enables per‑pixel lighting for all internal markers (navigation, pedestrian,
inactive variants) and the halo when assigned. While <code>materialReflectivity</code> is non‑null the
markers are shaded by scene lights using the provided ambient / diffuse factors. When set
back to <code>null</code>, lighting is disabled and markers revert to unlit (emissive) rendering.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="opacity">
/sdk-for-flutter-explore-mapview-locationindicator-opacity
↔ double
</dt>
<dd>
  The factor applied to the alpha channel of both the location indicator's texture and the accuracy indicator's halo color.
Default value is 1.0 which means location
indicator is displayed with the default alpha channel of the texture.
Gets the current opacity of the location indicator.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-mapview-locationindicator-runtimetype
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
<dt class="callable" id="disable">
/sdk-for-flutter-explore-mapview-locationindicator-disable(<wbr/>)
    → void

</dt>
<dd>
  This function removes /sdk-for-flutter-explore-mapview-locationindicator-class from map view.
  

</dd>
<dt class="callable" id="enable">
/sdk-for-flutter-explore-mapview-locationindicator-enable(<wbr/>/sdk-for-flutter-explore-mapview-mapviewbase-class mapView)
    → void

</dt>
<dd>
  Enables /sdk-for-flutter-explore-mapview-locationindicator-class for provided /sdk-for-flutter-explore-mapview-mapviewbase-class.
  

</dd>
<dt class="callable" id="getHaloColor">
/sdk-for-flutter-explore-mapview-locationindicator-gethalocolor(<wbr/>/sdk-for-flutter-explore-mapview-locationindicatorindicatorstyle style)
    → Color

</dt>
<dd>
  Retrieves the color of the accuracy indicator halo for the requested IndicatorStyle.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-mapview-locationindicator-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="setHaloColor">
/sdk-for-flutter-explore-mapview-locationindicator-sethalocolor(<wbr/>/sdk-for-flutter-explore-mapview-locationindicatorindicatorstyle style, Color color)
    → void

</dt>
<dd>
  Sets the color of the accuracy indicator halo for a given style.
  

</dd>
<dt class="callable" id="setMarker3dModel">
/sdk-for-flutter-explore-mapview-locationindicator-setmarker3dmodel(<wbr/>/sdk-for-flutter-explore-mapview-mapmarker3dmodel-class model, double scale, /sdk-for-flutter-explore-mapview-locationindicatormarkertype type)
    → void

</dt>
<dd>
  Sets the MapMarker3DModel asset to be displayed as location indicator for a specified type.
  

</dd>
<dt class="callable" id="setMarker3dModelWithRenderSizeUnit">
/sdk-for-flutter-explore-mapview-locationindicator-setmarker3dmodelwithrendersizeunit(<wbr/>/sdk-for-flutter-explore-mapview-mapmarker3dmodel-class model, double scale, /sdk-for-flutter-explore-mapview-locationindicatormarkertype type, /sdk-for-flutter-explore-mapview-rendersizeunit renderSizeUnit)
    → void

</dt>
<dd>
  Sets the /sdk-for-flutter-explore-mapview-mapmarker3dmodel-class asset to be displayed as location indicator for a specified type.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-mapview-locationindicator-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="updateLocation">
/sdk-for-flutter-explore-mapview-locationindicator-updatelocation(<wbr/>/sdk-for-flutter-explore-core-location-class location)
    → void

</dt>
<dd>
  Updates the indicator to a new location.
  

</dd>
<dt class="callable" id="updateLocationAndCamera">
/sdk-for-flutter-explore-mapview-locationindicator-updatelocationandcamera(<wbr/>/sdk-for-flutter-explore-core-location-class location, /sdk-for-flutter-explore-mapview-mapcameraupdate-class cameraUpdate)
    → void

</dt>
<dd>
  Updates the indicator to a new location and applies a camera update at the same time.
  

</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-explore-mapview-locationindicator-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">LocationIndicator class</li>
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
