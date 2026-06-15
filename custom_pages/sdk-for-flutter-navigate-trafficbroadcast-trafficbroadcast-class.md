---
title: "TrafficBroadcast class abstract"
slug: "sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficBroadcast-class.html -->


<div>
<h1>TrafficBroadcast class abstract</h1></div>

<p>A <code>TrafficBroadcast</code> is expecting the <a href="https://en.wikipedia.org/wiki/Traffic_message_channel">RDS-TMC</a>
format and it can be used when there is no internet connection, so that the <code>OfflineRoutingEngine</code>
can utilize traffic data coming over a radio channel.</p>
<p>The <a href="sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-activate">TrafficBroadcast.activate</a> method needs to be called to
receive traffic data events.</p>
<p><strong>Note:</strong> In order to adopt the <code>TrafficDataProvider</code> interface special hardware is required. Talk
to your HERE representative for more details. Only by adopting the <code>TrafficDataProvider</code> interface
you can integrate radio station signals providing traffic broadcasts. Traffic broadcasts are meant
to be used <em>independently</em> from the already included traffic on routes, on the map and from the
HERE backends (when using the <code>TrafficEngine</code>).</p>
<p>This class continuously reacts to new locations provided from a location source and acts as a
<a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a>. The location must be updated regardless of calling <a href="sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-activate">TrafficBroadcast.activate</a>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>


<ul><li>Implemented types</li></ul>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-trafficbroadcast">TrafficBroadcast</a></li><li><a href="sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-trafficbroadcast-withsdkengine">TrafficBroadcast.withSdkEngine</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-core-locationlistener-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-core-locationlistener-runtimetype">runtimeType</a></li><li><a href="sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-trafficdataprovider">trafficDataProvider</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-activate">activate</a></li><li><a href="sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-deactivate">deactivate</a></li><li><a href="sdk-for-flutter-navigate-core-locationlistener-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-core-locationlistener-onlocationupdated">onLocationUpdated</a></li><li><a href="sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-ontmcdataupdated">onTMCDataUpdated</a></li><li><a href="sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-ontmcserviceproviderinfoupdated">onTMCServiceProviderInfoUpdated</a></li><li><a href="sdk-for-flutter-navigate-core-locationlistener-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-core-locationlistener-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
