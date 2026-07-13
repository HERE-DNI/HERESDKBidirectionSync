---
title: "PhysicalAttributes class - mapdata library - Dart API"
slug: "sdk-for-flutter-navigate-mapdata-physicalattributes-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapdata/mapdata-library-sidebar.html" data-below-sidebar="mapdata/PhysicalAttributes-class-sidebar.html">

<div>

# <span class="kind-class">PhysicalAttributes</span> class

</div>

<div class="section desc markdown">

Physical attributes of the segment.

***Note*** a road can have more than one attribute at the same time.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-physicalattributes-physicalattributes">PhysicalAttributes</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-physicalattributes-divider">divider</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-mapdata-roaddivider">RoadDivider</a>?</span>  
Indicates the presence of a road divider.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-physicalattributes-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-physicalattributes-isboatferry">isBoatFerry</a></span> <span class="signature">↔ bool</span>  
Identifies a generalised route of a boat ferry for passengers or vehicles over water.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-physicalattributes-isbridge">isBridge</a></span> <span class="signature">↔ bool</span>  
Identifies a structure that allows a road, railway, or walkway to pass over another road, railway, waterway, or valley serving map display and route guidance functionalities. Bridge is published on segments that represent significant bridges and/or overpasses; elevated roads are not published as bridge.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-physicalattributes-isdirtroad">isDirtRoad</a></span> <span class="signature">↔ bool</span>  
Indicates whether the navigable segment is paved. Paved is primarily used for map display and routing by assigning higher penalties to unpaved roads. Paved roads are made of concrete, asphalt, cobblestone or brick. Unpaved roads do not have a solid surface, e.g. are made of gravel, dirt or grass.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-physicalattributes-ismultiplydigitized">isMultiplyDigitized</a></span> <span class="signature">↔ bool</span>  
Identifies separately digitised roads, i.e., roads that are digitised with one line per direction of traffic instead of one line per road. It may be flagged on roads when certain physical features (e.g. a walkway, a tram, a bus lane) are located between the separately digitised opposing roadbeds if driver perception remains unchanged.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-physicalattributes-isprivate">isPrivate</a></span> <span class="signature">↔ bool</span>  
Private identifies roads that are not maintained by an organization responsible for maintenance of public roads. Allows for unique cartographic representation of roads that restrict public use. May be used to avoid routing through a private road.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-physicalattributes-israilferry">isRailFerry</a></span> <span class="signature">↔ bool</span>  
Identifies a generalised route of a ferry for passengers or vehicles via rail. It is applied on a segment that represent a ferry route for vehicles over rail such as: a route for ferrying passengers over rail, if destination is not accessible by the road network or prohibits the use of automobiles.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-physicalattributes-isroundabout">isRoundabout</a></span> <span class="signature">↔ bool</span>  
Indicates the presence of a roundabout.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-physicalattributes-istunnel">isTunnel</a></span> <span class="signature">↔ bool</span>  
Identifies an enclosed (on all sides) passageway through or under an obstruction. This attribute can be used for display or route guidance.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-physicalattributes-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-physicalattributes-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-physicalattributes-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-physicalattributes-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

