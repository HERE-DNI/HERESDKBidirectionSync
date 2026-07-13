---
title: "lastCharacterOfLicensePlate property - BusOptions class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-busoptions-lastcharacteroflicenseplate"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lastCharacterOfLicensePlate.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/BusOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">lastCharacterOfLicensePlate</span> property

</div>

<div class="section multi-line-signature">

String? <span class="name">lastCharacterOfLicensePlate</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Specifies the last character of a vehicle's license plate, typically used to evaluate traffic restrictions in certain environmental or low-emission zones. In cities like Bogotá, Mexico City, or Jakarta, specific license plate digits may be restricted on certain days or in certain areas to reduce congestion and emissions. When this value is provided, the HERE SDK considers it during route calculation to avoid roads or areas where your vehicle may be restricted based on local regulations. Example usage: "7", when the license plate of a vehicle looks like "B-ET-182487".

If this value is not set, such license plate-based restrictions are ignored, and routing is performed without considering them.

</div>

## Implementation

``` dart
String? lastCharacterOfLicensePlate;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
