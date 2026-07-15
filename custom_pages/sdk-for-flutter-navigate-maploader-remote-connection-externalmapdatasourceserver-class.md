---
title: "ExternalMapDataSourceServer class - maploader.remote.connection library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceserver-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader.remote.connection/maploader.remote.connection-library-sidebar.html" data-below-sidebar="maploader.remote.connection/ExternalMapDataSourceServer-class-sidebar.html">

<div>

# <span class="kind-class">ExternalMapDataSourceServer</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.

Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceserver-externalmapdatasourceserver">ExternalMapDataSourceServer</a></span><span class="signature">()</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceserver-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceserver-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceserver-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceserver-start">start</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-start-param-url" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">url</span>, </span><span id="sdk-for-flutter-navigate-start-param-engine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">engine</span>, </span><span id="sdk-for-flutter-navigate-start-param-serviceCredential" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-remote-connection-sslservercredentialsoptions-class">SslServerCredentialsOptions</a>?</span> <span class="parameter-name">serviceCredential</span>, </span><span id="sdk-for-flutter-navigate-start-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-remote-connection-serverstartedcallback">ServerStartedCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Exposes map data source as GRPC service on given url for <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a>.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceserver-stop">stop</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Stops the exposed map data source GRPC service started using <a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceserver-start">ExternalMapDataSourceServer.start</a>.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceserver-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceserver-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

