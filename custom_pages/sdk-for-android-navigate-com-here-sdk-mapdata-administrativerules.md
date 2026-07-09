---
title: "AdministrativeRules (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- AdministrativeRules.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapdata</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.mapdata.AdministrativeRules</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">AdministrativeRules</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Represents a set of administrative rules for a country or a state.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-mapdata-admincontextid" title="class in com.here.sdk.mapdata">AdminContextId</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#adminContextId">adminContextId</a></code></div>
<div className="col-last even-row-color">
<div className="block">The administrative context ID used to identify this administrative region.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-mapdata-bloodalcoholcontentlimit" title="class in com.here.sdk.mapdata">BloodAlcoholContentLimit</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#bloodAlcoholContentLimit">bloodAlcoholContentLimit</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Indicates the rules regarding alcohol in blood content limit in a country or state for
 all types of drivers.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#countryCode">countryCode</a></code></div>
<div className="col-last even-row-color">
<div className="block">Country code for which the administrative rules apply.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#daylightSavingPeriod">daylightSavingPeriod</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Time rule indicating the time periods in which daylight savings applies.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-mapdata-drivingside" title="enum class in com.here.sdk.mapdata">DrivingSide</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#drivingSide">drivingSide</a></code></div>
<div className="col-last even-row-color">
<div className="block">The side of the road used for driving in the country or state.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapdata-headlightsrequirement" title="enum class in com.here.sdk.mapdata">HeadlightsRequirement</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#headlightsRequirements">headlightsRequirements</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Indicates in which conditions should the headlights be turned on.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#isCleanAirStickerRequired">isCleanAirStickerRequired</a></code></div>
<div className="col-last even-row-color">
<div className="block">Indicates if the country or state requires an ecological sticker.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#isTollRequired">isTollRequired</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Indicates if the country or state requires paid fees for usage of the motorways / controlled access
 roads.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#isTollStickerRequired">isTollStickerRequired</a></code></div>
<div className="col-last even-row-color">
<div className="block">Indicates if the country or state requires a toll sticker.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#isUturnRestricted">isUturnRestricted</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Indicates if performing a u-turn maneuver is restricted.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapdata-admincontextid" title="class in com.here.sdk.mapdata">AdminContextId</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#parentAdminContextIds">parentAdminContextIds</a></code></div>
<div className="col-last even-row-color">
<div className="block">The list of parent administrative context IDs.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapdata-parkingsideregulation" title="enum class in com.here.sdk.mapdata">ParkingSideRegulation</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#parkingSideRegulations">parkingSideRegulations</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Indicates the regulations for parking on the side of the road.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-mapdata-pretripplanning" title="class in com.here.sdk.mapdata">PreTripPlanning</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#preTripPlanning">preTripPlanning</a></code></div>
<div className="col-last even-row-color">
<div className="block">Indicates the legal requirements to be considered before a trip for all vehicles types.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-transport-generalvehiclespeedlimits" title="class in com.here.sdk.transport">GeneralVehicleSpeedLimits</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#speedLimits">speedLimits</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The general speed limits in the country or state.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#stateCode">stateCode</a></code></div>
<div className="col-last even-row-color">
<div className="block">The state code for which the administrative rules apply.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#timeZoneOffsetsInMinutes">timeZoneOffsetsInMinutes</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The time zone offset from UTC of the country or state expressed in minutes.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapdata-tollsystem" title="class in com.here.sdk.mapdata">TollSystem</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#tollSystems">tollSystems</a></code></div>
<div className="col-last even-row-color">
<div className="block">Indicates the toll systems present in a country or state.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapdata-turnonredregulation" title="enum class in com.here.sdk.mapdata">TurnOnRedRegulation</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#turnOnRedRegulations">turnOnRedRegulations</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Indicates the regulations for turning on the red color of the traffic light.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#unitSystem">unitSystem</a></code></div>
<div className="col-last even-row-color">
<div className="block">Defines the measurement system used for distances.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules#%3Cinit%3E(com.here.sdk.mapdata.AdminContextId)">AdministrativeRules</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapdata-admincontextid" title="class in com.here.sdk.mapdata">AdminContextId</a> adminContextId)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="countryCode">
<h3>countryCode</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a></span> <span className="element-name">countryCode</span></div>
<div className="block"><p>Country code for which the administrative rules apply.</p></div>
</section>
</li>
<li>
<section className="detail" id="stateCode">
<h3>stateCode</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">stateCode</span></div>
<div className="block"><p>The state code for which the administrative rules apply. It represents the state / province code. It is
 a 1 to 3 upper-case characters string that follows the ISO 3166-2 standard, but without the preceding
 country code (e.g. for Texas, the state code will be TX).
 It will be <code>null</code> if the rules are applying to the entire country and not just a specific state.</p></div>
