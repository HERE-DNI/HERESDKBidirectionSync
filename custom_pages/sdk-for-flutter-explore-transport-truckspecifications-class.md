---
title: "TruckSpecifications class - transport library - Dart API"
slug: "sdk-for-flutter-explore-transport-truckspecifications-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="transport/transport-library-sidebar.html" data-below-sidebar="transport/TruckSpecifications-class-sidebar.html">

<div>

# <span class="kind-class">TruckSpecifications</span> class

</div>

<div class="section desc markdown">

Truck specifications contain vehicle related attributes.

Examples: Dimensions, weight, axle count. Only the fields that are set are considered for restriction handling.

</div>

<div class="section">

Annotations  
- @Deprecated("Will be removed in v4.28.0. Use \`TransportSpecification\` instead.")

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-transport-truckspecifications-truckspecifications">TruckSpecifications</a></span><span class="signature">(\<a href="sdk-for-flutter-explore-transport-weightperaxlegroup-class"><span id="sdk-for-flutter-explore-param-grossWeightInKilograms" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">grossWeightInKilograms</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-explore-param-currentWeightInKilograms" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">currentWeightInKilograms</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-explore-param-weightPerAxleInKilograms" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">weightPerAxleInKilograms</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-explore-param-weightPerAxleGroup" class="parameter"><span class="type-annotation">[WeightPerAxleGroup</a>?</span> <span class="parameter-name">weightPerAxleGroup</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-explore-param-heightInCentimeters" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">heightInCentimeters</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-explore-param-widthInCentimeters" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">widthInCentimeters</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-explore-param-lengthInCentimeters" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">lengthInCentimeters</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-explore-param-axleCount" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">axleCount</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-explore-param-trailerCount" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">trailerCount</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-explore-param-truckType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-transport-trucktype" class="deprecated">TruckType</a></span> <span class="parameter-name">truckType</span> = <span class="default-value">TruckType.straight</span>, </span><span id="sdk-for-flutter-explore-param-isTruckLight" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isTruckLight</span> = <span class="default-value">false</span>, </span><span id="sdk-for-flutter-explore-param-payloadCapacityInKilograms" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">payloadCapacityInKilograms</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-explore-param-trailerAxleCount" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">trailerAxleCount</span> = <span class="default-value">null</span></span>\])</span>  
Creates a new instance.

