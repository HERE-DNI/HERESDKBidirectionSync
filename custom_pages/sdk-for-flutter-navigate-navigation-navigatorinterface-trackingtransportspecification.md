---
title: "trackingTransportSpecification property"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-trackingtransportspecification"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- trackingTransportSpecification.html -->


<div>
<h1>trackingTransportSpecification property</h1></div>
<section id="getter">

<a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a>?
trackingTransportSpecification


<p>Defines the transport specification for the <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>, when no route is present.
Properly setting the transport specification optimizes the navigation experience, and improves
resource consumption. An <a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a> must have the <a href="sdk-for-flutter-navigate-transport-transportspecification-transportmode">TransportSpecification.transportMode</a> set.
A transport specification can have several parameters defined such as <a href="sdk-for-flutter-navigate-transport-vehiclespecification-lengthincentimeters">VehicleSpecification.lengthInCentimeters</a>
defined in <a href="sdk-for-flutter-navigate-transport-transportspecification-vehiclespecification">TransportSpecification.vehicleSpecification</a> to set the source of information describing the vehicle.
By default the <a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a> will have the transport mode set to <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.car</a>.</p>
<p>Currently used members of <a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a></p>
<ul>
<li><a href="sdk-for-flutter-navigate-transport-transportspecification-transportmode">TransportSpecification.transportMode</a>: Sets the transport mode.</li>
<li>From <a href="sdk-for-flutter-navigate-transport-transportspecification-vehiclespecification">TransportSpecification.vehicleSpecification</a>:
<ul>
<li><a href="sdk-for-flutter-navigate-transport-vehiclespecification-grossweightinkilograms">VehicleSpecification.grossWeightInKilograms</a>: Required for truck related speed information.</li>
<li><a href="sdk-for-flutter-navigate-transport-vehiclespecification-heightincentimeters">VehicleSpecification.heightInCentimeters</a>: Required for truck related speed information.</li>
<li><a href="sdk-for-flutter-navigate-transport-vehiclespecification-widthincentimeters">VehicleSpecification.widthInCentimeters</a>: Additional truck definition for more specific truck speed information.</li>
<li><a href="sdk-for-flutter-navigate-transport-vehiclespecification-lengthincentimeters">VehicleSpecification.lengthInCentimeters</a>: Additional truck definition for more specific truck speed information.
Gets the transport specification for the <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>, when no route is present.</li>
</ul>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TransportSpecification? get trackingTransportSpecification;</code></pre>

</section>
<section id="setter">

void
trackingTransportSpecification=(<a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a>? value)


<p>Defines the transport specification for the <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>, when no route is present.
Properly setting the transport specification optimizes the navigation experience, and improves
resource consumption. An <a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a> must have the <a href="sdk-for-flutter-navigate-transport-transportspecification-transportmode">TransportSpecification.transportMode</a> set.
A transport specification can have several parameters defined such as <a href="sdk-for-flutter-navigate-transport-vehiclespecification-lengthincentimeters">VehicleSpecification.lengthInCentimeters</a>
defined in <a href="sdk-for-flutter-navigate-transport-transportspecification-vehiclespecification">TransportSpecification.vehicleSpecification</a> to set the source of information describing the vehicle.
By default the <a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a> will have the transport mode set to <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.car</a>.</p>
<p>Currently used members of <a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a></p>
<ul>
<li><a href="sdk-for-flutter-navigate-transport-transportspecification-transportmode">TransportSpecification.transportMode</a>: Sets the transport mode.</li>
<li>From <a href="sdk-for-flutter-navigate-transport-transportspecification-vehiclespecification">TransportSpecification.vehicleSpecification</a>:
<ul>
<li><a href="sdk-for-flutter-navigate-transport-vehiclespecification-grossweightinkilograms">VehicleSpecification.grossWeightInKilograms</a>: Required for truck related speed information.</li>
<li><a href="sdk-for-flutter-navigate-transport-vehiclespecification-heightincentimeters">VehicleSpecification.heightInCentimeters</a>: Required for truck related speed information.</li>
<li><a href="sdk-for-flutter-navigate-transport-vehiclespecification-widthincentimeters">VehicleSpecification.widthInCentimeters</a>: Additional truck definition for more specific truck speed information.</li>
<li><a href="sdk-for-flutter-navigate-transport-vehiclespecification-lengthincentimeters">VehicleSpecification.lengthInCentimeters</a>: Additional truck definition for more specific truck speed information.
Sets the transport specification for the <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>, when no route is present.</li>
</ul>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set trackingTransportSpecification(TransportSpecification? value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
