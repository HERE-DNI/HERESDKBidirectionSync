---
title: "trackingTransportSpecification property - NavigatorInterface class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-trackingtransportspecification"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/NavigatorInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">trackingTransportSpecification</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a>?</span> <span class="name">trackingTransportSpecification</span>

</div>

<div class="section desc markdown">

Defines the transport specification for the <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>, when no route is present. Properly setting the transport specification optimizes the navigation experience, and improves resource consumption. An <a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a> must have the <a href="sdk-for-flutter-navigate-transport-transportspecification-transportmode">TransportSpecification.transportMode</a> set. A transport specification can have several parameters defined such as <a href="sdk-for-flutter-navigate-transport-vehiclespecification-lengthincentimeters">VehicleSpecification.lengthInCentimeters</a> defined in <a href="sdk-for-flutter-navigate-transport-transportspecification-vehiclespecification">TransportSpecification.vehicleSpecification</a> to set the source of information describing the vehicle. By default the <a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a> will have the transport mode set to <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.car</a>.

Currently used members of <a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a>

- <a href="sdk-for-flutter-navigate-transport-transportspecification-transportmode">TransportSpecification.transportMode</a>: Sets the transport mode.
- From <a href="sdk-for-flutter-navigate-transport-transportspecification-vehiclespecification">TransportSpecification.vehicleSpecification</a>:
  - <a href="sdk-for-flutter-navigate-transport-vehiclespecification-grossweightinkilograms">VehicleSpecification.grossWeightInKilograms</a>: Required for truck related speed information.
  - <a href="sdk-for-flutter-navigate-transport-vehiclespecification-heightincentimeters">VehicleSpecification.heightInCentimeters</a>: Required for truck related speed information.
  - <a href="sdk-for-flutter-navigate-transport-vehiclespecification-widthincentimeters">VehicleSpecification.widthInCentimeters</a>: Additional truck definition for more specific truck speed information.
  - <a href="sdk-for-flutter-navigate-transport-vehiclespecification-lengthincentimeters">VehicleSpecification.lengthInCentimeters</a>: Additional truck definition for more specific truck speed information. Gets the transport specification for the <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>, when no route is present.

</div>

## Implementation

``` dart
TransportSpecification? get trackingTransportSpecification;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">trackingTransportSpecification=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-trackingTransportSpecification-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a>?</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Defines the transport specification for the <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>, when no route is present. Properly setting the transport specification optimizes the navigation experience, and improves resource consumption. An <a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a> must have the <a href="sdk-for-flutter-navigate-transport-transportspecification-transportmode">TransportSpecification.transportMode</a> set. A transport specification can have several parameters defined such as <a href="sdk-for-flutter-navigate-transport-vehiclespecification-lengthincentimeters">VehicleSpecification.lengthInCentimeters</a> defined in <a href="sdk-for-flutter-navigate-transport-transportspecification-vehiclespecification">TransportSpecification.vehicleSpecification</a> to set the source of information describing the vehicle. By default the <a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a> will have the transport mode set to <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.car</a>.

Currently used members of <a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a>

- <a href="sdk-for-flutter-navigate-transport-transportspecification-transportmode">TransportSpecification.transportMode</a>: Sets the transport mode.
- From <a href="sdk-for-flutter-navigate-transport-transportspecification-vehiclespecification">TransportSpecification.vehicleSpecification</a>:
  - <a href="sdk-for-flutter-navigate-transport-vehiclespecification-grossweightinkilograms">VehicleSpecification.grossWeightInKilograms</a>: Required for truck related speed information.
  - <a href="sdk-for-flutter-navigate-transport-vehiclespecification-heightincentimeters">VehicleSpecification.heightInCentimeters</a>: Required for truck related speed information.
  - <a href="sdk-for-flutter-navigate-transport-vehiclespecification-widthincentimeters">VehicleSpecification.widthInCentimeters</a>: Additional truck definition for more specific truck speed information.
  - <a href="sdk-for-flutter-navigate-transport-vehiclespecification-lengthincentimeters">VehicleSpecification.lengthInCentimeters</a>: Additional truck definition for more specific truck speed information. Sets the transport specification for the <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>, when no route is present.

</div>

## Implementation

``` dart
set trackingTransportSpecification(TransportSpecification? value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