</section>
</li>
<li>
<section className="detail" id="adminContextId">
<h3>adminContextId</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-admincontextid" title="class in com.here.sdk.mapdata">AdminContextId</a></span> <span className="element-name">adminContextId</span></div>
<div className="block"><p>The administrative context ID used to identify this administrative region.
 This ID is used internally to load commercial vehicle regulations and other
 administrative-specific data.</p></div>
</section>
</li>
<li>
<section className="detail" id="parentAdminContextIds">
<h3>parentAdminContextIds</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapdata-admincontextid" title="class in com.here.sdk.mapdata">AdminContextId</a>&gt;</span> <span className="element-name">parentAdminContextIds</span></div>
<div className="block"><p>The list of parent administrative context IDs.
 These represent the administrative hierarchy (e.g., state-&gt;country).
 Used internally to load commercial vehicle regulations that may be inherited
 from parent administrative regions.</p></div>
</section>
</li>
<li>
<section className="detail" id="drivingSide">
<h3>drivingSide</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-drivingside" title="enum class in com.here.sdk.mapdata">DrivingSide</a></span> <span className="element-name">drivingSide</span></div>
<div className="block"><p>The side of the road used for driving in the country or state. Defaults to right driving side.</p></div>
</section>
</li>
<li>
<section className="detail" id="unitSystem">
<h3>unitSystem</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a></span> <span className="element-name">unitSystem</span></div>
<div className="block"><p>Defines the measurement system used for distances. Defaults to metric measurement system.</p></div>
</section>
</li>
<li>
<section className="detail" id="speedLimits">
<h3>speedLimits</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-generalvehiclespeedlimits" title="class in com.here.sdk.transport">GeneralVehicleSpeedLimits</a></span> <span className="element-name">speedLimits</span></div>
<div className="block"><p>The general speed limits in the country or state.</p></div>
</section>
</li>
<li>
<section className="detail" id="timeZoneOffsetsInMinutes">
<h3>timeZoneOffsetsInMinutes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a>&gt;</span> <span className="element-name">timeZoneOffsetsInMinutes</span></div>
<div className="block"><p>The time zone offset from UTC of the country or state expressed in minutes. The value can also be negative
 (e.g.: Eastern Standard Time (EST) will be -360 minutes, Central European Time (CET) will be 60 minutes).
 Defaults to 0 minutes.
 <strong>Note:</strong> A time zone with a positive shift of 1 hour and 30 minutes will result in a time zone offset of
 90 minutes. A time zone with a negative shift of 3 hour and 30 minutes will result in an time zone offset
 of -210 minutes. In order to properly calculate the time zone offset, the [AdministrativeRules.daylight_saving_period]
 should be taken into consideration and if the daylight savings time is observed at the time of the
 calculation, then a value of 60 minutes should be substracted from the time zone offset.</p></div>
