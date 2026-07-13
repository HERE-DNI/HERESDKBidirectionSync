---
title: "TruckSpecifications constructor - TruckSpecifications - transport library - Dart API"
slug: "sdk-for-flutter-navigate-transport-truckspecifications-truckspecifications"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TruckSpecifications.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="transport/TruckSpecifications-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">TruckSpecifications</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">TruckSpecifications</span>(<wbr></wbr>\<a href="sdk-for-flutter-navigate-transport-weightperaxlegroup-class">

1.  <span id="sdk-for-flutter-navigate-param-grossWeightInKilograms" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">grossWeightInKilograms</span> = <span class="default-value">null</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-currentWeightInKilograms" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">currentWeightInKilograms</span> = <span class="default-value">null</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-weightPerAxleInKilograms" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">weightPerAxleInKilograms</span> = <span class="default-value">null</span>, </span>
4.  <span id="sdk-for-flutter-navigate-param-weightPerAxleGroup" class="parameter"><span class="type-annotation">[WeightPerAxleGroup</a>?</span> <span class="parameter-name">weightPerAxleGroup</span> = <span class="default-value">null</span>, </span>
5.  <span id="sdk-for-flutter-navigate-param-heightInCentimeters" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">heightInCentimeters</span> = <span class="default-value">null</span>, </span>
6.  <span id="sdk-for-flutter-navigate-param-widthInCentimeters" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">widthInCentimeters</span> = <span class="default-value">null</span>, </span>
7.  <span id="sdk-for-flutter-navigate-param-lengthInCentimeters" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">lengthInCentimeters</span> = <span class="default-value">null</span>, </span>
8.  <span id="sdk-for-flutter-navigate-param-axleCount" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">axleCount</span> = <span class="default-value">null</span>, </span>
9.  <span id="sdk-for-flutter-navigate-param-trailerCount" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">trailerCount</span> = <span class="default-value">null</span>, </span>
10. <span id="sdk-for-flutter-navigate-param-truckType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-trucktype" class="deprecated">TruckType</a></span> <span class="parameter-name">truckType</span> = <span class="default-value">TruckType.straight</span>, </span>
11. <span id="sdk-for-flutter-navigate-param-isTruckLight" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isTruckLight</span> = <span class="default-value">false</span>, </span>
12. <span id="sdk-for-flutter-navigate-param-payloadCapacityInKilograms" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">payloadCapacityInKilograms</span> = <span class="default-value">null</span>, </span>
13. <span id="sdk-for-flutter-navigate-param-trailerAxleCount" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">trailerAxleCount</span> = <span class="default-value">null</span>, </span>

\])

</div>

<div class="section desc markdown">

Creates a new instance.

- `grossWeightInKilograms` Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in kilograms. The provided value must be greater than or equal to 0. If unspecified, it will default to <a href="sdk-for-flutter-navigate-transport-truckspecifications-currentweightinkilograms">TruckSpecifications.currentWeightInKilograms</a>. By default, it is not set.
- `currentWeightInKilograms` Current truck weight, including trailers and shipped goods currently loaded, specified in kilograms. The provided value must be greater than or equal to 0. If unspecified, it will default to <a href="sdk-for-flutter-navigate-transport-truckspecifications-grossweightinkilograms">TruckSpecifications.grossWeightInKilograms</a>. By default, it is not set.
- `weightPerAxleInKilograms` Heaviest weight per axle, regardless of axle type or axle group. It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions. The provided value must be greater or equal to 0. By default, it is not set. **Note:** `weight_per_axle_in_kilograms` and `weight_per_axle_group` are incompatible. When available for your edition, if both attributes are set, during online RoutingEngine an `sdk.routing.RoutingError.INVALID_PARAMETER` error is generated. Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.
- `weightPerAxleGroup` Allows specification of axle weights in a more fine-grained way than `weight_per_axle_in_kilograms`. This is relevant in countries with signs and regulations that specify different limits for different axle groups, like the USA and Sweden. By default is not set. **Note:** `weight_per_axle_in_kilograms` and `weight_per_axle_group` are incompatible. When available for your edition, if both attributes are set, during online RoutingEngine an `sdk.routing.RoutingError.INVALID_PARAMETER` error is generated. Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.
- `heightInCentimeters` Truck height in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.
- `widthInCentimeters` Truck width in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.
- `lengthInCentimeters` Truck length in centimeters. The provided value must be in the range \[0, 30000\]. By default, it is not set.
- `axleCount` Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2. By default, it is not set. Route calculation: When not set, possible axle count restrictions will not be taken into consideration. Rendering `sdk.mapview.TruckProfile`: When set, truck restriction icons for an axle count greater than <a href="sdk-for-flutter-navigate-transport-truckspecifications-axlecount">TruckSpecifications.axleCount</a> will not be displayed. When specifying <a href="sdk-for-flutter-navigate-transport-truckspecifications-traileraxlecount">TruckSpecifications.trailerAxleCount</a>, then <a href="sdk-for-flutter-navigate-transport-truckspecifications-axlecount">TruckSpecifications.axleCount</a> is required and must be greater than <a href="sdk-for-flutter-navigate-transport-truckspecifications-traileraxlecount">TruckSpecifications.trailerAxleCount</a>.
- `trailerCount` Defines number of trailers attached to the vehicle. The provided value must be in the range \[0, 255\]. By default, it is not set. When specifying <a href="sdk-for-flutter-navigate-transport-truckspecifications-traileraxlecount">TruckSpecifications.trailerAxleCount</a>, then <a href="sdk-for-flutter-navigate-transport-truckspecifications-trailercount">TruckSpecifications.trailerCount</a> is required and must be greater than 0.
- `truckType` Defines the type of truck. By default, it is <a href="sdk-for-flutter-navigate-transport-trucktype">TruckType.straight</a>. Rendering `sdk.mapview.TruckProfile`: <a href="sdk-for-flutter-navigate-transport-truckspecifications-trucktype">TruckSpecifications.truckType</a> is ignored and has no effect.
- `isTruckLight` A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan. The flag should not be set to `true` in other countries than Japan. The flag defaults to `false`.

