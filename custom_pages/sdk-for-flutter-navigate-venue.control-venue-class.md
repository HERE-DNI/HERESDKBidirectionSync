---
title: "Venue class - venue.control library - Dart API"
slug: "sdk-for-flutter-navigate-venue.control-venue-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.control/venue.control-library-sidebar.html" data-below-sidebar="venue.control/Venue-class-sidebar.html">

<div>

# <span class="kind-class">Venue</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Controls the <a href="sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a> inside the <a href="sdk-for-flutter-navigate-venue-control-venuemap-class">VenueMap</a> object.

The venue controls the selection of the <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a> and the <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> of the <a href="sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a>. It provides the possibility to customize styles for the <a href="sdk-for-flutter-navigate-venue-data-venuegeometry-class">VenueGeometry</a>. Objects of this class can only be created using methods <a href="sdk-for-flutter-navigate-venue-control-venuemap-addvenueasyncwitherrorsstr">VenueMap.addVenueAsyncWithErrorsStr</a> and <a href="sdk-for-flutter-navigate-venue-control-venuemap-selectvenueasyncwitherrorsstr">VenueMap.selectVenueAsyncWithErrorsStr</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venue-venue">Venue</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venue-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venue-istopologyvisible">isTopologyVisible</a></span> <span class="signature">↔ bool</span>  
Returns true if topology is visible. It can be used to check the status of topology visibility. Gets the current status of topology visibility.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venue-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venue-selecteddrawing">selectedDrawing</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a></span>  
The selected drawing. Only the selected drawing will be visible as active on the map. All others will be hidden or displayed without details, depending on the implementation of the renderer. Gets the currently selected <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a> of the <a href="sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venue-selectedlevel">selectedLevel</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a></span>  
The selected level. Only the selected level will be visible as active on the map. All others will be hidden or displayed without details, depending on a renderer implementation. If the level doesn't belong to the currently selected drawing, it can not be selected. Gets the currently selected <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> from the selected <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venue-selectedlevelindex">selectedLevelIndex</a></span> <span class="signature">↔ int</span>  
The index of the <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> selected from the level array of the <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a>. Unlike the Z index, it can't have a negative value. Gets the index of the currently selected <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> in the level array of the related <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a>. The level array can be taken from <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-levels">VenueDrawing.levels</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venue-selectedlevelzindex">selectedLevelZIndex</a></span> <span class="signature">↔ int</span>  
The Z index value of the <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> selected. Z index 0 represents the ground level, negative values represent underground levels, positive values - levels above the ground. Z index can also be taken from <a href="sdk-for-flutter-navigate-venue-data-venuelevel-zindex">VenueLevel.zIndex</a>. Gets the Z index of the currently selected <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venue-venuemodel">venueModel</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a></span>  
The <a href="sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a> controlled by this object. It can be used to get the <a href="sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a> belonging to this object, like a building or a complex of buildings. Gets the <a href="sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a> controlled by this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venue-venuestyle">venueStyle</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-style-venuestyle-class">VenueStyle</a></span>  
The <a href="sdk-for-flutter-navigate-venue-style-venuestyle-class">VenueStyle</a> associated with the <a href="sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a> controlled by this object. It can be used to get the style of the venue. Contains the information about the geometry and label styles available for the venue. Gets the <a href="sdk-for-flutter-navigate-venue-style-venuestyle-class">VenueStyle</a> associated with the <a href="sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a> controlled by this object.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venue-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venue-setcustomstyle">setCustomStyle</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setCustomStyle-param-geometries" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-venue-data-venuegeometry-class">VenueGeometry</a></span>\></span></span> <span class="parameter-name">geometries</span>, </span><span id="sdk-for-flutter-navigate-setCustomStyle-param-style" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-style-venuegeometrystyle-class">VenueGeometryStyle</a>?</span> <span class="parameter-name">style</span>, </span><span id="sdk-for-flutter-navigate-setCustomStyle-param-labelStyle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-style-venuelabelstyle-class">VenueLabelStyle</a>?</span> <span class="parameter-name">labelStyle</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets a custom style for geometries and related labels.

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venue-setcustomstyletocrosswalk">setCustomStyleToCrosswalk</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setCustomStyleToCrosswalk-param-crosswalks" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-venue-data-crosswalk-class">Crosswalk</a></span>\></span></span> <span class="parameter-name">crosswalks</span>, </span><span id="sdk-for-flutter-navigate-setCustomStyleToCrosswalk-param-style" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-style-venuegeometrystyle-class">VenueGeometryStyle</a>?</span> <span class="parameter-name">style</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets a custom style for crosswalk.

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venue-setcustomstyletotopology">setCustomStyleToTopology</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setCustomStyleToTopology-param-topologies" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-venue-data-venuetopology-class">VenueTopology</a></span>\></span></span> <span class="parameter-name">topologies</span>, </span><span id="sdk-for-flutter-navigate-setCustomStyleToTopology-param-style" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-style-venuegeometrystyle-class">VenueGeometryStyle</a>?</span> <span class="parameter-name">style</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets a custom style for topologies.

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venue-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venue-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

