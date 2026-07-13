---
title: "trackingTransportProfile property - NavigatorInterface class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-trackingtransportprofile"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/NavigatorInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">trackingTransportProfile</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<div>

1.  @Deprecated("Will be removed in v4.28.0. Use \`NavigatorInterface.trackingTransportSpecification\` instead.")

</div>

<span class="returntype"><a href="sdk-for-flutter-navigate-core-transportprofile-class" class="deprecated">TransportProfile</a>?</span> <span class="name deprecated">trackingTransportProfile</span>

</div>

<div class="section desc markdown">

Defines the transport profile for the <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>, when no route is present. Properly setting the transport profile optimizes the navigation experience, and improves resource consumption. For example, a <a href="sdk-for-flutter-navigate-core-transportprofile-class" class="deprecated">TransportProfile</a> can be defined with a <a href="sdk-for-flutter-navigate-transport-vehicleprofile-class" class="deprecated">VehicleProfile</a>. A vehicle profile can have several parameters such as <a href="sdk-for-flutter-navigate-transport-vehicletype" class="deprecated">VehicleType</a> to set the source of information describing the vehicle. The default is a <a href="sdk-for-flutter-navigate-transport-vehicletype">VehicleType.car</a> profile.

Currently used members of <a href="sdk-for-flutter-navigate-core-transportprofile-class" class="deprecated">TransportProfile</a>

- <a href="sdk-for-flutter-navigate-transport-vehicletype" class="deprecated">VehicleType</a>: Sets the transport mode.
- From `vehicleProfile`:
  - `grossWeightInKilograms`: Required for truck related speed information.
  - `heightInCentimeters`: Required for truck related speed information.
  - `widthInCentimeters`: Additional truck definition for more specific truck speed information.
  - `lengthInCentimeters`: Additional truck definition for more specific truck speed information. Gets the transport profile for the <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>, when no route is present.

</div>

## Implementation

``` dart
@Deprecated("Will be removed in v4.28.0. Use `NavigatorInterface.trackingTransportSpecification` instead.")
TransportProfile? get trackingTransportProfile;
```

</pre>

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<div>

1.  @Deprecated("Will be removed in v4.28.0. Use \`NavigatorInterface.trackingTransportSpecification\` instead.")

</div>

<span class="returntype">void</span> <span class="name deprecated">trackingTransportProfile=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-trackingTransportProfile-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-transportprofile-class" class="deprecated">TransportProfile</a>?</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Defines the transport profile for the <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>, when no route is present. Properly setting the transport profile optimizes the navigation experience, and improves resource consumption. For example, a <a href="sdk-for-flutter-navigate-core-transportprofile-class" class="deprecated">TransportProfile</a> can be defined with a <a href="sdk-for-flutter-navigate-transport-vehicleprofile-class" class="deprecated">VehicleProfile</a>. A vehicle profile can have several parameters such as <a href="sdk-for-flutter-navigate-transport-vehicletype" class="deprecated">VehicleType</a> to set the source of information describing the vehicle. The default is a <a href="sdk-for-flutter-navigate-transport-vehicletype">VehicleType.car</a> profile.

Currently used members of <a href="sdk-for-flutter-navigate-core-transportprofile-class" class="deprecated">TransportProfile</a>

- <a href="sdk-for-flutter-navigate-transport-vehicletype" class="deprecated">VehicleType</a>: Sets the transport mode.
- From `vehicleProfile`:
  - `grossWeightInKilograms`: Required for truck related speed information.
  - `heightInCentimeters`: Required for truck related speed information.
  - `widthInCentimeters`: Additional truck definition for more specific truck speed information.
  - `lengthInCentimeters`: Additional truck definition for more specific truck speed information. Sets the transport profile for the <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>, when no route is present.

</div>

## Implementation

``` dart
@Deprecated("Will be removed in v4.28.0. Use `NavigatorInterface.trackingTransportSpecification` instead.")
set trackingTransportProfile(TransportProfile? value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

