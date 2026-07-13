---
title: "Location class - core library - Dart API"
slug: "sdk-for-flutter-explore-core-location-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/Location-class-sidebar.html">

<div>

# <span class="kind-class">Location</span> class

</div>

<div class="section desc markdown">

Describes a location in the world at a given time.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-core-location-location-withcoordinates">Location.withCoordinates</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withCoordinates-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span></span>)</span>  
Creates a new Location instance from the provided GeoCoordinates value. timestamp is initialized with `January 1, 1970, 00:00:00 GMT` value. The rest of the fields will be initialized to null.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-core-location-bearingaccuracyindegrees">bearingAccuracyInDegrees</a></span> <span class="signature">↔ double?</span>  
Estimated bearing accuracy for this location, in degrees. If it cannot be determined, the value is `null`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-location-bearingindegrees">bearingInDegrees</a></span> <span class="signature">↔ double?</span>  
Bearing (also known as course) is the device's horizontal direction of travel. Starts at 0 in the geographical north and rotates around the compass in a clockwise direction. This means for going north it is equal to 0, for northeast it is 45, for east it is 90 and so on. Note that this may be different from the orientation of the device. If it cannot be determined, the value is `null`. Otherwise, it is guaranteed to be in the range \<a href="sdk-for-flutter-explore-core-location-coordinates">0, 360).

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name">[coordinates</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span>  
The geographic coordinates of the location.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-location-gnsstime">gnssTime</a></span> <span class="signature">↔ Duration?</span>  
Optional gnss time at which the location was determined. It is a time interval from the Unix time epoch in milliseconds. If it cannot be determined, the value is `null`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-location-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-location-horizontalaccuracyinmeters">horizontalAccuracyInMeters</a></span> <span class="signature">↔ double?</span>  
The estimated horizontal accuracy. The actual location will lie within this radius of uncertainty.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-location-locationtechnology">locationTechnology</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-core-locationtechnology">LocationTechnology</a>?</span>  
Optional technology or provider of this location. If it cannot be determined, the value is `null`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-location-pitchindegrees">pitchInDegrees</a></span> <span class="signature">↔ double?</span>  
Pitch of this location, in degrees. If it cannot be determined, the value is `null`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-location-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-location-source">source</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-core-locationsource">LocationSource</a>?</span>  
Optional source of this location. If it cannot be determined, the value is `null`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-location-speedaccuracyinmeterspersecond">speedAccuracyInMetersPerSecond</a></span> <span class="signature">↔ double?</span>  
Estimated speed accuracy of this location, in meters per second. If it cannot be determined, the value is `null`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-location-speedinmeterspersecond">speedInMetersPerSecond</a></span> <span class="signature">↔ double?</span>  
Current speed of the device. If it cannot be determined, the value is `null`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-location-time">time</a></span> <span class="signature">↔ DateTime?</span>  
The time at which the location was determined.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-location-timestampsinceboot">timestampSinceBoot</a></span> <span class="signature">↔ Duration?</span>  
The time at which the location was determined, relative to device boot time. This time is monotonic and not affected by leap time or other system time adjustments, so this is the recommended basis for general purpose interval timing between location updates. If it cannot be determined, the value is `null`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-location-verticalaccuracyinmeters">verticalAccuracyInMeters</a></span> <span class="signature">↔ double?</span>  
Estimated vertical accuracy. Given that the received Location contains the altitude, the real value of the altitude is estimated to lie within the following range: \[altitude - vertical accuracy, altitude + vertical accuracy\]. For example, when the altitude is equal to 50 and the vertical accuracy is 8, then the actual value is most likely in the range \[42, 58\].

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-core-location-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-location-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-core-location-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

