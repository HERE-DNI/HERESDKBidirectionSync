---
title: "LocationManager class - mapmatcher library - Dart API"
slug: "sdk-for-flutter-navigate-mapmatcher-locationmanager-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapmatcher/mapmatcher-library-sidebar.html" data-below-sidebar="mapmatcher/LocationManager-class-sidebar.html">

<div>

# <span class="kind-class">LocationManager</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

LocationManager listens to position updates and provides the map-matched location using the LocationManagerListener.

**Note:** This is a **beta** release of this feature. There may be bugs and unexpected behaviors. Related APIs may change in future releases without a deprecation process.

</div>

<div class="section">

Implemented types  
- <a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapmatcher-locationmanager-locationmanager">LocationManager</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span></span>)</span>  
Creates a new instance of <a href="sdk-for-flutter-navigate-mapmatcher-locationmanager-class">LocationManager</a>.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-core-locationlistener-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-locationlistener-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapmatcher-locationmanager-addmatchedlocationlistener">addMatchedLocationListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addMatchedLocationListener-param-matchedLocationListener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapmatcher-matchedlocationlistener-class">MatchedLocationListener</a></span> <span class="parameter-name">matchedLocationListener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds the <a href="sdk-for-flutter-navigate-mapmatcher-matchedlocationlistener-class">MatchedLocationListener</a> to the subscribtion list.

<span class="name"><a href="sdk-for-flutter-navigate-core-locationlistener-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-locationlistener-onlocationupdated">onLocationUpdated</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onLocationUpdated-param-location" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-location-class">Location</a></span> <span class="parameter-name">location</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called each time a new location is available.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapmatcher-locationmanager-removematchedlocationlistener">removeMatchedLocationListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeMatchedLocationListener-param-matchedLocationListener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapmatcher-matchedlocationlistener-class">MatchedLocationListener</a></span> <span class="parameter-name">matchedLocationListener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes the <a href="sdk-for-flutter-navigate-mapmatcher-matchedlocationlistener-class">MatchedLocationListener</a> from the subscribtion list.

<span class="name"><a href="sdk-for-flutter-navigate-mapmatcher-locationmanager-setmapmatcher">setMapMatcher</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setMapMatcher-param-mapMatcher" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher</a>?</span> <span class="parameter-name">mapMatcher</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets the <a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher</a> for exclusive use by <a href="sdk-for-flutter-navigate-mapmatcher-locationmanager-class">LocationManager</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapmatcher-locationmanager-takemapmatcher">takeMapMatcher</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher</a>?</span> </span>  
Retrieves and removes the <a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-class">MapMatcher</a> from <a href="sdk-for-flutter-navigate-mapmatcher-locationmanager-class">LocationManager</a>.

<span class="name"><a href="sdk-for-flutter-navigate-core-locationlistener-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-core-locationlistener-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

