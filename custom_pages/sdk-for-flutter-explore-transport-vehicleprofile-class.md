---
title: "VehicleProfile class - transport library - Dart API"
slug: "sdk-for-flutter-explore-transport-vehicleprofile-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="transport/transport-library-sidebar.html" data-below-sidebar="transport/VehicleProfile-class-sidebar.html">

<div>

# <span class="kind-class">VehicleProfile</span> class

</div>

<div class="section desc markdown">

A vehicle profile describes the vehicle being used with the HSDK.

The profile is planned to be used as single source of information describing the vehicle.

Current modules that use this profile:

- Navigation: Tracking mode for truck related vehicle restrictions.

**Note:** This is a beta release of this vehicle profile, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases or even become unsupported, without a deprecation process.

</div>

<div class="section">

Annotations  
- @Deprecated("Will be removed in v4.28.0. Use \`sdk.transport.TransportSpecification\` instead.")

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-transport-vehicleprofile-vehicleprofile">VehicleProfile</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-vehicleType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-transport-vehicletype" class="deprecated">VehicleType</a></span> <span class="parameter-name">vehicleType</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-transport-vehicleprofile-axlecount">axleCount</a></span> <span class="signature">↔ int?</span>  
Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2. When not set, possible axle count restrictions will not be taken into consideration for route calculation. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-vehicleprofile-grossweightinkilograms">grossWeightInKilograms</a></span> <span class="signature">↔ int?</span>  
Vehicle weight including trailers and shipped goods in kilograms. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-vehicleprofile-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-vehicleprofile-hazardousmaterials">hazardousMaterials</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-transport-hazardousmaterial">HazardousMaterial</a></span>\></span></span>  
Specifies a list of hazardous materials shipped in the vehicle. Refer to <a href="sdk-for-flutter-explore-transport-hazardousmaterial">HazardousMaterial</a> for the available options.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-vehicleprofile-heightincentimeters">heightInCentimeters</a></span> <span class="signature">↔ int?</span>  
Vehicle height in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-vehicleprofile-lengthincentimeters">lengthInCentimeters</a></span> <span class="signature">↔ int?</span>  
Vehicle length in centimeters. The provided value must be in the range \[0, 30000\]. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-vehicleprofile-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-vehicleprofile-trailercount">trailerCount</a></span> <span class="signature">↔ int</span>  
Defines number of trailers attached to the vehicle. The provided value must be in the range \[0, 255\]. When not set, possible trailer count restrictions will not be taken into consideration for route calculation. By default, it is 0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-vehicleprofile-truckcategory">truckCategory</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-transport-truckcategory">TruckCategory</a>?</span>  
Defines the truck category. Only used when the <a href="sdk-for-flutter-explore-transport-vehicleprofile-vehicletype">VehicleProfile.vehicleType</a> is <a href="sdk-for-flutter-explore-transport-vehicletype">VehicleType.truck</a> By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-vehicleprofile-tunnelcategory">tunnelCategory</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-transport-tunnelcategory">TunnelCategory</a>?</span>  
Specifies the tunnel categories to restrict certain route links. The route will pass only through tunnels of a less strict category. Refer to <a href="sdk-for-flutter-explore-transport-tunnelcategory">TunnelCategory</a> for the available options.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-vehicleprofile-vehicletype">vehicleType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-transport-vehicletype" class="deprecated">VehicleType</a></span>  
Defines the vehicle type.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-vehicleprofile-weightperaxleinkilograms">weightPerAxleInKilograms</a></span> <span class="signature">↔ int?</span>  
Vehicle weight per axle in kilograms. The provided value must be greater or equal to 0. When not set, possible weight per axle restrictions will not be taken into consideration for route calculation. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-vehicleprofile-widthincentimeters">widthInCentimeters</a></span> <span class="signature">↔ int?</span>  
Vehicle width in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-transport-vehicleprofile-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-vehicleprofile-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-transport-vehicleprofile-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

