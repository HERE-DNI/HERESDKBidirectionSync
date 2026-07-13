---
title: "PhysicalConsumptionModel class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-physicalconsumptionmodel-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/PhysicalConsumptionModel-class-sidebar.html">

<div>

# <span class="kind-class">PhysicalConsumptionModel</span> class

</div>

<div class="section desc markdown">

Defines the physical consumption model for electric vehicles, using vehicle-specific parameters to calculate energy consumption along a route.

**Note:** <a href="sdk-for-flutter-navigate-transport-vehiclespecification-currentweightinkilograms">VehicleSpecification.currentWeightInKilograms</a> must be set. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-physicalconsumptionmodel-physicalconsumptionmodel">PhysicalConsumptionModel</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-physicalconsumptionmodel-airdragcoefficient">airDragCoefficient</a></span> <span class="signature">↔ double</span>  
The drag coefficient of an vehicle defines the way the vehicle is expected to pass through the surrounding air. More streamlined vehicles are more aerodynamic and therefore have smaller drag coefficient.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-physicalconsumptionmodel-auxiliarypowerconsumptioninwatts">auxiliaryPowerConsumptionInWatts</a></span> <span class="signature">↔ double</span>  
Power (in W) consumed by the vehicle's auxiliary systems (for example, air conditioning, lights).

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-physicalconsumptionmodel-drivetrainefficiency">driveTrainEfficiency</a></span> <span class="signature">↔ double</span>  
The proportion of the energy drawn from the battery that is used to move the vehicle. (This is to factor in energy losses through heat in the motors, for example.) Supported range from 0 to 1

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-physicalconsumptionmodel-frontalareainsquaremeters">frontalAreaInSquareMeters</a></span> <span class="signature">↔ double</span>  
Frontal area represents the total cross section area of the vehicle as viewed from the front, specified in square meters. Physical consumption model is using this value in combination with `airDragCoefficient` to calculate the consumption caused by air resistance. As fallback <a href="sdk-for-flutter-navigate-transport-vehiclespecification-widthincentimeters">VehicleSpecification.widthInCentimeters</a> and <a href="sdk-for-flutter-navigate-transport-vehiclespecification-heightincentimeters">VehicleSpecification.heightInCentimeters</a> are used.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-physicalconsumptionmodel-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-physicalconsumptionmodel-recuperationefficiency">recuperationEfficiency</a></span> <span class="signature">↔ double</span>  
The proportion of the energy gained when braking or going downhill that can be recuperated and restored as battery charge.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-physicalconsumptionmodel-rollingresistancecoefficient">rollingResistanceCoefficient</a></span> <span class="signature">↔ double</span>  
Rolling resistance refers to the resistance experienced by your vehicle tire as it rolls over a surface. The main causes of this resistance are tire deformation, wing drag, and friction with the ground. The coefficient of rolling resistance is a numerical value indicating the severity of this factor.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-physicalconsumptionmodel-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-physicalconsumptionmodel-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-physicalconsumptionmodel-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-physicalconsumptionmodel-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

