---
title: "trackingTransportProfile property"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-trackingtransportprofile"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- trackingTransportProfile.html -->


<div>
<h1>trackingTransportProfile property</h1></div>
<section id="getter">

<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.28.0. Use NavigatorInterface.trackingTransportSpecification instead.")</li>
</ol>
</div>
<a class="deprecated" href="/sdk-for-flutter-navigate-core-transportprofile-class">TransportProfile</a>?
trackingTransportProfile


<p>Defines the transport profile for the <a href="/sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>, when no route is present.
Properly setting the transport profile optimizes the navigation experience, and improves resource consumption.
For example, a <a class="deprecated" href="/sdk-for-flutter-navigate-core-transportprofile-class">TransportProfile</a> can be defined with a <a class="deprecated" href="/sdk-for-flutter-navigate-transport-vehicleprofile-class">VehicleProfile</a>.
A vehicle profile can have several parameters such as <a class="deprecated" href="/sdk-for-flutter-navigate-transport-vehicletype">VehicleType</a> to set the
source of information describing the vehicle.
The default is a <a href="/sdk-for-flutter-navigate-transport-vehicletype">VehicleType.car</a> profile.</p>
<p>Currently used members of <a class="deprecated" href="/sdk-for-flutter-navigate-core-transportprofile-class">TransportProfile</a></p>
<ul>
<li><a class="deprecated" href="/sdk-for-flutter-navigate-transport-vehicletype">VehicleType</a>: Sets the transport mode.</li>
<li>From <code>vehicleProfile</code>:
<ul>
<li><code>grossWeightInKilograms</code>: Required for truck related speed information.</li>
<li><code>heightInCentimeters</code>: Required for truck related speed information.</li>
<li><code>widthInCentimeters</code>: Additional truck definition for more specific truck speed information.</li>
<li><code>lengthInCentimeters</code>: Additional truck definition for more specific truck speed information.
Gets the transport profile for the <a href="/sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>, when no route is present.</li>
</ul>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.28.0. Use NavigatorInterface.trackingTransportSpecification instead.")
TransportProfile? get trackingTransportProfile;</code></pre>

</section>
<section id="setter">

<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.28.0. Use NavigatorInterface.trackingTransportSpecification instead.")</li>
</ol>
</div>
void
trackingTransportProfile=(<a class="deprecated" href="/sdk-for-flutter-navigate-core-transportprofile-class">TransportProfile</a>? value)


<p>Defines the transport profile for the <a href="/sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>, when no route is present.
Properly setting the transport profile optimizes the navigation experience, and improves resource consumption.
For example, a <a class="deprecated" href="/sdk-for-flutter-navigate-core-transportprofile-class">TransportProfile</a> can be defined with a <a class="deprecated" href="/sdk-for-flutter-navigate-transport-vehicleprofile-class">VehicleProfile</a>.
A vehicle profile can have several parameters such as <a class="deprecated" href="/sdk-for-flutter-navigate-transport-vehicletype">VehicleType</a> to set the
source of information describing the vehicle.
The default is a <a href="/sdk-for-flutter-navigate-transport-vehicletype">VehicleType.car</a> profile.</p>
<p>Currently used members of <a class="deprecated" href="/sdk-for-flutter-navigate-core-transportprofile-class">TransportProfile</a></p>
<ul>
<li><a class="deprecated" href="/sdk-for-flutter-navigate-transport-vehicletype">VehicleType</a>: Sets the transport mode.</li>
<li>From <code>vehicleProfile</code>:
<ul>
<li><code>grossWeightInKilograms</code>: Required for truck related speed information.</li>
<li><code>heightInCentimeters</code>: Required for truck related speed information.</li>
<li><code>widthInCentimeters</code>: Additional truck definition for more specific truck speed information.</li>
<li><code>lengthInCentimeters</code>: Additional truck definition for more specific truck speed information.
Sets the transport profile for the <a href="/sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>, when no route is present.</li>
</ul>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.28.0. Use NavigatorInterface.trackingTransportSpecification instead.")
set trackingTransportProfile(TransportProfile? value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
