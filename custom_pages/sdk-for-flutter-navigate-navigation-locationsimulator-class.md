---
title: "LocationSimulator class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-locationsimulator-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationSimulator-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/LocationSimulator-class-sidebar.html">

<div>

# <span class="kind-class">LocationSimulator</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Use the `LocationSimulator` to generate locations along a route or a GPX document.

It notifies the registered object about the current location at a fixed interval. In order to customize the interval, see <a href="sdk-for-flutter-navigate-navigation-locationsimulatoroptions-class">LocationSimulatorOptions</a>. The locations are closely matched to the shape and proceeded from the start to the destination as found in the provided route or the GPX document. When providing a route, the `LocationSimulator` uses a base speed taken from each span found in the provided route object. This base speed can be multiplied upfront with a custom `speedFactor` for simulation purposes. Effectively, this means that traffic-related information is not considered to adjust the speed of the simulation. For the `GPXTrack`, a speed is either based on timestamps in the original file or provided by the user. The following data is read from a `GPXTrack` and inserted into the provided `Location` object: `latitude`, `longitude`, `altitude`, `time`, `bearingInDegrees`, `speedInMetersPerSecond`, `horizontalAccuracyInMeters`, `verticalAccuracyInMeters` and `locationTechnology`.

Note that simulation works offline and independent from any map data

- only the information found in the provided route or GPX document is considered.
- When initializing the `LocationSimulator` with a route, then interpolations take place between the vertices of the route's polyline. The distance between interpolated locations is a function of the current span's speed and the set notification interval.
- When initializing the `LocationSimulator` with a GPX file, the `LocationSimulator` does not apply any interpolation on the provided location data as this would shadow the recorded GPX data.

Notifications will stop after the entire route has been traveled.

**Note:** Map-matched locations are only accessible from <a href="sdk-for-flutter-navigate-navigation-routeprogress-class">RouteProgress</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-locationsimulator-locationsimulator-withroute">LocationSimulator.withRoute</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withRoute-param-route" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-route-class">Route</a></span> <span class="parameter-name">route</span>, </span><span id="sdk-for-flutter-navigate-withRoute-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-locationsimulatoroptions-class">LocationSimulatorOptions</a></span> <span class="parameter-name">options</span></span>)</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-locationsimulator-locationsimulator-withtrack">LocationSimulator.withTrack</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withTrack-param-gpxTrack" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-gpxtrack-class">GPXTrack</a></span> <span class="parameter-name">gpxTrack</span>, </span><span id="sdk-for-flutter-navigate-withTrack-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-locationsimulatoroptions-class">LocationSimulatorOptions</a></span> <span class="parameter-name">options</span></span>)</span>  
Create a location simulator

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-locationsimulator-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-locationsimulator-listener">listener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a>?</span>  
The object that notifies on location updates. Gets a `LocationListener` that notifies on location updates.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-locationsimulator-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-locationsimulator-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-locationsimulator-pause">pause</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Pauses sending notifications to the subscribers.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-locationsimulator-resume">resume</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Resumes sending notifications to the subscribers.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-locationsimulator-start">start</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Starts the location provider to send notifications to the subscribers.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-locationsimulator-stop">stop</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Stops the location provider from sending notifications to the subscribers.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-locationsimulator-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-locationsimulator-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
