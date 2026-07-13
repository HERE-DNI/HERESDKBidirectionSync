---
title: "NetworkSettings class - core.engine library - Dart API"
slug: "sdk-for-flutter-navigate-core.engine-networksettings-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- NetworkSettings-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/NetworkSettings-class-sidebar.html">

<div>

# <span class="kind-class">NetworkSettings</span> class

</div>

<div class="section desc markdown">

Network configuration to be used by <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a> during the initialization.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-networksettings-networksettings">NetworkSettings</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-networksettings-certificates">certificates</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-engine-certificatesettings-class">CertificateSettings</a>?</span>  
Certificate settings to use on Android Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-networksettings-diagnosticsoutputpath">diagnosticsOutputPath</a></span> <span class="signature">↔ String?</span>  
Absolute file path to be used for redirecting CURL verbose output. The application must have read and write permissions to the given path. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-networksettings-domainnamesystemservers">domainNameSystemServers</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-networkendpoint-class">NetworkEndpoint</a></span>\></span></span>  
Domain Name Server list. This list fully replaces embedded mechanism to detect DNS. The order is important. To reduce response time make sure that most probably servers are at the beginning. Currently only IPv4 is supported.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-networksettings-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-networksettings-proxysettings">proxySettings</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-engine-proxysettings-class">ProxySettings</a>?</span>  
Proxy settings. It can be later accessed or changed with <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-proxysettings">SDKNativeEngine.proxySettings</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-networksettings-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-networksettings-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-networksettings-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-networksettings-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
