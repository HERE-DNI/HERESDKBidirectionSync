---
title: "ExternalMapDataSourceErrorCode enum - maploader.remote.connection library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceerrorcode"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader.remote.connection/maploader.remote.connection-library-sidebar.html" data-below-sidebar="maploader.remote.connection/ExternalMapDataSourceErrorCode-enum-sidebar.html">

<div>

# <span class="kind-enum">ExternalMapDataSourceErrorCode</span> enum

</div>

<div class="section desc markdown">

Describes the reason for failing to configure <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a> with external map data source.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Values

<span class="name">internalError</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceerrorcode">ExternalMapDataSourceErrorCode</a></span>  
Internal error occurred.

<span class="name">addCatalogError</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceerrorcode">ExternalMapDataSourceErrorCode</a></span>  
Error while adding catalog to `DataStoreClient`. Verify the same catalogs are added to the `DataStoreServer` instance on the server side.

<span class="name">invalidCredentials</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceerrorcode">ExternalMapDataSourceErrorCode</a></span>  
Error while checking credentials. E.g. some field is empty but expected not empty

<span class="name">serviceRegisterError</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceerrorcode">ExternalMapDataSourceErrorCode</a></span>  
Error while attempting to register OCM AM service

<span class="name">clientDisposedError</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceerrorcode">ExternalMapDataSourceErrorCode</a></span>  
While attempting to register the connection, the client was being disposed

<span class="name">serverUnavailable</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceerrorcode">ExternalMapDataSourceErrorCode</a></span>  
This means that server is not launched or configuration settings is wrong. Make sense only on client side

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceerrorcode-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceerrorcode-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceerrorcode-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceerrorcode-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceerrorcode-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceerrorcode-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceerrorcode-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceerrorcode">ExternalMapDataSourceErrorCode</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

