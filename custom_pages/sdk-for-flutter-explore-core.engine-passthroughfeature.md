---
title: "PassThroughFeature enum - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core.engine-passthroughfeature"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PassThroughFeature.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/PassThroughFeature-enum-sidebar.html">

<div>

# <span class="kind-enum">PassThroughFeature</span> enum

</div>

<div class="section desc markdown">

Represents features that are allowed to consume online data when the HERE SDK's offline mode is activated via <a href="sdk-for-flutter-explore-core-engine-sdknativeengine-isofflinemode">SDKNativeEngine.isOfflineMode</a> and/or <a href="sdk-for-flutter-explore-core-engine-sdkoptions-offlinemode">SDKOptions.offlineMode</a>.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Values

<span class="name">trafficData</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-passthroughfeature">PassThroughFeature</a></span>  
When set, then the `TrafficEngine` is not blocked from initiating online connections to search for traffic data such as incidents.

<span class="name">trafficTilesFlow</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-passthroughfeature">PassThroughFeature</a></span>  
When set, then the corresponding `MapFeature` will not be blocked and online connections can be initiated by the HERE SDK to retrieve traffic flow data.

<span class="name">trafficTilesIncidents</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-passthroughfeature">PassThroughFeature</a></span>  
When set, then the corresponding `MapFeature` will not be blocked and online connections can be initiated by the HERE SDK to retrieve traffic incident data.

<span class="name">onlineRouting</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-passthroughfeature">PassThroughFeature</a></span>  
When set, online routing can be performed by the HERE SDK, allowing the retrieval of up-to-date routing information from online services even when offline mode is enabled.

<span class="name">onlineSearch</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-passthroughfeature">PassThroughFeature</a></span>  
When set, online search can be performed by the HERE SDK, allowing the retrieval of up-to-date search information from online services even when offline mode is enabled.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-core-engine-passthroughfeature-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-passthroughfeature-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-passthroughfeature-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-core-engine-passthroughfeature-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-passthroughfeature-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-core-engine-passthroughfeature-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-explore-core-engine-passthroughfeature-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-engine-passthroughfeature">PassThroughFeature</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
