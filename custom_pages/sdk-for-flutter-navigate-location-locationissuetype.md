---
title: "LocationIssueType enum - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationissuetype"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationIssueType.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/location-library-sidebar.html" data-below-sidebar="location/LocationIssueType-enum-sidebar.html">

<div>

# <span class="kind-enum">LocationIssueType</span> enum

</div>

<div class="section desc markdown">

Represents specific issues affecting location retrieval quality, availability, or functionality.

- Issues are detected automatically by the positioning system and reported via LocationIssueListener.
- Multiple issues may be active simultaneously (e.g., both quality degradation and connectivity problems).
- Issues clear automatically when underlying conditions improve (no manual dismissal needed).

</div>

## Values

<span class="name">hdgnssDeviceNotSupported</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationissuetype">LocationIssueType</a></span>  
Device hardware does not support HD GNSS positioning capabilities.

<span class="name">hdgnssOsVersionNotSupported</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationissuetype">LocationIssueType</a></span>  
Operating system version is below minimum required for HD GNSS (Android 12+).

<span class="name">hdgnssConnectionNotAvailable</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationissuetype">LocationIssueType</a></span>  
Network connection to HD GNSS assistance server is unavailable.

<span class="name">hdgnssDegradedMeasurementQuality</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationissuetype">LocationIssueType</a></span>  
Satellite measurement quality is degraded; HD GNSS accuracy level may not be achieved.

<span class="name">hdgnssInsufficientMeasurementQuality</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationissuetype">LocationIssueType</a></span>  
Satellite measurement quality is insufficient to achieve HD GNSS accuracy level.

<span class="name">featureNotLicensed</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationissuetype">LocationIssueType</a></span>  
Requested feature requires a valid license (missing or expired).

<span class="name">featureNotIncluded</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationissuetype">LocationIssueType</a></span>  
Requested feature not available for the used license.

<span class="name">sensorPositioningNotAvailable</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationissuetype">LocationIssueType</a></span>  
Device sensors required for sensor fusion positioning are unavailable.

<span class="name">positionNotFound</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationissuetype">LocationIssueType</a></span>  
Unable to determine position from available positioning sources.

<span class="name">positionNoCellMeasurements</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationissuetype">LocationIssueType</a></span>  
No usable cellular network signal measurements available for positioning.

<span class="name">positionNoWlanMeasurements</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationissuetype">LocationIssueType</a></span>  
No usable Wi-Fi network signal measurements available for positioning.

<span class="name">positionCellScanError</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationissuetype">LocationIssueType</a></span>  
Failed to scan for cellular network signals.

<span class="name">positionWlanScanError</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationissuetype">LocationIssueType</a></span>  
Failed to scan for Wi-Fi network signals.

<span class="name">hdgnssPosExtrapolated</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-location-locationissuetype">LocationIssueType</a></span>  
Hd gnss position was calculated by extrapolation.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-location-locationissuetype-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationissuetype-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationissuetype-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-location-locationissuetype-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationissuetype-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-location-locationissuetype-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-location-locationissuetype-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-location-locationissuetype">LocationIssueType</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
