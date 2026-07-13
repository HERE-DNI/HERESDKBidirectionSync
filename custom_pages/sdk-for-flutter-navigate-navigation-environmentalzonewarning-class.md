---
title: "EnvironmentalZoneWarning class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-environmentalzonewarning-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EnvironmentalZoneWarning-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/EnvironmentalZoneWarning-class-sidebar.html">

<div>

# <span class="kind-class">EnvironmentalZoneWarning</span> class

</div>

<div class="section desc markdown">

Represents Environmental zones.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-environmentalzonewarning-environmentalzonewarning">EnvironmentalZoneWarning</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-distanceInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">distanceInMeters</span>, </span><span id="sdk-for-flutter-navigate-param-distanceType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span> <span class="parameter-name">distanceType</span>, </span><span id="sdk-for-flutter-navigate-param-zoneId" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">zoneId</span>, </span><span id="sdk-for-flutter-navigate-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-environmentalzonewarning-description">description</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-localizedtexts-class">LocalizedTexts</a></span>  
Indicates the description of the environmental zone in the available languages.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-environmentalzonewarning-distanceinmeters">distanceInMeters</a></span> <span class="signature">↔ double</span>  
The distance from the current location to the environmental zone.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-environmentalzonewarning-distancetype">distanceType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span>  
Indicates if the specified zone is ahead of the vehicle or has just passed by. If it is ahead, then <a href="sdk-for-flutter-navigate-navigation-environmentalzonewarning-distanceinmeters">EnvironmentalZoneWarning.distanceInMeters</a> is greater than 0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-environmentalzonewarning-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-environmentalzonewarning-id">id</a></span> <span class="signature">↔ int</span>  
Unique identifier for this specific environmental zone warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-environmentalzonewarning-name">name</a></span> <span class="signature">↔ String</span>  
Indicates the official name of the environmental zone.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-environmentalzonewarning-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-environmentalzonewarning-websiteurl">websiteUrl</a></span> <span class="signature">↔ String?</span>  
Indicates the website of the environmental zone, if available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-environmentalzonewarning-zoneid">zoneId</a></span> <span class="signature">↔ String</span>  
Indicates the environmental zone id in the map data.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-environmentalzonewarning-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-environmentalzonewarning-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-environmentalzonewarning-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
