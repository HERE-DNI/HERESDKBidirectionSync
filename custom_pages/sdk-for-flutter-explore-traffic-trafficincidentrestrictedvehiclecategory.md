---
title: "TrafficIncidentRestrictedVehicleCategory enum - traffic library - Dart API"
slug: "sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficIncidentRestrictedVehicleCategory.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="traffic/traffic-library-sidebar.html" data-below-sidebar="traffic/TrafficIncidentRestrictedVehicleCategory-enum-sidebar.html">

<div>

# <span class="kind-enum">TrafficIncidentRestrictedVehicleCategory</span> enum

</div>

<div class="section desc markdown">

The vehicle categories that can be restricted.

Note, a vehicle can belong to several categories (e.g. a passenger motor car belongs to <a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory">TrafficIncidentRestrictedVehicleCategory.car</a>, <a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory">TrafficIncidentRestrictedVehicleCategory.motorVehicle</a>, and <a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory">TrafficIncidentRestrictedVehicleCategory.all</a>). A vehicle is restricted if it belongs to the category presented in the map <a href="sdk-for-flutter-explore-traffic-trafficincident-vehiclerestrictions">TrafficIncident.vehicleRestrictions</a> and at least one of the vehicle properties is under the matching <a href="sdk-for-flutter-explore-traffic-trafficincidentvehiclerestriction-class">TrafficIncidentVehicleRestriction</a>.

</div>

## Values

<span class="name">bus</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory">TrafficIncidentRestrictedVehicleCategory</a></span>  
Bus.

<span class="name">car</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory">TrafficIncidentRestrictedVehicleCategory</a></span>  
Car.

<span class="name">heavyGoodsVehicle</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory">TrafficIncidentRestrictedVehicleCategory</a></span>  
Heavy goods vehicle (or large goods vehicle). In the European Union heavy goods vehicle is any truck with a gross combination mass (GCM) of over 3,500 kg.

<span class="name">truck</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory">TrafficIncidentRestrictedVehicleCategory</a></span>  
Truck.

<span class="name">motorcycle</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory">TrafficIncidentRestrictedVehicleCategory</a></span>  
Motorcycle.

<span class="name">motorVehicle</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory">TrafficIncidentRestrictedVehicleCategory</a></span>  
Motor vehicle. Definition: it is a self-propelled vehicle, that does not operate on rails and is used for the transportation of people or cargo.

<span class="name">taxi</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory">TrafficIncidentRestrictedVehicleCategory</a></span>  
Taxi.

<span class="name">train</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory">TrafficIncidentRestrictedVehicleCategory</a></span>  
Train.

<span class="name">transportingAbnormalSizeLoad</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory">TrafficIncidentRestrictedVehicleCategory</a></span>  
Transporting an abnormal size load. See rules of the exact country that describe the exact parameters.

<span class="name">transportingHazardousGoods</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory">TrafficIncidentRestrictedVehicleCategory</a></span>  
Transporting hazardous goods.

<span class="name">vehicleWithTrailer</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory">TrafficIncidentRestrictedVehicleCategory</a></span>  
Vehicle with trailer.

<span class="name">other</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory">TrafficIncidentRestrictedVehicleCategory</a></span>  
Other vehicles.

<span class="name">all</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory">TrafficIncidentRestrictedVehicleCategory</a></span>  
All the vehicles are applicable for this category.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory">TrafficIncidentRestrictedVehicleCategory</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
