---
title: "isTrafficOnRouteVisible property"
slug: "sdk-for-flutter-navigate-navigation-visualnavigator-istrafficonroutevisible"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isTrafficOnRouteVisible.html -->


<div>
<h1>isTrafficOnRouteVisible property</h1></div>
<section id="getter">

bool
isTrafficOnRouteVisible


<p>A boolean which defines whether to perform rendering of traffic conditions on the route when <code>Route</code> visualization
is enabled during visual navigation.
When enabled the route's <code>MapPolyline</code> will be enhanced with visualization of the traffic conditions.
Colors used for this visualization are defined in <a href="/sdk-for-flutter-navigate-navigation-visualnavigatorcolors-trafficonroutecolors">VisualNavigatorColors.trafficOnRouteColors</a>.
The presented traffic information is either set by the user via <a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-trafficonroute">NavigatorInterface.trafficOnRoute</a> or
is generated from historical traffic data stored in the map.
<strong>Note:</strong> <code>VisualNavigator</code> does not perform automatic traffic data updates. The updated traffic information is available
through the <code>sdk.routing.RoutingEngine.calculate_traffic_on_route</code> interface. The returned <a href="/sdk-for-flutter-navigate-routing-trafficonroute-class">TrafficOnRoute</a>
could then be used to update <code>sdk.navigation.NavigatorInterface.traffic_on_route</code> to refresh the traffic on route visualization.
Defaults to <code>false</code>.
Gets the current state whether traffic conditions on route should be displayed during visual navigation.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool get isTrafficOnRouteVisible;</code></pre>

</section>
<section id="setter">

void
isTrafficOnRouteVisible=(bool value)


<p>A boolean which defines whether to perform rendering of traffic conditions on the route when <code>Route</code> visualization
is enabled during visual navigation.
When enabled the route's <code>MapPolyline</code> will be enhanced with visualization of the traffic conditions.
Colors used for this visualization are defined in <a href="/sdk-for-flutter-navigate-navigation-visualnavigatorcolors-trafficonroutecolors">VisualNavigatorColors.trafficOnRouteColors</a>.
The presented traffic information is either set by the user via <a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-trafficonroute">NavigatorInterface.trafficOnRoute</a> or
is generated from historical traffic data stored in the map.
<strong>Note:</strong> <code>VisualNavigator</code> does not perform automatic traffic data updates. The updated traffic information is available
through the <code>sdk.routing.RoutingEngine.calculate_traffic_on_route</code> interface. The returned <a href="/sdk-for-flutter-navigate-routing-trafficonroute-class">TrafficOnRoute</a>
could then be used to update <code>sdk.navigation.NavigatorInterface.traffic_on_route</code> to refresh the traffic on route visualization.
Defaults to <code>false</code>.
Sets whether to perform rendering of traffic conditions on the route when <code>Route</code> visualization is enabled
during visual navigation.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set isTrafficOnRouteVisible(bool value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
