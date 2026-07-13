---
title: "InstantiationErrorCode enum - core.errors library - Dart API"
slug: "sdk-for-flutter-navigate-core.errors-instantiationerrorcode"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- InstantiationErrorCode.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.errors/core.errors-library-sidebar.html" data-below-sidebar="core.errors/InstantiationErrorCode-enum-sidebar.html">

<div>

# <span class="kind-enum">InstantiationErrorCode</span> enum

</div>

<div class="section desc markdown">

Instantiation error.

</div>

## Values

<span class="name">illegalArguments</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-errors-instantiationerrorcode">InstantiationErrorCode</a></span>  
Illegal arguments.

<span class="name">failed</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-errors-instantiationerrorcode">InstantiationErrorCode</a></span>  
Instantiation attempt failed. Please check log for error.

<span class="name">sharedSdkEngineNotInstantiated</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-errors-instantiationerrorcode">InstantiationErrorCode</a></span>  
Instantiation attempt failed because the shared SDK engine is not instantiated. Please initialise the SDK.

<span class="name">cacheFolderAccessDenied</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-errors-instantiationerrorcode">InstantiationErrorCode</a></span>  
Access to the specified cache folder is denied

<span class="name">persistentMapStorageFolderAccessDenied</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-errors-instantiationerrorcode">InstantiationErrorCode</a></span>  
Access to the specified persistent map storage folder is denied

<span class="name">failedToLockCacheFolder</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-errors-instantiationerrorcode">InstantiationErrorCode</a></span>  
The cache folder for given access key id is locked by other instance of SDKNativeEngine

<span class="name">failedToCreateAnalyticsService</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-errors-instantiationerrorcode">InstantiationErrorCode</a></span>  
Analytics service can not be created

<span class="name">accessKeyContainsIllegalSymbol</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-errors-instantiationerrorcode">InstantiationErrorCode</a></span>  
Access key contains illegal symbols. The below characters are not supported: A. '(single quote) B. "(double quote)

<span class="name">accessKeySecretContainsIllegalSymbol</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-errors-instantiationerrorcode">InstantiationErrorCode</a></span>  
Access key secret contains illegal symbols. The below characters are not supported: A. '(single quote) B. "(double quote)

<span class="name">layerConfigurationMismatch</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-errors-instantiationerrorcode">InstantiationErrorCode</a></span>  
Please check SDKOptions.layerConfiguration against SDK modules configuration.

<span class="name">sdkEngineAlreadyDisposed</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-errors-instantiationerrorcode">InstantiationErrorCode</a></span>  
Instantiation attempt failed because the

    dispose()

method from `SDKNativeEngine` was called already.

</p>

<span class="name">invalidCatalogConfiguration</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-errors-instantiationerrorcode">InstantiationErrorCode</a></span>  
`CatalogConfiguration` contains invalid parameters. Check the corectness of HRNs and versions.

<span class="name">dataFolderAccessDenied</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-core-errors-instantiationerrorcode">InstantiationErrorCode</a></span>  
Access to the specified data folder is denied

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-core-errors-instantiationerrorcode-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-errors-instantiationerrorcode-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-errors-instantiationerrorcode-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-core-errors-instantiationerrorcode-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-errors-instantiationerrorcode-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-core-errors-instantiationerrorcode-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-core-errors-instantiationerrorcode-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-errors-instantiationerrorcode">InstantiationErrorCode</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