<span class="name"><a href="sdk-for-flutter-explore-transport-truckspecifications-truckspecifications-withdefaults">TruckSpecifications.withDefaults</a></span><span class="signature">()</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-transport-truckspecifications-axlecount">axleCount</a></span> <span class="signature">↔ int?</span>  
Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2. By default, it is not set. Route calculation: When not set, possible axle count restrictions will not be taken into consideration. Rendering `sdk.mapview.TruckProfile`: When set, truck restriction icons for an axle count greater than <a href="sdk-for-flutter-explore-transport-truckspecifications-axlecount">TruckSpecifications.axleCount</a> will not be displayed. When specifying <a href="sdk-for-flutter-explore-transport-truckspecifications-traileraxlecount">TruckSpecifications.trailerAxleCount</a>, then <a href="sdk-for-flutter-explore-transport-truckspecifications-axlecount">TruckSpecifications.axleCount</a> is required and must be greater than <a href="sdk-for-flutter-explore-transport-truckspecifications-traileraxlecount">TruckSpecifications.trailerAxleCount</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-truckspecifications-currentweightinkilograms">currentWeightInKilograms</a></span> <span class="signature">↔ int?</span>  
Current truck weight, including trailers and shipped goods currently loaded, specified in kilograms. The provided value must be greater than or equal to 0. If unspecified, it will default to <a href="sdk-for-flutter-explore-transport-truckspecifications-grossweightinkilograms">TruckSpecifications.grossWeightInKilograms</a>. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-truckspecifications-grossweightinkilograms">grossWeightInKilograms</a></span> <span class="signature">↔ int?</span>  
Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in kilograms. The provided value must be greater than or equal to 0. If unspecified, it will default to <a href="sdk-for-flutter-explore-transport-truckspecifications-currentweightinkilograms">TruckSpecifications.currentWeightInKilograms</a>. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-truckspecifications-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-truckspecifications-heightincentimeters">heightInCentimeters</a></span> <span class="signature">↔ int?</span>  
Truck height in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-truckspecifications-istrucklight">isTruckLight</a></span> <span class="signature">↔ bool</span>  
A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan. The flag should not be set to `true` in other countries than Japan. The flag defaults to `false`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-truckspecifications-lengthincentimeters">lengthInCentimeters</a></span> <span class="signature">↔ int?</span>  
Truck length in centimeters. The provided value must be in the range \[0, 30000\]. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-truckspecifications-payloadcapacityinkilograms">payloadCapacityInKilograms</a></span> <span class="signature">↔ int?</span>  
Allowed payload capacity, including trailers, specified in kilograms. The provided value must be greater then or equal to 0. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-truckspecifications-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-truckspecifications-traileraxlecount">trailerAxleCount</a></span> <span class="signature">↔ int?</span>  
Defines total number of axles across all the trailers attached to the vehicle. This number is included in <a href="sdk-for-flutter-explore-transport-truckspecifications-axlecount">TruckSpecifications.axleCount</a>, hence <a href="sdk-for-flutter-explore-transport-truckspecifications-traileraxlecount">TruckSpecifications.trailerAxleCount</a> must be less than <a href="sdk-for-flutter-explore-transport-truckspecifications-axlecount">TruckSpecifications.axleCount</a> and greater than or equal to 1. <a href="sdk-for-flutter-explore-transport-truckspecifications-axlecount">TruckSpecifications.axleCount</a> and <a href="sdk-for-flutter-explore-transport-truckspecifications-trailercount">TruckSpecifications.trailerCount</a> are required to specify <a href="sdk-for-flutter-explore-transport-truckspecifications-traileraxlecount">TruckSpecifications.trailerAxleCount</a>. By default, it is not set. Note: This parameter is currently used only for the calculation of tolls in regions where it is applicable.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-truckspecifications-trailercount">trailerCount</a></span> <span class="signature">↔ int?</span>  
Defines number of trailers attached to the vehicle. The provided value must be in the range \[0, 255\]. By default, it is not set. When specifying <a href="sdk-for-flutter-explore-transport-truckspecifications-traileraxlecount">TruckSpecifications.trailerAxleCount</a>, then <a href="sdk-for-flutter-explore-transport-truckspecifications-trailercount">TruckSpecifications.trailerCount</a> is required and must be greater than 0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-truckspecifications-trucktype">truckType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-transport-trucktype" class="deprecated">TruckType</a></span>  
Defines the type of truck. By default, it is <a href="sdk-for-flutter-explore-transport-trucktype">TruckType.straight</a>. Rendering `sdk.mapview.TruckProfile`: <a href="sdk-for-flutter-explore-transport-truckspecifications-trucktype">TruckSpecifications.truckType</a> is ignored and has no effect.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-truckspecifications-weightperaxlegroup">weightPerAxleGroup</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-transport-weightperaxlegroup-class">WeightPerAxleGroup</a>?</span>  
Allows specification of axle weights in a more fine-grained way than `weight_per_axle_in_kilograms`. This is relevant in countries with signs and regulations that specify different limits for different axle groups, like the USA and Sweden. By default is not set. **Note:** `weight_per_axle_in_kilograms` and `weight_per_axle_group` are incompatible. When available for your edition, if both attributes are set, during online RoutingEngine an `sdk.routing.RoutingError.INVALID_PARAMETER` error is generated. Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-truckspecifications-weightperaxleinkilograms">weightPerAxleInKilograms</a></span> <span class="signature">↔ int?</span>  
Heaviest weight per axle, regardless of axle type or axle group. It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions. The provided value must be greater or equal to 0. By default, it is not set. **Note:** `weight_per_axle_in_kilograms` and `weight_per_axle_group` are incompatible. When available for your edition, if both attributes are set, during online RoutingEngine an `sdk.routing.RoutingError.INVALID_PARAMETER` error is generated. Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-truckspecifications-widthincentimeters">widthInCentimeters</a></span> <span class="signature">↔ int?</span>  
Truck width in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-transport-truckspecifications-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-truckspecifications-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-transport-truckspecifications-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

