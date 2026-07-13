---
title: "vehicleTypesFilter property - RoadSignWarningOptions class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-roadsignwarningoptions-vehicletypesfilter"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/RoadSignWarningOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">vehicleTypesFilter</span> property

</div>

<div class="section multi-line-signature">

List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-roadsignvehicletype">RoadSignVehicleType</a></span>\></span> <span class="name">vehicleTypesFilter</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The list of road sign vehicle types for which a warning will be given. If the list is empty, road signs are not filtered by vehicle type, which means that you get road sign warnings for all vehicle types.

**Example:** For a filter that contains only bus and trucks you will only receive specific road sign warnings for bus and trucks - you will not get signs for the other types, such as heavy trucks or motorhomes. Furthermore, you will *not* get any signs that are generally applicable for all vehicles. For example, you cannot set a filter that allows to get signs for trucks *and* cars. If you want to get signs for standard vehicles like cars, then the only option is to set an empty list as filter.

</div>

## Implementation

``` dart
List<RoadSignVehicleType> vehicleTypesFilter;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

