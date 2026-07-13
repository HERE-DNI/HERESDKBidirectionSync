---
title: "EVChargingLocation class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-evcharginglocation-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EVChargingLocation-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVChargingLocation-class-sidebar.html">

<div>

# <span class="kind-class">EVChargingLocation</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

An electric vehicle (EV) charging location.

The semantics generally follow the OCPI 2.2.1 standard.

Known EV-specific acronyms:

- EV: Electric Vehicle
- OCPI: Open Charge Point Interface (a standard with a rather wide adoption worldwide, <https://evroaming.org/>)
- CPO: Charge Point Operator (company that runs the EV charging location)
- eMSP: e-Mobility Service Provider (customer-facing company)
- EVSE: Electric Vehicle Supply Equipment (the actual charger that can charge one car at a time)

A charging location includes a collection of one or more EV supply equipment (EVSE) instances. Typically, the charging location is the exact location of the group of EVSEs, simplified to a single point, but it can also be the entrance of a parking structure which contains these EVSEs. Each EVSE supports more precise position, where applicable.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-search-evcharginglocation-evcharginglocation">EVChargingLocation</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-search-evcharginglocation-connectorgroups">connectorGroups</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-evchargingconnectorgroup-class">EVChargingConnectorGroup</a></span>\></span></span>  
Connector groups for the location. Provides an overview of the charging connectors in the location by type and power. Available only if `EVChargingLocationFeature.CONNECTOR_GROUPS` is included in `EVSearchOptions.additional_features`, otherwise empty. Gets the connector groups for the location.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evcharginglocation-cpoid">cpoID</a></span> <span class="signature">→ String?</span>  
CPO's own ID for the location. This ID may be relevant for some clients to map the charging location data to their own or 3rd party systems. Available only if `EVChargingLocationFeature.LOCATION_INFO` is included in `EVSearchOptions.additional_features`, otherwise `null`. Gets the CPO's own ID for the location.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evcharginglocation-emobilityserviceproviders">eMobilityServiceProviders</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-evchargingoperator-class">EVChargingOperator</a></span>\></span></span>  
eMSPs with a roaming agreement enabling access to the EV charging location. Available only if `EVChargingLocationFeature.EMSPS` is included in `EVSearchOptions.additional_features`, otherwise empty. Gets the list of eMSPs with a roaming agreement enabling access to the EV charging location.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evcharginglocation-energymix">energyMix</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-search-energymix-class">EnergyMix</a>?</span>  
Details on the energy supplied at the charging location. Available only if `EVChargingLocationFeature.LOCATION_INFO` is included in `EVSearchOptions.additional_features`, otherwise `null`. Gets the details on the energy supplied at the charging location.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evcharginglocation-evchargingoperator">evChargingOperator</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-search-evchargingoperator-class">EVChargingOperator</a>?</span>  
Operator of the charging point, if available. Gets the operator of the charging point, if available.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evcharginglocation-evchargingsuboperator">evChargingSubOperator</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-search-evchargingoperator-class">EVChargingOperator</a>?</span>  
Suboperator of the charging point, if available. Gets the suboperator of the charging point, if available.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evcharginglocation-evses">evses</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-evseinfo-class">EVSEInfo</a></span>\></span></span>  
List of EVSEs at the charging station. Available only if `EVChargingLocationFeature.EVSES` is included in `EVSearchOptions.additional_features`, otherwise empty. Gets the list of EVSEs at the charging station.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evcharginglocation-facilitytypes">facilityTypes</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-facilitytype">FacilityType</a></span>\></span></span>  
Facilities available at the charging location, for example hotel, wifi, parking lot etc. Available only if `EVChargingLocationFeature.NEARBY` is included in `EVSearchOptions.additional_features`, otherwise empty. Gets the list of facilities available at the charging location, for example hotel, wifi, parking lot etc.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evcharginglocation-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evcharginglocation-id">id</a></span> <span class="signature">→ String</span>  
A unique identifier of the charging location. Gets the unique identifier of the charging location.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evcharginglocation-name">name</a></span> <span class="signature">→ String?</span>  
Display name of the charging location, if available. Gets the display name of the charging location, if available.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evcharginglocation-openinghours">openingHours</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-search-evchargingopeninghours-class">EVChargingOpeningHours</a>?</span>  
The times when the EVSEs at the charging location can be accessed for charging. Available only if `EVChargingLocationFeature.LOCATION_INFO` is included in `EVSearchOptions.additional_features`, otherwise `null`. Gets the times when the EVSEs at the charging location can be accessed for charging.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evcharginglocation-parkingtype">parkingType</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-search-parkingtype">ParkingType</a>?</span>  
The type of parking at the charging location. Available only if `EVChargingLocationFeature.LOCATION_INFO` is included in `EVSearchOptions.additional_features`, otherwise `null`. Gets the type of parking at the charging location.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evcharginglocation-restrictions">restrictions</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-evaccessrestrictionreason">EVAccessRestrictionReason</a></span>\></span></span>  
Reason(s) for restricted access. Gets the list of restrictions.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evcharginglocation-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evcharginglocation-supportedvehicles">supportedVehicles</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-evchargingvehiclecategory">EVChargingVehicleCategory</a></span>\></span></span>  
List of vehicle categories this charging location can support. For example, the same location can be suitable for charging passenger cars and motorcycles. There may be some further restrictions specified in other attributes, for example the available connector types may not be suitable for all vehicles in the supported category. Gets the list of vehicle categories this charging location can support. For example, the same location can be suitable for charging passenger cars and motorcycles.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evcharginglocation-supportphonenumber">supportPhoneNumber</a></span> <span class="signature">→ String?</span>  
The phone number that EV drivers should call when need assistance at the charge location, in E.164 format. Available only if `EVChargingLocationFeature.LOCATION_INFO` is included in `EVSearchOptions.additional_features`, otherwise `null`. Gets the phone number that EV drivers should call when need assistance at the charge location.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evcharginglocation-tariffs">tariffs</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-evchargingtariff-class">EVChargingTariff</a></span>\></span></span>  
List of tariffs or price plans for the connectors of the charging station. Tariffs are typically connector-type specific. Hence, they are always linked with connectors and/or connector groups, by indexes to this list.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evcharginglocation-timezone">timeZone</a></span> <span class="signature">→ String?</span>  
The time zone of the charging location. Based on IANA tzdata's TZ-values. Available only if `EVChargingLocationFeature.LOCATION_INFO` is included in `EVSearchOptions.additional_features`, otherwise `null`. Gets the time zone of the charging location. Based on IANA tzdata's TZ-values.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evcharginglocation-truckrestrictions">truckRestrictions</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-search-evchargingtruckrestriction-class">EVChargingTruckRestriction</a>?</span>  
Access restrictions for trucks and light commercial vehicles. Restricted, only available to customers having a specific contract with HERE and if requested by including `EVChargingLocationFeature.TRUCK_RESTRICTIONS` in `EVSearchOptions.additional_features`, otherwise `null`. Gets the access restrictions for trucks and light commercial vehicles.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-search-evcharginglocation-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evcharginglocation-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-search-evcharginglocation-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
