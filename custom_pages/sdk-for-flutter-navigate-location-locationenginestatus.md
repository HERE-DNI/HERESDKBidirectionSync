---
title: "LocationEngineStatus enum - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationenginestatus"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationEngineStatus.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/location-library-sidebar.html" data-below-sidebar="location/LocationEngineStatus-enum-sidebar.html">

<div>

# <span class="kind-enum">LocationEngineStatus</span> enum

</div>

<div class="section desc markdown">

Indicates the status of the LocationEngine.

</div>

## Values

<span class="name">engineStarted</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span>  
LocationEngine successfully started.

<span class="name">alreadyStarted</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span>  
Tried to start LocationEngine that is already started.

<span class="name">engineStopped</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span>  
LocationEngine has been stopped.

<span class="name">startFailed</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span>  
Start failed due to an internal error.

<span class="name">userConsentNotHandled</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span>  
User consent has not been handled yet.

<span class="name">missingPermissions</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span>  
Missing one or more user permissions.

<span class="name">authenticationFailed</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span>  
Authentication failed. Check your credentials.

<span class="name">notSupported</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span>  
Request is not supported.

<span class="name">notAllowed</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span>  
Request is not supported in current region.

<span class="name">notReady</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span>  
Engine is not ready for the requested action.

<span class="name">locationServicesDisabled</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span>  
Location services are disabled in the system settings.

<span class="name">privacyNoticeUnconfirmed</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span>  
Method confirmHEREPrivacyNoticeInclusion() (or alternatively confirmHEREPrivacyNoticeException()) was not called before starting the `LocationEngine` or HERE privacy notice exception was not permitted.

<span class="name">ok</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span>  
Requested operation succeeded.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginestatus-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginestatus-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginestatus-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginestatus-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginestatus-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginestatus-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginestatus-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
