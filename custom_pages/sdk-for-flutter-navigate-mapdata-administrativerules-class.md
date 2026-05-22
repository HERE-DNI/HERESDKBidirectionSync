---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapdata-administrativerules-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- AdministrativeRules-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li class="self-crumb">AdministrativeRules class</li>
</ol>
<div class="self-name">AdministrativeRules</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="mapdata/mapdata-library-sidebar.html" data-below-sidebar="mapdata/AdministrativeRules-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>AdministrativeRules class</h1></div>
<section class="desc markdown">
<p>Represents a set of administrative rules for a country or a state.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="AdministrativeRules">
/sdk-for-flutter-navigate-mapdata-administrativerules-administrativerules(/sdk-for-flutter-navigate-mapdata-admincontextid-class adminContextId)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="adminContextId">
/sdk-for-flutter-navigate-mapdata-administrativerules-admincontextid
↔ /sdk-for-flutter-navigate-mapdata-admincontextid-class
</dt>
<dd>
  The administrative context ID used to identify this administrative region.
This ID is used internally to load commercial vehicle regulations and other
administrative-specific data.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="bloodAlcoholContentLimit">
/sdk-for-flutter-navigate-mapdata-administrativerules-bloodalcoholcontentlimit
↔ /sdk-for-flutter-navigate-mapdata-bloodalcoholcontentlimit-class
</dt>
<dd>
  Indicates the rules regarding alcohol in blood content limit in a country or state for
all types of drivers.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="countryCode">
/sdk-for-flutter-navigate-mapdata-administrativerules-countrycode
↔ /sdk-for-flutter-navigate-core-countrycode
</dt>
<dd>
  Country code for which the administrative rules apply.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="daylightSavingPeriod">
/sdk-for-flutter-navigate-mapdata-administrativerules-daylightsavingperiod
↔ /sdk-for-flutter-navigate-core-timerule-class?
</dt>
<dd>
  Time rule indicating the time periods in which daylight savings applies.
If the field is 'null' then daylight savings time is not observed in the country or state.
<strong>Note:</strong> In order to properly calculate the time zone offset, if the daylight savings time is observed at
the time of the calculation, then a value of 60 minutes should be substracted from the time zone offset.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="drivingSide">
/sdk-for-flutter-navigate-mapdata-administrativerules-drivingside
↔ /sdk-for-flutter-navigate-mapdata-drivingside?
</dt>
<dd>
  The side of the road used for driving in the country or state. Defaults to right driving side.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-mapdata-administrativerules-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="headlightsRequirements">
/sdk-for-flutter-navigate-mapdata-administrativerules-headlightsrequirements
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-mapdata-headlightsrequirement&gt;
</dt>
<dd>
  Indicates in which conditions should the headlights be turned on. Defaults to an empty list,
which means that by default there are no special situations in which the headlights should be
turned on.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isCleanAirStickerRequired">
/sdk-for-flutter-navigate-mapdata-administrativerules-iscleanairstickerrequired
↔ bool
</dt>
<dd>
  Indicates if the country or state requires an ecological sticker. Defaults to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isTollRequired">
/sdk-for-flutter-navigate-mapdata-administrativerules-istollrequired
↔ bool
</dt>
<dd>
  Indicates if the country or state requires paid fees for usage of the motorways / controlled access
roads. Defaults to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isTollStickerRequired">
/sdk-for-flutter-navigate-mapdata-administrativerules-istollstickerrequired
↔ bool
</dt>
<dd>
  Indicates if the country or state requires a toll sticker. Defaults to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isUturnRestricted">
/sdk-for-flutter-navigate-mapdata-administrativerules-isuturnrestricted
↔ bool
</dt>
<dd>
  Indicates if performing a u-turn maneuver is restricted. Defaults to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="parentAdminContextIds">
/sdk-for-flutter-navigate-mapdata-administrativerules-parentadmincontextids
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-mapdata-admincontextid-class&gt;
</dt>
<dd>
  The list of parent administrative context IDs.
These represent the administrative hierarchy (e.g., state-&gt;country).
Used internally to load commercial vehicle regulations that may be inherited
from parent administrative regions.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="parkingSideRegulations">
/sdk-for-flutter-navigate-mapdata-administrativerules-parkingsideregulations
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-mapdata-parkingsideregulation&gt;
</dt>
<dd>
  Indicates the regulations for parking on the side of the road.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="preTripPlanning">
/sdk-for-flutter-navigate-mapdata-administrativerules-pretripplanning
↔ /sdk-for-flutter-navigate-mapdata-pretripplanning-class
</dt>
<dd>
  Indicates the legal requirements to be considered before a trip for all vehicles types.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapdata-administrativerules-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="speedLimits">
/sdk-for-flutter-navigate-mapdata-administrativerules-speedlimits
↔ /sdk-for-flutter-navigate-transport-generalvehiclespeedlimits-class
</dt>
<dd>
  The general speed limits in the country or state.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="stateCode">
/sdk-for-flutter-navigate-mapdata-administrativerules-statecode
↔ String?
</dt>
<dd>
  The state code for which the administrative rules apply. It represents the state / province code. It is
a 1 to 3 upper-case characters string that follows the ISO 3166-2 standard, but without the preceding
country code (e.g. for Texas, the state code will be TX).
It will be <code>null</code> if the rules are applying to the entire country and not just a specific state.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="timeZoneOffsetsInMinutes">
/sdk-for-flutter-navigate-mapdata-administrativerules-timezoneoffsetsinminutes
↔ List&lt;<wbr/>Duration&gt;
</dt>
<dd>
  The time zone offset from UTC of the country or state expressed in minutes. The value can also be negative
(e.g.: Eastern Standard Time (EST) will be -360 minutes, Central European Time (CET) will be 60 minutes).
Defaults to 0 minutes.
<strong>Note:</strong> A time zone with a positive shift of 1 hour and 30 minutes will result in a time zone offset of
90 minutes. A time zone with a negative shift of 3 hour and 30 minutes will result in an time zone offset
of -210 minutes. In order to properly calculate the time zone offset, the <code>AdministrativeRules.daylight_saving_period</code>
should be taken into consideration and if the daylight savings time is observed at the time of the
calculation, then a value of 60 minutes should be substracted from the time zone offset.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="tollSystems">
/sdk-for-flutter-navigate-mapdata-administrativerules-tollsystems
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-mapdata-tollsystem-class&gt;
</dt>
<dd>
  Indicates the toll systems present in a country or state.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="turnOnRedRegulations">
/sdk-for-flutter-navigate-mapdata-administrativerules-turnonredregulations
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-mapdata-turnonredregulation&gt;
</dt>
<dd>
  Indicates the regulations for turning on the red color of the traffic light.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="unitSystem">
/sdk-for-flutter-navigate-mapdata-administrativerules-unitsystem
↔ /sdk-for-flutter-navigate-core-unitsystem?
</dt>
<dd>
  Defines the measurement system used for distances. Defaults to metric measurement system.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapdata-administrativerules-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapdata-administrativerules-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
/sdk-for-flutter-navigate-mapdata-administrativerules-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

</dd>
</dl>
</section>
</div> 
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">

<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li class="self-crumb">AdministrativeRules class</li>
</ol>
<h5>mapdata library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>
