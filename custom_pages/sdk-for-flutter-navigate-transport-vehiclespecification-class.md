---
title: "VehicleSpecification class - transport library - Dart API"
slug: "sdk-for-flutter-navigate-transport-vehiclespecification-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="transport/transport-library-sidebar.html" data-below-sidebar="transport/VehicleSpecification-class-sidebar.html">

<div>

# <span class="kind-class">VehicleSpecification</span> class

</div>

<div class="section desc markdown">

Contains vehicle related attributes.

Examples: Dimensions, weight, axle count. Only the fields that are set are considered for restriction handling.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-vehiclespecification">VehicleSpecification</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-axlecount">axleCount</a></span> <span class="signature">↔ int?</span>  
Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2. By default, it is not set. Route calculation: When not set, possible axle count restrictions will not be taken into consideration. Rendering: When set, truck restriction icons for an axle count greater than <a href="sdk-for-flutter-navigate-transport-vehiclespecification-axlecount">VehicleSpecification.axleCount</a> will not be displayed. When specifying <a href="sdk-for-flutter-navigate-transport-vehiclespecification-traileraxlecount">VehicleSpecification.trailerAxleCount</a>, then <a href="sdk-for-flutter-navigate-transport-vehiclespecification-axlecount">VehicleSpecification.axleCount</a> is required and must be greater than <a href="sdk-for-flutter-navigate-transport-vehiclespecification-traileraxlecount">VehicleSpecification.trailerAxleCount</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-currentweightinkilograms">currentWeightInKilograms</a></span> <span class="signature">↔ int?</span>  
Current truck weight, including trailers and shipped goods currently loaded, specified in kilograms. The provided value must be greater than or equal to 0. If unspecified, it will default to <a href="sdk-for-flutter-navigate-transport-vehiclespecification-grossweightinkilograms">VehicleSpecification.grossWeightInKilograms</a>. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-emptyweightinkilograms">emptyWeightInKilograms</a></span> <span class="signature">↔ int?</span>  
Empty weight of the vehicle without any load, excluding trailers, specified in kilograms. The provided value must be greater than or equal to 0. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-enginesizeincubiccentimeters">engineSizeInCubicCentimeters</a></span> <span class="signature">↔ int?</span>  
Engine size of the scooter in cubic centimeters. Shouldn't be less than 1 or greater than 65535. Default value is `null`, which means the scooter route calculation ignores all engine size limits on the road.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-grossweightinkilograms">grossWeightInKilograms</a></span> <span class="signature">↔ int?</span>  
Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in kilograms. The provided value must be greater than or equal to 0. If unspecified, it will default to <a href="sdk-for-flutter-navigate-transport-vehiclespecification-currentweightinkilograms">VehicleSpecification.currentWeightInKilograms</a>. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-hazardousmaterials">hazardousMaterials</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-transport-hazardousmaterial">HazardousMaterial</a></span>\></span></span>  
Specifies a list of hazardous materials shipped in the vehicle. Refer to <a href="sdk-for-flutter-navigate-transport-hazardousmaterial">HazardousMaterial</a> for the available options. By default, it is an empty list.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-heightincentimeters">heightInCentimeters</a></span> <span class="signature">↔ int?</span>  
Vehicle height in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-iscommercial">isCommercial</a></span> <span class="signature">↔ bool</span>  
Specifies whether the vehicle is a commercial or a non-commercial vehicle. Defaults to `false`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-istrucklight">isTruckLight</a></span> <span class="signature">↔ bool</span>  
A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan. The flag should not be set to `true` in other countries than Japan. Defaults to `false`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-kingpintorearaxledistanceincentimeters">kingpinToRearAxleDistanceInCentimeters</a></span> <span class="signature">↔ int?</span>  
Defines the kingpin to rear axle distance, in centimeters.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-lastcharacteroflicenseplate">lastCharacterOfLicensePlate</a></span> <span class="signature">↔ String?</span>  
Last character of license plate in String format. This value can be used to evaluate restrictions in environmental zones. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-lengthincentimeters">lengthInCentimeters</a></span> <span class="signature">↔ int?</span>  
Vehicle length in centimeters. The provided value must be in the range \[0, 30000\]. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-occupancy">occupancy</a></span> <span class="signature">↔ int?</span>  
Specifies the number of occupants in the vehicle, including driver, can affect the vehicle's ability to use HOV/carpool restricted lanes. Should not be less than 1 or greater than 255. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-payloadcapacityinkilograms">payloadCapacityInKilograms</a></span> <span class="signature">↔ int?</span>  
Allowed payload capacity, including trailers, specified in kilograms. The provided value must be greater then or equal to 0. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-tirescount">tiresCount</a></span> <span class="signature">↔ int?</span>  
The total number of tires the vehicle has, i.e., the tires on the base vehicle and any attached trailers. By default, it is not set. Otherwise it is guaranteed to be in the range \[1, 255\].

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-traileraxlecount">trailerAxleCount</a></span> <span class="signature">↔ int?</span>  
Defines total number of axles across all the trailers attached to the vehicle. This number is included in <a href="sdk-for-flutter-navigate-transport-vehiclespecification-axlecount">VehicleSpecification.axleCount</a>, hence <a href="sdk-for-flutter-navigate-transport-vehiclespecification-traileraxlecount">VehicleSpecification.trailerAxleCount</a> must be less than <a href="sdk-for-flutter-navigate-transport-vehiclespecification-axlecount">VehicleSpecification.axleCount</a> and greater than or equal to 1. <a href="sdk-for-flutter-navigate-transport-vehiclespecification-axlecount">VehicleSpecification.axleCount</a> and <a href="sdk-for-flutter-navigate-transport-vehiclespecification-trailercount">VehicleSpecification.trailerCount</a> are required to specify <a href="sdk-for-flutter-navigate-transport-vehiclespecification-traileraxlecount">VehicleSpecification.trailerAxleCount</a>. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-trailercount">trailerCount</a></span> <span class="signature">↔ int?</span>  
Defines number of trailers attached to the vehicle. The provided value must be in the range \[0, 255\]. By default, it is not set. When specifying <a href="sdk-for-flutter-navigate-transport-vehiclespecification-traileraxlecount">VehicleSpecification.trailerAxleCount</a>, then <a href="sdk-for-flutter-navigate-transport-vehiclespecification-trailercount">VehicleSpecification.trailerCount</a> is required and must be greater than 0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-truckcategory">truckCategory</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-transport-truckcategory">TruckCategory</a>?</span>  
Defines the truck category. By default, it is not set. Rendering: <a href="sdk-for-flutter-navigate-transport-vehiclespecification-truckcategory">VehicleSpecification.truckCategory</a> is ignored and has no effect.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-trucktype" class="deprecated">truckType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-transport-trucktype" class="deprecated">TruckType</a></span>  
Will be replaced with `truckCategory` when the `TruckSpecification` will be replaced by `VehicleSpecification`. Defines the type of truck. Defaults to <a href="sdk-for-flutter-navigate-transport-trucktype">TruckType.straight</a>. Rendering `sdk.mapview.TruckProfile`: <a href="sdk-for-flutter-navigate-transport-vehiclespecification-trucktype" class="deprecated">VehicleSpecification.truckType</a> is ignored and has no effect.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-tunnelcategory">tunnelCategory</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory</a>?</span>  
Specifies the tunnel categories to restrict certain route links. The route will pass only through tunnels of a less strict category. Refer to <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory</a> for the available options. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-weightperaxlegroup">weightPerAxleGroup</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-transport-weightperaxlegroup-class">WeightPerAxleGroup</a>?</span>  
Allows specification of axle weights in a more fine-grained way than <a href="sdk-for-flutter-navigate-transport-vehiclespecification-weightperaxleinkilograms">VehicleSpecification.weightPerAxleInKilograms</a>. This is relevant in countries with signs and regulations that specify different limits for different axle groups, like the USA and Sweden. By default is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-weightperaxleinkilograms">weightPerAxleInKilograms</a></span> <span class="signature">↔ int?</span>  
Heaviest weight per axle, regardless of axle type or axle group. It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions. The provided value must be greater or equal to 0. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-widthincentimeters">widthInCentimeters</a></span> <span class="signature">↔ int?</span>  
Vehicle width in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclespecification-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

