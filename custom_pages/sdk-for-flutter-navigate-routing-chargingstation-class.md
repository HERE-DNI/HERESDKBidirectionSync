---
title: "ChargingStation class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-chargingstation-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ChargingStation-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/ChargingStation-class-sidebar.html">

<div>

# <span class="kind-class">ChargingStation</span> class

</div>

<div class="section desc markdown">

Data for an electric vehicle charging station.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstation-chargingstation">ChargingStation</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-id" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">id</span>, </span><span id="sdk-for-flutter-navigate-param-name" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">name</span>, </span><span id="sdk-for-flutter-navigate-param-connectorAttributes" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-chargingconnectorattributes-class">ChargingConnectorAttributes</a>?</span> <span class="parameter-name">connectorAttributes</span></span>)</span>  
Creates a new instance.

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstation-chargingstation-withdetails">ChargingStation.withDetails</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withDetails-param-id" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">id</span>, </span><span id="sdk-for-flutter-navigate-withDetails-param-name" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">name</span>, </span><span id="sdk-for-flutter-navigate-withDetails-param-connectorAttributes" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-chargingconnectorattributes-class">ChargingConnectorAttributes</a>?</span> <span class="parameter-name">connectorAttributes</span>, </span><span id="sdk-for-flutter-navigate-withDetails-param-brand" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-nameid-class">NameID</a>?</span> <span class="parameter-name">brand</span>, </span><span id="sdk-for-flutter-navigate-withDetails-param-chargePointOperator" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-nameid-class">NameID</a>?</span> <span class="parameter-name">chargePointOperator</span>, </span><span id="sdk-for-flutter-navigate-withDetails-param-matchingEMobilityServiceProviders" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-nameid-class">NameID</a></span>\></span></span> <span class="parameter-name">matchingEMobilityServiceProviders</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstation-brand">brand</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-nameid-class">NameID</a>?</span>  
Charging station brand. <a href="sdk-for-flutter-navigate-core-nameid-name">NameID.name</a> reflect to charging station brand name. <a href="sdk-for-flutter-navigate-core-nameid-id">NameID.id</a> reflect to charging station brand unique ID.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstation-chargepointoperator">chargePointOperator</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-nameid-class">NameID</a>?</span>  
Charging station charge-point-operator. <a href="sdk-for-flutter-navigate-core-nameid-name">NameID.name</a> reflect to charge-point-operator name. <a href="sdk-for-flutter-navigate-core-nameid-id">NameID.id</a> reflect to charge-point-operator ID.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstation-connectorattributes">connectorAttributes</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-chargingconnectorattributes-class">ChargingConnectorAttributes</a>?</span>  
Details of the connector suggested to be used.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstation-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstation-id">id</a></span> <span class="signature">↔ String?</span>  
Identifier of this charging station. It can only be null when custom charging stations from non-HERE datasets have been injected on the HERE platform. By default, with HERE datasets it is guranteed to be not null.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstation-matchingemobilityserviceproviders">matchingEMobilityServiceProviders</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-nameid-class">NameID</a></span>\></span></span>  
List of matched E-Mobility Service Providers. Populated only when <a href="sdk-for-flutter-navigate-routing-electricvehicleoptions-evmobilityserviceproviderpreferences">ElectricVehicleOptions.evMobilityServiceProviderPreferences</a> was set. This list reflects the subset of E-Mobility Service Providers supported by the charging station, from the list specified in the request parameter <a href="sdk-for-flutter-navigate-routing-electricvehicleoptions-evmobilityserviceproviderpreferences">ElectricVehicleOptions.evMobilityServiceProviderPreferences</a>. <a href="sdk-for-flutter-navigate-core-nameid-name">NameID.name</a> in each list item reflect to E-Mobility Service Provider name. <a href="sdk-for-flutter-navigate-core-nameid-id">NameID.id</a> in each list item reflect to E-Mobility Service Provider id.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstation-name">name</a></span> <span class="signature">↔ String?</span>  
Human readable name of this charging station. It can be null when there is no name associated with the station.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstation-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstation-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstation-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstation-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