A light truck exempts from many legal restrictions for normal trucks in Japan, for example, which streets the vehicle can access, which access restrictions apply, and which speed limits are applicable. Restrictions related to the dimensions of the truck, or its cargo may still apply and setting this flag will not always overwrite these settings: Make sure to not exceed the specifications that classify a truck as light.

In Japan, for light trucks the same restrictions apply as for cars. Therefore, when the flag is set to true, you will get, for example, the same speed limits as for cars. Make sure to set the flag only to true, when a vehicle matches the classification for light trucks according to the vehicle regulations in Japan.

When `TruckSpecifications` are set as part of `MapContentSettings`, then this flag will be ignored and has no effect.

**Note:** This flag and the concept of light trucks are supported only in Japan as beta and are considered to be experimental in other regions. Therefore, for now, it is recommended to use this flag only in Japan. Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases with a deprecation process.

- `payloadCapacityInKilograms` Allowed payload capacity, including trailers, specified in kilograms. The provided value must be greater then or equal to 0. By default, it is not set.
- `trailerAxleCount` Defines total number of axles across all the trailers attached to the vehicle. This number is included in <a href="sdk-for-flutter-navigate-transport-truckspecifications-axlecount">TruckSpecifications.axleCount</a>, hence <a href="sdk-for-flutter-navigate-transport-truckspecifications-traileraxlecount">TruckSpecifications.trailerAxleCount</a> must be less than <a href="sdk-for-flutter-navigate-transport-truckspecifications-axlecount">TruckSpecifications.axleCount</a> and greater than or equal to 1. <a href="sdk-for-flutter-navigate-transport-truckspecifications-axlecount">TruckSpecifications.axleCount</a> and <a href="sdk-for-flutter-navigate-transport-truckspecifications-trailercount">TruckSpecifications.trailerCount</a> are required to specify <a href="sdk-for-flutter-navigate-transport-truckspecifications-traileraxlecount">TruckSpecifications.trailerAxleCount</a>. By default, it is not set. Note: This parameter is currently used only for the calculation of tolls in regions where it is applicable.

</div>

## Implementation

``` dart
TruckSpecifications([int? grossWeightInKilograms = null, int? currentWeightInKilograms = null, int? weightPerAxleInKilograms = null, WeightPerAxleGroup? weightPerAxleGroup = null, int? heightInCentimeters = null, int? widthInCentimeters = null, int? lengthInCentimeters = null, int? axleCount = null, int? trailerCount = null, TruckType truckType = TruckType.straight, bool isTruckLight = false, int? payloadCapacityInKilograms = null, int? trailerAxleCount = null])
  : grossWeightInKilograms = grossWeightInKilograms, currentWeightInKilograms = currentWeightInKilograms, weightPerAxleInKilograms = weightPerAxleInKilograms, weightPerAxleGroup = weightPerAxleGroup ?? null, heightInCentimeters = heightInCentimeters, widthInCentimeters = widthInCentimeters, lengthInCentimeters = lengthInCentimeters, axleCount = axleCount, trailerCount = trailerCount, truckType = truckType, isTruckLight = isTruckLight, payloadCapacityInKilograms = payloadCapacityInKilograms, trailerAxleCount = trailerAxleCount;
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
