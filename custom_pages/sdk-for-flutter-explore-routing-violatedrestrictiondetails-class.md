---
title: "ViolatedRestrictionDetails class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-violatedrestrictiondetails-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/ViolatedRestrictionDetails-class-sidebar.html">

<div>

# <span class="kind-class">ViolatedRestrictionDetails</span> class

</div>

<div class="section desc markdown">

Optional restriction details, contains additional information depending on the specific violation, zero or more member might be set.

For example, if the vehicle violates the maximum allowed height during the trip, then the member `max_height_in_centimeters` will be set with the maximum allowed height value.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-violatedrestrictiondetails">ViolatedRestrictionDetails</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-forbiddenaxlecount">forbiddenAxleCount</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-core-integerrange-class">IntegerRange</a>?</span>  
The restriction to trucks with axles number within specified range during the trip. This property will be set if the <a href="sdk-for-flutter-explore-transport-vehiclespecification-axlecount">VehicleSpecification.axleCount</a> is within this range.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-forbiddenhazardousgoods">forbiddenHazardousGoods</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-transport-hazardousmaterial">HazardousMaterial</a></span>\></span></span>  
There are two lists for our trip: Hazardous goods restrictions applied during the trip, and the list used for the route calculation provided using <a href="sdk-for-flutter-explore-transport-vehiclespecification-hazardousmaterials">VehicleSpecification.hazardousMaterials</a> from <a href="sdk-for-flutter-explore-transport-transportspecification-vehiclespecification">TransportSpecification.vehicleSpecification</a> from <a href="sdk-for-flutter-explore-routing-routingoptions-transportspecification">RoutingOptions.transportSpecification</a>. This property is the intersection of the two lists.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-forbiddentrailercount">forbiddenTrailerCount</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-core-integerrange-class">IntegerRange</a>?</span>  
Constrains the restriction to trucks with number of trailer within specified range during the trip. This property will be set if the <a href="sdk-for-flutter-explore-transport-vehiclespecification-trailercount">VehicleSpecification.trailerCount</a> is within this range.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-forbiddentruckcategory">forbiddenTruckCategory</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-transport-truckcategory">TruckCategory</a>?</span>  
This property will be set if a restriction applies to the value of <a href="sdk-for-flutter-explore-transport-truckcategory">TruckCategory</a> parameter used for route calculation.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-forbiddentruckroadtypes">forbiddenTruckRoadTypes</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-transport-truckroadtype">TruckRoadType</a></span>\></span></span>  
Contains violated restrictions for truck road types.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-forbiddentrucktype" class="deprecated">forbiddenTruckType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-transport-trucktype" class="deprecated">TruckType</a>?</span>  
This property will be set if a restriction applies to the value of <a href="sdk-for-flutter-explore-transport-trucktype" class="deprecated">TruckType</a> parameter used for route calculation.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxheightincentimeters">maxHeightInCentimeters</a></span> <span class="signature">↔ int?</span>  
Max permitted height during the trip, in centimeters. This property will be set if the <a href="sdk-for-flutter-explore-transport-vehiclespecification-heightincentimeters">VehicleSpecification.heightInCentimeters</a> exceeds this value.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxkingpintorearaxledistanceincentimeters">maxKingpinToRearAxleDistanceInCentimeters</a></span> <span class="signature">↔ int?</span>  
Contains the maximum permitted distance from kingpin to the rear axle in centimeters. This property will be set if the <a href="sdk-for-flutter-explore-transport-vehiclespecification-kingpintorearaxledistanceincentimeters">VehicleSpecification.kingpinToRearAxleDistanceInCentimeters</a> exceeds the specified value.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxlengthincentimeters">maxLengthInCentimeters</a></span> <span class="signature">↔ int?</span>  
Max permitted length during the trip, in centimeters. This property will be set if the <a href="sdk-for-flutter-explore-transport-vehiclespecification-lengthincentimeters">VehicleSpecification.lengthInCentimeters</a> exceeds this value.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxnumberoftires">maxNumberOfTires</a></span> <span class="signature">↔ int?</span>  
Contains the maximum permitted number of tires. This property will be set if the <a href="sdk-for-flutter-explore-transport-vehiclespecification-tirescount">VehicleSpecification.tiresCount</a> exceeds the specified value.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxpayloadcapacityinkilograms">maxPayloadCapacityInKilograms</a></span> <span class="signature">↔ int?</span>  
Max permitted payload capacity during the trip, in kilograms. This property will be set if the <a href="sdk-for-flutter-explore-transport-vehiclespecification-payloadcapacityinkilograms">VehicleSpecification.payloadCapacityInKilograms</a> exceeds this value.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxtunnelcategory">maxTunnelCategory</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-transport-tunnelcategory">TunnelCategory</a>?</span>  
Tunnel category to restrict transport of specific goods during the trip. This property will be set if the <a href="sdk-for-flutter-explore-transport-vehiclespecification-tunnelcategory">VehicleSpecification.tunnelCategory</a> from <a href="sdk-for-flutter-explore-transport-transportspecification-vehiclespecification">TransportSpecification.vehicleSpecification</a> from <a href="sdk-for-flutter-explore-routing-routingoptions-transportspecification">RoutingOptions.transportSpecification</a> exceeds this value.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxweight">maxWeight</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-vehiclerestrictionmaxweight-class">VehicleRestrictionMaxWeight</a>?</span>  
Max permitted weight during the trip, in kilograms, along with the specific type of maximum permitted weight restriction. This property will be set if the <a href="sdk-for-flutter-explore-transport-vehiclespecification-grossweightinkilograms">VehicleSpecification.grossWeightInKilograms</a> parameter used for route calculation exceeds this value.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxweightperaxlegroupinkilograms">maxWeightPerAxleGroupInKilograms</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-maxaxlegroupweight-class">MaxAxleGroupWeight</a>?</span>  
Max permitted weight per axle group during the trip, in kilograms. This property will be set if the <a href="sdk-for-flutter-explore-transport-vehiclespecification-weightperaxlegroup">VehicleSpecification.weightPerAxleGroup</a> exceeds this value.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxweightperaxleinkilograms">maxWeightPerAxleInKilograms</a></span> <span class="signature">↔ int?</span>  
Max permitted weight per axle during the trip, in kilograms. This property will be set if the <a href="sdk-for-flutter-explore-transport-vehiclespecification-weightperaxleinkilograms">VehicleSpecification.weightPerAxleInKilograms</a> exceeds this value.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxwidthincentimeters">maxWidthInCentimeters</a></span> <span class="signature">↔ int?</span>  
Max permitted width during the trip, in centimeters. This property will be set if the <a href="sdk-for-flutter-explore-transport-vehiclespecification-widthincentimeters">VehicleSpecification.widthInCentimeters</a> exceeds this value.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-routingzonereference">routingZoneReference</a></span> <span class="signature">↔ String?</span>  
Contains the restricted routing zone reference This property will be set if the <a href="sdk-for-flutter-explore-routing-avoidanceoptions-zonecategories">AvoidanceOptions.zoneCategories</a> is not empty

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-timerule">timeRule</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-core-timerule-class">TimeRule</a>?</span>  
Time intervals during which restrictions are enforced.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