</section>
</li>
<li>
<section className="detail" id="daylightSavingPeriod">
<h3>daylightSavingPeriod</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a></span> <span className="element-name">daylightSavingPeriod</span></div>
<div className="block"><p>Time rule indicating the time periods in which daylight savings applies.
 If the field is 'null' then daylight savings time is not observed in the country or state.
 <strong>Note:</strong> In order to properly calculate the time zone offset, if the daylight savings time is observed at
 the time of the calculation, then a value of 60 minutes should be substracted from the time zone offset.</p></div>
</section>
</li>
<li>
<section className="detail" id="isUturnRestricted">
<h3>isUturnRestricted</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isUturnRestricted</span></div>
<div className="block"><p>Indicates if performing a u-turn maneuver is restricted. Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="headlightsRequirements">
<h3>headlightsRequirements</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapdata-headlightsrequirement" title="enum class in com.here.sdk.mapdata">HeadlightsRequirement</a>&gt;</span> <span className="element-name">headlightsRequirements</span></div>
<div className="block"><p>Indicates in which conditions should the headlights be turned on. Defaults to an empty list,
 which means that by default there are no special situations in which the headlights should be
 turned on.</p></div>
</section>
</li>
<li>
<section className="detail" id="isTollRequired">
<h3>isTollRequired</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isTollRequired</span></div>
<div className="block"><p>Indicates if the country or state requires paid fees for usage of the motorways / controlled access
 roads. Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="isTollStickerRequired">
<h3>isTollStickerRequired</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isTollStickerRequired</span></div>
<div className="block"><p>Indicates if the country or state requires a toll sticker. Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="turnOnRedRegulations">
<h3>turnOnRedRegulations</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapdata-turnonredregulation" title="enum class in com.here.sdk.mapdata">TurnOnRedRegulation</a>&gt;</span> <span className="element-name">turnOnRedRegulations</span></div>
<div className="block"><p>Indicates the regulations for turning on the red color of the traffic light.</p></div>
</section>
</li>
<li>
<section className="detail" id="parkingSideRegulations">
<h3>parkingSideRegulations</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapdata-parkingsideregulation" title="enum class in com.here.sdk.mapdata">ParkingSideRegulation</a>&gt;</span> <span className="element-name">parkingSideRegulations</span></div>
<div className="block"><p>Indicates the regulations for parking on the side of the road.</p></div>
</section>
</li>
<li>
<section className="detail" id="isCleanAirStickerRequired">
<h3>isCleanAirStickerRequired</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isCleanAirStickerRequired</span></div>
<div className="block"><p>Indicates if the country or state requires an ecological sticker. Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="bloodAlcoholContentLimit">
<h3>bloodAlcoholContentLimit</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-bloodalcoholcontentlimit" title="class in com.here.sdk.mapdata">BloodAlcoholContentLimit</a></span> <span className="element-name">bloodAlcoholContentLimit</span></div>
<div className="block"><p>Indicates the rules regarding alcohol in blood content limit in a country or state for
 all types of drivers.</p></div>
</section>
</li>
<li>
<section className="detail" id="tollSystems">
<h3>tollSystems</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapdata-tollsystem" title="class in com.here.sdk.mapdata">TollSystem</a>&gt;</span> <span className="element-name">tollSystems</span></div>
<div className="block"><p>Indicates the toll systems present in a country or state.</p></div>
</section>
</li>
<li>
<section className="detail" id="preTripPlanning">
<h3>preTripPlanning</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-pretripplanning" title="class in com.here.sdk.mapdata">PreTripPlanning</a></span> <span className="element-name">preTripPlanning</span></div>
<div className="block"><p>Indicates the legal requirements to be considered before a trip for all vehicles types.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapdata.AdminContextId)">
<h3>AdministrativeRules</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">AdministrativeRules</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapdata-admincontextid" title="class in com.here.sdk.mapdata">AdminContextId</a> adminContextId)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>adminContextId</code> - <p>The administrative context ID used to identify this administrative region.
 This ID is used internally to load commercial vehicle regulations and other
 administrative-specific data.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="hashCode()">
<h3>hashCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">hashCode</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->

</div>
</div>



</div>
`
}</HTMLBlock>
