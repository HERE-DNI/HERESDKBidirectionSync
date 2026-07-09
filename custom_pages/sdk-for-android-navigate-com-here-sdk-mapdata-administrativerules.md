---
title: "AdministrativeRules (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapdata-package-summary">com.here.sdk.mapdata</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.mapdata.AdministrativeRules → com.here.sdk.mapdata.AdministrativeRules

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">AdministrativeRules</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents a set of administrative rules for a country or a state.

</div>

</div>

- <div id="sdk-for-android-navigate-field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Field

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-admincontextid" title="class in com.here.sdk.mapdata">`AdminContextId`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#adminContextId" class="member-name-link"><code>adminContextId</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The administrative context ID used to identify this administrative region.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-bloodalcoholcontentlimit" title="class in com.here.sdk.mapdata">`BloodAlcoholContentLimit`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#bloodAlcoholContentLimit" class="member-name-link"><code>bloodAlcoholContentLimit</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Indicates the rules regarding alcohol in blood content limit in a country or state for all types of drivers.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">`CountryCode`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#countryCode" class="member-name-link"><code>countryCode</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Country code for which the administrative rules apply.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">`TimeRule`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#daylightSavingPeriod" class="member-name-link"><code>daylightSavingPeriod</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Time rule indicating the time periods in which daylight savings applies.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-drivingside" title="enum class in com.here.sdk.mapdata">`DrivingSide`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#drivingSide" class="member-name-link"><code>drivingSide</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The side of the road used for driving in the country or state.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-mapdata-headlightsrequirement" title="enum class in com.here.sdk.mapdata">`HeadlightsRequirement`</a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#headlightsRequirements" class="member-name-link"><code>headlightsRequirements</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Indicates in which conditions should the headlights be turned on.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#isCleanAirStickerRequired" class="member-name-link"><code>isCleanAirStickerRequired</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Indicates if the country or state requires an ecological sticker.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#isTollRequired" class="member-name-link"><code>isTollRequired</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Indicates if the country or state requires paid fees for usage of the motorways / controlled access roads.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#isTollStickerRequired" class="member-name-link"><code>isTollStickerRequired</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Indicates if the country or state requires a toll sticker.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#isUturnRestricted" class="member-name-link"><code>isUturnRestricted</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Indicates if performing a u-turn maneuver is restricted.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-mapdata-admincontextid" title="class in com.here.sdk.mapdata">`AdminContextId`</a>`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#parentAdminContextIds" class="member-name-link"><code>parentAdminContextIds</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The list of parent administrative context IDs.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-mapdata-parkingsideregulation" title="enum class in com.here.sdk.mapdata">`ParkingSideRegulation`</a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#parkingSideRegulations" class="member-name-link"><code>parkingSideRegulations</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Indicates the regulations for parking on the side of the road.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-pretripplanning" title="class in com.here.sdk.mapdata">`PreTripPlanning`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#preTripPlanning" class="member-name-link"><code>preTripPlanning</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Indicates the legal requirements to be considered before a trip for all vehicles types.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-transport-generalvehiclespeedlimits" title="class in com.here.sdk.transport">`GeneralVehicleSpeedLimits`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#speedLimits" class="member-name-link"><code>speedLimits</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The general speed limits in the country or state.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#stateCode" class="member-name-link"><code>stateCode</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The state code for which the administrative rules apply.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">`Duration`</a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#timeZoneOffsetsInMinutes" class="member-name-link"><code>timeZoneOffsetsInMinutes</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The time zone offset from UTC of the country or state expressed in minutes.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-mapdata-tollsystem" title="class in com.here.sdk.mapdata">`TollSystem`</a>`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#tollSystems" class="member-name-link"><code>tollSystems</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Indicates the toll systems present in a country or state.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-mapdata-turnonredregulation" title="enum class in com.here.sdk.mapdata">`TurnOnRedRegulation`</a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#turnOnRedRegulations" class="member-name-link"><code>turnOnRedRegulations</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Indicates the regulations for turning on the red color of the traffic light.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-unitsystem" title="enum class in com.here.sdk.core">`UnitSystem`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#unitSystem" class="member-name-link"><code>unitSystem</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Defines the measurement system used for distances.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      AdministrativeRules ( AdminContextId adminContextId)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals ( Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-countryCode" class="section detail">

    ### countryCode

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a></span> <span class="element-name">countryCode</span>

    </div>

    <div class="block">

    Country code for which the administrative rules apply.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-stateCode" class="section detail">

    ### stateCode

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">stateCode</span>

    </div>

    <div class="block">

    The state code for which the administrative rules apply. It represents the state / province code. It is a 1 to 3 upper-case characters string that follows the ISO 3166-2 standard, but without the preceding country code (e.g. for Texas, the state code will be TX). It will be null if the rules are applying to the entire country and not just a specific state.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-adminContextId" class="section detail">

    ### adminContextId

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-admincontextid" title="class in com.here.sdk.mapdata">AdminContextId</a></span> <span class="element-name">adminContextId</span>

    </div>

    <div class="block">

    The administrative context ID used to identify this administrative region. This ID is used internally to load commercial vehicle regulations and other administrative-specific data.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-parentAdminContextIds" class="section detail">

    ### parentAdminContextIds

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-mapdata-admincontextid" title="class in com.here.sdk.mapdata">AdminContextId</a>\></span> <span class="element-name">parentAdminContextIds</span>

    </div>

    <div class="block">

    The list of parent administrative context IDs. These represent the administrative hierarchy (e.g., state-\>country). Used internally to load commercial vehicle regulations that may be inherited from parent administrative regions.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-drivingSide" class="section detail">

    ### drivingSide

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-drivingside" title="enum class in com.here.sdk.mapdata">DrivingSide</a></span> <span class="element-name">drivingSide</span>

    </div>

    <div class="block">

    The side of the road used for driving in the country or state. Defaults to right driving side.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-unitSystem" class="section detail">

    ### unitSystem

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a></span> <span class="element-name">unitSystem</span>

    </div>

    <div class="block">

    Defines the measurement system used for distances. Defaults to metric measurement system.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-speedLimits" class="section detail">

    ### speedLimits

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-generalvehiclespeedlimits" title="class in com.here.sdk.transport">GeneralVehicleSpeedLimits</a></span> <span class="element-name">speedLimits</span>

    </div>

    <div class="block">

    The general speed limits in the country or state.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-timeZoneOffsetsInMinutes" class="section detail">

    ### timeZoneOffsetsInMinutes

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a>\></span> <span class="element-name">timeZoneOffsetsInMinutes</span>

    </div>

    <div class="block">

    The time zone offset from UTC of the country or state expressed in minutes. The value can also be negative (e.g.: Eastern Standard Time (EST) will be -360 minutes, Central European Time (CET) will be 60 minutes). Defaults to 0 minutes. Note: A time zone with a positive shift of 1 hour and 30 minutes will result in a time zone offset of 90 minutes. A time zone with a negative shift of 3 hour and 30 minutes will result in an time zone offset of -210 minutes. In order to properly calculate the time zone offset, the \[AdministrativeRules.daylight_saving_period\] should be taken into consideration and if the daylight savings time is observed at the time of the calculation, then a value of 60 minutes should be substracted from the time zone offset.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-daylightSavingPeriod" class="section detail">

    ### daylightSavingPeriod

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a></span> <span class="element-name">daylightSavingPeriod</span>

    </div>

    <div class="block">

    Time rule indicating the time periods in which daylight savings applies. If the field is 'null' then daylight savings time is not observed in the country or state. Note: In order to properly calculate the time zone offset, if the daylight savings time is observed at the time of the calculation, then a value of 60 minutes should be substracted from the time zone offset.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isUturnRestricted" class="section detail">

    ### isUturnRestricted

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUturnRestricted</span>

    </div>

    <div class="block">

    Indicates if performing a u-turn maneuver is restricted. Defaults to false .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-headlightsRequirements" class="section detail">

    ### headlightsRequirements

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-mapdata-headlightsrequirement" title="enum class in com.here.sdk.mapdata">HeadlightsRequirement</a>\></span> <span class="element-name">headlightsRequirements</span>

    </div>

    <div class="block">

    Indicates in which conditions should the headlights be turned on. Defaults to an empty list, which means that by default there are no special situations in which the headlights should be turned on.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isTollRequired" class="section detail">

    ### isTollRequired

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTollRequired</span>

    </div>

    <div class="block">

    Indicates if the country or state requires paid fees for usage of the motorways / controlled access roads. Defaults to false .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isTollStickerRequired" class="section detail">

    ### isTollStickerRequired

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTollStickerRequired</span>

    </div>

    <div class="block">

    Indicates if the country or state requires a toll sticker. Defaults to false .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-turnOnRedRegulations" class="section detail">

    ### turnOnRedRegulations

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-mapdata-turnonredregulation" title="enum class in com.here.sdk.mapdata">TurnOnRedRegulation</a>\></span> <span class="element-name">turnOnRedRegulations</span>

    </div>

    <div class="block">

    Indicates the regulations for turning on the red color of the traffic light.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-parkingSideRegulations" class="section detail">

    ### parkingSideRegulations

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-mapdata-parkingsideregulation" title="enum class in com.here.sdk.mapdata">ParkingSideRegulation</a>\></span> <span class="element-name">parkingSideRegulations</span>

    </div>

    <div class="block">

    Indicates the regulations for parking on the side of the road.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isCleanAirStickerRequired" class="section detail">

    ### isCleanAirStickerRequired

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCleanAirStickerRequired</span>

    </div>

    <div class="block">

    Indicates if the country or state requires an ecological sticker. Defaults to false .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-bloodAlcoholContentLimit" class="section detail">

    ### bloodAlcoholContentLimit

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-bloodalcoholcontentlimit" title="class in com.here.sdk.mapdata">BloodAlcoholContentLimit</a></span> <span class="element-name">bloodAlcoholContentLimit</span>

    </div>

    <div class="block">

    Indicates the rules regarding alcohol in blood content limit in a country or state for all types of drivers.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-tollSystems" class="section detail">

    ### tollSystems

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-mapdata-tollsystem" title="class in com.here.sdk.mapdata">TollSystem</a>\></span> <span class="element-name">tollSystems</span>

    </div>

    <div class="block">

    Indicates the toll systems present in a country or state.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-preTripPlanning" class="section detail">

    ### preTripPlanning

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-pretripplanning" title="class in com.here.sdk.mapdata">PreTripPlanning</a></span> <span class="element-name">preTripPlanning</span>

    </div>

    <div class="block">

    Indicates the legal requirements to be considered before a trip for all vehicles types.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-com-here-sdk-mapdata-AdminContextId" class="section detail">

    ### AdministrativeRules

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">AdministrativeRules</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapdata-admincontextid" title="class in com.here.sdk.mapdata">AdminContextId</a> adminContextId)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `adminContextId` -

    The administrative context ID used to identify this administrative region. This ID is used internally to load commercial vehicle regulations and other administrative-specific data.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-navigate-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

