---
title: "EVChargingStation class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-evchargingstation-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EVChargingStation-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVChargingStation-class-sidebar.html">

<div>

# <span class="kind-class">EVChargingStation</span> class

</div>

<div class="section desc markdown">

Group of connectors for electric vehicles (EVs), defined by a common charging connector type and maximum power level.

Use <a href="sdk-for-flutter-navigate-search-placecategory-businessandservicesevchargingstation">PlaceCategory.businessAndServicesEvChargingStation</a> to find stations. In the `Details` of a `Place` result you can find the list of found pools containing stations, if any.

For offline EV rich attributes, enable <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.ev</a> in <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-layerconfiguration">SDKOptions.layerConfiguration</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingstation-evchargingstation-withdefaults">EVChargingStation.withDefaults</a></span><span class="signature">()</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingstation-availableconnectorcount">availableConnectorCount</a></span> <span class="signature">↔ int?</span>  
Number of available physical connectors at the charging station. This field is always `null` for offline search using the `OfflineSearchEngine`. For online searches using the `SearchEngine`, it may be `null` if the data is unavailable.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingstation-chargingmode">chargingMode</a></span> <span class="signature">↔ String?</span>  
Charging mode of the charging station. For more information, see <https://en.wikipedia.org/w/index.php?title=Charging_station&oldid=1013010605#IEC-61851-1_Charging_Modes> standard. This field can be `null` if data is unavailable.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingstation-connectorcount">connectorCount</a></span> <span class="signature">↔ int?</span>  
Number of physical connectors at the charging station. This field can be `null` if data is unavailable.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingstation-connectortypeid">connectorTypeId</a></span> <span class="signature">↔ String?</span>  
ID of the connector type. For more information on the current connector types, see <https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html> This field is always `null` for offline search using the `OfflineSearchEngine`. For online searches using the `SearchEngine`, it may be `null` if the data is unavailable.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingstation-connectortypename">connectorTypeName</a></span> <span class="signature">↔ String?</span>  
Name of the connector type. For more information on the current connector types, see <https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html> May include customer-facing names. In such cases, a 'customer names' label is present. This field can be `null` if data is unavailable.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingstation-currentrangeinamperes">currentRangeInAmperes</a></span> <span class="signature">↔ String?</span>  
Current range provided by the charging station, in amperes. Values are alphanumeric represented by the Ampere value followed by an 'A', for example '12A-80A'. This field can be `null` if data is unavailable.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingstation-hasfixedcable">hasFixedCable</a></span> <span class="signature">↔ bool?</span>  
Indicates that the cable is fixed or not fixed for a specific Connector Type on the charge station. This field can be `null` if data is unavailable.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingstation-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingstation-lastupdated">lastUpdated</a></span> <span class="signature">↔ DateTime?</span>  
Last update of the `available_connector_count` and `occupied_connector_count` fields. This field is always `null` for offline search using the `OfflineSearchEngine`. For online searches using the `SearchEngine`, it may be `null` if the data is unavailable.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingstation-maxpowerinkilowatts">maxPowerInKilowatts</a></span> <span class="signature">↔ double?</span>  
Maximum charge power of connectors in kW. This field can be `null` if data is unavailable.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingstation-occupiedconnectorcount">occupiedConnectorCount</a></span> <span class="signature">↔ int?</span>  
Number of occupied physical connectors at the charging station. This field is always `null` for offline search using the `OfflineSearchEngine`. For online searches using the `SearchEngine`, it may be `null` if the data is unavailable.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingstation-outofserviceconnectorcount">outOfServiceConnectorCount</a></span> <span class="signature">↔ int?</span>  
Number of physical connectors that are out of service at the charging station. This field is always `null` for offline search using the `OfflineSearchEngine`. For online searches using the `SearchEngine`, it may be `null` if the data is unavailable.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingstation-phasecount">phaseCount</a></span> <span class="signature">↔ int?</span>  
Number of phases used by the charging station. This field can be `null` if data is unavailable.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingstation-physicalreference">physicalReference</a></span> <span class="signature">↔ String?</span>  
Printed on the outside of the EVSE for visual identification. Available only in offline search. This field can be `null` if data is unavailable.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingstation-powerfeedtypeid">powerFeedTypeId</a></span> <span class="signature">↔ String?</span>  
ID of the power feed type, as defined by the <https://en.wikipedia.org/wiki/SAE_J1772#Charging> standard. No data in case of offline search. This field is always `null` for offline search using the `OfflineSearchEngine`. For online searches using the `SearchEngine`, it may be `null` if the data is unavailable.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingstation-powerfeedtypename">powerFeedTypeName</a></span> <span class="signature">↔ String?</span>  
Name of the power feed type, as defined by the <https://en.wikipedia.org/wiki/SAE_J1772#Charging> standard. Provides the customer information on the charge level of the specific Connector Type. Also, can describe level that is used in North America and Australia. In that case label 'North America (Australia)' is present. This field can be `null` if data is unavailable.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingstation-reservedconnectorcount">reservedConnectorCount</a></span> <span class="signature">↔ int?</span>  
Number of physical connectors that are reserved at the charging station. This field is always `null` for offline search using the `OfflineSearchEngine`. For online searches using the `SearchEngine`, it may be `null` if the data is unavailable.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingstation-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingstation-suppliername">supplierName</a></span> <span class="signature">↔ String?</span>  
The EV charging station operator. This field is always `null` for offline search using the `OfflineSearchEngine`. For online search using the `SearchEngine`, it can be null if data is unavailable.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingstation-voltagerangeinvolts">voltageRangeInVolts</a></span> <span class="signature">↔ String?</span>  
Voltage range of the charge provided by the charging station, in volts. Values are alphanumeric represented by the voltage range followed by 'V' and by the current type 'AC' or 'DC', for example: '100-120V AC'. This field can be `null` if data is unavailable.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingstation-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingstation-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingstation-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
