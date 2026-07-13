---
title: "matchingEMobilityServiceProviders property - ChargingStation class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-chargingstation-matchingemobilityserviceproviders"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/ChargingStation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">matchingEMobilityServiceProviders</span> property

</div>

<div class="section multi-line-signature">

List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-nameid-class">NameID</a></span>\></span> <span class="name">matchingEMobilityServiceProviders</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

List of matched E-Mobility Service Providers. Populated only when <a href="sdk-for-flutter-navigate-routing-electricvehicleoptions-evmobilityserviceproviderpreferences">ElectricVehicleOptions.evMobilityServiceProviderPreferences</a> was set. This list reflects the subset of E-Mobility Service Providers supported by the charging station, from the list specified in the request parameter <a href="sdk-for-flutter-navigate-routing-electricvehicleoptions-evmobilityserviceproviderpreferences">ElectricVehicleOptions.evMobilityServiceProviderPreferences</a>. <a href="sdk-for-flutter-navigate-core-nameid-name">NameID.name</a> in each list item reflect to E-Mobility Service Provider name. <a href="sdk-for-flutter-navigate-core-nameid-id">NameID.id</a> in each list item reflect to E-Mobility Service Provider id.

</div>

## Implementation

``` dart
List<NameID> matchingEMobilityServiceProviders;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

