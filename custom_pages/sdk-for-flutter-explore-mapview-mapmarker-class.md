---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-mapmarker-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarker-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">MapMarker class</li>
</ol>
<div class="self-name">MapMarker</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapMarker-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapMarker class abstract</h1></div>
<section class="desc markdown">
<p><code>MapMarker</code> is used to draw images on the map, for example to mark a specific location.</p>
<p>By default, the marker is centered on the given geographic coordinates.
Markers keep their size regardless of the current zoom level of the map view.</p>
<p>The image to be displayed is represented by /sdk-for-flutter-explore-mapview-mapimage-class object. For performance reasons,
it is highly recommended to reuse a single instance of the image when creating multiple
identical markers.</p>
<p>To display the map marker, it needs to be added to the scene using /sdk-for-flutter-explore-mapview-mapscene-addmapmarker.
To stop displaying it, remove it from the scene using /sdk-for-flutter-explore-mapview-mapscene-removemapmarker.</p>
<p>The display of a map marker is only guaranteed in case its origin is within the viewport.
At the moment, this is a known limitation that mostly affects map markers which are visually
large and cover a sizeable part of the viewport.</p>
<p><strong>Note:</strong>
Due to technical limitations using the MapMarkers API to add a very large number of markers
(several thousands, especially 10000+) is not recommended. Adding this many markers will have a
negative impact on the performance leading to stuttering of the app and lower frame rates.
To work around this limitation the following approach can be used:
Register to map camera updates using /sdk-for-flutter-explore-mapview-mapcamera-addlistener. Query the bounding box of the
camera viewport using /sdk-for-flutter-explore-mapview-mapcamera-boundingbox (it may be extended)
and then use the method /sdk-for-flutter-explore-core-geobox-containsgeocoordinates in combination with
/sdk-for-flutter-explore-mapview-mapcamerastate-distancetotargetinmeters to determine which MapMarkers are actually visible
to the user in the current camera viewport and thus need to be added to the map.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapMarker">
/sdk-for-flutter-explore-mapview-mapmarker-mapmarker(/sdk-for-flutter-explore-core-geocoordinates-class coordinates, /sdk-for-flutter-explore-mapview-mapimage-class image)
</dt>
<dd>
          Creates an instance of a marker at given coordinates, represented by specified image.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="MapMarker.withAnchor">
/sdk-for-flutter-explore-mapview-mapmarker-mapmarker-withanchor(/sdk-for-flutter-explore-core-geocoordinates-class coordinates, /sdk-for-flutter-explore-mapview-mapimage-class image, /sdk-for-flutter-explore-core-anchor2d-class anchor)
</dt>
<dd>
          Creates an instance of a marker at given coordinates, represented by specified image,
with anchor point specifying how the image is positioned relative to the marker's coordinates.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="MapMarker.withImageAndText">
/sdk-for-flutter-explore-mapview-mapmarker-mapmarker-withimageandtext(/sdk-for-flutter-explore-core-geocoordinates-class coordinates, /sdk-for-flutter-explore-mapview-mapimage-class image, String text)
</dt>
<dd>
          Creates a <code>MapMarker</code> instance at given coordinates with specified image and text and a default text style.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="anchor">
/sdk-for-flutter-explore-mapview-mapmarker-anchor
↔ /sdk-for-flutter-explore-core-anchor2d-class
</dt>
<dd>
  The anchor point for the marker image which specifies the position offset relative
to the marker's coordinates.
Gets current anchor point for the marker image.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="coordinates">
/sdk-for-flutter-explore-mapview-mapmarker-coordinates
↔ /sdk-for-flutter-explore-core-geocoordinates-class
</dt>
<dd>
  The point on the map where the map marker is drawn.
Gets the point on the map where the marker is drawn.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="drawOrder">
/sdk-for-flutter-explore-mapview-mapmarker-draworder
↔ int
</dt>
<dd>
  The draw order of this marker relative to other markers.
Gets draw order of this marker relative to other markers. The default value is 0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="fadeDuration">
/sdk-for-flutter-explore-mapview-mapmarker-fadeduration
↔ Duration
</dt>
<dd>
  Duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.
Gets the current duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-mapview-mapmarker-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="image">
/sdk-for-flutter-explore-mapview-mapmarker-image
↔ /sdk-for-flutter-explore-mapview-mapimage-class
</dt>
<dd>
  Image representing the marker on the screen.
Gets currently used map image.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isOverlapAllowed">
/sdk-for-flutter-explore-mapview-mapmarker-isoverlapallowed
↔ bool
</dt>
<dd>
  Determines whether or not the marker can overlap other markers.
Returns <code>true</code> if the marker allows overlap with other markers, <code>false</code> otherwise.
Defaults to <code>true</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isTextOptional">
/sdk-for-flutter-explore-mapview-mapmarker-istextoptional
↔ bool
</dt>
<dd>
  Determines if the marker can be displayed with icon and without text.
Returns <code>true</code> if the marker allows text to be hidden, <code>false</code> otherwise.
Defaults to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="metadata">
/sdk-for-flutter-explore-mapview-mapmarker-metadata
↔ /sdk-for-flutter-explore-core-metadata-class?
</dt>
<dd>
  The Metadata instance attached to this marker, see /sdk-for-flutter-explore-core-metadata-class.
Gets the Metadata instance attached to this marker.
This will be <code>null</code> if nothing has been attached before.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="opacity">
/sdk-for-flutter-explore-mapview-mapmarker-opacity
↔ double
</dt>
<dd>
  Opacity, the factor applied to the alpha channel of the marker image.
Gets the current opacity of the marker image. Value is in the range of [0.0, 1.0].
Default value is 1.0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-mapview-mapmarker-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="text">
/sdk-for-flutter-explore-mapview-mapmarker-text
↔ String
</dt>
<dd>
  The text to be drawn on the map along with the image of the <code>MapMarker</code>.
Gets the text drawn on the map by the <code>MapMarker</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="textStyle">
/sdk-for-flutter-explore-mapview-mapmarker-textstyle
↔ /sdk-for-flutter-explore-mapview-mapmarkertextstyle-class
</dt>
<dd>
  The <code>TextStyle</code> applied to the text of the <code>MapMarker</code>.
Gets a copy of the <code>TextStyle</code> currently in use by the <code>MapMarker</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="visibilityRanges">
/sdk-for-flutter-explore-mapview-mapmarker-visibilityranges
↔ List&lt;<wbr/>/sdk-for-flutter-explore-mapview-mapmeasurerange-class&gt;
</dt>
<dd>
  The list of visibility ranges. The map marker is visible only inside these map measure ranges.
Gets the list of visibility ranges. The map marker is visible only inside these map measure
ranges. When empty (the default), the map marker is visible without map measure restrictions.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="cancelAnimation">
/sdk-for-flutter-explore-mapview-mapmarker-cancelanimation(<wbr/>/sdk-for-flutter-explore-animation-mapmarkeranimation-class animation)
    → void

</dt>
<dd>
  Cancels single ongoing animation.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-mapview-mapmarker-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="startAnimation">
/sdk-for-flutter-explore-mapview-mapmarker-startanimation(<wbr/>/sdk-for-flutter-explore-animation-mapmarkeranimation-class animation, /sdk-for-flutter-explore-animation-animationlistener-class? animationListener)
    → void

</dt>
<dd>
  Starts animation of this map marker according to provided /sdk-for-flutter-explore-animation-mapmarkeranimation-class.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-mapview-mapmarker-tostring(<wbr/>)
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
/sdk-for-flutter-explore-mapview-mapmarker-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">MapMarker class</li>
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
