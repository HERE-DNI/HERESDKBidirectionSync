---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-structs-administrativerules"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- AdministrativeRules.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/AdministrativeRules"></a>
<a title="AdministrativeRules Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-mapdata">MapData</a>
<img alt="" id="carat" src="../img/carat.png"/>
        AdministrativeRules Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>AdministrativeRules</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">AdministrativeRules</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents a set of administrative rules for a country or a state.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19AdministrativeRulesV11countryCodeAA07CountryE0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/countryCode"></a>
<a class="token" href="#/s:7heresdk19AdministrativeRulesV11countryCodeAA07CountryE0Ovp">countryCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Country code for which the administrative rules apply.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">countryCode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-countrycode">CountryCode</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19AdministrativeRulesV9stateCodeSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/stateCode"></a>
<a class="token" href="#/s:7heresdk19AdministrativeRulesV9stateCodeSSSgvp">stateCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The state code for which the administrative rules apply. It represents the state / province code. It is
a 1 to 3 upper-case characters string that follows the ISO 3166-2 standard, but without the preceding
country code (e.g. for Texas, the state code will be TX).
It will be <code>nil</code> if the rules are applying to the entire country and not just a specific state.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">stateCode</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19AdministrativeRulesV14adminContextIdAA05AdmineF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/adminContextId"></a>
<a class="token" href="#/s:7heresdk19AdministrativeRulesV14adminContextIdAA05AdmineF0Vvp">adminContextId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The administrative context ID used to identify this administrative region.
This ID is used internally to load commercial vehicle regulations and other
administrative-specific data.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">adminContextId</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-admincontextid">AdminContextId</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19AdministrativeRulesV21parentAdminContextIdsSayAA0eF2IdVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/parentAdminContextIds"></a>
<a class="token" href="#/s:7heresdk19AdministrativeRulesV21parentAdminContextIdsSayAA0eF2IdVGvp">parentAdminContextIds</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of parent administrative context IDs.
These represent the administrative hierarchy (e.g., state-&gt;country).
Used internally to load commercial vehicle regulations that may be inherited
from parent administrative regions.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">parentAdminContextIds</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-admincontextid">AdminContextId</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19AdministrativeRulesV11drivingSideAA07DrivingE0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/drivingSide"></a>
<a class="token" href="#/s:7heresdk19AdministrativeRulesV11drivingSideAA07DrivingE0OSgvp">drivingSide</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The side of the road used for driving in the country or state. Defaults to right driving side.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">drivingSide</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-drivingside">DrivingSide</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19AdministrativeRulesV10unitSystemAA04UnitE0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/unitSystem"></a>
<a class="token" href="#/s:7heresdk19AdministrativeRulesV10unitSystemAA04UnitE0OSgvp">unitSystem</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the measurement system used for distances. Defaults to metric measurement system.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">unitSystem</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-unitsystem">UnitSystem</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19AdministrativeRulesV11speedLimitsAA019GeneralVehicleSpeedE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedLimits"></a>
<a class="token" href="#/s:7heresdk19AdministrativeRulesV11speedLimitsAA019GeneralVehicleSpeedE0Vvp">speedLimits</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The general speed limits in the country or state.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">speedLimits</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-generalvehiclespeedlimits">GeneralVehicleSpeedLimits</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19AdministrativeRulesV24timeZoneOffsetsInMinutesSaySdGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/timeZoneOffsetsInMinutes"></a>
<a class="token" href="#/s:7heresdk19AdministrativeRulesV24timeZoneOffsetsInMinutesSaySdGvp">timeZoneOffsetsInMinutes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The time zone offset from UTC of the country or state expressed in minutes. The value can also be negative
(e.g.: Eastern Standard Time (EST) will be -360 minutes, Central European Time (CET) will be 60 minutes).
Defaults to 0 minutes.
<strong>Note:</strong> A time zone with a positive shift of 1 hour and 30 minutes will result in a time zone offset of
90 minutes. A time zone with a negative shift of 3 hour and 30 minutes will result in an time zone offset
of -210 minutes. In order to properly calculate the time zone offset, the [AdministrativeRules.daylight_saving_period]
should be taken into consideration and if the daylight savings time is observed at the time of the
calculation, then a value of 60 minutes should be substracted from the time zone offset.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">timeZoneOffsetsInMinutes</span><span class="p">:</span> <span class="p">[</span><span class="kt">TimeInterval</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19AdministrativeRulesV20daylightSavingPeriodAA8TimeRuleCSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/daylightSavingPeriod"></a>
<a class="token" href="#/s:7heresdk19AdministrativeRulesV20daylightSavingPeriodAA8TimeRuleCSgvp">daylightSavingPeriod</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Time rule indicating the time periods in which daylight savings applies.
If the field is ‘null’ then daylight savings time is not observed in the country or state.
<strong>Note:</strong> In order to properly calculate the time zone offset, if the daylight savings time is observed at
the time of the calculation, then a value of 60 minutes should be substracted from the time zone offset.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">daylightSavingPeriod</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-timerule">TimeRule</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19AdministrativeRulesV17isUturnRestrictedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isUturnRestricted"></a>
<a class="token" href="#/s:7heresdk19AdministrativeRulesV17isUturnRestrictedSbvp">isUturnRestricted</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates if performing a u-turn maneuver is restricted. Defaults to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isUturnRestricted</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19AdministrativeRulesV22headlightsRequirementsSayAA21HeadlightsRequirementOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/headlightsRequirements"></a>
<a class="token" href="#/s:7heresdk19AdministrativeRulesV22headlightsRequirementsSayAA21HeadlightsRequirementOGvp">headlightsRequirements</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates in which conditions should the headlights be turned on. Defaults to an empty list,
which means that by default there are no special situations in which the headlights should be
turned on.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">headlightsRequirements</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-headlightsrequirement">HeadlightsRequirement</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19AdministrativeRulesV14isTollRequiredSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isTollRequired"></a>
<a class="token" href="#/s:7heresdk19AdministrativeRulesV14isTollRequiredSbvp">isTollRequired</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates if the country or state requires paid fees for usage of the motorways / controlled access
roads. Defaults to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isTollRequired</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19AdministrativeRulesV21isTollStickerRequiredSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isTollStickerRequired"></a>
<a class="token" href="#/s:7heresdk19AdministrativeRulesV21isTollStickerRequiredSbvp">isTollStickerRequired</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates if the country or state requires a toll sticker. Defaults to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isTollStickerRequired</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19AdministrativeRulesV20turnOnRedRegulationsSayAA04TurneF10RegulationOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/turnOnRedRegulations"></a>
<a class="token" href="#/s:7heresdk19AdministrativeRulesV20turnOnRedRegulationsSayAA04TurneF10RegulationOGvp">turnOnRedRegulations</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the regulations for turning on the red color of the traffic light.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">turnOnRedRegulations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-turnonredregulation">TurnOnRedRegulation</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19AdministrativeRulesV22parkingSideRegulationsSayAA07ParkingE10RegulationOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/parkingSideRegulations"></a>
<a class="token" href="#/s:7heresdk19AdministrativeRulesV22parkingSideRegulationsSayAA07ParkingE10RegulationOGvp">parkingSideRegulations</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the regulations for parking on the side of the road.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">parkingSideRegulations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-parkingsideregulation">ParkingSideRegulation</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19AdministrativeRulesV25isCleanAirStickerRequiredSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isCleanAirStickerRequired"></a>
<a class="token" href="#/s:7heresdk19AdministrativeRulesV25isCleanAirStickerRequiredSbvp">isCleanAirStickerRequired</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates if the country or state requires an ecological sticker. Defaults to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isCleanAirStickerRequired</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19AdministrativeRulesV24bloodAlcoholContentLimitAA05BloodefG0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/bloodAlcoholContentLimit"></a>
<a class="token" href="#/s:7heresdk19AdministrativeRulesV24bloodAlcoholContentLimitAA05BloodefG0Vvp">bloodAlcoholContentLimit</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the rules regarding alcohol in blood content limit in a country or state for
all types of drivers.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">bloodAlcoholContentLimit</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-bloodalcoholcontentlimit">BloodAlcoholContentLimit</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19AdministrativeRulesV11tollSystemsSayAA10TollSystemVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tollSystems"></a>
<a class="token" href="#/s:7heresdk19AdministrativeRulesV11tollSystemsSayAA10TollSystemVGvp">tollSystems</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the toll systems present in a country or state.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">tollSystems</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-tollsystem">TollSystem</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19AdministrativeRulesV15preTripPlanningAA03PreeF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/preTripPlanning"></a>
<a class="token" href="#/s:7heresdk19AdministrativeRulesV15preTripPlanningAA03PreeF0Vvp">preTripPlanning</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the legal requirements to be considered before a trip for all vehicles types.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">preTripPlanning</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-pretripplanning">PreTripPlanning</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19AdministrativeRulesV11countryCode05stateE014adminContextId011parentAdminH3Ids11drivingSide10unitSystem11speedLimits24timeZoneOffsetsInMinutes20daylightSavingPeriod17isUturnRestricted22headlightsRequirements14isTollRequired21isTollStickerRequired20turnOnRedRegulations07parkingN11Regulations25isCleanAirStickerRequired24bloodAlcoholContentLimit11tollSystems15preTripPlanningAcA07CountryE0O_SSSgAA0khI0VSayA_GAA07DrivingN0OSgAA04UnitP0OSgAA019GeneralVehicleSpeedR0VSaySdGAA8TimeRuleCSgSbSayAA21HeadlightsRequirementOGS2bSayAA19TurnOnRedRegulationOGSayAA07ParkingN10RegulationOGSbAA24BloodAlcoholContentLimitVSayAA04TollP0VGAA15PreTripPlanningVtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(countryCode:stateCode:adminContextId:parentAdminContextIds:drivingSide:unitSystem:speedLimits:timeZoneOffsetsInMinutes:daylightSavingPeriod:isUturnRestricted:headlightsRequirements:isTollRequired:isTollStickerRequired:turnOnRedRegulations:parkingSideRegulations:isCleanAirStickerRequired:bloodAlcoholContentLimit:tollSystems:preTripPlanning:)"></a>
<a class="token" href="#/s:7heresdk19AdministrativeRulesV11countryCode05stateE014adminContextId011parentAdminH3Ids11drivingSide10unitSystem11speedLimits24timeZoneOffsetsInMinutes20daylightSavingPeriod17isUturnRestricted22headlightsRequirements14isTollRequired21isTollStickerRequired20turnOnRedRegulations07parkingN11Regulations25isCleanAirStickerRequired24bloodAlcoholContentLimit11tollSystems15preTripPlanningAcA07CountryE0O_SSSgAA0khI0VSayA_GAA07DrivingN0OSgAA04UnitP0OSgAA019GeneralVehicleSpeedR0VSaySdGAA8TimeRuleCSgSbSayAA21HeadlightsRequirementOGS2bSayAA19TurnOnRedRegulationOGSayAA07ParkingN10RegulationOGSbAA24BloodAlcoholContentLimitVSayAA04TollP0VGAA15PreTripPlanningVtcfc">init(countryCode:<wbr/>stateCode:<wbr/>adminContextId:<wbr/>parentAdminContextIds:<wbr/>drivingSide:<wbr/>unitSystem:<wbr/>speedLimits:<wbr/>timeZoneOffsetsInMinutes:<wbr/>daylightSavingPeriod:<wbr/>isUturnRestricted:<wbr/>headlightsRequirements:<wbr/>isTollRequired:<wbr/>isTollStickerRequired:<wbr/>turnOnRedRegulations:<wbr/>parkingSideRegulations:<wbr/>isCleanAirStickerRequired:<wbr/>bloodAlcoholContentLimit:<wbr/>tollSystems:<wbr/>preTripPlanning:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">countryCode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-countrycode">CountryCode</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-countrycode">CountryCode</a></span><span class="o">.</span><span class="n">abw</span><span class="p">,</span> <span class="nv">stateCode</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">adminContextId</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-admincontextid">AdminContextId</a></span><span class="p">,</span> <span class="nv">parentAdminContextIds</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-admincontextid">AdminContextId</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">drivingSide</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-drivingside">DrivingSide</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">unitSystem</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-unitsystem">UnitSystem</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">speedLimits</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-generalvehiclespeedlimits">GeneralVehicleSpeedLimits</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-generalvehiclespeedlimits">GeneralVehicleSpeedLimits</a></span><span class="p">(),</span> <span class="nv">timeZoneOffsetsInMinutes</span><span class="p">:</span> <span class="p">[</span><span class="kt">TimeInterval</span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">daylightSavingPeriod</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-timerule">TimeRule</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">isUturnRestricted</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">headlightsRequirements</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-headlightsrequirement">HeadlightsRequirement</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">isTollRequired</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">isTollStickerRequired</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">turnOnRedRegulations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-turnonredregulation">TurnOnRedRegulation</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">parkingSideRegulations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-parkingsideregulation">ParkingSideRegulation</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">isCleanAirStickerRequired</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">bloodAlcoholContentLimit</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-bloodalcoholcontentlimit">BloodAlcoholContentLimit</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-bloodalcoholcontentlimit">BloodAlcoholContentLimit</a></span><span class="p">(),</span> <span class="nv">tollSystems</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-tollsystem">TollSystem</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">preTripPlanning</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-pretripplanning">PreTripPlanning</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-pretripplanning">PreTripPlanning</a></span><span class="p">())</span></code></pre>
</div>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>
</body>
</html>

</div>
`
}</HTMLBlock>
