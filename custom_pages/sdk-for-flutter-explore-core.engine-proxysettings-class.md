---
title: "ProxySettings class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core.engine-proxysettings-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/ProxySettings-class-sidebar.html">

<div>

# <span class="kind-class">ProxySettings</span> class

</div>

<div class="section desc markdown">

Proxy configuration for the HERE SDK network that is applied per request.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-core-engine-proxysettings-proxysettings">ProxySettings</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-type" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-engine-proxysettingsproxytype">ProxySettingsProxyType</a></span> <span class="parameter-name">type</span>, </span><span id="sdk-for-flutter-explore-param-ipAddress" class="parameter"><span class="type-annotation">InternetAddress</span> <span class="parameter-name">ipAddress</span>, </span><span id="sdk-for-flutter-explore-param-port" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">port</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-core-engine-proxysettings-credentials">credentials</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-core-engine-proxysettingscredentials-class">ProxySettingsCredentials</a>?</span>  
Optional field to define credentials to authenticate a user to the proxy server.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-proxysettings-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-proxysettings-ipaddress">ipAddress</a></span> <span class="signature">↔ InternetAddress</span>  
Represents the IP Address of the proxy server.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-proxysettings-networkinterface">networkInterface</a></span> <span class="signature">↔ String?</span>  
Network interface. It's taken into account on Android platform when IPv6 is used. Default value is "wlan0". If not set then no interface is used.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-proxysettings-port">port</a></span> <span class="signature">↔ int</span>  
Represents the port number of the proxy server.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-proxysettings-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-proxysettings-type">type</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-core-engine-proxysettingsproxytype">ProxySettingsProxyType</a></span>  
Represents the type of the proxy server.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-core-engine-proxysettings-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-proxysettings-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-core-engine-proxysettings-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

