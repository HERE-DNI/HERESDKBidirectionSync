---
title: "AdministrativeRules class - mapdata library - Dart API"
slug: "sdk-for-flutter-navigate-mapdata-administrativerules-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- AdministrativeRules-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapdata/mapdata-library-sidebar.html" data-below-sidebar="mapdata/AdministrativeRules-class-sidebar.html">

<div>

# <span class="kind-class">AdministrativeRules</span> class

</div>

<div class="section desc markdown">

Represents a set of administrative rules for a country or a state.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-administrativerules">AdministrativeRules</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-adminContextId" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-admincontextid-class">AdminContextId</a></span> <span class="parameter-name">adminContextId</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-admincontextid">adminContextId</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-mapdata-admincontextid-class">AdminContextId</a></span>  
The administrative context ID used to identify this administrative region. This ID is used internally to load commercial vehicle regulations and other administrative-specific data.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-bloodalcoholcontentlimit">bloodAlcoholContentLimit</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-mapdata-bloodalcoholcontentlimit-class">BloodAlcoholContentLimit</a></span>  
Indicates the rules regarding alcohol in blood content limit in a country or state for all types of drivers.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-countrycode">countryCode</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-countrycode">CountryCode</a></span>  
Country code for which the administrative rules apply.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-daylightsavingperiod">daylightSavingPeriod</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-timerule-class">TimeRule</a>?</span>  
Time rule indicating the time periods in which daylight savings applies. If the field is 'null' then daylight savings time is not observed in the country or state. **Note:** In order to properly calculate the time zone offset, if the daylight savings time is observed at the time of the calculation, then a value of 60 minutes should be substracted from the time zone offset.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-drivingside">drivingSide</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-mapdata-drivingside">DrivingSide</a>?</span>  
The side of the road used for driving in the country or state. Defaults to right driving side.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-headlightsrequirements">headlightsRequirements</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapdata-headlightsrequirement">HeadlightsRequirement</a></span>\></span></span>  
Indicates in which conditions should the headlights be turned on. Defaults to an empty list, which means that by default there are no special situations in which the headlights should be turned on.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-iscleanairstickerrequired">isCleanAirStickerRequired</a></span> <span class="signature">↔ bool</span>  
Indicates if the country or state requires an ecological sticker. Defaults to `false`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-istollrequired">isTollRequired</a></span> <span class="signature">↔ bool</span>  
Indicates if the country or state requires paid fees for usage of the motorways / controlled access roads. Defaults to `false`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-istollstickerrequired">isTollStickerRequired</a></span> <span class="signature">↔ bool</span>  
Indicates if the country or state requires a toll sticker. Defaults to `false`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-isuturnrestricted">isUturnRestricted</a></span> <span class="signature">↔ bool</span>  
Indicates if performing a u-turn maneuver is restricted. Defaults to `false`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-parentadmincontextids">parentAdminContextIds</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapdata-admincontextid-class">AdminContextId</a></span>\></span></span>  
The list of parent administrative context IDs. These represent the administrative hierarchy (e.g., state-\>country). Used internally to load commercial vehicle regulations that may be inherited from parent administrative regions.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-parkingsideregulations">parkingSideRegulations</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapdata-parkingsideregulation">ParkingSideRegulation</a></span>\></span></span>  
Indicates the regulations for parking on the side of the road.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-pretripplanning">preTripPlanning</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-mapdata-pretripplanning-class">PreTripPlanning</a></span>  
Indicates the legal requirements to be considered before a trip for all vehicles types.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-speedlimits">speedLimits</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-transport-generalvehiclespeedlimits-class">GeneralVehicleSpeedLimits</a></span>  
The general speed limits in the country or state.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-statecode">stateCode</a></span> <span class="signature">↔ String?</span>  
The state code for which the administrative rules apply. It represents the state / province code. It is a 1 to 3 upper-case characters string that follows the ISO 3166-2 standard, but without the preceding country code (e.g. for Texas, the state code will be TX). It will be `null` if the rules are applying to the entire country and not just a specific state.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-timezoneoffsetsinminutes">timeZoneOffsetsInMinutes</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter">Duration</span>\></span></span>  
The time zone offset from UTC of the country or state expressed in minutes. The value can also be negative (e.g.: Eastern Standard Time (EST) will be -360 minutes, Central European Time (CET) will be 60 minutes). Defaults to 0 minutes. **Note:** A time zone with a positive shift of 1 hour and 30 minutes will result in a time zone offset of 90 minutes. A time zone with a negative shift of 3 hour and 30 minutes will result in an time zone offset of -210 minutes. In order to properly calculate the time zone offset, the `AdministrativeRules.daylight_saving_period` should be taken into consideration and if the daylight savings time is observed at the time of the calculation, then a value of 60 minutes should be substracted from the time zone offset.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-tollsystems">tollSystems</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapdata-tollsystem-class">TollSystem</a></span>\></span></span>  
Indicates the toll systems present in a country or state.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-turnonredregulations">turnOnRedRegulations</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapdata-turnonredregulation">TurnOnRedRegulation</a></span>\></span></span>  
Indicates the regulations for turning on the red color of the traffic light.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-unitsystem">unitSystem</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-unitsystem">UnitSystem</a>?</span>  
Defines the measurement system used for distances. Defaults to metric measurement system.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
