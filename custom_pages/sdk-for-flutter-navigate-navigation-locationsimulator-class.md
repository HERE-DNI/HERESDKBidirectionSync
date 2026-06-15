---
title: "LocationSimulator class abstract"
slug: "sdk-for-flutter-navigate-navigation-locationsimulator-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationSimulator-class.html -->


<div>
<h1>LocationSimulator class abstract</h1></div>

<p>Use the <code>LocationSimulator</code> to generate locations along a route or a GPX document.</p>
<p>It notifies
the registered object about the current location at a fixed interval. In order to customize
the interval, see <a href="sdk-for-flutter-navigate-navigation-locationsimulatoroptions-class">LocationSimulatorOptions</a>.
The locations are closely matched to the shape and proceeded from the start to the
destination as found in the provided route or the GPX document.
When providing a route, the <code>LocationSimulator</code> uses a base speed taken from each span
found in the provided route object. This base speed can be multiplied upfront
with a custom <code>speedFactor</code> for simulation purposes.
Effectively, this means that traffic-related information is not considered
to adjust the speed of the simulation.
For the <code>GPXTrack</code>, a speed is either based on timestamps in the original file or provided by the user. The following data is read from a <code>GPXTrack</code> and inserted into the provided <code>Location</code> object: <code>latitude</code>, <code>longitude</code>, <code>altitude</code>, <code>time</code>, <code>bearingInDegrees</code>, <code>speedInMetersPerSecond</code>, <code>horizontalAccuracyInMeters</code>, <code>verticalAccuracyInMeters</code> and <code>locationTechnology</code>.</p>
<p>Note that simulation works offline and independent from any map data</p>
<ul>
<li>only the information found in the provided route or GPX document is considered.</li>
<li>When initializing the <code>LocationSimulator</code> with a route, then interpolations take place between the vertices of the route's
polyline. The distance between interpolated locations is a function of the current span's speed and the set notification interval.</li>
<li>When initializing the <code>LocationSimulator</code> with a GPX file, the <code>LocationSimulator</code> does not apply
any interpolation on the provided location data as this would shadow the recorded GPX data.</li>
</ul>
<p>Notifications will stop after the entire route has been traveled.</p>
<p><strong>Note:</strong>
Map-matched locations are only accessible from <a href="sdk-for-flutter-navigate-navigation-routeprogress-class">RouteProgress</a>.</p>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-locationsimulator-locationsimulator-withroute">LocationSimulator.withRoute</a></li><li><a href="sdk-for-flutter-navigate-navigation-locationsimulator-locationsimulator-withtrack">LocationSimulator.withTrack</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-locationsimulator-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-navigation-locationsimulator-listener">listener</a></li><li><a href="sdk-for-flutter-navigate-navigation-locationsimulator-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-locationsimulator-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-navigation-locationsimulator-pause">pause</a></li><li><a href="sdk-for-flutter-navigate-navigation-locationsimulator-resume">resume</a></li><li><a href="sdk-for-flutter-navigate-navigation-locationsimulator-start">start</a></li><li><a href="sdk-for-flutter-navigate-navigation-locationsimulator-stop">stop</a></li><li><a href="sdk-for-flutter-navigate-navigation-locationsimulator-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-locationsimulator-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
