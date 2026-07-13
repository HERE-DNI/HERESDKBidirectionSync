---
title: "TrafficBroadcast class - trafficbroadcast library - Dart API"
slug: "sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficBroadcast-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="trafficbroadcast/trafficbroadcast-library-sidebar.html" data-below-sidebar="trafficbroadcast/TrafficBroadcast-class-sidebar.html">

<div>

# <span class="kind-class">TrafficBroadcast</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

A `TrafficBroadcast` is expecting the <a href="https://en.wikipedia.org/wiki/Traffic_message_channel">RDS-TMC</a> format and it can be used when there is no internet connection, so that the `OfflineRoutingEngine` can utilize traffic data coming over a radio channel.

The <a href="sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-activate">TrafficBroadcast.activate</a> method needs to be called to receive traffic data events.

**Note:** In order to adopt the `TrafficDataProvider` interface special hardware is required. Talk to your HERE representative for more details. Only by adopting the `TrafficDataProvider` interface you can integrate radio station signals providing traffic broadcasts. Traffic broadcasts are meant to be used *independently* from the already included traffic on routes, on the map and from the HERE backends (when using the `TrafficEngine`).

This class continuously reacts to new locations provided from a location source and acts as a <a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a>. The location must be updated regardless of calling <a href="sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-activate">TrafficBroadcast.activate</a>.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section">

Implemented types  
- <a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-trafficbroadcast">TrafficBroadcast</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-parameters" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcastparameters-class">TrafficBroadcastParameters</a></span> <span class="parameter-name">parameters</span></span>)</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-trafficbroadcast-withsdkengine">TrafficBroadcast.withSdkEngine</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withSdkEngine-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span>, </span><span id="sdk-for-flutter-navigate-withSdkEngine-param-parameters" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcastparameters-class">TrafficBroadcastParameters</a></span> <span class="parameter-name">parameters</span></span>)</span>  
Creates a new instance of this class.

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

<span class="name"><a href="sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-trafficdataprovider">trafficDataProvider</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-traffic-trafficdataprovider-class">TrafficDataProvider</a>?</span>  
The traffic data provider that provides the traffic information.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-activate">activate</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Activates the reception of traffic data over the radio channel.

<span class="name"><a href="sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-deactivate">deactivate</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Deactivates the reception of traffic data over the radio channel.

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

<span class="name"><a href="sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-ontmcdataupdated">onTMCDataUpdated</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onTMCDataUpdated-param-tmcData" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-trafficbroadcast-tmcdata-class">TMCData</a></span> <span class="parameter-name">tmcData</span></span>) <span class="returntype parameter">→ void</span> </span>  
Must be called on every TMC data update.

<span class="name"><a href="sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-ontmcserviceproviderinfoupdated">onTMCServiceProviderInfoUpdated</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onTMCServiceProviderInfoUpdated-param-tmcServiceProdiverInfo" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-trafficbroadcast-tmcserviceproviderinfo-class">TMCServiceProviderInfo</a></span> <span class="parameter-name">tmcServiceProdiverInfo</span></span>) <span class="returntype parameter">→ void</span> </span>  
Must be called on every TMC service prodiver info update.

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

</div>
`
}</HTMLBlock>
