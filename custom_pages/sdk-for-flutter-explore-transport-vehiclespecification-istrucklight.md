---
title: "isTruckLight property - VehicleSpecification class - transport library - Dart API"
slug: "sdk-for-flutter-explore-transport-vehiclespecification-istrucklight"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isTruckLight.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="transport/VehicleSpecification-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">isTruckLight</span> property

</div>

<div class="section multi-line-signature">

bool <span class="name">isTruckLight</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan. The flag should not be set to `true` in other countries than Japan. Defaults to `false`.

A light truck exempts from many legal restrictions for normal trucks in Japan, for example, which streets the vehicle can access, which access restrictions apply, and which speed limits are applicable. Restrictions related to the dimensions of the truck, or its cargo may still apply and setting this flag will not always overwrite these settings. Make sure to not exceed the specifications that classify a truck as light.

In Japan, for light trucks the same restrictions apply as for cars. Therefore, when the flag is set to `true`, you will get, for example, the same speed limits as for cars. Make sure to set the flag only to `true`, when a vehicle matches the classification for light trucks according to the vehicle regulations in Japan.

When on `MapContentSettings`, then this flag will be ignored and has no effect.

**Notes:**

- This flag and the concept of light trucks are supported only in Japan as beta and are considered to be experimental in other regions. Therefore, for now, it is recommended to use this flag only in Japan.
- Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.
- Supported only in <a href="sdk-for-flutter-explore-transport-transportmode">TransportMode.truck</a> transport mode.

</div>

## Implementation

``` dart
bool isTruckLight;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
